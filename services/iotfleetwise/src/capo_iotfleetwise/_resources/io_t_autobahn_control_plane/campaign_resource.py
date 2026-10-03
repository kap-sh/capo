from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_iotfleetwise._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.campaign_name
    import capo_iotfleetwise.types.campaign_summary
    import capo_iotfleetwise.types.collection_scheme
    import capo_iotfleetwise.types.compression
    import capo_iotfleetwise.types.create_campaign_request
    import capo_iotfleetwise.types.create_campaign_response
    import capo_iotfleetwise.types.data_destination_configs
    import capo_iotfleetwise.types.data_extra_dimension_node_path_list
    import capo_iotfleetwise.types.data_partitions
    import capo_iotfleetwise.types.delete_campaign_request
    import capo_iotfleetwise.types.delete_campaign_response
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.diagnostics_mode
    import capo_iotfleetwise.types.get_campaign_request
    import capo_iotfleetwise.types.get_campaign_response
    import capo_iotfleetwise.types.list_campaigns_request
    import capo_iotfleetwise.types.list_campaigns_response
    import capo_iotfleetwise.types.list_response_scope
    import capo_iotfleetwise.types.max_results
    import capo_iotfleetwise.types.next_token
    import capo_iotfleetwise.types.priority
    import capo_iotfleetwise.types.signal_fetch_information_list
    import capo_iotfleetwise.types.signal_information_list
    import capo_iotfleetwise.types.spooling_mode
    import capo_iotfleetwise.types.status_str
    import capo_iotfleetwise.types.tag_list
    import capo_iotfleetwise.types.timestamp
    import capo_iotfleetwise.types.uint32
    import capo_iotfleetwise.types.update_campaign_action
    import capo_iotfleetwise.types.update_campaign_request
    import capo_iotfleetwise.types.update_campaign_response
    from capo_iotfleetwise._services.async_io_t_fleet_wise import (
        AsyncIoTFleetWiseClient,
        AsyncIoTFleetWiseClientConfig,
    )
    from capo_iotfleetwise._services.io_t_fleet_wise import (
        IoTFleetWiseClient,
        IoTFleetWiseClientConfig,
    )


class CampaignResource:
    def __init__(self, service: IoTFleetWiseClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_iotfleetwise.types.campaign_name.campaignName",
        signal_catalog_arn: "capo_iotfleetwise.types.arn.arn",
        target_arn: "capo_iotfleetwise.types.arn.arn",
        collection_scheme: "capo_iotfleetwise.types.collection_scheme.CollectionScheme",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
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
        """<p>Creates an orchestration of data collection rules. The Amazon Web Services IoT FleetWise Edge Agent software running in vehicles uses campaigns to decide how to collect and transfer data to the cloud. You create campaigns in the cloud. After you or your team approve campaigns, Amazon Web Services IoT FleetWise automatically deploys them to vehicles. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html">Collect and transfer data with campaigns</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

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

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.create_campaign_request.CreateCampaignRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_campaign

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.create_campaign.create_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        name: "capo_iotfleetwise.types.campaign_name.campaignName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse":
        """<p> Retrieves information about a campaign. </p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

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

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.get_campaign_request.GetCampaignRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_campaign

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.get_campaign.get_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.get_campaign_request.GetCampaignRequest = {
            "name": name
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
        name: "capo_iotfleetwise.types.campaign_name.campaignName",
        action: "capo_iotfleetwise.types.update_campaign_action.UpdateCampaignAction",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.update_campaign_request.UpdateCampaignRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.update_campaign_response.UpdateCampaignResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_campaign

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.update_campaign.update_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.update_campaign_request.UpdateCampaignRequest = {
            "name": name,
            "action": action,
        }
        if description is not None:
            input_["description"] = description
        if data_extra_dimensions is not None:
            input_["data_extra_dimensions"] = data_extra_dimensions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        name: "capo_iotfleetwise.types.campaign_name.campaignName",
        *,
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.delete_campaign_response.DeleteCampaignResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_campaign

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.delete_campaign.delete_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.delete_campaign_request.DeleteCampaignRequest = {
            "name": name
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
        config_overrides: Optional[IoTFleetWiseClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[capo_iotfleetwise.types.list_campaigns_request.ListCampaignsRequest]",
        ) -> OperationResponse[
            "capo_iotfleetwise.types.list_campaigns_response.ListCampaignsResponse"
        ]:
            import capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_campaigns

            output, http_response = (
                capo_iotfleetwise._operations.io_t_autobahn_control_plane.list_campaigns.list_campaigns(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_iotfleetwise.types.list_campaigns_request.ListCampaignsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if list_response_scope is not None:
            input_["list_response_scope"] = list_response_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCampaignResource:
    def __init__(self, service: AsyncIoTFleetWiseClient) -> None:
        self._service = service

    async def put(
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
        """<p>Creates an orchestration of data collection rules. The Amazon Web Services IoT FleetWise Edge Agent software running in vehicles uses campaigns to decide how to collect and transfer data to the cloud. You create campaigns in the cloud. After you or your team approve campaigns, Amazon Web Services IoT FleetWise automatically deploys them to vehicles. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html">Collect and transfer data with campaigns</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def read(
        self,
        name: "capo_iotfleetwise.types.campaign_name.campaignName",
        *,
        config_overrides: Optional[AsyncIoTFleetWiseClientConfig] = None,
    ) -> "capo_iotfleetwise.types.get_campaign_response.GetCampaignResponse":
        """<p> Retrieves information about a campaign. </p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>

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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def update(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def delete(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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

    async def list(
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

        interceptors_, options_ = self._service.operation_options(config_overrides)
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
