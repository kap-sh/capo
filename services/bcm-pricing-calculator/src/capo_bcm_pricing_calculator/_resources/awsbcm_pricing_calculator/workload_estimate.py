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
    import capo_bcm_pricing_calculator.types.client_token
    import capo_bcm_pricing_calculator.types.create_workload_estimate_request
    import capo_bcm_pricing_calculator.types.create_workload_estimate_response
    import capo_bcm_pricing_calculator.types.delete_workload_estimate_request
    import capo_bcm_pricing_calculator.types.delete_workload_estimate_response
    import capo_bcm_pricing_calculator.types.filter_timestamp
    import capo_bcm_pricing_calculator.types.get_workload_estimate_request
    import capo_bcm_pricing_calculator.types.get_workload_estimate_response
    import capo_bcm_pricing_calculator.types.list_workload_estimates_filters
    import capo_bcm_pricing_calculator.types.list_workload_estimates_request
    import capo_bcm_pricing_calculator.types.list_workload_estimates_response
    import capo_bcm_pricing_calculator.types.max_results
    import capo_bcm_pricing_calculator.types.next_page_token
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.tags
    import capo_bcm_pricing_calculator.types.update_workload_estimate_request
    import capo_bcm_pricing_calculator.types.update_workload_estimate_response
    import capo_bcm_pricing_calculator.types.workload_estimate_name
    import capo_bcm_pricing_calculator.types.workload_estimate_rate_type
    import capo_bcm_pricing_calculator.types.workload_estimate_summary
    from capo_bcm_pricing_calculator._services.async_bcm_pricing_calculator import (
        AsyncBCMPricingCalculatorClient,
        AsyncBCMPricingCalculatorClientConfig,
    )
    from capo_bcm_pricing_calculator._services.bcm_pricing_calculator import (
        BCMPricingCalculatorClient,
        BCMPricingCalculatorClientConfig,
    )


