from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_mediaconnect._auth._signers
import capo_mediaconnect._auth._sigv4
from capo_mediaconnect._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mediaconnect.types.__list_of_add_bridge_output_request
    import capo_mediaconnect.types.__list_of_add_bridge_source_request
    import capo_mediaconnect.types.add_bridge_outputs_request
    import capo_mediaconnect.types.add_bridge_outputs_response
    import capo_mediaconnect.types.add_bridge_sources_request
    import capo_mediaconnect.types.add_bridge_sources_response
    import capo_mediaconnect.types.add_egress_gateway_bridge_request
    import capo_mediaconnect.types.add_ingress_gateway_bridge_request
    import capo_mediaconnect.types.bridge_arn
    import capo_mediaconnect.types.create_bridge_request
    import capo_mediaconnect.types.create_bridge_response
    import capo_mediaconnect.types.delete_bridge_request
    import capo_mediaconnect.types.delete_bridge_response
    import capo_mediaconnect.types.describe_bridge_request
    import capo_mediaconnect.types.describe_bridge_response
    import capo_mediaconnect.types.desired_state
    import capo_mediaconnect.types.failover_config
    import capo_mediaconnect.types.list_bridges_request
    import capo_mediaconnect.types.list_bridges_response
    import capo_mediaconnect.types.listed_bridge
    import capo_mediaconnect.types.max_results
    import capo_mediaconnect.types.remove_bridge_output_request
    import capo_mediaconnect.types.remove_bridge_output_response
    import capo_mediaconnect.types.remove_bridge_source_request
    import capo_mediaconnect.types.remove_bridge_source_response
    import capo_mediaconnect.types.update_bridge_flow_source_request
    import capo_mediaconnect.types.update_bridge_network_output_request
    import capo_mediaconnect.types.update_bridge_network_source_request
    import capo_mediaconnect.types.update_bridge_output_request
    import capo_mediaconnect.types.update_bridge_output_response
    import capo_mediaconnect.types.update_bridge_request
    import capo_mediaconnect.types.update_bridge_response
    import capo_mediaconnect.types.update_bridge_source_request
    import capo_mediaconnect.types.update_bridge_source_response
    import capo_mediaconnect.types.update_bridge_state_request
    import capo_mediaconnect.types.update_bridge_state_response
    import capo_mediaconnect.types.update_egress_gateway_bridge_request
    import capo_mediaconnect.types.update_failover_config
    import capo_mediaconnect.types.update_ingress_gateway_bridge_request
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class BridgeResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        egress_gateway_bridge: Optional[
            "capo_mediaconnect.types.add_egress_gateway_bridge_request.AddEgressGatewayBridgeRequest"
        ] = None,
        ingress_gateway_bridge: Optional[
            "capo_mediaconnect.types.add_ingress_gateway_bridge_request.AddIngressGatewayBridgeRequest"
        ] = None,
        name: Optional[str] = None,
        outputs: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_output_request.__listOfAddBridgeOutputRequest"
        ] = None,
        placement_arn: Optional[str] = None,
        source_failover_config: Optional[
            "capo_mediaconnect.types.failover_config.FailoverConfig"
        ] = None,
        sources: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_source_request.__listOfAddBridgeSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.create_bridge_response.CreateBridgeResponse":
        """<p> Creates a new bridge. The request must include one source.</p>

        Args:
            egress_gateway_bridge: <p>An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>
            ingress_gateway_bridge: <p>An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>
            name: <p> The name of the bridge. This name can not be modified after the bridge is created.</p>
            outputs: <p> The outputs that you want to add to this bridge.</p>
            placement_arn: <p> The bridge placement Amazon Resource Number (ARN).</p>
            source_failover_config: <p> The settings for source failover.</p>
            sources: <p> The sources that you want to add to this bridge.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.create_bridge420_exception.CreateBridge420Exception: <p>Exception raised by Elemental MediaConnect when creating the bridge. See the error message for the operation for more information on the cause of this exception. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.create_bridge_request.CreateBridgeRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.create_bridge_response.CreateBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_bridge

            output, http_response = (
                capo_mediaconnect._operations.media_connect.create_bridge.create_bridge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateBridge")
        )
        input_: capo_mediaconnect.types.create_bridge_request.CreateBridgeRequest = {}
        if egress_gateway_bridge is not None:
            input_["egress_gateway_bridge"] = egress_gateway_bridge
        if ingress_gateway_bridge is not None:
            input_["ingress_gateway_bridge"] = ingress_gateway_bridge
        if name is not None:
            input_["name"] = name
        if outputs is not None:
            input_["outputs"] = outputs
        if placement_arn is not None:
            input_["placement_arn"] = placement_arn
        if source_failover_config is not None:
            input_["source_failover_config"] = source_failover_config
        if sources is not None:
            input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_bridge_response.DescribeBridgeResponse":
        """<p> Displays the details of a bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to describe.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_bridge_request.DescribeBridgeRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_bridge_response.DescribeBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_bridge

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_bridge.describe_bridge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeBridge")
        )
        input_: capo_mediaconnect.types.describe_bridge_request.DescribeBridgeRequest = {
            "bridge_arn": bridge_arn
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
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        egress_gateway_bridge: Optional[
            "capo_mediaconnect.types.update_egress_gateway_bridge_request.UpdateEgressGatewayBridgeRequest"
        ] = None,
        ingress_gateway_bridge: Optional[
            "capo_mediaconnect.types.update_ingress_gateway_bridge_request.UpdateIngressGatewayBridgeRequest"
        ] = None,
        source_failover_config: Optional[
            "capo_mediaconnect.types.update_failover_config.UpdateFailoverConfig"
        ] = None,
    ) -> "capo_mediaconnect.types.update_bridge_response.UpdateBridgeResponse":
        """<p> Updates the bridge.</p>

        Args:
            bridge_arn: <p> TheAmazon Resource Name (ARN) of the bridge that you want to update. </p>
            egress_gateway_bridge: <p> A cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>
            ingress_gateway_bridge: <p> A ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>
            source_failover_config: <p> The settings for source failover. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_bridge_request.UpdateBridgeRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_bridge_response.UpdateBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_bridge.update_bridge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBridge")
        )
        input_: capo_mediaconnect.types.update_bridge_request.UpdateBridgeRequest = {
            "bridge_arn": bridge_arn
        }
        if egress_gateway_bridge is not None:
            input_["egress_gateway_bridge"] = egress_gateway_bridge
        if ingress_gateway_bridge is not None:
            input_["ingress_gateway_bridge"] = ingress_gateway_bridge
        if source_failover_config is not None:
            input_["source_failover_config"] = source_failover_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_bridge_response.DeleteBridgeResponse":
        """<p> Deletes a bridge. Before you can delete a bridge, you must stop the bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.delete_bridge_request.DeleteBridgeRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.delete_bridge_response.DeleteBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_bridge

            output, http_response = (
                capo_mediaconnect._operations.media_connect.delete_bridge.delete_bridge(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBridge")
        )
        input_: capo_mediaconnect.types.delete_bridge_request.DeleteBridgeRequest = {
            "bridge_arn": bridge_arn
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
        config_overrides: Optional[MediaConnectClientConfig] = None,
        filter_arn: Optional[str] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_bridges_response.ListBridgesResponse":
        """<p> Displays a list of bridges that are associated with this account and an optionally specified Amazon Resource Name (ARN). This request returns a paginated result.</p>

        Args:
            filter_arn: <p> Filter the list results to display only the bridges associated with the selected ARN.</p>
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListBridges</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListBridges</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListBridges</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_bridges_request.ListBridgesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_bridges_response.ListBridgesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_bridges

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_bridges.list_bridges(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListBridges")
        )
        input_: capo_mediaconnect.types.list_bridges_request.ListBridgesRequest = {}
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
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

    def add_bridge_outputs(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        outputs: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_output_request.__listOfAddBridgeOutputRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_bridge_outputs_response.AddBridgeOutputsResponse":
        """<p> Adds outputs to an existing bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            outputs: <p> The outputs that you want to add to this bridge.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.add_bridge_outputs_request.AddBridgeOutputsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.add_bridge_outputs_response.AddBridgeOutputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_bridge_outputs

            output, http_response = (
                capo_mediaconnect._operations.media_connect.add_bridge_outputs.add_bridge_outputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AddBridgeOutputs")
        )
        input_: capo_mediaconnect.types.add_bridge_outputs_request.AddBridgeOutputsRequest = {
            "bridge_arn": bridge_arn
        }
        if outputs is not None:
            input_["outputs"] = outputs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def add_bridge_sources(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        sources: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_source_request.__listOfAddBridgeSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_bridge_sources_response.AddBridgeSourcesResponse":
        """<p> Adds sources to an existing bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            sources: <p> The sources that you want to add to this bridge.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.add_bridge_sources_request.AddBridgeSourcesRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.add_bridge_sources_response.AddBridgeSourcesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_bridge_sources

            output, http_response = (
                capo_mediaconnect._operations.media_connect.add_bridge_sources.add_bridge_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AddBridgeSources")
        )
        input_: capo_mediaconnect.types.add_bridge_sources_request.AddBridgeSourcesRequest = {
            "bridge_arn": bridge_arn
        }
        if sources is not None:
            input_["sources"] = sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_bridge_output(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        output_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_bridge_output_response.RemoveBridgeOutputResponse":
        """<p> Removes an output from a bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            output_name: <p> The name of the bridge output that you want to remove.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.remove_bridge_output_request.RemoveBridgeOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.remove_bridge_output_response.RemoveBridgeOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_bridge_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.remove_bridge_output.remove_bridge_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RemoveBridgeOutput")
        )
        input_: capo_mediaconnect.types.remove_bridge_output_request.RemoveBridgeOutputRequest = {
            "bridge_arn": bridge_arn,
            "output_name": output_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_bridge_source(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        source_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_bridge_source_response.RemoveBridgeSourceResponse":
        """<p> Removes a source from a bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            source_name: <p> The name of the bridge source that you want to remove.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.remove_bridge_source_request.RemoveBridgeSourceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.remove_bridge_source_response.RemoveBridgeSourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_bridge_source

            output, http_response = (
                capo_mediaconnect._operations.media_connect.remove_bridge_source.remove_bridge_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RemoveBridgeSource")
        )
        input_: capo_mediaconnect.types.remove_bridge_source_request.RemoveBridgeSourceRequest = {
            "bridge_arn": bridge_arn,
            "source_name": source_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bridge_output(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        output_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        network_output: Optional[
            "capo_mediaconnect.types.update_bridge_network_output_request.UpdateBridgeNetworkOutputRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.update_bridge_output_response.UpdateBridgeOutputResponse":
        """<p> Updates an existing bridge output.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            network_output: <p> The network of the bridge output. </p>
            output_name: <p> Tname of the output that you want to update. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_bridge_output_request.UpdateBridgeOutputRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_bridge_output_response.UpdateBridgeOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge_output

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_bridge_output.update_bridge_output(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBridgeOutput")
        )
        input_: capo_mediaconnect.types.update_bridge_output_request.UpdateBridgeOutputRequest = {
            "bridge_arn": bridge_arn,
            "output_name": output_name,
        }
        if network_output is not None:
            input_["network_output"] = network_output

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bridge_source(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        source_name: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        flow_source: Optional[
            "capo_mediaconnect.types.update_bridge_flow_source_request.UpdateBridgeFlowSourceRequest"
        ] = None,
        network_source: Optional[
            "capo_mediaconnect.types.update_bridge_network_source_request.UpdateBridgeNetworkSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.update_bridge_source_response.UpdateBridgeSourceResponse":
        """<p> Updates an existing bridge source.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            flow_source: <p> The name of the flow that you want to update.</p>
            network_source: <p> The network for the bridge source. </p>
            source_name: <p> The name of the source that you want to update. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_bridge_source_request.UpdateBridgeSourceRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_bridge_source_response.UpdateBridgeSourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge_source

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_bridge_source.update_bridge_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBridgeSource")
        )
        input_: capo_mediaconnect.types.update_bridge_source_request.UpdateBridgeSourceRequest = {
            "bridge_arn": bridge_arn,
            "source_name": source_name,
        }
        if flow_source is not None:
            input_["flow_source"] = flow_source
        if network_source is not None:
            input_["network_source"] = network_source

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_bridge_state(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        desired_state: Optional[
            "capo_mediaconnect.types.desired_state.DesiredState"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.update_bridge_state_response.UpdateBridgeStateResponse"
    ):
        """<p> Updates the bridge state. </p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update the state of. </p>
            desired_state: <p> The desired state for the bridge. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.update_bridge_state_request.UpdateBridgeStateRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.update_bridge_state_response.UpdateBridgeStateResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge_state

            output, http_response = (
                capo_mediaconnect._operations.media_connect.update_bridge_state.update_bridge_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBridgeState")
        )
        input_: capo_mediaconnect.types.update_bridge_state_request.UpdateBridgeStateRequest = {
            "bridge_arn": bridge_arn
        }
        if desired_state is not None:
            input_["desired_state"] = desired_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncBridgeResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        egress_gateway_bridge: Optional[
            "capo_mediaconnect.types.add_egress_gateway_bridge_request.AddEgressGatewayBridgeRequest"
        ] = None,
        ingress_gateway_bridge: Optional[
            "capo_mediaconnect.types.add_ingress_gateway_bridge_request.AddIngressGatewayBridgeRequest"
        ] = None,
        name: Optional[str] = None,
        outputs: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_output_request.__listOfAddBridgeOutputRequest"
        ] = None,
        placement_arn: Optional[str] = None,
        source_failover_config: Optional[
            "capo_mediaconnect.types.failover_config.FailoverConfig"
        ] = None,
        sources: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_source_request.__listOfAddBridgeSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.create_bridge_response.CreateBridgeResponse":
        """<p> Creates a new bridge. The request must include one source.</p>

        Args:
            egress_gateway_bridge: <p>An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>
            ingress_gateway_bridge: <p>An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>
            name: <p> The name of the bridge. This name can not be modified after the bridge is created.</p>
            outputs: <p> The outputs that you want to add to this bridge.</p>
            placement_arn: <p> The bridge placement Amazon Resource Number (ARN).</p>
            source_failover_config: <p> The settings for source failover.</p>
            sources: <p> The sources that you want to add to this bridge.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.create_bridge420_exception.CreateBridge420Exception: <p>Exception raised by Elemental MediaConnect when creating the bridge. See the error message for the operation for more information on the cause of this exception. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.create_bridge_request.CreateBridgeRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.create_bridge_response.CreateBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.create_bridge

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.create_bridge.async_create_bridge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateBridge")
        )
        input_: capo_mediaconnect.types.create_bridge_request.CreateBridgeRequest = {}
        if egress_gateway_bridge is not None:
            input_["egress_gateway_bridge"] = egress_gateway_bridge
        if ingress_gateway_bridge is not None:
            input_["ingress_gateway_bridge"] = ingress_gateway_bridge
        if name is not None:
            input_["name"] = name
        if outputs is not None:
            input_["outputs"] = outputs
        if placement_arn is not None:
            input_["placement_arn"] = placement_arn
        if source_failover_config is not None:
            input_["source_failover_config"] = source_failover_config
        if sources is not None:
            input_["sources"] = sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_bridge_response.DescribeBridgeResponse":
        """<p> Displays the details of a bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to describe.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.describe_bridge_request.DescribeBridgeRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.describe_bridge_response.DescribeBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_bridge

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.describe_bridge.async_describe_bridge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeBridge")
        )
        input_: capo_mediaconnect.types.describe_bridge_request.DescribeBridgeRequest = {
            "bridge_arn": bridge_arn
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
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        egress_gateway_bridge: Optional[
            "capo_mediaconnect.types.update_egress_gateway_bridge_request.UpdateEgressGatewayBridgeRequest"
        ] = None,
        ingress_gateway_bridge: Optional[
            "capo_mediaconnect.types.update_ingress_gateway_bridge_request.UpdateIngressGatewayBridgeRequest"
        ] = None,
        source_failover_config: Optional[
            "capo_mediaconnect.types.update_failover_config.UpdateFailoverConfig"
        ] = None,
    ) -> "capo_mediaconnect.types.update_bridge_response.UpdateBridgeResponse":
        """<p> Updates the bridge.</p>

        Args:
            bridge_arn: <p> TheAmazon Resource Name (ARN) of the bridge that you want to update. </p>
            egress_gateway_bridge: <p> A cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. </p>
            ingress_gateway_bridge: <p> A ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud. </p>
            source_failover_config: <p> The settings for source failover. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_bridge_request.UpdateBridgeRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_bridge_response.UpdateBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_bridge.async_update_bridge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBridge")
        )
        input_: capo_mediaconnect.types.update_bridge_request.UpdateBridgeRequest = {
            "bridge_arn": bridge_arn
        }
        if egress_gateway_bridge is not None:
            input_["egress_gateway_bridge"] = egress_gateway_bridge
        if ingress_gateway_bridge is not None:
            input_["ingress_gateway_bridge"] = ingress_gateway_bridge
        if source_failover_config is not None:
            input_["source_failover_config"] = source_failover_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.delete_bridge_response.DeleteBridgeResponse":
        """<p> Deletes a bridge. Before you can delete a bridge, you must stop the bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to delete.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.delete_bridge_request.DeleteBridgeRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.delete_bridge_response.DeleteBridgeResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.delete_bridge

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.delete_bridge.async_delete_bridge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBridge")
        )
        input_: capo_mediaconnect.types.delete_bridge_request.DeleteBridgeRequest = {
            "bridge_arn": bridge_arn
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
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        filter_arn: Optional[str] = None,
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_bridges_response.ListBridgesResponse":
        """<p> Displays a list of bridges that are associated with this account and an optionally specified Amazon Resource Name (ARN). This request returns a paginated result.</p>

        Args:
            filter_arn: <p> Filter the list results to display only the bridges associated with the selected ARN.</p>
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListBridges</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListBridges</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListBridges</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_bridges_request.ListBridgesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_bridges_response.ListBridgesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_bridges

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_bridges.async_list_bridges(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListBridges")
        )
        input_: capo_mediaconnect.types.list_bridges_request.ListBridgesRequest = {}
        if filter_arn is not None:
            input_["filter_arn"] = filter_arn
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

    async def add_bridge_outputs(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        outputs: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_output_request.__listOfAddBridgeOutputRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_bridge_outputs_response.AddBridgeOutputsResponse":
        """<p> Adds outputs to an existing bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            outputs: <p> The outputs that you want to add to this bridge.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.add_bridge_outputs_request.AddBridgeOutputsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.add_bridge_outputs_response.AddBridgeOutputsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_bridge_outputs

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.add_bridge_outputs.async_add_bridge_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AddBridgeOutputs")
        )
        input_: capo_mediaconnect.types.add_bridge_outputs_request.AddBridgeOutputsRequest = {
            "bridge_arn": bridge_arn
        }
        if outputs is not None:
            input_["outputs"] = outputs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_bridge_sources(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        sources: Optional[
            "capo_mediaconnect.types.__list_of_add_bridge_source_request.__listOfAddBridgeSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.add_bridge_sources_response.AddBridgeSourcesResponse":
        """<p> Adds sources to an existing bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            sources: <p> The sources that you want to add to this bridge.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.add_bridge_sources_request.AddBridgeSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.add_bridge_sources_response.AddBridgeSourcesResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.add_bridge_sources

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.add_bridge_sources.async_add_bridge_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AddBridgeSources")
        )
        input_: capo_mediaconnect.types.add_bridge_sources_request.AddBridgeSourcesRequest = {
            "bridge_arn": bridge_arn
        }
        if sources is not None:
            input_["sources"] = sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_bridge_output(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        output_name: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_bridge_output_response.RemoveBridgeOutputResponse":
        """<p> Removes an output from a bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            output_name: <p> The name of the bridge output that you want to remove.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.remove_bridge_output_request.RemoveBridgeOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.remove_bridge_output_response.RemoveBridgeOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_bridge_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.remove_bridge_output.async_remove_bridge_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RemoveBridgeOutput")
        )
        input_: capo_mediaconnect.types.remove_bridge_output_request.RemoveBridgeOutputRequest = {
            "bridge_arn": bridge_arn,
            "output_name": output_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_bridge_source(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        source_name: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.remove_bridge_source_response.RemoveBridgeSourceResponse":
        """<p> Removes a source from a bridge.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            source_name: <p> The name of the bridge source that you want to remove.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.remove_bridge_source_request.RemoveBridgeSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.remove_bridge_source_response.RemoveBridgeSourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.remove_bridge_source

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.remove_bridge_source.async_remove_bridge_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RemoveBridgeSource")
        )
        input_: capo_mediaconnect.types.remove_bridge_source_request.RemoveBridgeSourceRequest = {
            "bridge_arn": bridge_arn,
            "source_name": source_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bridge_output(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        output_name: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        network_output: Optional[
            "capo_mediaconnect.types.update_bridge_network_output_request.UpdateBridgeNetworkOutputRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.update_bridge_output_response.UpdateBridgeOutputResponse":
        """<p> Updates an existing bridge output.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            network_output: <p> The network of the bridge output. </p>
            output_name: <p> Tname of the output that you want to update. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_bridge_output_request.UpdateBridgeOutputRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_bridge_output_response.UpdateBridgeOutputResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge_output

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_bridge_output.async_update_bridge_output(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBridgeOutput")
        )
        input_: capo_mediaconnect.types.update_bridge_output_request.UpdateBridgeOutputRequest = {
            "bridge_arn": bridge_arn,
            "output_name": output_name,
        }
        if network_output is not None:
            input_["network_output"] = network_output

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bridge_source(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        source_name: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        flow_source: Optional[
            "capo_mediaconnect.types.update_bridge_flow_source_request.UpdateBridgeFlowSourceRequest"
        ] = None,
        network_source: Optional[
            "capo_mediaconnect.types.update_bridge_network_source_request.UpdateBridgeNetworkSourceRequest"
        ] = None,
    ) -> "capo_mediaconnect.types.update_bridge_source_response.UpdateBridgeSourceResponse":
        """<p> Updates an existing bridge source.</p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update.</p>
            flow_source: <p> The name of the flow that you want to update.</p>
            network_source: <p> The network for the bridge source. </p>
            source_name: <p> The name of the source that you want to update. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_bridge_source_request.UpdateBridgeSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_bridge_source_response.UpdateBridgeSourceResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge_source

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_bridge_source.async_update_bridge_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBridgeSource")
        )
        input_: capo_mediaconnect.types.update_bridge_source_request.UpdateBridgeSourceRequest = {
            "bridge_arn": bridge_arn,
            "source_name": source_name,
        }
        if flow_source is not None:
            input_["flow_source"] = flow_source
        if network_source is not None:
            input_["network_source"] = network_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bridge_state(
        self,
        bridge_arn: "capo_mediaconnect.types.bridge_arn.BridgeArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        desired_state: Optional[
            "capo_mediaconnect.types.desired_state.DesiredState"
        ] = None,
    ) -> (
        "capo_mediaconnect.types.update_bridge_state_response.UpdateBridgeStateResponse"
    ):
        """<p> Updates the bridge state. </p>

        Args:
            bridge_arn: <p> The Amazon Resource Name (ARN) of the bridge that you want to update the state of. </p>
            desired_state: <p> The desired state for the bridge. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.update_bridge_state_request.UpdateBridgeStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.update_bridge_state_response.UpdateBridgeStateResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.update_bridge_state

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.update_bridge_state.async_update_bridge_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBridgeState")
        )
        input_: capo_mediaconnect.types.update_bridge_state_request.UpdateBridgeStateRequest = {
            "bridge_arn": bridge_arn
        }
        if desired_state is not None:
            input_["desired_state"] = desired_state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
