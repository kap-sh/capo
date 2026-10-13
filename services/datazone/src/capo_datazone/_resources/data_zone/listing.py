from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.delete_listing_input
    import capo_datazone.types.delete_listing_output
    import capo_datazone.types.domain_id
    import capo_datazone.types.get_listing_input
    import capo_datazone.types.get_listing_output
    import capo_datazone.types.listing_id
    import capo_datazone.types.revision
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class Listing:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def read(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        listing_revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_listing_output.GetListingOutput":
        """<p>Gets a listing (a record of an asset at a given time). If you specify a listing version, only details that are specific to that version are returned.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing.</p>
            listing_revision: <p>The revision of the listing.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.get_listing_input.GetListingInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_listing_output.GetListingOutput"
        ]:
            import capo_datazone._operations.data_zone.get_listing

            output, http_response = (
                capo_datazone._operations.data_zone.get_listing.get_listing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_listing_output.GetListingOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_listing_output

            return capo_datazone.types.get_listing_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetListing", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_listing_input.GetListingInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if listing_revision is not None:
            input_["listing_revision"] = listing_revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_listing_output.DeleteListingOutput":
        """<p>Deletes a listing (a record of an asset at a given time).</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing to be deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.delete_listing_input.DeleteListingInput]",
        ) -> OperationResponse[
            "capo_datazone.types.delete_listing_output.DeleteListingOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_listing

            output, http_response = (
                capo_datazone._operations.data_zone.delete_listing.delete_listing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteListing")
        )
        input_: capo_datazone.types.delete_listing_input.DeleteListingInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncListing:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def read(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        listing_revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_listing_output.GetListingOutput":
        """<p>Gets a listing (a record of an asset at a given time). If you specify a listing version, only details that are specific to that version are returned.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing.</p>
            listing_revision: <p>The revision of the listing.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_listing_input.GetListingInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_listing_output.GetListingOutput"
        ]:
            import capo_datazone._operations.data_zone.get_listing

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_listing.async_get_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_datazone.types.get_listing_output.GetListingOutput",
        ) -> dict[str, Any]:
            import capo_datazone.types.get_listing_output

            return capo_datazone.types.get_listing_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetListing", redact_output=_redact_output),
        )
        input_: capo_datazone.types.get_listing_input.GetListingInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if listing_revision is not None:
            input_["listing_revision"] = listing_revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_listing_output.DeleteListingOutput":
        """<p>Deletes a listing (a record of an asset at a given time).</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing to be deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_listing_input.DeleteListingInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_listing_output.DeleteListingOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_listing

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_listing.async_delete_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteListing")
        )
        input_: capo_datazone.types.delete_listing_input.DeleteListingInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
