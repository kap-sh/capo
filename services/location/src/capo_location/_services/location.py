"""Generated from Smithy shape ``com.amazonaws.location#LocationService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_location._auth._signers
import capo_location._auth._sigv4
from capo_location._auth._identity import Credentials
from capo_location._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_location._auth._zapros_handler import AuthMiddleware
from capo_location._pagination import resolve_path as _resolve_path
from capo_location._resources.location_service.api_key_resource import ApiKeyResource
from capo_location._resources.location_service.generic_resource import GenericResource
from capo_location._resources.location_service.geofence_collection_resource import (
    GeofenceCollectionResource,
)
from capo_location._resources.location_service.job_resource import JobResource
from capo_location._resources.location_service.map_resource import MapResource
from capo_location._resources.location_service.place_index_resource import (
    PlaceIndexResource,
)
from capo_location._resources.location_service.route_calculator_resource import (
    RouteCalculatorResource,
)
from capo_location._resources.location_service.tracker_resource import TrackerResource
from capo_location._services._aws_config import aws_config
from capo_location._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.api_key_filter
    import capo_location.types.api_key_restrictions
    import capo_location.types.arn
    import capo_location.types.associate_tracker_consumer_request
    import capo_location.types.associate_tracker_consumer_response
    import capo_location.types.batch_delete_device_position_history_request
    import capo_location.types.batch_delete_device_position_history_response
    import capo_location.types.batch_delete_geofence_request
    import capo_location.types.batch_delete_geofence_response
    import capo_location.types.batch_evaluate_geofences_request
    import capo_location.types.batch_evaluate_geofences_response
    import capo_location.types.batch_get_device_position_request
    import capo_location.types.batch_get_device_position_response
    import capo_location.types.batch_put_geofence_request
    import capo_location.types.batch_put_geofence_request_entry_list
    import capo_location.types.batch_put_geofence_response
    import capo_location.types.batch_update_device_position_request
    import capo_location.types.batch_update_device_position_response
    import capo_location.types.bounding_box
    import capo_location.types.calculate_route_car_mode_options
    import capo_location.types.calculate_route_matrix_request
    import capo_location.types.calculate_route_matrix_response
    import capo_location.types.calculate_route_request
    import capo_location.types.calculate_route_response
    import capo_location.types.calculate_route_truck_mode_options
    import capo_location.types.cancel_job_request
    import capo_location.types.cancel_job_response
    import capo_location.types.client_token
    import capo_location.types.country_code_list
    import capo_location.types.create_geofence_collection_request
    import capo_location.types.create_geofence_collection_response
    import capo_location.types.create_key_request
    import capo_location.types.create_key_response
    import capo_location.types.create_map_request
    import capo_location.types.create_map_response
    import capo_location.types.create_place_index_request
    import capo_location.types.create_place_index_response
    import capo_location.types.create_route_calculator_request
    import capo_location.types.create_route_calculator_response
    import capo_location.types.create_tracker_request
    import capo_location.types.create_tracker_response
    import capo_location.types.data_source_configuration
    import capo_location.types.delete_geofence_collection_request
    import capo_location.types.delete_geofence_collection_response
    import capo_location.types.delete_key_request
    import capo_location.types.delete_key_response
    import capo_location.types.delete_map_request
    import capo_location.types.delete_map_response
    import capo_location.types.delete_place_index_request
    import capo_location.types.delete_place_index_response
    import capo_location.types.delete_route_calculator_request
    import capo_location.types.delete_route_calculator_response
    import capo_location.types.delete_tracker_request
    import capo_location.types.delete_tracker_response
    import capo_location.types.describe_geofence_collection_request
    import capo_location.types.describe_geofence_collection_response
    import capo_location.types.describe_key_request
    import capo_location.types.describe_key_response
    import capo_location.types.describe_map_request
    import capo_location.types.describe_map_response
    import capo_location.types.describe_place_index_request
    import capo_location.types.describe_place_index_response
    import capo_location.types.describe_route_calculator_request
    import capo_location.types.describe_route_calculator_response
    import capo_location.types.describe_tracker_request
    import capo_location.types.describe_tracker_response
    import capo_location.types.device_ids_list
    import capo_location.types.device_position
    import capo_location.types.device_position_update_list
    import capo_location.types.device_state
    import capo_location.types.disassociate_tracker_consumer_request
    import capo_location.types.disassociate_tracker_consumer_response
    import capo_location.types.distance_unit
    import capo_location.types.filter_place_category_list
    import capo_location.types.forecast_geofence_events_device_state
    import capo_location.types.forecast_geofence_events_request
    import capo_location.types.forecast_geofence_events_response
    import capo_location.types.forecasted_event
    import capo_location.types.geofence_geometry
    import capo_location.types.get_device_position_history_request
    import capo_location.types.get_device_position_history_response
    import capo_location.types.get_device_position_request
    import capo_location.types.get_device_position_response
    import capo_location.types.get_geofence_request
    import capo_location.types.get_geofence_response
    import capo_location.types.get_job_request
    import capo_location.types.get_job_response
    import capo_location.types.get_map_glyphs_request
    import capo_location.types.get_map_glyphs_response
    import capo_location.types.get_map_sprites_request
    import capo_location.types.get_map_sprites_response
    import capo_location.types.get_map_style_descriptor_request
    import capo_location.types.get_map_style_descriptor_response
    import capo_location.types.get_map_tile_request
    import capo_location.types.get_map_tile_response
    import capo_location.types.get_place_request
    import capo_location.types.get_place_response
    import capo_location.types.iam_role_arn
    import capo_location.types.id
    import capo_location.types.id_list
    import capo_location.types.job_action
    import capo_location.types.job_action_options
    import capo_location.types.job_id
    import capo_location.types.job_input_options
    import capo_location.types.job_output_options
    import capo_location.types.jobs_filter
    import capo_location.types.kms_key_id
    import capo_location.types.language_tag
    import capo_location.types.large_token
    import capo_location.types.list_device_positions_request
    import capo_location.types.list_device_positions_response
    import capo_location.types.list_device_positions_response_entry
    import capo_location.types.list_geofence_collections_request
    import capo_location.types.list_geofence_collections_response
    import capo_location.types.list_geofence_collections_response_entry
    import capo_location.types.list_geofence_response_entry
    import capo_location.types.list_geofences_request
    import capo_location.types.list_geofences_response
    import capo_location.types.list_jobs_request
    import capo_location.types.list_jobs_response
    import capo_location.types.list_jobs_response_entry
    import capo_location.types.list_keys_request
    import capo_location.types.list_keys_response
    import capo_location.types.list_keys_response_entry
    import capo_location.types.list_maps_request
    import capo_location.types.list_maps_response
    import capo_location.types.list_maps_response_entry
    import capo_location.types.list_place_indexes_request
    import capo_location.types.list_place_indexes_response
    import capo_location.types.list_place_indexes_response_entry
    import capo_location.types.list_route_calculators_request
    import capo_location.types.list_route_calculators_response
    import capo_location.types.list_route_calculators_response_entry
    import capo_location.types.list_tags_for_resource_request
    import capo_location.types.list_tags_for_resource_response
    import capo_location.types.list_tracker_consumers_request
    import capo_location.types.list_tracker_consumers_response
    import capo_location.types.list_trackers_request
    import capo_location.types.list_trackers_response
    import capo_location.types.list_trackers_response_entry
    import capo_location.types.map_configuration
    import capo_location.types.map_configuration_update
    import capo_location.types.optimization_mode
    import capo_location.types.place_id
    import capo_location.types.place_index_search_result_limit
    import capo_location.types.position
    import capo_location.types.position_filtering
    import capo_location.types.position_list
    import capo_location.types.pricing_plan
    import capo_location.types.property_map
    import capo_location.types.put_geofence_request
    import capo_location.types.put_geofence_response
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.search_place_index_for_position_request
    import capo_location.types.search_place_index_for_position_response
    import capo_location.types.search_place_index_for_suggestions_request
    import capo_location.types.search_place_index_for_suggestions_response
    import capo_location.types.search_place_index_for_text_request
    import capo_location.types.search_place_index_for_text_response
    import capo_location.types.sensitive_boolean
    import capo_location.types.sensitive_string
    import capo_location.types.speed_unit
    import capo_location.types.start_job_request
    import capo_location.types.start_job_response
    import capo_location.types.tag_keys
    import capo_location.types.tag_map
    import capo_location.types.tag_resource_request
    import capo_location.types.tag_resource_response
    import capo_location.types.timestamp
    import capo_location.types.token
    import capo_location.types.tracking_filter_geometry
    import capo_location.types.travel_mode
    import capo_location.types.untag_resource_request
    import capo_location.types.untag_resource_response
    import capo_location.types.update_geofence_collection_request
    import capo_location.types.update_geofence_collection_response
    import capo_location.types.update_key_request
    import capo_location.types.update_key_response
    import capo_location.types.update_map_request
    import capo_location.types.update_map_response
    import capo_location.types.update_place_index_request
    import capo_location.types.update_place_index_response
    import capo_location.types.update_route_calculator_request
    import capo_location.types.update_route_calculator_response
    import capo_location.types.update_tracker_request
    import capo_location.types.update_tracker_response
    import capo_location.types.verify_device_position_request
    import capo_location.types.verify_device_position_response
    import capo_location.types.waypoint_position_list


class LocationClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class LocationClient:
    """A client for the ``Location`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = LocationClientConfig(
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
        self.api_key_resource = ApiKeyResource(self)
        self.generic_resource = GenericResource(self)
        self.geofence_collection_resource = GeofenceCollectionResource(self)
        self.job_resource = JobResource(self)
        self.map_resource = MapResource(self)
        self.place_index_resource = PlaceIndexResource(self)
        self.route_calculator_resource = RouteCalculatorResource(self)
        self.tracker_resource = TrackerResource(self)

    def operation_options(
        self, config_overrides: Optional[LocationClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: LocationClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def create_key(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        restrictions: "capo_location.types.api_key_restrictions.ApiKeyRestrictions",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        expire_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        no_expiry: Optional[bool] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_key_response.CreateKeyResponse":
        """<p>Creates an API key resource in your Amazon Web Services account, which lets you grant actions for Amazon Location resources to the API key bearer.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key_name: <p>A custom name for the API key resource.</p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). </p> </li> <li> <p>Must be a unique API key name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleAPIKey</code>.</p> </li> </ul>
            restrictions: <p>The API key restrictions for the API key resource.</p>
            description: <p>An optional description for the API key resource.</p>
            expire_time: <p>The optional timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. One of <code>NoExpiry</code> or <code>ExpireTime</code> must be set.</p>
            no_expiry: <p>Optionally set to <code>true</code> to set no expiration time for the API key. One of <code>NoExpiry</code> or <code>ExpireTime</code> must be set.</p>
            tags: <p>Applies one or more tags to the map resource. A tag is a key-value pair that helps manage, identify, search, and filter your resources by labelling them.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.create_key_request.CreateKeyRequest]",
        ) -> OperationResponse[
            "capo_location.types.create_key_response.CreateKeyResponse"
        ]:
            import capo_location._operations.location_service.create_key

            output, http_response = (
                capo_location._operations.location_service.create_key.create_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.create_key_request.CreateKeyRequest = {
            "key_name": key_name,
            "restrictions": restrictions,
        }
        if description is not None:
            input_["description"] = description
        if expire_time is not None:
            input_["expire_time"] = expire_time
        if no_expiry is not None:
            input_["no_expiry"] = no_expiry
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_key(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.describe_key_response.DescribeKeyResponse":
        """<p>Retrieves the API key resource details.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key_name: <p>The name of the API key resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.describe_key_request.DescribeKeyRequest]",
        ) -> OperationResponse[
            "capo_location.types.describe_key_response.DescribeKeyResponse"
        ]:
            import capo_location._operations.location_service.describe_key

            output, http_response = (
                capo_location._operations.location_service.describe_key.describe_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.describe_key_request.DescribeKeyRequest = {
            "key_name": key_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_key(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        expire_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        no_expiry: Optional[bool] = None,
        force_update: Optional[bool] = None,
        restrictions: Optional[
            "capo_location.types.api_key_restrictions.ApiKeyRestrictions"
        ] = None,
    ) -> "capo_location.types.update_key_response.UpdateKeyResponse":
        """<p>Updates the specified properties of a given API key resource.</p>

        Args:
            key_name: <p>The name of the API key resource to update.</p>
            description: <p>Updates the description for the API key resource.</p>
            expire_time: <p>Updates the timestamp for when the API key resource will expire in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>
            no_expiry: <p>Whether the API key should expire. Set to <code>true</code> to set the API key to have no expiration time.</p>
            force_update: <p>The boolean flag to be included for updating <code>ExpireTime</code> or <code>Restrictions</code> details.</p> <p>Must be set to <code>true</code> to update an API key resource that has been used in the past 7 days.</p> <p> <code>False</code> if force update is not preferred</p> <p>Default value: <code>False</code> </p>
            restrictions: <p>Updates the API key restrictions for the API key resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.update_key_request.UpdateKeyRequest]",
        ) -> OperationResponse[
            "capo_location.types.update_key_response.UpdateKeyResponse"
        ]:
            import capo_location._operations.location_service.update_key

            output, http_response = (
                capo_location._operations.location_service.update_key.update_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.update_key_request.UpdateKeyRequest = {
            "key_name": key_name
        }
        if description is not None:
            input_["description"] = description
        if expire_time is not None:
            input_["expire_time"] = expire_time
        if no_expiry is not None:
            input_["no_expiry"] = no_expiry
        if force_update is not None:
            input_["force_update"] = force_update
        if restrictions is not None:
            input_["restrictions"] = restrictions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_key(
        self,
        key_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        force_delete: Optional[bool] = None,
    ) -> "capo_location.types.delete_key_response.DeleteKeyResponse":
        """<p>Deletes the specified API key. The API key must have been deactivated more than 90 days previously.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            key_name: <p>The name of the API key to delete.</p>
            force_delete: <p>ForceDelete bypasses an API key's expiry conditions and deletes the key. Set the parameter <code>true</code> to delete the key or to <code>false</code> to not preemptively delete the API key.</p> <p>Valid values: <code>true</code>, or <code>false</code>.</p> <p>Required: No</p> <note> <p>This action is irreversible. Only use ForceDelete if you are certain the key is no longer in use.</p> </note>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.delete_key_request.DeleteKeyRequest]",
        ) -> OperationResponse[
            "capo_location.types.delete_key_response.DeleteKeyResponse"
        ]:
            import capo_location._operations.location_service.delete_key

            output, http_response = (
                capo_location._operations.location_service.delete_key.delete_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.delete_key_request.DeleteKeyRequest = {
            "key_name": key_name
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_keys(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
        filter: Optional["capo_location.types.api_key_filter.ApiKeyFilter"] = None,
    ) -> "capo_location.types.list_keys_response.ListKeysResponse":
        """<p>Lists API key resources in your Amazon Web Services account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html">Use API keys to authenticate</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            max_results: <p>An optional limit for the number of resources returned in a single call. </p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>
            filter: <p>Optionally filter the list to only <code>Active</code> or <code>Expired</code> API keys.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_keys_request.ListKeysRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_keys_response.ListKeysResponse"
        ]:
            import capo_location._operations.location_service.list_keys

            output, http_response = (
                capo_location._operations.location_service.list_keys.list_keys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_keys_request.ListKeysRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_keys(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
        filter: Optional["capo_location.types.api_key_filter.ApiKeyFilter"] = None,
    ) -> "Iterator[capo_location.types.list_keys_response_entry.ListKeysResponseEntry]":
        _token = next_token
        while True:
            _response = self.list_keys(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_location.types.arn.Arn",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags that are applied to the specified Amazon Location resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_location._operations.location_service.list_tags_for_resource

            output, http_response = (
                capo_location._operations.location_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_location.types.arn.Arn",
        tags: "capo_location.types.tag_map.TagMap",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified Amazon Location Service resource.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.</p> <p>You can use the <code>TagResource</code> operation with an Amazon Location Service resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the tags already associated with the resource. If you specify a tag key that's already associated with the resource, the new tag value that you specify replaces the previous value for that tag. </p> <p>You can associate up to 50 tags with a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource whose tags you want to update.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
            tags: <p>Applies one or more tags to specific resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource.</p> </li> <li> <p>Each tag key must be unique and must have exactly one associated value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @</p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_location.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_location._operations.location_service.tag_resource

            output, http_response = (
                capo_location._operations.location_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_location.types.arn.Arn",
        tag_keys: "capo_location.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified Amazon Location resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which you want to remove tags.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:resourcetype/ExampleResource</code> </p> </li> </ul>
            tag_keys: <p>The list of tag keys to remove from the specified resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_location.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_location._operations.location_service.untag_resource

            output, http_response = (
                capo_location._operations.location_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_geofence_collection(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        pricing_plan_data_source: Optional[str] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
        kms_key_id: Optional["capo_location.types.kms_key_id.KmsKeyId"] = None,
    ) -> "capo_location.types.create_geofence_collection_response.CreateGeofenceCollectionResponse":
        """<p>Creates a geofence collection, which manages and stores geofences.</p>

        Args:
            collection_name: <p>A custom name for the geofence collection.</p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). </p> </li> <li> <p>Must be a unique geofence collection name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleGeofenceCollection</code>.</p> </li> </ul>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            pricing_plan_data_source: <p>This parameter is no longer used.</p>
            description: <p>An optional description for the geofence collection.</p>
            tags: <p>Applies one or more tags to the geofence collection. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>
            kms_key_id: <p>A key identifier for an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a>. Enter a key ID, key ARN, alias name, or alias ARN. </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.create_geofence_collection_request.CreateGeofenceCollectionRequest]",
        ) -> OperationResponse[
            "capo_location.types.create_geofence_collection_response.CreateGeofenceCollectionResponse"
        ]:
            import capo_location._operations.location_service.create_geofence_collection

            output, http_response = (
                capo_location._operations.location_service.create_geofence_collection.create_geofence_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.create_geofence_collection_request.CreateGeofenceCollectionRequest = {
            "collection_name": collection_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if pricing_plan_data_source is not None:
            input_["pricing_plan_data_source"] = pricing_plan_data_source
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_geofence_collection(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.describe_geofence_collection_response.DescribeGeofenceCollectionResponse":
        """<p>Retrieves the geofence collection details.</p>

        Args:
            collection_name: <p>The name of the geofence collection.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.describe_geofence_collection_request.DescribeGeofenceCollectionRequest]",
        ) -> OperationResponse[
            "capo_location.types.describe_geofence_collection_response.DescribeGeofenceCollectionResponse"
        ]:
            import capo_location._operations.location_service.describe_geofence_collection

            output, http_response = (
                capo_location._operations.location_service.describe_geofence_collection.describe_geofence_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.describe_geofence_collection_request.DescribeGeofenceCollectionRequest = {
            "collection_name": collection_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_geofence_collection(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        pricing_plan_data_source: Optional[str] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_location.types.update_geofence_collection_response.UpdateGeofenceCollectionResponse":
        """<p>Updates the specified properties of a given geofence collection.</p>

        Args:
            collection_name: <p>The name of the geofence collection to update.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            pricing_plan_data_source: <p>This parameter is no longer used.</p>
            description: <p>Updates the description for the geofence collection.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.update_geofence_collection_request.UpdateGeofenceCollectionRequest]",
        ) -> OperationResponse[
            "capo_location.types.update_geofence_collection_response.UpdateGeofenceCollectionResponse"
        ]:
            import capo_location._operations.location_service.update_geofence_collection

            output, http_response = (
                capo_location._operations.location_service.update_geofence_collection.update_geofence_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.update_geofence_collection_request.UpdateGeofenceCollectionRequest = {
            "collection_name": collection_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if pricing_plan_data_source is not None:
            input_["pricing_plan_data_source"] = pricing_plan_data_source
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_geofence_collection(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.delete_geofence_collection_response.DeleteGeofenceCollectionResponse":
        """<p>Deletes a geofence collection from your Amazon Web Services account.</p> <note> <p>This operation deletes the resource permanently. If the geofence collection is the target of a tracker resource, the devices will no longer be monitored.</p> </note>

        Args:
            collection_name: <p>The name of the geofence collection to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.delete_geofence_collection_request.DeleteGeofenceCollectionRequest]",
        ) -> OperationResponse[
            "capo_location.types.delete_geofence_collection_response.DeleteGeofenceCollectionResponse"
        ]:
            import capo_location._operations.location_service.delete_geofence_collection

            output, http_response = (
                capo_location._operations.location_service.delete_geofence_collection.delete_geofence_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.delete_geofence_collection_request.DeleteGeofenceCollectionRequest = {
            "collection_name": collection_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_geofence_collections(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_geofence_collections_response.ListGeofenceCollectionsResponse":
        """<p>Lists geofence collections in your Amazon Web Services account.</p>

        Args:
            max_results: <p>An optional limit for the number of resources returned in a single call. </p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_geofence_collections_request.ListGeofenceCollectionsRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_geofence_collections_response.ListGeofenceCollectionsResponse"
        ]:
            import capo_location._operations.location_service.list_geofence_collections

            output, http_response = (
                capo_location._operations.location_service.list_geofence_collections.list_geofence_collections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_geofence_collections_request.ListGeofenceCollectionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_geofence_collections(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "Iterator[capo_location.types.list_geofence_collections_response_entry.ListGeofenceCollectionsResponseEntry]":
        _token = next_token
        while True:
            _response = self.list_geofence_collections(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def batch_delete_geofence(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        geofence_ids: "capo_location.types.id_list.IdList",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> (
        "capo_location.types.batch_delete_geofence_response.BatchDeleteGeofenceResponse"
    ):
        """<p>Deletes a batch of geofences from a geofence collection.</p> <note> <p>This operation deletes the resource permanently.</p> </note>

        Args:
            collection_name: <p>The geofence collection storing the geofences to be deleted.</p>
            geofence_ids: <p>The batch of geofences to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.batch_delete_geofence_request.BatchDeleteGeofenceRequest]",
        ) -> OperationResponse[
            "capo_location.types.batch_delete_geofence_response.BatchDeleteGeofenceResponse"
        ]:
            import capo_location._operations.location_service.batch_delete_geofence

            output, http_response = (
                capo_location._operations.location_service.batch_delete_geofence.batch_delete_geofence(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.batch_delete_geofence_request.BatchDeleteGeofenceRequest = {
            "collection_name": collection_name,
            "geofence_ids": geofence_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_evaluate_geofences(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        device_position_updates: "capo_location.types.device_position_update_list.DevicePositionUpdateList",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.batch_evaluate_geofences_response.BatchEvaluateGeofencesResponse":
        """<p>Evaluates device positions against the geofence geometries from a given geofence collection.</p> <p>This operation always returns an empty response because geofences are asynchronously evaluated. The evaluation determines if the device has entered or exited a geofenced area, and then publishes one of the following events to Amazon EventBridge:</p> <ul> <li> <p> <code>ENTER</code> if Amazon Location determines that the tracked device has entered a geofenced area.</p> </li> <li> <p> <code>EXIT</code> if Amazon Location determines that the tracked device has exited a geofenced area.</p> </li> </ul> <note> <p>The last geofence that a device was observed within is tracked for 30 days after the most recent device position update.</p> </note> <note> <p>Geofence evaluation uses the given device position. It does not account for the optional <code>Accuracy</code> of a <code>DevicePositionUpdate</code>.</p> </note> <note> <p>The <code>DeviceID</code> is used as a string to represent the device. You do not need to have a <code>Tracker</code> associated with the <code>DeviceID</code>.</p> </note>

        Args:
            collection_name: <p>The geofence collection used in evaluating the position of devices against its geofences.</p>
            device_position_updates: <p>Contains device details for each device to be evaluated against the given geofence collection.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.batch_evaluate_geofences_request.BatchEvaluateGeofencesRequest]",
        ) -> OperationResponse[
            "capo_location.types.batch_evaluate_geofences_response.BatchEvaluateGeofencesResponse"
        ]:
            import capo_location._operations.location_service.batch_evaluate_geofences

            output, http_response = (
                capo_location._operations.location_service.batch_evaluate_geofences.batch_evaluate_geofences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.batch_evaluate_geofences_request.BatchEvaluateGeofencesRequest = {
            "collection_name": collection_name,
            "device_position_updates": device_position_updates,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_put_geofence(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        entries: "capo_location.types.batch_put_geofence_request_entry_list.BatchPutGeofenceRequestEntryList",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.batch_put_geofence_response.BatchPutGeofenceResponse":
        """<p>A batch request for storing geofence geometries into a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.</p>

        Args:
            collection_name: <p>The geofence collection storing the geofences.</p>
            entries: <p>The batch of geofences to be stored in a geofence collection.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.batch_put_geofence_request.BatchPutGeofenceRequest]",
        ) -> OperationResponse[
            "capo_location.types.batch_put_geofence_response.BatchPutGeofenceResponse"
        ]:
            import capo_location._operations.location_service.batch_put_geofence

            output, http_response = (
                capo_location._operations.location_service.batch_put_geofence.batch_put_geofence(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.batch_put_geofence_request.BatchPutGeofenceRequest = {
            "collection_name": collection_name,
            "entries": entries,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def forecast_geofence_events(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        device_state: "capo_location.types.forecast_geofence_events_device_state.ForecastGeofenceEventsDeviceState",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        time_horizon_minutes: Optional[float] = None,
        distance_unit: Optional[
            "capo_location.types.distance_unit.DistanceUnit"
        ] = None,
        speed_unit: Optional["capo_location.types.speed_unit.SpeedUnit"] = None,
        next_token: Optional["capo_location.types.large_token.LargeToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_location.types.forecast_geofence_events_response.ForecastGeofenceEventsResponse":
        """<p>This action forecasts future geofence events that are likely to occur within a specified time horizon if a device continues moving at its current speed. Each forecasted event is associated with a geofence from a provided geofence collection. A forecast event can have one of the following states:</p> <p> <code>ENTER</code>: The device position is outside the referenced geofence, but the device may cross into the geofence during the forecasting time horizon if it maintains its current speed.</p> <p> <code>EXIT</code>: The device position is inside the referenced geofence, but the device may leave the geofence during the forecasted time horizon if the device maintains it's current speed.</p> <p> <code>IDLE</code>:The device is inside the geofence, and it will remain inside the geofence through the end of the time horizon if the device maintains it's current speed.</p> <note> <p>Heading direction is not considered in the current version. The API takes a conservative approach and includes events that can occur for any heading.</p> </note>

        Args:
            collection_name: <p>The name of the geofence collection.</p>
            device_state: <p>Represents the device's state, including its current position and speed. When speed is omitted, this API performs a <i>containment check</i>. The <i>containment check</i> operation returns <code>IDLE</code> events for geofences where the device is currently inside of, but no other events.</p>
            time_horizon_minutes: <p>The forward-looking time window for forecasting, specified in minutes. The API only returns events that are predicted to occur within this time horizon. When no value is specified, this API performs a <i>containment check</i>. The <i>containment check</i> operation returns <code>IDLE</code> events for geofences where the device is currently inside of, but no other events.</p>
            distance_unit: <p>The distance unit used for the <code>NearestDistance</code> property returned in a forecasted event. The measurement system must match for <code>DistanceUnit</code> and <code>SpeedUnit</code>; if <code>Kilometers</code> is specified for <code>DistanceUnit</code>, then <code>SpeedUnit</code> must be <code>KilometersPerHour</code>. </p> <p>Default Value: <code>Kilometers</code> </p>
            speed_unit: <p>The speed unit for the device captured by the device state. The measurement system must match for <code>DistanceUnit</code> and <code>SpeedUnit</code>; if <code>Kilometers</code> is specified for <code>DistanceUnit</code>, then <code>SpeedUnit</code> must be <code>KilometersPerHour</code>.</p> <p>Default Value: <code>KilometersPerHour</code>.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default value: <code>null</code> </p>
            max_results: <p>An optional limit for the number of resources returned in a single call.</p> <p>Default value: <code>20</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.forecast_geofence_events_request.ForecastGeofenceEventsRequest]",
        ) -> OperationResponse[
            "capo_location.types.forecast_geofence_events_response.ForecastGeofenceEventsResponse"
        ]:
            import capo_location._operations.location_service.forecast_geofence_events

            output, http_response = (
                capo_location._operations.location_service.forecast_geofence_events.forecast_geofence_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.forecast_geofence_events_request.ForecastGeofenceEventsRequest = {
            "collection_name": collection_name,
            "device_state": device_state,
        }
        if time_horizon_minutes is not None:
            input_["time_horizon_minutes"] = time_horizon_minutes
        if distance_unit is not None:
            input_["distance_unit"] = distance_unit
        if speed_unit is not None:
            input_["speed_unit"] = speed_unit
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_forecast_geofence_events(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        device_state: "capo_location.types.forecast_geofence_events_device_state.ForecastGeofenceEventsDeviceState",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        time_horizon_minutes: Optional[float] = None,
        distance_unit: Optional[
            "capo_location.types.distance_unit.DistanceUnit"
        ] = None,
        speed_unit: Optional["capo_location.types.speed_unit.SpeedUnit"] = None,
        next_token: Optional["capo_location.types.large_token.LargeToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_location.types.forecasted_event.ForecastedEvent]":
        _token = next_token
        while True:
            _response = self.forecast_geofence_events(
                collection_name,
                device_state,
                config_overrides=config_overrides,
                time_horizon_minutes=time_horizon_minutes,
                distance_unit=distance_unit,
                speed_unit=speed_unit,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("forecasted_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_geofence(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        geofence_id: "capo_location.types.id.Id",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.get_geofence_response.GetGeofenceResponse":
        """<p>Retrieves the geofence details from a geofence collection.</p> <note> <p>The returned geometry will always match the geometry format used when the geofence was created.</p> </note>

        Args:
            collection_name: <p>The geofence collection storing the target geofence.</p>
            geofence_id: <p>The geofence you're retrieving details for.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_geofence_request.GetGeofenceRequest]",
        ) -> OperationResponse[
            "capo_location.types.get_geofence_response.GetGeofenceResponse"
        ]:
            import capo_location._operations.location_service.get_geofence

            output, http_response = (
                capo_location._operations.location_service.get_geofence.get_geofence(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.get_geofence_request.GetGeofenceRequest = {
            "collection_name": collection_name,
            "geofence_id": geofence_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_geofences(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        next_token: Optional["capo_location.types.large_token.LargeToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_location.types.list_geofences_response.ListGeofencesResponse":
        """<p>Lists geofences stored in a given geofence collection.</p>

        Args:
            collection_name: <p>The name of the geofence collection storing the list of geofences.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>
            max_results: <p>An optional limit for the number of geofences returned in a single call. </p> <p>Default value: <code>100</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_geofences_request.ListGeofencesRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_geofences_response.ListGeofencesResponse"
        ]:
            import capo_location._operations.location_service.list_geofences

            output, http_response = (
                capo_location._operations.location_service.list_geofences.list_geofences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_geofences_request.ListGeofencesRequest = {
            "collection_name": collection_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_geofences(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        next_token: Optional["capo_location.types.large_token.LargeToken"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_location.types.list_geofence_response_entry.ListGeofenceResponseEntry]":
        _token = next_token
        while True:
            _response = self.list_geofences(
                collection_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_geofence(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        geofence_id: "capo_location.types.id.Id",
        geometry: "capo_location.types.geofence_geometry.GeofenceGeometry",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        geofence_properties: Optional[
            "capo_location.types.property_map.PropertyMap"
        ] = None,
    ) -> "capo_location.types.put_geofence_response.PutGeofenceResponse":
        """<p>Stores a geofence geometry in a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request. </p>

        Args:
            collection_name: <p>The geofence collection to store the geofence in.</p>
            geofence_id: <p>An identifier for the geofence. For example, <code>ExampleGeofence-1</code>.</p>
            geometry: <p>Contains the details to specify the position of the geofence. Can be a circle, a polygon, or a multipolygon. <code>Polygon</code> and <code>MultiPolygon</code> geometries can be defined using their respective parameters, or encoded in Geobuf format using the <code>Geobuf</code> parameter. Including multiple geometry types in the same request will return a validation error.</p> <note> <p>The geofence <code>Polygon</code> and <code>MultiPolygon</code> formats support a maximum of 1,000 total vertices. The <code>Geobuf</code> format supports a maximum of 100,000 vertices.</p> </note>
            geofence_properties: <p>Associates one of more properties with the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.</p> <p>Format: <code>"key" : "value"</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.put_geofence_request.PutGeofenceRequest]",
        ) -> OperationResponse[
            "capo_location.types.put_geofence_response.PutGeofenceResponse"
        ]:
            import capo_location._operations.location_service.put_geofence

            output, http_response = (
                capo_location._operations.location_service.put_geofence.put_geofence(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.put_geofence_request.PutGeofenceRequest = {
            "collection_name": collection_name,
            "geofence_id": geofence_id,
            "geometry": geometry,
        }
        if geofence_properties is not None:
            input_["geofence_properties"] = geofence_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_job(
        self,
        action: "capo_location.types.job_action.JobAction",
        execution_role_arn: "capo_location.types.iam_role_arn.IamRoleArn",
        input_options: "capo_location.types.job_input_options.JobInputOptions",
        output_options: "capo_location.types.job_output_options.JobOutputOptions",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        client_token: Optional["capo_location.types.client_token.ClientToken"] = None,
        action_options: Optional[
            "capo_location.types.job_action_options.JobActionOptions"
        ] = None,
        name: Optional["capo_location.types.resource_name.ResourceName"] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.start_job_response.StartJobResponse":
        """<p> <code>StartJob</code> starts a new asynchronous bulk processing job. You specify the input data location in Amazon S3, the action to perform, and the output location where results are written.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            client_token: <p>A unique identifier for this request to ensure idempotency.</p>
            action: <p>The action to perform on the input data.</p>
            action_options: <p>Additional parameters that can be requested for each result.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that Amazon Location Service assumes during job processing. Amazon Location Service uses this role to access the input and output locations specified for the job.</p> <note> <p>The IAM role must be created in the same Amazon Web Services account where you plan to run your job.</p> </note> <p>For more information about configuring IAM roles for Amazon Location jobs, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/configure-iam-role-policy-credentials.html">Configure IAM permissions</a> in the <i>Amazon Location Service Developer Guide</i>.</p>
            input_options: <p>Configuration for input data location and format.</p> <note> <p>Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.</p> </note>
            name: <p>An optional name for the job resource.</p>
            output_options: <p>Configuration for output data location and format.</p>
            tags: <p>Tags and corresponding values to be associated with the job.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.start_job_request.StartJobRequest]",
        ) -> OperationResponse[
            "capo_location.types.start_job_response.StartJobResponse"
        ]:
            import capo_location._operations.location_service.start_job

            output, http_response = (
                capo_location._operations.location_service.start_job.start_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.start_job_request.StartJobRequest = {
            "action": action,
            "execution_role_arn": execution_role_arn,
            "input_options": input_options,
            "output_options": output_options,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if action_options is not None:
            input_["action_options"] = action_options
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_job(
        self,
        job_id: "capo_location.types.job_id.JobId",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.get_job_response.GetJobResponse":
        """<p> <code>GetJob</code> retrieves detailed information about a specific job, including its current status, configuration, and error information if the job failed.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            job_id: <p>The unique identifier of the job to retrieve.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_job_request.GetJobRequest]",
        ) -> OperationResponse["capo_location.types.get_job_response.GetJobResponse"]:
            import capo_location._operations.location_service.get_job

            output, http_response = (
                capo_location._operations.location_service.get_job.get_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.get_job_request.GetJobRequest = {"job_id": job_id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_jobs(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        filter: Optional["capo_location.types.jobs_filter.JobsFilter"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.large_token.LargeToken"] = None,
    ) -> "capo_location.types.list_jobs_response.ListJobsResponse":
        """<p> <code>ListJobs</code> retrieves a list of jobs with optional filtering and pagination support.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            filter: <p>An optional structure containing criteria by which to filter job results.</p>
            max_results: <p>Maximum number of jobs to return.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_jobs_request.ListJobsRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_jobs_response.ListJobsResponse"
        ]:
            import capo_location._operations.location_service.list_jobs

            output, http_response = (
                capo_location._operations.location_service.list_jobs.list_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_jobs_request.ListJobsRequest = {}
        if filter is not None:
            input_["filter"] = filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_jobs(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        filter: Optional["capo_location.types.jobs_filter.JobsFilter"] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.large_token.LargeToken"] = None,
    ) -> "Iterator[capo_location.types.list_jobs_response_entry.ListJobsResponseEntry]":
        _token = next_token
        while True:
            _response = self.list_jobs(
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def cancel_job(
        self,
        job_id: "capo_location.types.job_id.JobId",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.cancel_job_response.CancelJobResponse":
        """<p> <code>CancelJob</code> cancels a job that is currently running or pending. If the job is already in a terminal state (<code>Completed</code>, <code>Failed</code>, or <code>Cancelled</code>), the operation returns successfully with the current status.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/location/latest/developerguide/jobs-concepts.html">Job concepts</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            job_id: <p>The unique identifier of the job to cancel.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.cancel_job_request.CancelJobRequest]",
        ) -> OperationResponse[
            "capo_location.types.cancel_job_response.CancelJobResponse"
        ]:
            import capo_location._operations.location_service.cancel_job

            output, http_response = (
                capo_location._operations.location_service.cancel_job.cancel_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.cancel_job_request.CancelJobRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_map(
        self,
        map_name: "capo_location.types.resource_name.ResourceName",
        configuration: "capo_location.types.map_configuration.MapConfiguration",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_map_response.CreateMapResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend upgrading to the Maps API V2 unless you require <code>Grab</code> data.</p> <ul> <li> <p> <code>CreateMap</code> is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Maps API version 2 has a simplified interface that can be used without creating or managing map resources.</p> </li> <li> <p>If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under <code>geo-maps</code> or <code>geo_maps</code>, not under <code>location</code>.</p> </li> <li> <p>Since <code>Grab</code> is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using <code>Grab</code>.</p> </li> <li> <p>Start your version 2 API journey with the <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html">Maps V2 API Reference</a> or the <a href="https://docs.aws.amazon.com/location/latest/developerguide/maps.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Creates a map resource in your Amazon Web Services account, which provides map tiles of different styles sourced from global location data providers.</p> <note> <p>If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the <a href="http://aws.amazon.com/service-terms">Amazon Web Services service terms</a> for more details.</p> </note>

        Args:
            map_name: <p>The name for the map resource.</p> <p>Requirements:</p> <ul> <li> <p>Must contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). </p> </li> <li> <p>Must be a unique map resource name. </p> </li> <li> <p>No spaces allowed. For example, <code>ExampleMap</code>.</p> </li> </ul>
            configuration: <p>Specifies the <code>MapConfiguration</code>, including the map style, for the map resource that you create. The map style defines the look of maps and the data provider for your map resource.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>An optional description for the map resource.</p>
            tags: <p>Applies one or more tags to the map resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.create_map_request.CreateMapRequest]",
        ) -> OperationResponse[
            "capo_location.types.create_map_response.CreateMapResponse"
        ]:
            import capo_location._operations.location_service.create_map

            output, http_response = (
                capo_location._operations.location_service.create_map.create_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.create_map_request.CreateMapRequest = {
            "map_name": map_name,
            "configuration": configuration,
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_map(
        self,
        map_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.describe_map_response.DescribeMapResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend upgrading to the Maps API V2 unless you require <code>Grab</code> data.</p> <ul> <li> <p> <code>DescribeMap</code> is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Maps API version 2 has a simplified interface that can be used without creating or managing map resources.</p> </li> <li> <p>If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under <code>geo-maps</code> or <code>geo_maps</code>, not under <code>location</code>.</p> </li> <li> <p>Since <code>Grab</code> is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using <code>Grab</code>.</p> </li> <li> <p>Start your version 2 API journey with the <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html">Maps V2 API Reference</a> or the <a href="https://docs.aws.amazon.com/location/latest/developerguide/maps.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves the map resource details.</p>

        Args:
            map_name: <p>The name of the map resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.describe_map_request.DescribeMapRequest]",
        ) -> OperationResponse[
            "capo_location.types.describe_map_response.DescribeMapResponse"
        ]:
            import capo_location._operations.location_service.describe_map

            output, http_response = (
                capo_location._operations.location_service.describe_map.describe_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.describe_map_request.DescribeMapRequest = {
            "map_name": map_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_map(
        self,
        map_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        configuration_update: Optional[
            "capo_location.types.map_configuration_update.MapConfigurationUpdate"
        ] = None,
    ) -> "capo_location.types.update_map_response.UpdateMapResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend upgrading to the Maps API V2 unless you require <code>Grab</code> data.</p> <ul> <li> <p> <code>UpdateMap</code> is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Maps API version 2 has a simplified interface that can be used without creating or managing map resources.</p> </li> <li> <p>If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under <code>geo-maps</code> or <code>geo_maps</code>, not under <code>location</code>.</p> </li> <li> <p>Since <code>Grab</code> is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using <code>Grab</code>.</p> </li> <li> <p>Start your version 2 API journey with the <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html">Maps V2 API Reference</a> or the <a href="https://docs.aws.amazon.com/location/latest/developerguide/maps.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Updates the specified properties of a given map resource.</p>

        Args:
            map_name: <p>The name of the map resource to update.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>Updates the description for the map resource.</p>
            configuration_update: <p>Updates the parts of the map configuration that can be updated, including the political view.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.update_map_request.UpdateMapRequest]",
        ) -> OperationResponse[
            "capo_location.types.update_map_response.UpdateMapResponse"
        ]:
            import capo_location._operations.location_service.update_map

            output, http_response = (
                capo_location._operations.location_service.update_map.update_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.update_map_request.UpdateMapRequest = {
            "map_name": map_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if configuration_update is not None:
            input_["configuration_update"] = configuration_update

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_map(
        self,
        map_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.delete_map_response.DeleteMapResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend upgrading to the Maps API V2 unless you require <code>Grab</code> data.</p> <ul> <li> <p> <code>DeleteMap</code> is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Maps API version 2 has a simplified interface that can be used without creating or managing map resources.</p> </li> <li> <p>If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under <code>geo-maps</code> or <code>geo_maps</code>, not under <code>location</code>.</p> </li> <li> <p>Since <code>Grab</code> is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using <code>Grab</code>.</p> </li> <li> <p>Start your version 2 API journey with the <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html">Maps V2 API Reference</a> or the <a href="https://docs.aws.amazon.com/location/latest/developerguide/maps.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Deletes a map resource from your Amazon Web Services account.</p> <note> <p>This operation deletes the resource permanently. If the map is being used in an application, the map may not render.</p> </note>

        Args:
            map_name: <p>The name of the map resource to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.delete_map_request.DeleteMapRequest]",
        ) -> OperationResponse[
            "capo_location.types.delete_map_response.DeleteMapResponse"
        ]:
            import capo_location._operations.location_service.delete_map

            output, http_response = (
                capo_location._operations.location_service.delete_map.delete_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.delete_map_request.DeleteMapRequest = {
            "map_name": map_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_maps(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_maps_response.ListMapsResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend upgrading to the Maps API V2 unless you require <code>Grab</code> data.</p> <ul> <li> <p> <code>ListMaps</code> is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Maps API version 2 has a simplified interface that can be used without creating or managing map resources.</p> </li> <li> <p>If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under <code>geo-maps</code> or <code>geo_maps</code>, not under <code>location</code>.</p> </li> <li> <p>Since <code>Grab</code> is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using <code>Grab</code>.</p> </li> <li> <p>Start your version 2 API journey with the <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html">Maps V2 API Reference</a> or the <a href="https://docs.aws.amazon.com/location/latest/developerguide/maps.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Lists map resources in your Amazon Web Services account.</p>

        Args:
            max_results: <p>An optional limit for the number of resources returned in a single call. </p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_maps_request.ListMapsRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_maps_response.ListMapsResponse"
        ]:
            import capo_location._operations.location_service.list_maps

            output, http_response = (
                capo_location._operations.location_service.list_maps.list_maps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_maps_request.ListMapsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_maps(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "Iterator[capo_location.types.list_maps_response_entry.ListMapsResponseEntry]":
        _token = next_token
        while True:
            _response = self.list_maps(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_map_glyphs(
        self,
        map_name: "capo_location.types.resource_name.ResourceName",
        font_stack: str,
        font_unicode_range: str,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.get_map_glyphs_response.GetMapGlyphsResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend upgrading to <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetGlyphs.html"> <code>GetGlyphs</code> </a> unless you require <code>Grab</code> data.</p> <ul> <li> <p> <code>GetMapGlyphs</code> is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>GetGlyphs</code> operation gives a better user experience and is compatible with the remainder of the V2 Maps API.</p> </li> <li> <p>If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under <code>geo-maps</code> or <code>geo_maps</code>, not under <code>location</code>.</p> </li> <li> <p>Since <code>Grab</code> is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using <code>Grab</code>.</p> </li> <li> <p>Start your version 2 API journey with the <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html">Maps V2 API Reference</a> or the <a href="https://docs.aws.amazon.com/location/latest/developerguide/maps.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves glyphs used to display labels on a map.</p>

        Args:
            map_name: <p>The map resource associated with the glyph ﬁle.</p>
            font_stack: <p>A comma-separated list of fonts to load glyphs from in order of preference. For example, <code>Noto Sans Regular, Arial Unicode</code>.</p> <p>Valid font stacks for <a href="https://docs.aws.amazon.com/location/previous/developerguide/esri.html">Esri</a> styles: </p> <ul> <li> <p>VectorEsriDarkGrayCanvas – <code>Ubuntu Medium Italic</code> | <code>Ubuntu Medium</code> | <code>Ubuntu Italic</code> | <code>Ubuntu Regular</code> | <code>Ubuntu Bold</code> </p> </li> <li> <p>VectorEsriLightGrayCanvas – <code>Ubuntu Italic</code> | <code>Ubuntu Regular</code> | <code>Ubuntu Light</code> | <code>Ubuntu Bold</code> </p> </li> <li> <p>VectorEsriTopographic – <code>Noto Sans Italic</code> | <code>Noto Sans Regular</code> | <code>Noto Sans Bold</code> | <code>Noto Serif Regular</code> | <code>Roboto Condensed Light Italic</code> </p> </li> <li> <p>VectorEsriStreets – <code>Arial Regular</code> | <code>Arial Italic</code> | <code>Arial Bold</code> </p> </li> <li> <p>VectorEsriNavigation – <code>Arial Regular</code> | <code>Arial Italic</code> | <code>Arial Bold</code> </p> </li> </ul> <p>Valid font stacks for <a href="https://docs.aws.amazon.com/location/previous/developerguide/HERE.html">HERE Technologies</a> styles:</p> <ul> <li> <p>VectorHereContrast – <code>Fira GO Regular</code> | <code>Fira GO Bold</code> </p> </li> <li> <p>VectorHereExplore, VectorHereExploreTruck, HybridHereExploreSatellite – <code>Fira GO Italic</code> | <code>Fira GO Map</code> | <code>Fira GO Map Bold</code> | <code>Noto Sans CJK JP Bold</code> | <code>Noto Sans CJK JP Light</code> | <code>Noto Sans CJK JP Regular</code> </p> </li> </ul> <p>Valid font stacks for <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a> styles:</p> <ul> <li> <p>VectorGrabStandardLight, VectorGrabStandardDark – <code>Noto Sans Regular</code> | <code>Noto Sans Medium</code> | <code>Noto Sans Bold</code> </p> </li> </ul> <p>Valid font stacks for <a href="https://docs.aws.amazon.com/location/previous/developerguide/open-data.html">Open Data</a> styles:</p> <ul> <li> <p>VectorOpenDataStandardLight, VectorOpenDataStandardDark, VectorOpenDataVisualizationLight, VectorOpenDataVisualizationDark – <code>Amazon Ember Regular,Noto Sans Regular</code> | <code>Amazon Ember Bold,Noto Sans Bold</code> | <code>Amazon Ember Medium,Noto Sans Medium</code> | <code>Amazon Ember Regular Italic,Noto Sans Italic</code> | <code>Amazon Ember Condensed RC Regular,Noto Sans Regular</code> | <code>Amazon Ember Condensed RC Bold,Noto Sans Bold</code> | <code>Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular</code> | <code>Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold</code> | <code>Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold</code> | <code>Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular</code> | <code>Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular</code> | <code>Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium</code> </p> </li> </ul> <note> <p>The fonts used by the Open Data map styles are combined fonts that use <code>Amazon Ember</code> for most glyphs but <code>Noto Sans</code> for glyphs unsupported by <code>Amazon Ember</code>.</p> </note>
            font_unicode_range: <p>A Unicode range of characters to download glyphs for. Each response will contain 256 characters. For example, 0–255 includes all characters from range <code>U+0000</code> to <code>00FF</code>. Must be aligned to multiples of 256.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_map_glyphs_request.GetMapGlyphsRequest]",
        ) -> OperationResponse[
            "capo_location.types.get_map_glyphs_response.GetMapGlyphsResponse"
        ]:
            import capo_location._operations.location_service.get_map_glyphs

            output, http_response = (
                capo_location._operations.location_service.get_map_glyphs.get_map_glyphs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.get_map_glyphs_request.GetMapGlyphsRequest = {
            "map_name": map_name,
            "font_stack": font_stack,
            "font_unicode_range": font_unicode_range,
        }
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_map_sprites(
        self,
        map_name: "capo_location.types.resource_name.ResourceName",
        file_name: str,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.get_map_sprites_response.GetMapSpritesResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend upgrading to <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetSprites.html"> <code>GetSprites</code> </a> unless you require <code>Grab</code> data.</p> <ul> <li> <p> <code>GetMapSprites</code> is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>GetSprites</code> operation gives a better user experience and is compatible with the remainder of the V2 Maps API.</p> </li> <li> <p>If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under <code>geo-maps</code> or <code>geo_maps</code>, not under <code>location</code>.</p> </li> <li> <p>Since <code>Grab</code> is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using <code>Grab</code>.</p> </li> <li> <p>Start your version 2 API journey with the <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html">Maps V2 API Reference</a> or the <a href="https://docs.aws.amazon.com/location/latest/developerguide/maps.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves the sprite sheet corresponding to a map resource. The sprite sheet is a PNG image paired with a JSON document describing the offsets of individual icons that will be displayed on a rendered map.</p>

        Args:
            map_name: <p>The map resource associated with the sprite ﬁle.</p>
            file_name: <p>The name of the sprite ﬁle. Use the following ﬁle names for the sprite sheet:</p> <ul> <li> <p> <code>sprites.png</code> </p> </li> <li> <p> <code>sprites@2x.png</code> for high pixel density displays</p> </li> </ul> <p>For the JSON document containing image offsets. Use the following ﬁle names:</p> <ul> <li> <p> <code>sprites.json</code> </p> </li> <li> <p> <code>sprites@2x.json</code> for high pixel density displays</p> </li> </ul>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_map_sprites_request.GetMapSpritesRequest]",
        ) -> OperationResponse[
            "capo_location.types.get_map_sprites_response.GetMapSpritesResponse"
        ]:
            import capo_location._operations.location_service.get_map_sprites

            output, http_response = (
                capo_location._operations.location_service.get_map_sprites.get_map_sprites(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.get_map_sprites_request.GetMapSpritesRequest = {
            "map_name": map_name,
            "file_name": file_name,
        }
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_map_style_descriptor(
        self,
        map_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.get_map_style_descriptor_response.GetMapStyleDescriptorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend upgrading to <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStyleDescriptor.html"> <code>GetStyleDescriptor</code> </a> unless you require <code>Grab</code> data.</p> <ul> <li> <p> <code>GetMapStyleDescriptor</code> is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>GetStyleDescriptor</code> operation gives a better user experience and is compatible with the remainder of the V2 Maps API.</p> </li> <li> <p>If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under <code>geo-maps</code> or <code>geo_maps</code>, not under <code>location</code>.</p> </li> <li> <p>Since <code>Grab</code> is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using <code>Grab</code>.</p> </li> <li> <p>Start your version 2 API journey with the <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html">Maps V2 API Reference</a> or the <a href="https://docs.aws.amazon.com/location/latest/developerguide/maps.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves the map style descriptor from a map resource. </p> <p>The style descriptor contains speciﬁcations on how features render on a map. For example, what data to display, what order to display the data in, and the style for the data. Style descriptors follow the Mapbox Style Specification.</p>

        Args:
            map_name: <p>The map resource to retrieve the style descriptor from.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_map_style_descriptor_request.GetMapStyleDescriptorRequest]",
        ) -> OperationResponse[
            "capo_location.types.get_map_style_descriptor_response.GetMapStyleDescriptorResponse"
        ]:
            import capo_location._operations.location_service.get_map_style_descriptor

            output, http_response = (
                capo_location._operations.location_service.get_map_style_descriptor.get_map_style_descriptor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.get_map_style_descriptor_request.GetMapStyleDescriptorRequest = {
            "map_name": map_name
        }
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_map_tile(
        self,
        map_name: "capo_location.types.resource_name.ResourceName",
        z: "capo_location.types.sensitive_string.SensitiveString",
        x: "capo_location.types.sensitive_string.SensitiveString",
        y: "capo_location.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.get_map_tile_response.GetMapTileResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend upgrading to <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html"> <code>GetTile</code> </a> unless you require <code>Grab</code> data.</p> <ul> <li> <p> <code>GetMapTile</code> is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>GetTile</code> operation gives a better user experience and is compatible with the remainder of the V2 Maps API.</p> </li> <li> <p>If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under <code>geo-maps</code> or <code>geo_maps</code>, not under <code>location</code>.</p> </li> <li> <p>Since <code>Grab</code> is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using <code>Grab</code>.</p> </li> <li> <p>Start your version 2 API journey with the <a href="https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html">Maps V2 API Reference</a> or the <a href="https://docs.aws.amazon.com/location/latest/developerguide/maps.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves a vector data tile from the map resource. Map tiles are used by clients to render a map. they're addressed using a grid arrangement with an X coordinate, Y coordinate, and Z (zoom) level. </p> <p>The origin (0, 0) is the top left of the map. Increasing the zoom level by 1 doubles both the X and Y dimensions, so a tile containing data for the entire world at (0/0/0) will be split into 4 tiles at zoom 1 (1/0/0, 1/0/1, 1/1/0, 1/1/1).</p>

        Args:
            map_name: <p>The map resource to retrieve the map tiles from.</p>
            z: <p>The zoom value for the map tile.</p>
            x: <p>The X axis value for the map tile.</p>
            y: <p>The Y axis value for the map tile. </p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_map_tile_request.GetMapTileRequest]",
        ) -> OperationResponse[
            "capo_location.types.get_map_tile_response.GetMapTileResponse"
        ]:
            import capo_location._operations.location_service.get_map_tile

            output, http_response = (
                capo_location._operations.location_service.get_map_tile.get_map_tile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.get_map_tile_request.GetMapTileRequest = {
            "map_name": map_name,
            "z": z,
            "x": x,
            "y": y,
        }
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_place_index(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        data_source: str,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        data_source_configuration: Optional[
            "capo_location.types.data_source_configuration.DataSourceConfiguration"
        ] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_place_index_response.CreatePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>CreatePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Creates a place index resource in your Amazon Web Services account. Use a place index resource to geocode addresses and other text queries by using the <code>SearchPlaceIndexForText</code> operation, and reverse geocode coordinates by using the <code>SearchPlaceIndexForPosition</code> operation, and enable autosuggestions by using the <code>SearchPlaceIndexForSuggestions</code> operation.</p> <note> <p>If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the <a href="http://aws.amazon.com/service-terms">Amazon Web Services service terms</a> for more details.</p> </note>

        Args:
            index_name: <p>The name of the place index resource. </p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).</p> </li> <li> <p>Must be a unique place index resource name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExamplePlaceIndex</code>.</p> </li> </ul>
            data_source: <p>Specifies the geospatial data provider for the new place index.</p> <note> <p>This field is case-sensitive. Enter the valid values as shown. For example, entering <code>HERE</code> returns an error.</p> </note> <p>Valid values include:</p> <ul> <li> <p> <code>Esri</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/esri.html">Esri</a>'s coverage in your region of interest, see <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm">Esri details on geocoding coverage</a>.</p> </li> <li> <p> <code>Grab</code> – Grab provides place index functionality for Southeast Asia. For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a>' coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area">GrabMaps countries and areas covered</a>.</p> </li> <li> <p> <code>Here</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/HERE.html">HERE Technologies</a>' coverage in your region of interest, see <a href="https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html">HERE details on goecoding coverage</a>.</p> <important> <p>If you specify HERE Technologies (<code>Here</code>) as the data provider, you may not <a href="https://docs.aws.amazon.com/location-places/latest/APIReference/API_DataSourceConfiguration.html">store results</a> for locations in Japan. For more information, see the <a href="http://aws.amazon.com/service-terms/">Amazon Web Services service terms</a> for Amazon Location Service.</p> </important> </li> </ul> <p>For additional information , see <a href="https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html">Data providers</a> on the <i>Amazon Location Service developer guide</i>.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>The optional description for the place index resource.</p>
            data_source_configuration: <p>Specifies the data storage option requesting Places.</p>
            tags: <p>Applies one or more tags to the place index resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource.</p> </li> <li> <p>Each tag key must be unique and must have exactly one associated value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @</p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.create_place_index_request.CreatePlaceIndexRequest]",
        ) -> OperationResponse[
            "capo_location.types.create_place_index_response.CreatePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.create_place_index

            output, http_response = (
                capo_location._operations.location_service.create_place_index.create_place_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.create_place_index_request.CreatePlaceIndexRequest = {
            "index_name": index_name,
            "data_source": data_source,
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if data_source_configuration is not None:
            input_["data_source_configuration"] = data_source_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_place_index(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.describe_place_index_response.DescribePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DescribePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves the place index resource details.</p>

        Args:
            index_name: <p>The name of the place index resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.describe_place_index_request.DescribePlaceIndexRequest]",
        ) -> OperationResponse[
            "capo_location.types.describe_place_index_response.DescribePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.describe_place_index

            output, http_response = (
                capo_location._operations.location_service.describe_place_index.describe_place_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.describe_place_index_request.DescribePlaceIndexRequest = {
            "index_name": index_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_place_index(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        data_source_configuration: Optional[
            "capo_location.types.data_source_configuration.DataSourceConfiguration"
        ] = None,
    ) -> "capo_location.types.update_place_index_response.UpdatePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>UpdatePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Updates the specified properties of a given place index resource.</p>

        Args:
            index_name: <p>The name of the place index resource to update.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>Updates the description for the place index resource.</p>
            data_source_configuration: <p>Updates the data storage option for the place index resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.update_place_index_request.UpdatePlaceIndexRequest]",
        ) -> OperationResponse[
            "capo_location.types.update_place_index_response.UpdatePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.update_place_index

            output, http_response = (
                capo_location._operations.location_service.update_place_index.update_place_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.update_place_index_request.UpdatePlaceIndexRequest = {
            "index_name": index_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if data_source_configuration is not None:
            input_["data_source_configuration"] = data_source_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_place_index(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.delete_place_index_response.DeletePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DeletePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Deletes a place index resource from your Amazon Web Services account.</p> <note> <p>This operation deletes the resource permanently.</p> </note>

        Args:
            index_name: <p>The name of the place index resource to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.delete_place_index_request.DeletePlaceIndexRequest]",
        ) -> OperationResponse[
            "capo_location.types.delete_place_index_response.DeletePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.delete_place_index

            output, http_response = (
                capo_location._operations.location_service.delete_place_index.delete_place_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.delete_place_index_request.DeletePlaceIndexRequest = {
            "index_name": index_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_place_indexes(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_place_indexes_response.ListPlaceIndexesResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>ListPlaceIndexes</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Lists place index resources in your Amazon Web Services account.</p>

        Args:
            max_results: <p>An optional limit for the maximum number of results returned in a single call.</p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_place_indexes_request.ListPlaceIndexesRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_place_indexes_response.ListPlaceIndexesResponse"
        ]:
            import capo_location._operations.location_service.list_place_indexes

            output, http_response = (
                capo_location._operations.location_service.list_place_indexes.list_place_indexes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_place_indexes_request.ListPlaceIndexesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_place_indexes(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "Iterator[capo_location.types.list_place_indexes_response_entry.ListPlaceIndexesResponseEntry]":
        _token = next_token
        while True:
            _response = self.list_place_indexes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_place(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        place_id: "capo_location.types.place_id.PlaceId",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.get_place_response.GetPlaceResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the <a href="/location/latest/APIReference/API_geoplaces_GetPlace.html">V2 <code>GetPlace</code> </a> operation unless you require Grab data.</p> <ul> <li> <p>This version of <code>GetPlace</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>Version 2 of the <code>GetPlace</code> operation interoperates with the rest of the Places V2 API, while this version does not.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Finds a place by its unique ID. A <code>PlaceId</code> is returned by other search operations.</p> <note> <p>A PlaceId is valid only if all of the following are the same in the original search request and the call to <code>GetPlace</code>.</p> <ul> <li> <p>Customer Amazon Web Services account</p> </li> <li> <p>Amazon Web Services Region</p> </li> <li> <p>Data provider specified in the place index resource</p> </li> </ul> </note> <note> <p>If your Place index resource is configured with Grab as your geolocation provider and Storage as Intended use, the GetPlace operation is unavailable. For more information, see <a href="http://aws.amazon.com/service-terms">AWS service terms</a>.</p> </note>

        Args:
            index_name: <p>The name of the place index resource that you want to use for the search.</p>
            place_id: <p>The identifier of the place to find.</p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the <code>language</code> parameter set to <code>en</code>. The <code>city</code> in the results will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the <code>city</code> in the results will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_place_request.GetPlaceRequest]",
        ) -> OperationResponse[
            "capo_location.types.get_place_response.GetPlaceResponse"
        ]:
            import capo_location._operations.location_service.get_place

            output, http_response = (
                capo_location._operations.location_service.get_place.get_place(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.get_place_request.GetPlaceRequest = {
            "index_name": index_name,
            "place_id": place_id,
        }
        if language is not None:
            input_["language"] = language
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_place_index_for_position(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        position: "capo_location.types.position.Position",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[
            "capo_location.types.place_index_search_result_limit.PlaceIndexSearchResultLimit"
        ] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.search_place_index_for_position_response.SearchPlaceIndexForPositionResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_geoplaces_ReverseGeocode.html"> <code>ReverseGeocode</code> </a> or <a href="/location/latest/APIReference/API_geoplaces_SearchNearby.html"> <code>SearchNearby</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>SearchPlaceIndexForPosition</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>ReverseGeocode</code> operation gives better results in the address reverse-geocoding use case, while the version 2 <code>SearchNearby</code> operation gives better results when searching for businesses and points of interest near a specific location.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p>Reverse geocodes a given coordinate and returns a legible address. Allows you to search for Places or points of interest near a given position.</p>

        Args:
            index_name: <p>The name of the place index resource you want to use for the search.</p>
            position: <p>Specifies the longitude and latitude of the position to query.</p> <p> This parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents a position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p>
            max_results: <p>An optional parameter. The maximum number of results returned per request.</p> <p>Default value: <code>50</code> </p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the <code>language</code> parameter set to <code>en</code>. The <code>city</code> in the results will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the <code>city</code> in the results will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.search_place_index_for_position_request.SearchPlaceIndexForPositionRequest]",
        ) -> OperationResponse[
            "capo_location.types.search_place_index_for_position_response.SearchPlaceIndexForPositionResponse"
        ]:
            import capo_location._operations.location_service.search_place_index_for_position

            output, http_response = (
                capo_location._operations.location_service.search_place_index_for_position.search_place_index_for_position(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.search_place_index_for_position_request.SearchPlaceIndexForPositionRequest = {
            "index_name": index_name,
            "position": position,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_place_index_for_suggestions(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        text: "capo_location.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        bias_position: Optional["capo_location.types.position.Position"] = None,
        filter_b_box: Optional["capo_location.types.bounding_box.BoundingBox"] = None,
        filter_countries: Optional[
            "capo_location.types.country_code_list.CountryCodeList"
        ] = None,
        max_results: Optional[int] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        filter_categories: Optional[
            "capo_location.types.filter_place_category_list.FilterPlaceCategoryList"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.search_place_index_for_suggestions_response.SearchPlaceIndexForSuggestionsResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_geoplaces_Suggest.html"> <code>Suggest</code> </a> or <a href="/location/latest/APIReference/API_geoplaces_Autocomplete.html"> <code>Autocomplete</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>SearchPlaceIndexForSuggestions</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>Suggest</code> operation gives better results for typeahead place search suggestions with fuzzy matching, while the version 2 <code>Autocomplete</code> operation gives better results for address completion based on partial input.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p>Generates suggestions for addresses and points of interest based on partial or misspelled free-form text. This operation is also known as autocomplete, autosuggest, or fuzzy matching.</p> <p>Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.</p> <note> <p>You can search for suggested place names near a specified position by using <code>BiasPosition</code>, or filter results within a bounding box by using <code>FilterBBox</code>. These parameters are mutually exclusive; using both <code>BiasPosition</code> and <code>FilterBBox</code> in the same command returns an error.</p> </note>

        Args:
            index_name: <p>The name of the place index resource you want to use for the search.</p>
            text: <p>The free-form partial text to use to generate place suggestions. For example, <code>eiffel tow</code>.</p>
            bias_position: <p>An optional parameter that indicates a preference for place suggestions that are closer to a specified position.</p> <p> If provided, this parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p> <note> <p> <code>BiasPosition</code> and <code>FilterBBox</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_b_box: <p>An optional parameter that limits the search results by returning only suggestions within a specified bounding box.</p> <p> If provided, this parameter must contain a total of four consecutive numbers in two pairs. The first pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the southwest corner of the bounding box; the second pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the northeast corner of the bounding box.</p> <p>For example, <code>[-12.7935, -37.4835, -12.0684, -36.9542]</code> represents a bounding box where the southwest corner has longitude <code>-12.7935</code> and latitude <code>-37.4835</code>, and the northeast corner has longitude <code>-12.0684</code> and latitude <code>-36.9542</code>.</p> <note> <p> <code>FilterBBox</code> and <code>BiasPosition</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_countries: <p>An optional parameter that limits the search results by returning only suggestions within the provided list of countries.</p> <ul> <li> <p>Use the <a href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166</a> 3-digit country code. For example, Australia uses three upper-case characters: <code>AUS</code>.</p> </li> </ul>
            max_results: <p>An optional parameter. The maximum number of results returned per request. </p> <p>The default: <code>5</code> </p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for <code>Athens, Gr</code> to get suggestions with the <code>language</code> parameter set to <code>en</code>. The results found will most likely be returned as <code>Athens, Greece</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the result found will more likely be returned as <code>Αθήνα, Ελλάδα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            filter_categories: <p>A list of one or more Amazon Location categories to filter the returned places. If you include more than one category, the results will include results that match <i>any</i> of the categories listed.</p> <p>For more information about using categories, including a list of Amazon Location categories, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html">Categories and filtering</a>, in the <i>Amazon Location Service developer guide</i>.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.search_place_index_for_suggestions_request.SearchPlaceIndexForSuggestionsRequest]",
        ) -> OperationResponse[
            "capo_location.types.search_place_index_for_suggestions_response.SearchPlaceIndexForSuggestionsResponse"
        ]:
            import capo_location._operations.location_service.search_place_index_for_suggestions

            output, http_response = (
                capo_location._operations.location_service.search_place_index_for_suggestions.search_place_index_for_suggestions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.search_place_index_for_suggestions_request.SearchPlaceIndexForSuggestionsRequest = {
            "index_name": index_name,
            "text": text,
        }
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter_b_box is not None:
            input_["filter_b_box"] = filter_b_box
        if filter_countries is not None:
            input_["filter_countries"] = filter_countries
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if filter_categories is not None:
            input_["filter_categories"] = filter_categories
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_place_index_for_text(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        text: "capo_location.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        bias_position: Optional["capo_location.types.position.Position"] = None,
        filter_b_box: Optional["capo_location.types.bounding_box.BoundingBox"] = None,
        filter_countries: Optional[
            "capo_location.types.country_code_list.CountryCodeList"
        ] = None,
        max_results: Optional[
            "capo_location.types.place_index_search_result_limit.PlaceIndexSearchResultLimit"
        ] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        filter_categories: Optional[
            "capo_location.types.filter_place_category_list.FilterPlaceCategoryList"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.search_place_index_for_text_response.SearchPlaceIndexForTextResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_geoplaces_Geocode.html"> <code>Geocode</code> </a> or <a href="/location/latest/APIReference/API_geoplaces_SearchText.html"> <code>SearchText</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>SearchPlaceIndexForText</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>Geocode</code> operation gives better results in the address geocoding use case, while the version 2 <code>SearchText</code> operation gives better results when searching for businesses and points of interest.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p>Geocodes free-form text, such as an address, name, city, or region to allow you to search for Places or points of interest. </p> <p>Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.</p> <note> <p>You can search for places near a given position using <code>BiasPosition</code>, or filter results within a bounding box using <code>FilterBBox</code>. Providing both parameters simultaneously returns an error.</p> </note> <p>Search results are returned in order of highest to lowest relevance.</p>

        Args:
            index_name: <p>The name of the place index resource you want to use for the search.</p>
            text: <p>The address, name, city, or region to be used in the search in free-form text format. For example, <code>123 Any Street</code>.</p>
            bias_position: <p>An optional parameter that indicates a preference for places that are closer to a specified position.</p> <p> If provided, this parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p> <note> <p> <code>BiasPosition</code> and <code>FilterBBox</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_b_box: <p>An optional parameter that limits the search results by returning only places that are within the provided bounding box.</p> <p> If provided, this parameter must contain a total of four consecutive numbers in two pairs. The first pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the southwest corner of the bounding box; the second pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the northeast corner of the bounding box.</p> <p>For example, <code>[-12.7935, -37.4835, -12.0684, -36.9542]</code> represents a bounding box where the southwest corner has longitude <code>-12.7935</code> and latitude <code>-37.4835</code>, and the northeast corner has longitude <code>-12.0684</code> and latitude <code>-36.9542</code>.</p> <note> <p> <code>FilterBBox</code> and <code>BiasPosition</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_countries: <p>An optional parameter that limits the search results by returning only places that are in a specified list of countries.</p> <ul> <li> <p>Valid values include <a href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166</a> 3-digit country codes. For example, Australia uses three upper-case characters: <code>AUS</code>.</p> </li> </ul>
            max_results: <p>An optional parameter. The maximum number of results returned per request. </p> <p>The default: <code>50</code> </p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for <code>Athens, Greece</code>, with the <code>language</code> parameter set to <code>en</code>. The result found will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the result found will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            filter_categories: <p>A list of one or more Amazon Location categories to filter the returned places. If you include more than one category, the results will include results that match <i>any</i> of the categories listed.</p> <p>For more information about using categories, including a list of Amazon Location categories, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html">Categories and filtering</a>, in the <i>Amazon Location Service developer guide</i>.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.search_place_index_for_text_request.SearchPlaceIndexForTextRequest]",
        ) -> OperationResponse[
            "capo_location.types.search_place_index_for_text_response.SearchPlaceIndexForTextResponse"
        ]:
            import capo_location._operations.location_service.search_place_index_for_text

            output, http_response = (
                capo_location._operations.location_service.search_place_index_for_text.search_place_index_for_text(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.search_place_index_for_text_request.SearchPlaceIndexForTextRequest = {
            "index_name": index_name,
            "text": text,
        }
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter_b_box is not None:
            input_["filter_b_box"] = filter_b_box
        if filter_countries is not None:
            input_["filter_countries"] = filter_countries
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if filter_categories is not None:
            input_["filter_categories"] = filter_categories
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_route_calculator(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        data_source: str,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_route_calculator_response.CreateRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>CreateRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Creates a route calculator resource in your Amazon Web Services account.</p> <p>You can send requests to a route calculator resource to estimate travel time, distance, and get directions. A route calculator sources traffic and road network data from your chosen data provider.</p> <note> <p>If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the <a href="http://aws.amazon.com/service-terms">Amazon Web Services service terms</a> for more details.</p> </note>

        Args:
            calculator_name: <p>The name of the route calculator resource. </p> <p>Requirements:</p> <ul> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9) , hyphens (-), periods (.), and underscores (_).</p> </li> <li> <p>Must be a unique Route calculator resource name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleRouteCalculator</code>.</p> </li> </ul>
            data_source: <p>Specifies the data provider of traffic and road network data.</p> <note> <p>This field is case-sensitive. Enter the valid values as shown. For example, entering <code>HERE</code> returns an error.</p> </note> <p>Valid values include:</p> <ul> <li> <p> <code>Esri</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/esri.html">Esri</a>'s coverage in your region of interest, see <a href="https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm">Esri details on street networks and traffic coverage</a>.</p> <p>Route calculators that use Esri as a data source only calculate routes that are shorter than 400 km.</p> </li> <li> <p> <code>Grab</code> – Grab provides routing functionality for Southeast Asia. For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a>' coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area">GrabMaps countries and areas covered</a>.</p> </li> <li> <p> <code>Here</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/HERE.html">HERE Technologies</a>' coverage in your region of interest, see <a href="https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/car-routing.html">HERE car routing coverage</a> and <a href="https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/truck-routing.html">HERE truck routing coverage</a>.</p> </li> </ul> <p>For additional information , see <a href="https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html">Data providers</a> on the <i>Amazon Location Service Developer Guide</i>.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>The optional description for the route calculator resource.</p>
            tags: <p>Applies one or more tags to the route calculator resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.</p> <ul> <li> <p>For example: { <code>"tag1" : "value1"</code>, <code>"tag2" : "value2"</code>}</p> </li> </ul> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.create_route_calculator_request.CreateRouteCalculatorRequest]",
        ) -> OperationResponse[
            "capo_location.types.create_route_calculator_response.CreateRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.create_route_calculator

            output, http_response = (
                capo_location._operations.location_service.create_route_calculator.create_route_calculator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.create_route_calculator_request.CreateRouteCalculatorRequest = {
            "calculator_name": calculator_name,
            "data_source": data_source,
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_route_calculator(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.describe_route_calculator_response.DescribeRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DescribeRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves the route calculator resource details.</p>

        Args:
            calculator_name: <p>The name of the route calculator resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.describe_route_calculator_request.DescribeRouteCalculatorRequest]",
        ) -> OperationResponse[
            "capo_location.types.describe_route_calculator_response.DescribeRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.describe_route_calculator

            output, http_response = (
                capo_location._operations.location_service.describe_route_calculator.describe_route_calculator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.describe_route_calculator_request.DescribeRouteCalculatorRequest = {
            "calculator_name": calculator_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_route_calculator(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_location.types.update_route_calculator_response.UpdateRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>UpdateRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Updates the specified properties for a given route calculator resource.</p>

        Args:
            calculator_name: <p>The name of the route calculator resource to update.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>Updates the description for the route calculator resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.update_route_calculator_request.UpdateRouteCalculatorRequest]",
        ) -> OperationResponse[
            "capo_location.types.update_route_calculator_response.UpdateRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.update_route_calculator

            output, http_response = (
                capo_location._operations.location_service.update_route_calculator.update_route_calculator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.update_route_calculator_request.UpdateRouteCalculatorRequest = {
            "calculator_name": calculator_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_route_calculator(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.delete_route_calculator_response.DeleteRouteCalculatorResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DeleteRouteCalculator</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Deletes a route calculator resource from your Amazon Web Services account.</p> <note> <p>This operation deletes the resource permanently.</p> </note>

        Args:
            calculator_name: <p>The name of the route calculator resource to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.delete_route_calculator_request.DeleteRouteCalculatorRequest]",
        ) -> OperationResponse[
            "capo_location.types.delete_route_calculator_response.DeleteRouteCalculatorResponse"
        ]:
            import capo_location._operations.location_service.delete_route_calculator

            output, http_response = (
                capo_location._operations.location_service.delete_route_calculator.delete_route_calculator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.delete_route_calculator_request.DeleteRouteCalculatorRequest = {
            "calculator_name": calculator_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_route_calculators(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_route_calculators_response.ListRouteCalculatorsResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.</p> <ul> <li> <p> <code>ListRouteCalculators</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Lists route calculator resources in your Amazon Web Services account.</p>

        Args:
            max_results: <p>An optional maximum number of results returned in a single call.</p> <p>Default Value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default Value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_route_calculators_request.ListRouteCalculatorsRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_route_calculators_response.ListRouteCalculatorsResponse"
        ]:
            import capo_location._operations.location_service.list_route_calculators

            output, http_response = (
                capo_location._operations.location_service.list_route_calculators.list_route_calculators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_route_calculators_request.ListRouteCalculatorsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_route_calculators(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "Iterator[capo_location.types.list_route_calculators_response_entry.ListRouteCalculatorsResponseEntry]":
        _token = next_token
        while True:
            _response = self.list_route_calculators(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def calculate_route(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        departure_position: "capo_location.types.position.Position",
        destination_position: "capo_location.types.position.Position",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        waypoint_positions: Optional[
            "capo_location.types.waypoint_position_list.WaypointPositionList"
        ] = None,
        travel_mode: Optional["capo_location.types.travel_mode.TravelMode"] = None,
        departure_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        depart_now: Optional[
            "capo_location.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        distance_unit: Optional[
            "capo_location.types.distance_unit.DistanceUnit"
        ] = None,
        include_leg_geometry: Optional[
            "capo_location.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        car_mode_options: Optional[
            "capo_location.types.calculate_route_car_mode_options.CalculateRouteCarModeOptions"
        ] = None,
        truck_mode_options: Optional[
            "capo_location.types.calculate_route_truck_mode_options.CalculateRouteTruckModeOptions"
        ] = None,
        arrival_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        optimize_for: Optional[
            "capo_location.types.optimization_mode.OptimizationMode"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.calculate_route_response.CalculateRouteResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_CalculateRoutes.html"> <code>CalculateRoutes</code> </a> or <a href="/location/latest/APIReference/API_CalculateIsolines.html"> <code>CalculateIsolines</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>CalculateRoute</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>CalculateRoutes</code> operation gives better results for point-to-point routing, while the version 2 <code>CalculateIsolines</code> operation adds support for calculating service areas and travel time envelopes.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route.html">Calculates a route</a> given the following required parameters: <code>DeparturePosition</code> and <code>DestinationPosition</code>. Requires that you first <a href="https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html">create a route calculator resource</a>.</p> <p>By default, a request that doesn't specify a departure time uses the best time of day to travel with the best traffic conditions when calculating the route.</p> <p>Additional options include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html">Specifying a departure time</a> using either <code>DepartureTime</code> or <code>DepartNow</code>. This calculates a route based on predictive traffic data at the given time. </p> <note> <p>You can't specify both <code>DepartureTime</code> and <code>DepartNow</code> in a single request. Specifying both parameters returns a validation error.</p> </note> </li> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html">Specifying a travel mode</a> using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in <code>CarModeOptions</code> if traveling by <code>Car</code>, or <code>TruckModeOptions</code> if traveling by <code>Truck</code>.</p> <note> <p>If you specify <code>walking</code> for the travel mode and your data provider is Esri, the start and destination must be within 40km.</p> </note> </li> </ul>

        Args:
            calculator_name: <p>The name of the route calculator resource that you want to use to calculate the route. </p>
            departure_position: <p>The start position for the route. Defined in <a href="https://earth-info.nga.mil/index.php?dir=wgs84&amp;action=wgs84">World Geodetic System (WGS 84)</a> format: <code>[longitude, latitude]</code>.</p> <ul> <li> <p>For example, <code>[-123.115, 49.285]</code> </p> </li> </ul> <note> <p>If you specify a departure that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a <code>400 RoutesValidationException</code> error.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            destination_position: <p>The finish position for the route. Defined in <a href="https://earth-info.nga.mil/index.php?dir=wgs84&amp;action=wgs84">World Geodetic System (WGS 84)</a> format: <code>[longitude, latitude]</code>.</p> <ul> <li> <p> For example, <code>[-122.339, 47.615]</code> </p> </li> </ul> <note> <p>If you specify a destination that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. </p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            waypoint_positions: <p>Specifies an ordered list of up to 23 intermediate positions to include along a route between the departure position and destination position. </p> <ul> <li> <p>For example, from the <code>DeparturePosition</code> <code>[-123.115, 49.285]</code>, the route follows the order that the waypoint positions are given <code>[[-122.757, 49.0021],[-122.349, 47.620]]</code> </p> </li> </ul> <note> <p>If you specify a waypoint position that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">moves the position to the nearest road</a>. </p> <p>Specifying more than 23 waypoints returns a <code>400 ValidationException</code> error.</p> <p>If Esri is the provider for your route calculator, specifying a route that is longer than 400 km returns a <code>400 RoutesValidationException</code> error.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            travel_mode: <p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility. You can choose <code>Car</code>, <code>Truck</code>, <code>Walking</code>, <code>Bicycle</code> or <code>Motorcycle</code> as options for the <code>TravelMode</code>.</p> <note> <p> <code>Bicycle</code> and <code>Motorcycle</code> are only valid when using Grab as a data provider, and only within Southeast Asia.</p> <p> <code>Truck</code> is not available for Grab.</p> <p>For more details on the using Grab for routing, including areas of coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>The <code>TravelMode</code> you specify also determines how you specify route preferences: </p> <ul> <li> <p>If traveling by <code>Car</code> use the <code>CarModeOptions</code> parameter.</p> </li> <li> <p>If traveling by <code>Truck</code> use the <code>TruckModeOptions</code> parameter.</p> </li> </ul> <p>Default Value: <code>Car</code> </p>
            departure_time: <p>Specifies the desired time of departure. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <ul> <li> <p>In <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>
            depart_now: <p>Sets the time of departure as the current time. Uses the current time to calculate a route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>
            distance_unit: <p>Set the unit system to specify the distance.</p> <p>Default Value: <code>Kilometers</code> </p>
            include_leg_geometry: <p>Set to include the geometry details in the result for each path between a pair of positions.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>
            car_mode_options: <p>Specifies route preferences when traveling by <code>Car</code>, such as avoiding routes that use ferries or tolls.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Car</code>.</p>
            truck_mode_options: <p>Specifies route preferences when traveling by <code>Truck</code>, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Truck</code>.</p>
            arrival_time: <p>Specifies the desired time of arrival. Uses the given time to calculate the route. Otherwise, the best time of day to travel with the best traffic conditions is used to calculate the route.</p> <note> <p>ArrivalTime is not supported Esri.</p> </note>
            optimize_for: <p>Specifies the distance to optimize for when calculating a route.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.calculate_route_request.CalculateRouteRequest]",
        ) -> OperationResponse[
            "capo_location.types.calculate_route_response.CalculateRouteResponse"
        ]:
            import capo_location._operations.location_service.calculate_route

            output, http_response = (
                capo_location._operations.location_service.calculate_route.calculate_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.calculate_route_request.CalculateRouteRequest = {
            "calculator_name": calculator_name,
            "departure_position": departure_position,
            "destination_position": destination_position,
        }
        if waypoint_positions is not None:
            input_["waypoint_positions"] = waypoint_positions
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if depart_now is not None:
            input_["depart_now"] = depart_now
        if distance_unit is not None:
            input_["distance_unit"] = distance_unit
        if include_leg_geometry is not None:
            input_["include_leg_geometry"] = include_leg_geometry
        if car_mode_options is not None:
            input_["car_mode_options"] = car_mode_options
        if truck_mode_options is not None:
            input_["truck_mode_options"] = truck_mode_options
        if arrival_time is not None:
            input_["arrival_time"] = arrival_time
        if optimize_for is not None:
            input_["optimize_for"] = optimize_for
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def calculate_route_matrix(
        self,
        calculator_name: "capo_location.types.resource_name.ResourceName",
        departure_positions: "capo_location.types.position_list.PositionList",
        destination_positions: "capo_location.types.position_list.PositionList",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        travel_mode: Optional["capo_location.types.travel_mode.TravelMode"] = None,
        departure_time: Optional["capo_location.types.timestamp.Timestamp"] = None,
        depart_now: Optional[
            "capo_location.types.sensitive_boolean.SensitiveBoolean"
        ] = None,
        distance_unit: Optional[
            "capo_location.types.distance_unit.DistanceUnit"
        ] = None,
        car_mode_options: Optional[
            "capo_location.types.calculate_route_car_mode_options.CalculateRouteCarModeOptions"
        ] = None,
        truck_mode_options: Optional[
            "capo_location.types.calculate_route_truck_mode_options.CalculateRouteTruckModeOptions"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.calculate_route_matrix_response.CalculateRouteMatrixResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the <a href="/location/latest/APIReference/API_CalculateRouteMatrix.html">V2 <code>CalculateRouteMatrix</code> </a> unless you require Grab data.</p> <ul> <li> <p>This version of <code>CalculateRouteMatrix</code> is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>CalculateRouteMatrix</code> operation gives better results for matrix routing calculations.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Routes API version 2 is found under <code>geo-routes</code> or <code>geo_routes</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Routes V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/routes.html">Developer Guide</a>.</p> </li> </ul> </important> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html"> Calculates a route matrix</a> given the following required parameters: <code>DeparturePositions</code> and <code>DestinationPositions</code>. <code>CalculateRouteMatrix</code> calculates routes and returns the travel time and travel distance from each departure position to each destination position in the request. For example, given departure positions A and B, and destination positions X and Y, <code>CalculateRouteMatrix</code> will return time and distance for routes from A to X, A to Y, B to X, and B to Y (in that order). The number of results returned (and routes calculated) will be the number of <code>DeparturePositions</code> times the number of <code>DestinationPositions</code>.</p> <note> <p>Your account is charged for each route calculated, not the number of requests.</p> </note> <p>Requires that you first <a href="https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html">create a route calculator resource</a>.</p> <p>By default, a request that doesn't specify a departure time uses the best time of day to travel with the best traffic conditions when calculating routes.</p> <p>Additional options include:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html"> Specifying a departure time</a> using either <code>DepartureTime</code> or <code>DepartNow</code>. This calculates routes based on predictive traffic data at the given time. </p> <note> <p>You can't specify both <code>DepartureTime</code> and <code>DepartNow</code> in a single request. Specifying both parameters returns a validation error.</p> </note> </li> <li> <p> <a href="https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html">Specifying a travel mode</a> using TravelMode sets the transportation mode used to calculate the routes. This also lets you specify additional route preferences in <code>CarModeOptions</code> if traveling by <code>Car</code>, or <code>TruckModeOptions</code> if traveling by <code>Truck</code>.</p> </li> </ul>

        Args:
            calculator_name: <p>The name of the route calculator resource that you want to use to calculate the route matrix. </p>
            departure_positions: <p>The list of departure (origin) positions for the route matrix. An array of points, each of which is itself a 2-value array defined in <a href="https://earth-info.nga.mil/GandG/wgs84/index.html">WGS 84</a> format: <code>[longitude, latitude]</code>. For example, <code>[-123.115, 49.285]</code>.</p> <important> <p>Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits"> Position restrictions</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </important> <note> <p>For route calculators that use Esri as the data provider, if you specify a departure that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html"> moves the position to the nearest road</a>. The snapped value is available in the result in <code>SnappedDeparturePositions</code>.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            destination_positions: <p>The list of destination positions for the route matrix. An array of points, each of which is itself a 2-value array defined in <a href="https://earth-info.nga.mil/GandG/wgs84/index.html">WGS 84</a> format: <code>[longitude, latitude]</code>. For example, <code>[-122.339, 47.615]</code> </p> <important> <p>Depending on the data provider selected in the route calculator resource there may be additional restrictions on the inputs you can choose. See <a href="https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html#matrix-routing-position-limits"> Position restrictions</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </important> <note> <p>For route calculators that use Esri as the data provider, if you specify a destination that's not located on a road, Amazon Location <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html"> moves the position to the nearest road</a>. The snapped value is available in the result in <code>SnappedDestinationPositions</code>.</p> </note> <p>Valid Values: <code>[-180 to 180,-90 to 90]</code> </p>
            travel_mode: <p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>The <code>TravelMode</code> you specify also determines how you specify route preferences: </p> <ul> <li> <p>If traveling by <code>Car</code> use the <code>CarModeOptions</code> parameter.</p> </li> <li> <p>If traveling by <code>Truck</code> use the <code>TruckModeOptions</code> parameter.</p> </li> </ul> <note> <p> <code>Bicycle</code> or <code>Motorcycle</code> are only valid when using <code>Grab</code> as a data provider, and only within Southeast Asia.</p> <p> <code>Truck</code> is not available for Grab.</p> <p>For more information about using Grab as a data provider, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a> in the <i>Amazon Location Service Developer Guide</i>.</p> </note> <p>Default Value: <code>Car</code> </p>
            departure_time: <p>Specifies the desired time of departure. Uses the given time to calculate the route matrix. You can't set both <code>DepartureTime</code> and <code>DepartNow</code>. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.</p> <note> <p>Setting a departure time in the past returns a <code>400 ValidationException</code> error.</p> </note> <ul> <li> <p>In <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>
            depart_now: <p>Sets the time of departure as the current time. Uses the current time to calculate the route matrix. You can't set both <code>DepartureTime</code> and <code>DepartNow</code>. If neither is set, the best time of day to travel with the best traffic conditions is used to calculate the route matrix.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>
            distance_unit: <p>Set the unit system to specify the distance.</p> <p>Default Value: <code>Kilometers</code> </p>
            car_mode_options: <p>Specifies route preferences when traveling by <code>Car</code>, such as avoiding routes that use ferries or tolls.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Car</code>.</p>
            truck_mode_options: <p>Specifies route preferences when traveling by <code>Truck</code>, such as avoiding routes that use ferries or tolls, and truck specifications to consider when choosing an optimal road.</p> <p>Requirements: <code>TravelMode</code> must be specified as <code>Truck</code>.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.calculate_route_matrix_request.CalculateRouteMatrixRequest]",
        ) -> OperationResponse[
            "capo_location.types.calculate_route_matrix_response.CalculateRouteMatrixResponse"
        ]:
            import capo_location._operations.location_service.calculate_route_matrix

            output, http_response = (
                capo_location._operations.location_service.calculate_route_matrix.calculate_route_matrix(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.calculate_route_matrix_request.CalculateRouteMatrixRequest = {
            "calculator_name": calculator_name,
            "departure_positions": departure_positions,
            "destination_positions": destination_positions,
        }
        if travel_mode is not None:
            input_["travel_mode"] = travel_mode
        if departure_time is not None:
            input_["departure_time"] = departure_time
        if depart_now is not None:
            input_["depart_now"] = depart_now
        if distance_unit is not None:
            input_["distance_unit"] = distance_unit
        if car_mode_options is not None:
            input_["car_mode_options"] = car_mode_options
        if truck_mode_options is not None:
            input_["truck_mode_options"] = truck_mode_options
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_tracker(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        kms_key_id: Optional["capo_location.types.kms_key_id.KmsKeyId"] = None,
        pricing_plan_data_source: Optional[str] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
        position_filtering: Optional[
            "capo_location.types.position_filtering.PositionFiltering"
        ] = None,
        event_bridge_enabled: Optional[bool] = None,
        kms_key_enable_geospatial_queries: Optional[bool] = None,
    ) -> "capo_location.types.create_tracker_response.CreateTrackerResponse":
        """<p>Creates a tracker resource in your Amazon Web Services account, which lets you retrieve current and historical location of devices.</p>

        Args:
            tracker_name: <p>The name for the tracker resource.</p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (_).</p> </li> <li> <p>Must be a unique tracker resource name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleTracker</code>.</p> </li> </ul>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            kms_key_id: <p>A key identifier for an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a>. Enter a key ID, key ARN, alias name, or alias ARN.</p>
            pricing_plan_data_source: <p>This parameter is no longer used.</p>
            description: <p>An optional description for the tracker resource.</p>
            tags: <p>Applies one or more tags to the tracker resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>
            position_filtering: <p>Specifies the position filtering for the tracker resource.</p> <p>Valid values:</p> <ul> <li> <p> <code>TimeBased</code> - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID. </p> </li> <li> <p> <code>DistanceBased</code> - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this area are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map. </p> </li> <li> <p> <code>AccuracyBased</code> - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This can reduce the effects of GPS noise when displaying device trajectories on a map, and can help control your costs by reducing the number of geofence evaluations. </p> </li> </ul> <p>This field is optional. If not specified, the default value is <code>TimeBased</code>.</p>
            event_bridge_enabled: <p>Whether to enable position <code>UPDATE</code> events from this tracker to be sent to EventBridge.</p> <note> <p>You do not need enable this feature to get <code>ENTER</code> and <code>EXIT</code> events for geofences with this tracker. Those events are always sent to EventBridge.</p> </note>
            kms_key_enable_geospatial_queries: <p>Enables <code>GeospatialQueries</code> for a tracker that uses a <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a>.</p> <p>This parameter is only used if you are using a KMS customer managed key.</p> <note> <p>If you wish to encrypt your data using your own KMS customer managed key, then the Bounding Polygon Queries feature will be disabled by default. This is because by using this feature, a representation of your device positions will not be encrypted using the your KMS managed key. The exact device position, however; is still encrypted using your managed key.</p> <p>You can choose to opt-in to the Bounding Polygon Quseries feature. This is done by setting the <code>KmsKeyEnableGeospatialQueries</code> parameter to true when creating or updating a Tracker.</p> </note>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.create_tracker_request.CreateTrackerRequest]",
        ) -> OperationResponse[
            "capo_location.types.create_tracker_response.CreateTrackerResponse"
        ]:
            import capo_location._operations.location_service.create_tracker

            output, http_response = (
                capo_location._operations.location_service.create_tracker.create_tracker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.create_tracker_request.CreateTrackerRequest = {
            "tracker_name": tracker_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if pricing_plan_data_source is not None:
            input_["pricing_plan_data_source"] = pricing_plan_data_source
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if position_filtering is not None:
            input_["position_filtering"] = position_filtering
        if event_bridge_enabled is not None:
            input_["event_bridge_enabled"] = event_bridge_enabled
        if kms_key_enable_geospatial_queries is not None:
            input_["kms_key_enable_geospatial_queries"] = (
                kms_key_enable_geospatial_queries
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_tracker(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.describe_tracker_response.DescribeTrackerResponse":
        """<p>Retrieves the tracker resource details.</p>

        Args:
            tracker_name: <p>The name of the tracker resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.describe_tracker_request.DescribeTrackerRequest]",
        ) -> OperationResponse[
            "capo_location.types.describe_tracker_response.DescribeTrackerResponse"
        ]:
            import capo_location._operations.location_service.describe_tracker

            output, http_response = (
                capo_location._operations.location_service.describe_tracker.describe_tracker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.describe_tracker_request.DescribeTrackerRequest = {
            "tracker_name": tracker_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_tracker(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        pricing_plan_data_source: Optional[str] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        position_filtering: Optional[
            "capo_location.types.position_filtering.PositionFiltering"
        ] = None,
        event_bridge_enabled: Optional[bool] = None,
        kms_key_enable_geospatial_queries: Optional[bool] = None,
    ) -> "capo_location.types.update_tracker_response.UpdateTrackerResponse":
        """<p>Updates the specified properties of a given tracker resource.</p>

        Args:
            tracker_name: <p>The name of the tracker resource to update.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            pricing_plan_data_source: <p>This parameter is no longer used.</p>
            description: <p>Updates the description for the tracker resource.</p>
            position_filtering: <p>Updates the position filtering for the tracker resource.</p> <p>Valid values:</p> <ul> <li> <p> <code>TimeBased</code> - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID. </p> </li> <li> <p> <code>DistanceBased</code> - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this distance are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map. </p> </li> <li> <p> <code>AccuracyBased</code> - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This helps educe the effects of GPS noise when displaying device trajectories on a map, and can help control costs by reducing the number of geofence evaluations. </p> </li> </ul>
            event_bridge_enabled: <p>Whether to enable position <code>UPDATE</code> events from this tracker to be sent to EventBridge.</p> <note> <p>You do not need enable this feature to get <code>ENTER</code> and <code>EXIT</code> events for geofences with this tracker. Those events are always sent to EventBridge.</p> </note>
            kms_key_enable_geospatial_queries: <p>Enables <code>GeospatialQueries</code> for a tracker that uses a <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a>.</p> <p>This parameter is only used if you are using a KMS customer managed key.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.update_tracker_request.UpdateTrackerRequest]",
        ) -> OperationResponse[
            "capo_location.types.update_tracker_response.UpdateTrackerResponse"
        ]:
            import capo_location._operations.location_service.update_tracker

            output, http_response = (
                capo_location._operations.location_service.update_tracker.update_tracker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.update_tracker_request.UpdateTrackerRequest = {
            "tracker_name": tracker_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if pricing_plan_data_source is not None:
            input_["pricing_plan_data_source"] = pricing_plan_data_source
        if description is not None:
            input_["description"] = description
        if position_filtering is not None:
            input_["position_filtering"] = position_filtering
        if event_bridge_enabled is not None:
            input_["event_bridge_enabled"] = event_bridge_enabled
        if kms_key_enable_geospatial_queries is not None:
            input_["kms_key_enable_geospatial_queries"] = (
                kms_key_enable_geospatial_queries
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_tracker(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.delete_tracker_response.DeleteTrackerResponse":
        """<p>Deletes a tracker resource from your Amazon Web Services account.</p> <note> <p>This operation deletes the resource permanently. If the tracker resource is in use, you may encounter an error. Make sure that the target resource isn't a dependency for your applications.</p> </note>

        Args:
            tracker_name: <p>The name of the tracker resource to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.delete_tracker_request.DeleteTrackerRequest]",
        ) -> OperationResponse[
            "capo_location.types.delete_tracker_response.DeleteTrackerResponse"
        ]:
            import capo_location._operations.location_service.delete_tracker

            output, http_response = (
                capo_location._operations.location_service.delete_tracker.delete_tracker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.delete_tracker_request.DeleteTrackerRequest = {
            "tracker_name": tracker_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_trackers(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_trackers_response.ListTrackersResponse":
        """<p>Lists tracker resources in your Amazon Web Services account.</p>

        Args:
            max_results: <p>An optional limit for the number of resources returned in a single call. </p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_trackers_request.ListTrackersRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_trackers_response.ListTrackersResponse"
        ]:
            import capo_location._operations.location_service.list_trackers

            output, http_response = (
                capo_location._operations.location_service.list_trackers.list_trackers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_trackers_request.ListTrackersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_trackers(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "Iterator[capo_location.types.list_trackers_response_entry.ListTrackersResponseEntry]":
        _token = next_token
        while True:
            _response = self.list_trackers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_tracker_consumer(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        consumer_arn: "capo_location.types.arn.Arn",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.associate_tracker_consumer_response.AssociateTrackerConsumerResponse":
        """<p>Creates an association between a geofence collection and a tracker resource. This allows the tracker resource to communicate location data to the linked geofence collection. </p> <p>You can associate up to five geofence collections to each tracker resource.</p> <note> <p>Currently not supported — Cross-account configurations, such as creating associations between a tracker resource in one account and a geofence collection in another account.</p> </note>

        Args:
            tracker_name: <p>The name of the tracker resource to be associated with a geofence collection.</p>
            consumer_arn: <p>The Amazon Resource Name (ARN) for the geofence collection to be associated to tracker resource. Used when you need to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer</code> </p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.associate_tracker_consumer_request.AssociateTrackerConsumerRequest]",
        ) -> OperationResponse[
            "capo_location.types.associate_tracker_consumer_response.AssociateTrackerConsumerResponse"
        ]:
            import capo_location._operations.location_service.associate_tracker_consumer

            output, http_response = (
                capo_location._operations.location_service.associate_tracker_consumer.associate_tracker_consumer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.associate_tracker_consumer_request.AssociateTrackerConsumerRequest = {
            "tracker_name": tracker_name,
            "consumer_arn": consumer_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_device_position_history(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_ids: "capo_location.types.device_ids_list.DeviceIdsList",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.batch_delete_device_position_history_response.BatchDeleteDevicePositionHistoryResponse":
        """<p>Deletes the position history of one or more devices from a tracker resource.</p>

        Args:
            tracker_name: <p>The name of the tracker resource to delete the device position history from.</p>
            device_ids: <p>Devices whose position history you want to delete.</p> <ul> <li> <p>For example, for two devices: <code>“DeviceIds” : [DeviceId1,DeviceId2]</code> </p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.batch_delete_device_position_history_request.BatchDeleteDevicePositionHistoryRequest]",
        ) -> OperationResponse[
            "capo_location.types.batch_delete_device_position_history_response.BatchDeleteDevicePositionHistoryResponse"
        ]:
            import capo_location._operations.location_service.batch_delete_device_position_history

            output, http_response = (
                capo_location._operations.location_service.batch_delete_device_position_history.batch_delete_device_position_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.batch_delete_device_position_history_request.BatchDeleteDevicePositionHistoryRequest = {
            "tracker_name": tracker_name,
            "device_ids": device_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_device_position(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_ids: "capo_location.types.id_list.IdList",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.batch_get_device_position_response.BatchGetDevicePositionResponse":
        """<p>Lists the latest device positions for requested devices.</p>

        Args:
            tracker_name: <p>The tracker resource retrieving the device position.</p>
            device_ids: <p>Devices whose position you want to retrieve.</p> <ul> <li> <p>For example, for two devices: <code>device-ids=DeviceId1&amp;device-ids=DeviceId2</code> </p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.batch_get_device_position_request.BatchGetDevicePositionRequest]",
        ) -> OperationResponse[
            "capo_location.types.batch_get_device_position_response.BatchGetDevicePositionResponse"
        ]:
            import capo_location._operations.location_service.batch_get_device_position

            output, http_response = (
                capo_location._operations.location_service.batch_get_device_position.batch_get_device_position(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.batch_get_device_position_request.BatchGetDevicePositionRequest = {
            "tracker_name": tracker_name,
            "device_ids": device_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_device_position(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        updates: "capo_location.types.device_position_update_list.DevicePositionUpdateList",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.batch_update_device_position_response.BatchUpdateDevicePositionResponse":
        """<p>Uploads position update data for one or more devices to a tracker resource (up to 10 devices per batch). Amazon Location uses the data when it reports the last known device position and position history. Amazon Location retains location data for 30 days.</p> <note> <p>Position updates are handled based on the <code>PositionFiltering</code> property of the tracker. When <code>PositionFiltering</code> is set to <code>TimeBased</code>, updates are evaluated against linked geofence collections, and location data is stored at a maximum of one position per 30 second interval. If your update frequency is more often than every 30 seconds, only one update per 30 seconds is stored for each unique device ID.</p> <p>When <code>PositionFiltering</code> is set to <code>DistanceBased</code> filtering, location data is stored and evaluated against linked geofence collections only if the device has moved more than 30 m (98.4 ft).</p> <p>When <code>PositionFiltering</code> is set to <code>AccuracyBased</code> filtering, location data is stored and evaluated against linked geofence collections only if the device has moved more than the measured accuracy. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is neither stored or evaluated if the device has moved less than 15 m. If <code>PositionFiltering</code> is set to <code>AccuracyBased</code> filtering, Amazon Location uses the default value <code>{ "Horizontal": 0}</code> when accuracy is not provided on a <code>DevicePositionUpdate</code>.</p> </note>

        Args:
            tracker_name: <p>The name of the tracker resource to update.</p>
            updates: <p>Contains the position update details for each device, up to 10 devices.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.batch_update_device_position_request.BatchUpdateDevicePositionRequest]",
        ) -> OperationResponse[
            "capo_location.types.batch_update_device_position_response.BatchUpdateDevicePositionResponse"
        ]:
            import capo_location._operations.location_service.batch_update_device_position

            output, http_response = (
                capo_location._operations.location_service.batch_update_device_position.batch_update_device_position(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.batch_update_device_position_request.BatchUpdateDevicePositionRequest = {
            "tracker_name": tracker_name,
            "updates": updates,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_tracker_consumer(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        consumer_arn: "capo_location.types.arn.Arn",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.disassociate_tracker_consumer_response.DisassociateTrackerConsumerResponse":
        """<p>Removes the association between a tracker resource and a geofence collection.</p> <note> <p>Once you unlink a tracker resource from a geofence collection, the tracker positions will no longer be automatically evaluated against geofences.</p> </note>

        Args:
            tracker_name: <p>The name of the tracker resource to be dissociated from the consumer.</p>
            consumer_arn: <p>The Amazon Resource Name (ARN) for the geofence collection to be disassociated from the tracker resource. Used when you need to specify a resource across all Amazon Web Services. </p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollectionConsumer</code> </p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.disassociate_tracker_consumer_request.DisassociateTrackerConsumerRequest]",
        ) -> OperationResponse[
            "capo_location.types.disassociate_tracker_consumer_response.DisassociateTrackerConsumerResponse"
        ]:
            import capo_location._operations.location_service.disassociate_tracker_consumer

            output, http_response = (
                capo_location._operations.location_service.disassociate_tracker_consumer.disassociate_tracker_consumer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.disassociate_tracker_consumer_request.DisassociateTrackerConsumerRequest = {
            "tracker_name": tracker_name,
            "consumer_arn": consumer_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_device_position(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_id: "capo_location.types.id.Id",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.get_device_position_response.GetDevicePositionResponse":
        """<p>Retrieves a device's most recent position according to its sample time.</p> <note> <p>Device positions are deleted after 30 days.</p> </note>

        Args:
            tracker_name: <p>The tracker resource receiving the position update.</p>
            device_id: <p>The device whose position you want to retrieve.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_device_position_request.GetDevicePositionRequest]",
        ) -> OperationResponse[
            "capo_location.types.get_device_position_response.GetDevicePositionResponse"
        ]:
            import capo_location._operations.location_service.get_device_position

            output, http_response = (
                capo_location._operations.location_service.get_device_position.get_device_position(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.get_device_position_request.GetDevicePositionRequest = {
            "tracker_name": tracker_name,
            "device_id": device_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_device_position_history(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_id: "capo_location.types.id.Id",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
        start_time_inclusive: Optional[
            "capo_location.types.timestamp.Timestamp"
        ] = None,
        end_time_exclusive: Optional["capo_location.types.timestamp.Timestamp"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_location.types.get_device_position_history_response.GetDevicePositionHistoryResponse":
        """<p>Retrieves the device position history from a tracker resource within a specified range of time.</p> <note> <p>Device positions are deleted after 30 days.</p> </note>

        Args:
            tracker_name: <p>The tracker resource receiving the request for the device position history.</p>
            device_id: <p>The device whose position history you want to retrieve.</p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>
            start_time_inclusive: <p>Specify the start time for the position history in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. By default, the value will be 24 hours prior to the time that the request is made.</p> <p>Requirement:</p> <ul> <li> <p>The time specified for <code>StartTimeInclusive</code> must be before <code>EndTimeExclusive</code>.</p> </li> </ul>
            end_time_exclusive: <p>Specify the end time for the position history in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. By default, the value will be the time that the request is made.</p> <p>Requirement:</p> <ul> <li> <p>The time specified for <code>EndTimeExclusive</code> must be after the time for <code>StartTimeInclusive</code>.</p> </li> </ul>
            max_results: <p>An optional limit for the number of device positions returned in a single call.</p> <p>Default value: <code>100</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_device_position_history_request.GetDevicePositionHistoryRequest]",
        ) -> OperationResponse[
            "capo_location.types.get_device_position_history_response.GetDevicePositionHistoryResponse"
        ]:
            import capo_location._operations.location_service.get_device_position_history

            output, http_response = (
                capo_location._operations.location_service.get_device_position_history.get_device_position_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.get_device_position_history_request.GetDevicePositionHistoryRequest = {
            "tracker_name": tracker_name,
            "device_id": device_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if start_time_inclusive is not None:
            input_["start_time_inclusive"] = start_time_inclusive
        if end_time_exclusive is not None:
            input_["end_time_exclusive"] = end_time_exclusive
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_device_position_history(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_id: "capo_location.types.id.Id",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
        start_time_inclusive: Optional[
            "capo_location.types.timestamp.Timestamp"
        ] = None,
        end_time_exclusive: Optional["capo_location.types.timestamp.Timestamp"] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_location.types.device_position.DevicePosition]":
        _token = next_token
        while True:
            _response = self.get_device_position_history(
                tracker_name,
                device_id,
                config_overrides=config_overrides,
                next_token=_token,
                start_time_inclusive=start_time_inclusive,
                end_time_exclusive=end_time_exclusive,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("device_positions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_device_positions(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
        filter_geometry: Optional[
            "capo_location.types.tracking_filter_geometry.TrackingFilterGeometry"
        ] = None,
    ) -> (
        "capo_location.types.list_device_positions_response.ListDevicePositionsResponse"
    ):
        """<p>A batch request to retrieve all device positions.</p>

        Args:
            tracker_name: <p>The tracker resource containing the requested devices.</p>
            max_results: <p>An optional limit for the number of entries returned in a single call.</p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default value: <code>null</code> </p>
            filter_geometry: <p>The geometry used to filter device positions.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_device_positions_request.ListDevicePositionsRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_device_positions_response.ListDevicePositionsResponse"
        ]:
            import capo_location._operations.location_service.list_device_positions

            output, http_response = (
                capo_location._operations.location_service.list_device_positions.list_device_positions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_device_positions_request.ListDevicePositionsRequest = {
            "tracker_name": tracker_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_geometry is not None:
            input_["filter_geometry"] = filter_geometry

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_device_positions(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
        filter_geometry: Optional[
            "capo_location.types.tracking_filter_geometry.TrackingFilterGeometry"
        ] = None,
    ) -> "Iterator[capo_location.types.list_device_positions_response_entry.ListDevicePositionsResponseEntry]":
        _token = next_token
        while True:
            _response = self.list_device_positions(
                tracker_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter_geometry=filter_geometry,
            )
            _page = _resolve_path(_response, ("entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tracker_consumers(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_tracker_consumers_response.ListTrackerConsumersResponse":
        """<p>Lists geofence collections currently associated to the given tracker resource.</p>

        Args:
            tracker_name: <p>The tracker resource whose associated geofence collections you want to list.</p>
            max_results: <p>An optional limit for the number of resources returned in a single call. </p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_tracker_consumers_request.ListTrackerConsumersRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_tracker_consumers_response.ListTrackerConsumersResponse"
        ]:
            import capo_location._operations.location_service.list_tracker_consumers

            output, http_response = (
                capo_location._operations.location_service.list_tracker_consumers.list_tracker_consumers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.list_tracker_consumers_request.ListTrackerConsumersRequest = {
            "tracker_name": tracker_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_tracker_consumers(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "Iterator[capo_location.types.arn.Arn]":
        _token = next_token
        while True:
            _response = self.list_tracker_consumers(
                tracker_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("consumer_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def verify_device_position(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_state: "capo_location.types.device_state.DeviceState",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        distance_unit: Optional[
            "capo_location.types.distance_unit.DistanceUnit"
        ] = None,
    ) -> "capo_location.types.verify_device_position_response.VerifyDevicePositionResponse":
        """<p>Verifies the integrity of the device's position by determining if it was reported behind a proxy, and by comparing it to an inferred position estimated based on the device's state.</p> <note> <p>The Location Integrity SDK provides enhanced features related to device verification, and it is available for use by request. To get access to the SDK, contact <a href="https://aws.amazon.com/contact-us/sales-support/?pg=locationprice&amp;cta=herobtn">Sales Support</a>.</p> </note>

        Args:
            tracker_name: <p>The name of the tracker resource to be associated with verification request.</p>
            device_state: <p>The device's state, including position, IP address, cell signals and Wi-Fi access points.</p>
            distance_unit: <p>The distance unit for the verification request.</p> <p>Default Value: <code>Kilometers</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.verify_device_position_request.VerifyDevicePositionRequest]",
        ) -> OperationResponse[
            "capo_location.types.verify_device_position_response.VerifyDevicePositionResponse"
        ]:
            import capo_location._operations.location_service.verify_device_position

            output, http_response = (
                capo_location._operations.location_service.verify_device_position.verify_device_position(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_location.types.verify_device_position_request.VerifyDevicePositionRequest = {
            "tracker_name": tracker_name,
            "device_state": device_state,
        }
        if distance_unit is not None:
            input_["distance_unit"] = distance_unit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
