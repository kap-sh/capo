from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

from capo_redshift_serverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_redshift_serverless.types.capacity
    import capo_redshift_serverless.types.create_reservation_request
    import capo_redshift_serverless.types.create_reservation_response
    import capo_redshift_serverless.types.get_reservation_offering_request
    import capo_redshift_serverless.types.get_reservation_offering_response
    import capo_redshift_serverless.types.get_reservation_request
    import capo_redshift_serverless.types.get_reservation_response
    import capo_redshift_serverless.types.list_reservation_offerings_request
    import capo_redshift_serverless.types.list_reservation_offerings_response
    import capo_redshift_serverless.types.list_reservations_request
    import capo_redshift_serverless.types.list_reservations_response
    import capo_redshift_serverless.types.offering_id
    import capo_redshift_serverless.types.pagination_token
    import capo_redshift_serverless.types.reservation
    import capo_redshift_serverless.types.reservation_id
    import capo_redshift_serverless.types.reservation_offering
    from capo_redshift_serverless._services.async_redshift_serverless import (
        AsyncRedshiftServerlessClient,
        AsyncRedshiftServerlessClientConfig,
    )
    from capo_redshift_serverless._services.redshift_serverless import (
        RedshiftServerlessClient,
        RedshiftServerlessClientConfig,
    )


