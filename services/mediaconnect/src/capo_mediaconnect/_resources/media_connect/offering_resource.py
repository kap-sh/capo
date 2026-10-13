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
    import capo_mediaconnect.types.describe_offering_request
    import capo_mediaconnect.types.describe_offering_response
    import capo_mediaconnect.types.list_offerings_request
    import capo_mediaconnect.types.list_offerings_response
    import capo_mediaconnect.types.max_results
    import capo_mediaconnect.types.offering
    import capo_mediaconnect.types.offering_arn
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class OfferingResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def read(
        self,
        offering_arn: "capo_mediaconnect.types.offering_arn.OfferingArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_offering_response.DescribeOfferingResponse":
        """<p> Displays the details of an offering. The response includes the offering description, duration, outbound bandwidth, price, and Amazon Resource Name (ARN).</p>

        Args:
            offering_arn: <p> The ARN of the offering.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_offering_request.DescribeOfferingRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_offering_response.DescribeOfferingResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_offering

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_offering.describe_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeOffering")
        )
        input_: capo_mediaconnect.types.describe_offering_request.DescribeOfferingRequest = {
            "offering_arn": offering_arn
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
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_offerings_response.ListOfferingsResponse":
        """<p> Displays a list of all offerings that are available to this account in the current Amazon Web Services Region. If you have an active reservation (which means you've purchased an offering that has already started and hasn't expired yet), your account isn't eligible for other offerings.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListOfferings</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_offerings_request.ListOfferingsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_offerings_response.ListOfferingsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_offerings

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_offerings.list_offerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListOfferings")
        )
        input_: capo_mediaconnect.types.list_offerings_request.ListOfferingsRequest = {}
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


class AsyncOfferingResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def read(
        self,
        offering_arn: "capo_mediaconnect.types.offering_arn.OfferingArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_offering_response.DescribeOfferingResponse":
        """<p> Displays the details of an offering. The response includes the offering description, duration, outbound bandwidth, price, and Amazon Resource Name (ARN).</p>

        Args:
            offering_arn: <p> The ARN of the offering.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.describe_offering_request.DescribeOfferingRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.describe_offering_response.DescribeOfferingResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_offering

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.describe_offering.async_describe_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeOffering")
        )
        input_: capo_mediaconnect.types.describe_offering_request.DescribeOfferingRequest = {
            "offering_arn": offering_arn
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
        max_results: Optional["capo_mediaconnect.types.max_results.MaxResults"] = None,
        next_token: Optional[str] = None,
    ) -> "capo_mediaconnect.types.list_offerings_response.ListOfferingsResponse":
        """<p> Displays a list of all offerings that are available to this account in the current Amazon Web Services Region. If you have an active reservation (which means you've purchased an offering that has already started and hasn't expired yet), your account isn't eligible for other offerings.</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a <code>NextToken</code> value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListOfferings</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListOfferings</code> request a second time and specify the <code>NextToken</code> value.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_offerings_request.ListOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_offerings_response.ListOfferingsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_offerings

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_offerings.async_list_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListOfferings")
        )
        input_: capo_mediaconnect.types.list_offerings_request.ListOfferingsRequest = {}
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
