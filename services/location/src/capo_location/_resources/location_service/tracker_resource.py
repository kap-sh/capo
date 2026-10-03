from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_location._auth._signers
import capo_location._auth._sigv4
from capo_location._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_location.types.arn
    import capo_location.types.associate_tracker_consumer_request
    import capo_location.types.associate_tracker_consumer_response
    import capo_location.types.batch_delete_device_position_history_request
    import capo_location.types.batch_delete_device_position_history_response
    import capo_location.types.batch_get_device_position_request
    import capo_location.types.batch_get_device_position_response
    import capo_location.types.batch_update_device_position_request
    import capo_location.types.batch_update_device_position_response
    import capo_location.types.create_tracker_request
    import capo_location.types.create_tracker_response
    import capo_location.types.delete_tracker_request
    import capo_location.types.delete_tracker_response
    import capo_location.types.describe_tracker_request
    import capo_location.types.describe_tracker_response
    import capo_location.types.device_ids_list
    import capo_location.types.device_position
    import capo_location.types.device_position_update_list
    import capo_location.types.device_state
    import capo_location.types.disassociate_tracker_consumer_request
    import capo_location.types.disassociate_tracker_consumer_response
    import capo_location.types.distance_unit
    import capo_location.types.get_device_position_history_request
    import capo_location.types.get_device_position_history_response
    import capo_location.types.get_device_position_request
    import capo_location.types.get_device_position_response
    import capo_location.types.id
    import capo_location.types.id_list
    import capo_location.types.kms_key_id
    import capo_location.types.list_device_positions_request
    import capo_location.types.list_device_positions_response
    import capo_location.types.list_device_positions_response_entry
    import capo_location.types.list_tracker_consumers_request
    import capo_location.types.list_tracker_consumers_response
    import capo_location.types.list_trackers_request
    import capo_location.types.list_trackers_response
    import capo_location.types.list_trackers_response_entry
    import capo_location.types.position_filtering
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map
    import capo_location.types.timestamp
    import capo_location.types.token
    import capo_location.types.tracking_filter_geometry
    import capo_location.types.update_tracker_request
    import capo_location.types.update_tracker_response
    import capo_location.types.verify_device_position_request
    import capo_location.types.verify_device_position_response
    from capo_location._services.async_location import (
        AsyncLocationClient,
        AsyncLocationClientConfig,
    )
    from capo_location._services.location import LocationClient, LocationClientConfig