class ReservationResource:
    def __init__(self, service: RedshiftServerlessClient) -> None:
        self._service = service

    def create_reservation(
        self,
        capacity: "capo_redshift_serverless.types.capacity.Capacity",
        offering_id: "capo_redshift_serverless.types.offering_id.OfferingId",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_redshift_serverless.types.create_reservation_response.CreateReservationResponse":
        """<p>Creates an Amazon Redshift Serverless reservation, which gives you the option to commit to a specified number of Redshift Processing Units (RPUs) for a year at a discount from Serverless on-demand (OD) rates.</p>

        Args:
            capacity: <p>The number of Redshift Processing Units (RPUs) to reserve.</p>
            offering_id: <p>The ID of the offering associated with the reservation. The offering determines the payment schedule for the reservation.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. This token must be a valid UUIDv4 value. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/"> Making retries safe with idempotent APIs </a>.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.create_reservation_request.CreateReservationRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.create_reservation_response.CreateReservationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_reservation

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.create_reservation.create_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_reservation_request.CreateReservationRequest = {
            "capacity": capacity,
            "offering_id": offering_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_reservation(
        self,
        reservation_id: "capo_redshift_serverless.types.reservation_id.ReservationId",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> (
        "capo_redshift_serverless.types.get_reservation_response.GetReservationResponse"
    ):
        """<p>Gets an Amazon Redshift Serverless reservation. A reservation gives you the option to commit to a specified number of Redshift Processing Units (RPUs) for a year at a discount from Serverless on-demand (OD) rates.</p>

        Args:
            reservation_id: <p>The ID of the reservation to retrieve.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.get_reservation_request.GetReservationRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.get_reservation_response.GetReservationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_reservation

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.get_reservation.get_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_reservation_request.GetReservationRequest = {
            "reservation_id": reservation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_reservation_offering(
        self,
        offering_id: "capo_redshift_serverless.types.offering_id.OfferingId",
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_reservation_offering_response.GetReservationOfferingResponse":
        """<p>Returns the reservation offering. The offering determines the payment schedule for the reservation.</p>

        Args:
            offering_id: <p>The identifier for the offering..</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.get_reservation_offering_request.GetReservationOfferingRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.get_reservation_offering_response.GetReservationOfferingResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_reservation_offering

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.get_reservation_offering.get_reservation_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_reservation_offering_request.GetReservationOfferingRequest = {
            "offering_id": offering_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_reservation_offerings(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_reservation_offerings_response.ListReservationOfferingsResponse":
        """<p>Returns the current reservation offerings in your account.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.list_reservation_offerings_request.ListReservationOfferingsRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.list_reservation_offerings_response.ListReservationOfferingsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_reservation_offerings

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.list_reservation_offerings.list_reservation_offerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_reservation_offerings_request.ListReservationOfferingsRequest = {}
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

    def list_reservations(
        self,
        *,
        config_overrides: Optional[RedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_reservations_response.ListReservationsResponse":
        """<p>Returns a list of Reservation objects.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_redshift_serverless.types.list_reservations_request.ListReservationsRequest]",
        ) -> OperationResponse[
            "capo_redshift_serverless.types.list_reservations_response.ListReservationsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_reservations

            output, http_response = (
                capo_redshift_serverless._operations.redshift_serverless.list_reservations.list_reservations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_reservations_request.ListReservationsRequest = {}
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


class AsyncReservationResource:
    def __init__(self, service: AsyncRedshiftServerlessClient) -> None:
        self._service = service

    async def create_reservation(
        self,
        capacity: "capo_redshift_serverless.types.capacity.Capacity",
        offering_id: "capo_redshift_serverless.types.offering_id.OfferingId",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_redshift_serverless.types.create_reservation_response.CreateReservationResponse":
        """<p>Creates an Amazon Redshift Serverless reservation, which gives you the option to commit to a specified number of Redshift Processing Units (RPUs) for a year at a discount from Serverless on-demand (OD) rates.</p>

        Args:
            capacity: <p>The number of Redshift Processing Units (RPUs) to reserve.</p>
            offering_id: <p>The ID of the offering associated with the reservation. The offering determines the payment schedule for the reservation.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. This token must be a valid UUIDv4 value. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/"> Making retries safe with idempotent APIs </a>.</p>

        Raises:
            capo_redshift_serverless.errors.conflict_exception.ConflictException: <p>The submitted action has conflicts.</p>
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service limit was exceeded.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeded the number of tags allowed for a resource.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.create_reservation_request.CreateReservationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.create_reservation_response.CreateReservationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.create_reservation

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.create_reservation.async_create_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.create_reservation_request.CreateReservationRequest = {
            "capacity": capacity,
            "offering_id": offering_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_reservation(
        self,
        reservation_id: "capo_redshift_serverless.types.reservation_id.ReservationId",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> (
        "capo_redshift_serverless.types.get_reservation_response.GetReservationResponse"
    ):
        """<p>Gets an Amazon Redshift Serverless reservation. A reservation gives you the option to commit to a specified number of Redshift Processing Units (RPUs) for a year at a discount from Serverless on-demand (OD) rates.</p>

        Args:
            reservation_id: <p>The ID of the reservation to retrieve.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_reservation_request.GetReservationRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_reservation_response.GetReservationResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_reservation

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_reservation.async_get_reservation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_reservation_request.GetReservationRequest = {
            "reservation_id": reservation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_reservation_offering(
        self,
        offering_id: "capo_redshift_serverless.types.offering_id.OfferingId",
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
    ) -> "capo_redshift_serverless.types.get_reservation_offering_response.GetReservationOfferingResponse":
        """<p>Returns the reservation offering. The offering determines the payment schedule for the reservation.</p>

        Args:
            offering_id: <p>The identifier for the offering..</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.get_reservation_offering_request.GetReservationOfferingRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.get_reservation_offering_response.GetReservationOfferingResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.get_reservation_offering

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.get_reservation_offering.async_get_reservation_offering(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.get_reservation_offering_request.GetReservationOfferingRequest = {
            "offering_id": offering_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_reservation_offerings(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_reservation_offerings_response.ListReservationOfferingsResponse":
        """<p>Returns the current reservation offerings in your account.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_reservation_offerings_request.ListReservationOfferingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_reservation_offerings_response.ListReservationOfferingsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_reservation_offerings

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_reservation_offerings.async_list_reservation_offerings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_reservation_offerings_request.ListReservationOfferingsRequest = {}
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

    async def list_reservations(
        self,
        *,
        config_overrides: Optional[AsyncRedshiftServerlessClientConfig] = None,
        next_token: Optional[
            "capo_redshift_serverless.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_redshift_serverless.types.list_reservations_response.ListReservationsResponse":
        """<p>Returns a list of Reservation objects.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_redshift_serverless.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_redshift_serverless.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_redshift_serverless.errors.validation_exception.ValidationException: <p>The input failed to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_redshift_serverless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_redshift_serverless.types.list_reservations_request.ListReservationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_redshift_serverless.types.list_reservations_response.ListReservationsResponse"
        ]:
            import capo_redshift_serverless._operations.redshift_serverless.list_reservations

            (
                output,
                http_response,
            ) = await capo_redshift_serverless._operations.redshift_serverless.list_reservations.async_list_reservations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_redshift_serverless.types.list_reservations_request.ListReservationsRequest = {}
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
