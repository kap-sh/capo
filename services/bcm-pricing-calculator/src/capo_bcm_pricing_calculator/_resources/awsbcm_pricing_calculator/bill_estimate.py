from __future__ import annotations

import datetime
import uuid
from typing import TYPE_CHECKING, Optional

from capo_bcm_pricing_calculator._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.bill_estimate_name
    import capo_bcm_pricing_calculator.types.bill_estimate_summary
    import capo_bcm_pricing_calculator.types.client_token
    import capo_bcm_pricing_calculator.types.create_bill_estimate_request
    import capo_bcm_pricing_calculator.types.create_bill_estimate_response
    import capo_bcm_pricing_calculator.types.delete_bill_estimate_request
    import capo_bcm_pricing_calculator.types.delete_bill_estimate_response
    import capo_bcm_pricing_calculator.types.filter_timestamp
    import capo_bcm_pricing_calculator.types.get_bill_estimate_request
    import capo_bcm_pricing_calculator.types.get_bill_estimate_response
    import capo_bcm_pricing_calculator.types.list_bill_estimates_filters
    import capo_bcm_pricing_calculator.types.list_bill_estimates_request
    import capo_bcm_pricing_calculator.types.list_bill_estimates_response
    import capo_bcm_pricing_calculator.types.max_results
    import capo_bcm_pricing_calculator.types.next_page_token
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.tags
    import capo_bcm_pricing_calculator.types.update_bill_estimate_request
    import capo_bcm_pricing_calculator.types.update_bill_estimate_response
    from capo_bcm_pricing_calculator._services.async_bcm_pricing_calculator import (
        AsyncBCMPricingCalculatorClient,
        AsyncBCMPricingCalculatorClientConfig,
    )
    from capo_bcm_pricing_calculator._services.bcm_pricing_calculator import (
        BCMPricingCalculatorClient,
        BCMPricingCalculatorClientConfig,
    )


class BillEstimate:
    def __init__(self, service: BCMPricingCalculatorClient) -> None:
        self._service = service

    def create(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        name: "capo_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bcm_pricing_calculator.types.tags.Tags"] = None,
    ) -> "capo_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse":
        """<p> Create a Bill estimate from a Bill scenario. In the Bill scenario you can model usage addition, usage changes, and usage removal. You can also model commitment addition and commitment removal. After all changes in a Bill scenario is made satisfactorily, you can call this API with a Bill scenario ID to generate the Bill estimate. Bill estimate calculates the pre-tax cost for your consolidated billing family, incorporating all modeled usage and commitments alongside existing usage and commitments from your most recent completed anniversary bill, with any applicable discounts applied. </p>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to create a Bill estimate. </p>
            name: <p> The name of the Bill estimate that will be created. Names must be unique for an account. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>
            tags: <p> An optional list of tags to associate with the specified BillEstimate. You can use resource tags to control access to your BillEstimate using IAM policies. Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags: </p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services. </p> </li> <li> <p>The maximum length of a key is 128 characters.</p> </li> <li> <p>The maximum length of a value is 256 characters.</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code>.</p> </li> <li> <p>Keys and values are case sensitive.</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services.</p> </li> </ul>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate.create_bill_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateBillEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest = {
            "bill_scenario_id": bill_scenario_id,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse":
        """<p> Retrieves details of a specific bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to retrieve. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate.get_bill_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBillEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest = {
            "identifier": identifier
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
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
        name: Optional[
            "capo_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse":
        """<p> Updates an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to update. </p>
            name: <p> The new name for the bill estimate. </p>
            expires_at: <p> The new expiration date for the bill estimate. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate.update_bill_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBillEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if expires_at is not None:
            input_["expires_at"] = expires_at

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse":
        """<p> Deletes an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to delete. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate.delete_bill_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBillEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest = {
            "identifier": identifier
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
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_bill_estimates_filters.ListBillEstimatesFilters"
        ] = None,
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse":
        """<p> Lists all bill estimates for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill estimates. </p>
            created_at_filter: <p> Filter bill estimates based on the creation date. </p>
            expires_at_filter: <p> Filter bill estimates based on the expiration date. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates.list_bill_estimates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListBillEstimates")
        )
        input_: capo_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if created_at_filter is not None:
            input_["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input_["expires_at_filter"] = expires_at_filter
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


class AsyncBillEstimate:
    def __init__(self, service: AsyncBCMPricingCalculatorClient) -> None:
        self._service = service

    async def create(
        self,
        bill_scenario_id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        name: "capo_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bcm_pricing_calculator.types.tags.Tags"] = None,
    ) -> "capo_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse":
        """<p> Create a Bill estimate from a Bill scenario. In the Bill scenario you can model usage addition, usage changes, and usage removal. You can also model commitment addition and commitment removal. After all changes in a Bill scenario is made satisfactorily, you can call this API with a Bill scenario ID to generate the Bill estimate. Bill estimate calculates the pre-tax cost for your consolidated billing family, incorporating all modeled usage and commitments alongside existing usage and commitments from your most recent completed anniversary bill, with any applicable discounts applied. </p>

        Args:
            bill_scenario_id: <p> The ID of the Bill Scenario for which you want to create a Bill estimate. </p>
            name: <p> The name of the Bill estimate that will be created. Names must be unique for an account. </p>
            client_token: <p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>
            tags: <p> An optional list of tags to associate with the specified BillEstimate. You can use resource tags to control access to your BillEstimate using IAM policies. Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags: </p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services. </p> </li> <li> <p>The maximum length of a key is 128 characters.</p> </li> <li> <p>The maximum length of a value is 256 characters.</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code>.</p> </li> <li> <p>Keys and values are case sensitive.</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services.</p> </li> </ul>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.create_bill_estimate_response.CreateBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_estimate.async_create_bill_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateBillEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.create_bill_estimate_request.CreateBillEstimateRequest = {
            "bill_scenario_id": bill_scenario_id,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse":
        """<p> Retrieves details of a specific bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to retrieve. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.get_bill_estimate_response.GetBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_estimate.async_get_bill_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBillEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.get_bill_estimate_request.GetBillEstimateRequest = {
            "identifier": identifier
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
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        name: Optional[
            "capo_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse":
        """<p> Updates an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to update. </p>
            name: <p> The new name for the bill estimate. </p>
            expires_at: <p> The new expiration date for the bill estimate. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified resource was not found. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.update_bill_estimate_response.UpdateBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_estimate.async_update_bill_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBillEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.update_bill_estimate_request.UpdateBillEstimateRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if expires_at is not None:
            input_["expires_at"] = expires_at

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse":
        """<p> Deletes an existing bill estimate. </p>

        Args:
            identifier: <p> The unique identifier of the bill estimate to delete. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.delete_bill_estimate_response.DeleteBillEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_estimate.async_delete_bill_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBillEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.delete_bill_estimate_request.DeleteBillEstimateRequest = {
            "identifier": identifier
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
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_bill_estimates_filters.ListBillEstimatesFilters"
        ] = None,
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse":
        """<p> Lists all bill estimates for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill estimates. </p>
            created_at_filter: <p> Filter bill estimates based on the creation date. </p>
            expires_at_filter: <p> Filter bill estimates based on the expiration date. </p>
            next_token: <p> A token to retrieve the next page of results. </p>
            max_results: <p> The maximum number of results to return per page. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_estimates_response.ListBillEstimatesResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_estimates.async_list_bill_estimates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListBillEstimates")
        )
        input_: capo_bcm_pricing_calculator.types.list_bill_estimates_request.ListBillEstimatesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if created_at_filter is not None:
            input_["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input_["expires_at_filter"] = expires_at_filter
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