class WorkloadEstimate:
    def __init__(self, service: BCMPricingCalculatorClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        rate_type: Optional[
            "capo_bcm_pricing_calculator.types.workload_estimate_rate_type.WorkloadEstimateRateType"
        ] = None,
        tags: Optional["capo_bcm_pricing_calculator.types.tags.Tags"] = None,
    ) -> "capo_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse":
        """<p> Creates a new workload estimate to model costs for a specific workload. </p>

        Args:
            name: <p> A descriptive name for the workload estimate. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            rate_type: <p> The type of pricing rates to use for the estimate. </p>
            tags: <p> The tags to apply to the workload estimate. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate.create_workload_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkloadEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if rate_type is not None:
            input_["rate_type"] = rate_type
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
    ) -> "capo_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse":
        """<p> Retrieves details of a specific workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to retrieve. </p>

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
            req: "OperationRequest[capo_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate.get_workload_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkloadEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest = {
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
            "capo_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse":
        """<p> Updates an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to update. </p>
            name: <p> The new name for the workload estimate. </p>
            expires_at: <p> The new expiration date for the workload estimate. </p>

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
            req: "OperationRequest[capo_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate.update_workload_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkloadEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest = {
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
    ) -> "capo_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse":
        """<p> Deletes an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to delete. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate.delete_workload_estimate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkloadEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest = {
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
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_workload_estimates_filters.ListWorkloadEstimatesFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse":
        """<p> Lists all workload estimates for the account. </p>

        Args:
            created_at_filter: <p> Filter workload estimates based on the creation date. </p>
            expires_at_filter: <p> Filter workload estimates based on the expiration date. </p>
            filters: <p> Filters to apply to the list of workload estimates. </p>
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
            req: "OperationRequest[capo_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates.list_workload_estimates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkloadEstimates")
        )
        input_: capo_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest = {}
        if created_at_filter is not None:
            input_["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input_["expires_at_filter"] = expires_at_filter
        if filters is not None:
            input_["filters"] = filters
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


class AsyncWorkloadEstimate:
    def __init__(self, service: AsyncBCMPricingCalculatorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        rate_type: Optional[
            "capo_bcm_pricing_calculator.types.workload_estimate_rate_type.WorkloadEstimateRateType"
        ] = None,
        tags: Optional["capo_bcm_pricing_calculator.types.tags.Tags"] = None,
    ) -> "capo_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse":
        """<p> Creates a new workload estimate to model costs for a specific workload. </p>

        Args:
            name: <p> A descriptive name for the workload estimate. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            rate_type: <p> The type of pricing rates to use for the estimate. </p>
            tags: <p> The tags to apply to the workload estimate. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.conflict_exception.ConflictException: <p> The request could not be processed because of conflict in the current state of the resource. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The request would cause you to exceed your service quota. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.create_workload_estimate_response.CreateWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_workload_estimate.async_create_workload_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateWorkloadEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.create_workload_estimate_request.CreateWorkloadEstimateRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if rate_type is not None:
            input_["rate_type"] = rate_type
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
    ) -> "capo_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse":
        """<p> Retrieves details of a specific workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to retrieve. </p>

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
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.get_workload_estimate_response.GetWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_workload_estimate.async_get_workload_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWorkloadEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.get_workload_estimate_request.GetWorkloadEstimateRequest = {
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
            "capo_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse":
        """<p> Updates an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to update. </p>
            name: <p> The new name for the workload estimate. </p>
            expires_at: <p> The new expiration date for the workload estimate. </p>

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
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.update_workload_estimate_response.UpdateWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_workload_estimate.async_update_workload_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateWorkloadEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.update_workload_estimate_request.UpdateWorkloadEstimateRequest = {
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
    ) -> "capo_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse":
        """<p> Deletes an existing workload estimate. </p>

        Args:
            identifier: <p> The unique identifier of the workload estimate to delete. </p>

        Raises:
            capo_bcm_pricing_calculator.errors.access_denied_exception.AccessDeniedException: <p> You do not have sufficient access to perform this action. </p>
            capo_bcm_pricing_calculator.errors.internal_server_exception.InternalServerException: <p> An internal error has occurred. Retry your request, but if the problem persists, contact Amazon Web Services support. </p>
            capo_bcm_pricing_calculator.errors.throttling_exception.ThrottlingException: <p> The request was denied due to request throttling. </p>
            capo_bcm_pricing_calculator.errors.validation_exception.ValidationException: <p> The input provided fails to satisfy the constraints specified by an Amazon Web Services service. </p>
            capo_bcm_pricing_calculator.errors.data_unavailable_exception.DataUnavailableException: <p> The requested data is currently unavailable. </p>
            capo_bcm_pricing_calculator.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.delete_workload_estimate_response.DeleteWorkloadEstimateResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_workload_estimate.async_delete_workload_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWorkloadEstimate")
        )
        input_: capo_bcm_pricing_calculator.types.delete_workload_estimate_request.DeleteWorkloadEstimateRequest = {
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
        created_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        expires_at_filter: Optional[
            "capo_bcm_pricing_calculator.types.filter_timestamp.FilterTimestamp"
        ] = None,
        filters: Optional[
            "capo_bcm_pricing_calculator.types.list_workload_estimates_filters.ListWorkloadEstimatesFilters"
        ] = None,
        next_token: Optional[
            "capo_bcm_pricing_calculator.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_bcm_pricing_calculator.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse":
        """<p> Lists all workload estimates for the account. </p>

        Args:
            created_at_filter: <p> Filter workload estimates based on the creation date. </p>
            expires_at_filter: <p> Filter workload estimates based on the expiration date. </p>
            filters: <p> Filters to apply to the list of workload estimates. </p>
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
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_workload_estimates_response.ListWorkloadEstimatesResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_workload_estimates.async_list_workload_estimates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWorkloadEstimates")
        )
        input_: capo_bcm_pricing_calculator.types.list_workload_estimates_request.ListWorkloadEstimatesRequest = {}
        if created_at_filter is not None:
            input_["created_at_filter"] = created_at_filter
        if expires_at_filter is not None:
            input_["expires_at_filter"] = expires_at_filter
        if filters is not None:
            input_["filters"] = filters
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
