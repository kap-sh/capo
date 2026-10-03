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
    import capo_location.types.batch_delete_geofence_request
    import capo_location.types.batch_delete_geofence_response
    import capo_location.types.batch_evaluate_geofences_request
    import capo_location.types.batch_evaluate_geofences_response
    import capo_location.types.batch_put_geofence_request
    import capo_location.types.batch_put_geofence_request_entry_list
    import capo_location.types.batch_put_geofence_response
    import capo_location.types.create_geofence_collection_request
    import capo_location.types.create_geofence_collection_response
    import capo_location.types.delete_geofence_collection_request
    import capo_location.types.delete_geofence_collection_response
    import capo_location.types.describe_geofence_collection_request
    import capo_location.types.describe_geofence_collection_response
    import capo_location.types.device_position_update_list
    import capo_location.types.distance_unit
    import capo_location.types.forecast_geofence_events_device_state
    import capo_location.types.forecast_geofence_events_request
    import capo_location.types.forecast_geofence_events_response
    import capo_location.types.forecasted_event
    import capo_location.types.geofence_geometry
    import capo_location.types.get_geofence_request
    import capo_location.types.get_geofence_response
    import capo_location.types.id
    import capo_location.types.id_list
    import capo_location.types.kms_key_id
    import capo_location.types.large_token
    import capo_location.types.list_geofence_collections_request
    import capo_location.types.list_geofence_collections_response
    import capo_location.types.list_geofence_collections_response_entry
    import capo_location.types.list_geofence_response_entry
    import capo_location.types.list_geofences_request
    import capo_location.types.list_geofences_response
    import capo_location.types.pricing_plan
    import capo_location.types.property_map
    import capo_location.types.put_geofence_request
    import capo_location.types.put_geofence_response
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.speed_unit
    import capo_location.types.tag_map
    import capo_location.types.token
    import capo_location.types.update_geofence_collection_request
    import capo_location.types.update_geofence_collection_response
    from capo_location._services.async_location import (
        AsyncLocationClient,
        AsyncLocationClientConfig,
    )
    from capo_location._services.location import LocationClient, LocationClientConfig


class GeofenceCollectionResource:
    def __init__(self, service: LocationClient) -> None:
        self._service = service

    def put(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def read(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def update(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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


class AsyncGeofenceCollectionResource:
    def __init__(self, service: AsyncLocationClient) -> None:
        self._service = service

    async def put(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.create_geofence_collection_request.CreateGeofenceCollectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.create_geofence_collection_response.CreateGeofenceCollectionResponse"
        ]:
            import capo_location._operations.location_service.create_geofence_collection

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.create_geofence_collection.async_create_geofence_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.describe_geofence_collection_request.DescribeGeofenceCollectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.describe_geofence_collection_response.DescribeGeofenceCollectionResponse"
        ]:
            import capo_location._operations.location_service.describe_geofence_collection

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.describe_geofence_collection.async_describe_geofence_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.describe_geofence_collection_request.DescribeGeofenceCollectionRequest = {
            "collection_name": collection_name
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
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.update_geofence_collection_request.UpdateGeofenceCollectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.update_geofence_collection_response.UpdateGeofenceCollectionResponse"
        ]:
            import capo_location._operations.location_service.update_geofence_collection

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.update_geofence_collection.async_update_geofence_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.update_geofence_collection_request.UpdateGeofenceCollectionRequest = {
            "collection_name": collection_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if pricing_plan_data_source is not None:
            input_["pricing_plan_data_source"] = pricing_plan_data_source
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.delete_geofence_collection_request.DeleteGeofenceCollectionRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.delete_geofence_collection_response.DeleteGeofenceCollectionResponse"
        ]:
            import capo_location._operations.location_service.delete_geofence_collection

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.delete_geofence_collection.async_delete_geofence_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.delete_geofence_collection_request.DeleteGeofenceCollectionRequest = {
            "collection_name": collection_name
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.list_geofence_collections_request.ListGeofenceCollectionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.list_geofence_collections_response.ListGeofenceCollectionsResponse"
        ]:
            import capo_location._operations.location_service.list_geofence_collections

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.list_geofence_collections.async_list_geofence_collections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_geofence_collections_request.ListGeofenceCollectionsRequest = {}
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

    async def batch_delete_geofence(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        geofence_ids: "capo_location.types.id_list.IdList",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.batch_delete_geofence_request.BatchDeleteGeofenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.batch_delete_geofence_response.BatchDeleteGeofenceResponse"
        ]:
            import capo_location._operations.location_service.batch_delete_geofence

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.batch_delete_geofence.async_batch_delete_geofence(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.batch_delete_geofence_request.BatchDeleteGeofenceRequest = {
            "collection_name": collection_name,
            "geofence_ids": geofence_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_evaluate_geofences(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        device_position_updates: "capo_location.types.device_position_update_list.DevicePositionUpdateList",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.batch_evaluate_geofences_request.BatchEvaluateGeofencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.batch_evaluate_geofences_response.BatchEvaluateGeofencesResponse"
        ]:
            import capo_location._operations.location_service.batch_evaluate_geofences

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.batch_evaluate_geofences.async_batch_evaluate_geofences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.batch_evaluate_geofences_request.BatchEvaluateGeofencesRequest = {
            "collection_name": collection_name,
            "device_position_updates": device_position_updates,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_put_geofence(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        entries: "capo_location.types.batch_put_geofence_request_entry_list.BatchPutGeofenceRequestEntryList",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.batch_put_geofence_request.BatchPutGeofenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.batch_put_geofence_response.BatchPutGeofenceResponse"
        ]:
            import capo_location._operations.location_service.batch_put_geofence

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.batch_put_geofence.async_batch_put_geofence(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.batch_put_geofence_request.BatchPutGeofenceRequest = {
            "collection_name": collection_name,
            "entries": entries,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def forecast_geofence_events(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        device_state: "capo_location.types.forecast_geofence_events_device_state.ForecastGeofenceEventsDeviceState",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.forecast_geofence_events_request.ForecastGeofenceEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.forecast_geofence_events_response.ForecastGeofenceEventsResponse"
        ]:
            import capo_location._operations.location_service.forecast_geofence_events

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.forecast_geofence_events.async_forecast_geofence_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_geofence(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        geofence_id: "capo_location.types.id.Id",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.get_geofence_request.GetGeofenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.get_geofence_response.GetGeofenceResponse"
        ]:
            import capo_location._operations.location_service.get_geofence

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.get_geofence.async_get_geofence(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.get_geofence_request.GetGeofenceRequest = {
            "collection_name": collection_name,
            "geofence_id": geofence_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_geofences(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.list_geofences_request.ListGeofencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.list_geofences_response.ListGeofencesResponse"
        ]:
            import capo_location._operations.location_service.list_geofences

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.list_geofences.async_list_geofences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_geofences_request.ListGeofencesRequest = {
            "collection_name": collection_name
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

    async def put_geofence(
        self,
        collection_name: "capo_location.types.resource_name.ResourceName",
        geofence_id: "capo_location.types.id.Id",
        geometry: "capo_location.types.geofence_geometry.GeofenceGeometry",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
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

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.put_geofence_request.PutGeofenceRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.put_geofence_response.PutGeofenceResponse"
        ]:
            import capo_location._operations.location_service.put_geofence

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.put_geofence.async_put_geofence(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.put_geofence_request.PutGeofenceRequest = {
            "collection_name": collection_name,
            "geofence_id": geofence_id,
            "geometry": geometry,
        }
        if geofence_properties is not None:
            input_["geofence_properties"] = geofence_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
