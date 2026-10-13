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
    import capo_mediaconnect.types.describe_reservation_request
    import capo_mediaconnect.types.describe_reservation_response
    import capo_mediaconnect.types.list_reservations_request
    import capo_mediaconnect.types.list_reservations_response
    import capo_mediaconnect.types.max_results
    import capo_mediaconnect.types.purchase_offering_request
    import capo_mediaconnect.types.purchase_offering_response
    import capo_mediaconnect.types.reservation
    import capo_mediaconnect.types.reservation_arn
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
        AsyncMediaConnectClientConfig,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
        MediaConnectClientConfig,
    )


class ReservationResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service

    def create(
        self,
        offering_arn: str,
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
        reservation_name: Optional[str] = None,
        start: Optional[str] = None,
    ) -> "capo_mediaconnect.types.purchase_offering_response.PurchaseOfferingResponse":
        """<p> Submits a request to purchase an offering. If you already have an active reservation, you can't purchase another offering.</p>

        Args:
            offering_arn: <p> The Amazon Resource Name (ARN) of the offering.</p>
            reservation_name: <p> The name that you want to use for the reservation.</p>
            start: <p> The date and time that you want the reservation to begin, in Coordinated Universal Time (UTC). </p> <p>You can specify any date and time between 12:00am on the first day of the current month to the current time on today's date, inclusive. Specify the start in a 24-hour notation. Use the following format: <code>YYYY-MM-DDTHH:mm:SSZ</code>, where <code>T</code> and <code>Z</code> are literal characters. For example, to specify 11:30pm on March 5, 2020, enter <code>2020-03-05T23:30:00Z</code>.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.purchase_offering_request.PurchaseOfferingRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.purchase_offering_response.PurchaseOfferingResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.purchase_offering

            output, http_response = (
                capo_mediaconnect._operations.media_connect.purchase_offering.purchase_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PurchaseOffering")
        )
        input_: capo_mediaconnect.types.purchase_offering_request.PurchaseOfferingRequest = {
            "offering_arn": offering_arn
        }
        if reservation_name is not None:
            input_["reservation_name"] = reservation_name
        if start is not None:
            input_["start"] = start

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        reservation_arn: "capo_mediaconnect.types.reservation_arn.ReservationArn",
        *,
        config_overrides: Optional[MediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_reservation_response.DescribeReservationResponse":
        """<p> Displays the details of a reservation. The response includes the reservation name, state, start date and time, and the details of the offering that make up the rest of the reservation (such as price, duration, and outbound bandwidth).</p>

        Args:
            reservation_arn: <p>The Amazon Resource Name (ARN) of the offering. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.describe_reservation_request.DescribeReservationRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.describe_reservation_response.DescribeReservationResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_reservation

            output, http_response = (
                capo_mediaconnect._operations.media_connect.describe_reservation.describe_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeReservation")
        )
        input_: capo_mediaconnect.types.describe_reservation_request.DescribeReservationRequest = {
            "reservation_arn": reservation_arn
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
    ) -> "capo_mediaconnect.types.list_reservations_response.ListReservationsResponse":
        """<p> Displays a list of all reservations that have been purchased by this account in the current Amazon Web Services Region. This list includes all reservations in all states (such as active and expired).</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListReservations</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListReservations</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListOfferings</code> request a second time and specify the <code>NextToken</code> value. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediaconnect.types.list_reservations_request.ListReservationsRequest]",
        ) -> OperationResponse[
            "capo_mediaconnect.types.list_reservations_response.ListReservationsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_reservations

            output, http_response = (
                capo_mediaconnect._operations.media_connect.list_reservations.list_reservations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListReservations")
        )
        input_: capo_mediaconnect.types.list_reservations_request.ListReservationsRequest = {}
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


class AsyncReservationResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service

    async def create(
        self,
        offering_arn: str,
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
        reservation_name: Optional[str] = None,
        start: Optional[str] = None,
    ) -> "capo_mediaconnect.types.purchase_offering_response.PurchaseOfferingResponse":
        """<p> Submits a request to purchase an offering. If you already have an active reservation, you can't purchase another offering.</p>

        Args:
            offering_arn: <p> The Amazon Resource Name (ARN) of the offering.</p>
            reservation_name: <p> The name that you want to use for the reservation.</p>
            start: <p> The date and time that you want the reservation to begin, in Coordinated Universal Time (UTC). </p> <p>You can specify any date and time between 12:00am on the first day of the current month to the current time on today's date, inclusive. Specify the start in a 24-hour notation. Use the following format: <code>YYYY-MM-DDTHH:mm:SSZ</code>, where <code>T</code> and <code>Z</code> are literal characters. For example, to specify 11:30pm on March 5, 2020, enter <code>2020-03-05T23:30:00Z</code>.</p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.forbidden_exception.ForbiddenException: <p>You do not have sufficient access to perform this action. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.purchase_offering_request.PurchaseOfferingRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.purchase_offering_response.PurchaseOfferingResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.purchase_offering

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.purchase_offering.async_purchase_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PurchaseOffering")
        )
        input_: capo_mediaconnect.types.purchase_offering_request.PurchaseOfferingRequest = {
            "offering_arn": offering_arn
        }
        if reservation_name is not None:
            input_["reservation_name"] = reservation_name
        if start is not None:
            input_["start"] = start

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        reservation_arn: "capo_mediaconnect.types.reservation_arn.ReservationArn",
        *,
        config_overrides: Optional[AsyncMediaConnectClientConfig] = None,
    ) -> "capo_mediaconnect.types.describe_reservation_response.DescribeReservationResponse":
        """<p> Displays the details of a reservation. The response includes the reservation name, state, start date and time, and the details of the offering that make up the rest of the reservation (such as price, duration, and outbound bandwidth).</p>

        Args:
            reservation_arn: <p>The Amazon Resource Name (ARN) of the offering. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.not_found_exception.NotFoundException: <p>One or more of the resources in the request does not exist in the system. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.describe_reservation_request.DescribeReservationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.describe_reservation_response.DescribeReservationResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.describe_reservation

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.describe_reservation.async_describe_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeReservation")
        )
        input_: capo_mediaconnect.types.describe_reservation_request.DescribeReservationRequest = {
            "reservation_arn": reservation_arn
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
    ) -> "capo_mediaconnect.types.list_reservations_response.ListReservationsResponse":
        """<p> Displays a list of all reservations that have been purchased by this account in the current Amazon Web Services Region. This list includes all reservations in all states (such as active and expired).</p>

        Args:
            max_results: <p> The maximum number of results to return per API request. </p> <p>For example, you submit a <code>ListReservations</code> request with <code>MaxResults</code> set at 5. Although 20 items match your request, the service returns no more than the first 5 items. (The service also returns a NextToken value that you can use to fetch the next batch of results.) </p> <p>The service might return fewer results than the <code>MaxResults</code> value. If <code>MaxResults</code> is not included in the request, the service defaults to pagination with a maximum of 10 results per page.</p>
            next_token: <p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListReservations</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListOfferings</code> request a second time and specify the <code>NextToken</code> value. </p>

        Raises:
            capo_mediaconnect.errors.bad_request_exception.BadRequestException: <p>This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message. </p>
            capo_mediaconnect.errors.internal_server_error_exception.InternalServerErrorException: <p>The server encountered an internal error and is unable to complete the request. </p>
            capo_mediaconnect.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is currently unavailable or busy. </p>
            capo_mediaconnect.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was denied due to request throttling. </p>
            capo_mediaconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediaconnect.types.list_reservations_request.ListReservationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediaconnect.types.list_reservations_response.ListReservationsResponse"
        ]:
            import capo_mediaconnect._operations.media_connect.list_reservations

            (
                output,
                http_response,
            ) = await capo_mediaconnect._operations.media_connect.list_reservations.async_list_reservations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListReservations")
        )
        input_: capo_mediaconnect.types.list_reservations_request.ListReservationsRequest = {}
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