class TrackerResource:
    def __init__(self, service: LocationClient) -> None:
        self._service = service

    def put(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def update(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncTrackerResource:
    def __init__(self, service: AsyncLocationClient) -> None:
        self._service = service

    async def put(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.create_tracker_request.CreateTrackerRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.create_tracker_response.CreateTrackerResponse"
        ]:
            import capo_location._operations.location_service.create_tracker

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.create_tracker.async_create_tracker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.describe_tracker_request.DescribeTrackerRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.describe_tracker_response.DescribeTrackerResponse"
        ]:
            import capo_location._operations.location_service.describe_tracker

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.describe_tracker.async_describe_tracker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.describe_tracker_request.DescribeTrackerRequest = {
            "tracker_name": tracker_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.update_tracker_request.UpdateTrackerRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.update_tracker_response.UpdateTrackerResponse"
        ]:
            import capo_location._operations.location_service.update_tracker

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.update_tracker.async_update_tracker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.delete_tracker_request.DeleteTrackerRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.delete_tracker_response.DeleteTrackerResponse"
        ]:
            import capo_location._operations.location_service.delete_tracker

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.delete_tracker.async_delete_tracker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.delete_tracker_request.DeleteTrackerRequest = {
            "tracker_name": tracker_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.list_trackers_request.ListTrackersRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.list_trackers_response.ListTrackersResponse"
        ]:
            import capo_location._operations.location_service.list_trackers

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.list_trackers.async_list_trackers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_trackers_request.ListTrackersRequest = {}
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

    async def associate_tracker_consumer(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        consumer_arn: "capo_location.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.associate_tracker_consumer_request.AssociateTrackerConsumerRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.associate_tracker_consumer_response.AssociateTrackerConsumerResponse"
        ]:
            import capo_location._operations.location_service.associate_tracker_consumer

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.associate_tracker_consumer.async_associate_tracker_consumer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.associate_tracker_consumer_request.AssociateTrackerConsumerRequest = {
            "tracker_name": tracker_name,
            "consumer_arn": consumer_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_device_position_history(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_ids: "capo_location.types.device_ids_list.DeviceIdsList",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.batch_delete_device_position_history_request.BatchDeleteDevicePositionHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.batch_delete_device_position_history_response.BatchDeleteDevicePositionHistoryResponse"
        ]:
            import capo_location._operations.location_service.batch_delete_device_position_history

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.batch_delete_device_position_history.async_batch_delete_device_position_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.batch_delete_device_position_history_request.BatchDeleteDevicePositionHistoryRequest = {
            "tracker_name": tracker_name,
            "device_ids": device_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_device_position(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_ids: "capo_location.types.id_list.IdList",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.batch_get_device_position_request.BatchGetDevicePositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.batch_get_device_position_response.BatchGetDevicePositionResponse"
        ]:
            import capo_location._operations.location_service.batch_get_device_position

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.batch_get_device_position.async_batch_get_device_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.batch_get_device_position_request.BatchGetDevicePositionRequest = {
            "tracker_name": tracker_name,
            "device_ids": device_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_device_position(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        updates: "capo_location.types.device_position_update_list.DevicePositionUpdateList",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.batch_update_device_position_request.BatchUpdateDevicePositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.batch_update_device_position_response.BatchUpdateDevicePositionResponse"
        ]:
            import capo_location._operations.location_service.batch_update_device_position

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.batch_update_device_position.async_batch_update_device_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.batch_update_device_position_request.BatchUpdateDevicePositionRequest = {
            "tracker_name": tracker_name,
            "updates": updates,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_tracker_consumer(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        consumer_arn: "capo_location.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.disassociate_tracker_consumer_request.DisassociateTrackerConsumerRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.disassociate_tracker_consumer_response.DisassociateTrackerConsumerResponse"
        ]:
            import capo_location._operations.location_service.disassociate_tracker_consumer

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.disassociate_tracker_consumer.async_disassociate_tracker_consumer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.disassociate_tracker_consumer_request.DisassociateTrackerConsumerRequest = {
            "tracker_name": tracker_name,
            "consumer_arn": consumer_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_device_position(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_id: "capo_location.types.id.Id",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.get_device_position_request.GetDevicePositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.get_device_position_response.GetDevicePositionResponse"
        ]:
            import capo_location._operations.location_service.get_device_position

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.get_device_position.async_get_device_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.get_device_position_request.GetDevicePositionRequest = {
            "tracker_name": tracker_name,
            "device_id": device_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_device_position_history(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_id: "capo_location.types.id.Id",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.get_device_position_history_request.GetDevicePositionHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.get_device_position_history_response.GetDevicePositionHistoryResponse"
        ]:
            import capo_location._operations.location_service.get_device_position_history

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.get_device_position_history.async_get_device_position_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_device_positions(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.list_device_positions_request.ListDevicePositionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.list_device_positions_response.ListDevicePositionsResponse"
        ]:
            import capo_location._operations.location_service.list_device_positions

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.list_device_positions.async_list_device_positions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_device_positions_request.ListDevicePositionsRequest = {
            "tracker_name": tracker_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_geometry is not None:
            input_["filter_geometry"] = filter_geometry

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tracker_consumers(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.list_tracker_consumers_request.ListTrackerConsumersRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.list_tracker_consumers_response.ListTrackerConsumersResponse"
        ]:
            import capo_location._operations.location_service.list_tracker_consumers

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.list_tracker_consumers.async_list_tracker_consumers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_tracker_consumers_request.ListTrackerConsumersRequest = {
            "tracker_name": tracker_name
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

    async def verify_device_position(
        self,
        tracker_name: "capo_location.types.resource_name.ResourceName",
        device_state: "capo_location.types.device_state.DeviceState",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.verify_device_position_request.VerifyDevicePositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.verify_device_position_response.VerifyDevicePositionResponse"
        ]:
            import capo_location._operations.location_service.verify_device_position

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.verify_device_position.async_verify_device_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.verify_device_position_request.VerifyDevicePositionRequest = {
            "tracker_name": tracker_name,
            "device_state": device_state,
        }
        if distance_unit is not None:
            input_["distance_unit"] = distance_unit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
