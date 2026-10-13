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
    import capo_bcm_pricing_calculator.types.bill_scenario_name
    import capo_bcm_pricing_calculator.types.bill_scenario_summary
    import capo_bcm_pricing_calculator.types.client_token
    import capo_bcm_pricing_calculator.types.cost_category_arn
    import capo_bcm_pricing_calculator.types.create_bill_scenario_request
    import capo_bcm_pricing_calculator.types.create_bill_scenario_response
    import capo_bcm_pricing_calculator.types.delete_bill_scenario_request
    import capo_bcm_pricing_calculator.types.delete_bill_scenario_response
    import capo_bcm_pricing_calculator.types.filter_timestamp
    import capo_bcm_pricing_calculator.types.get_bill_scenario_request
    import capo_bcm_pricing_calculator.types.get_bill_scenario_response
    import capo_bcm_pricing_calculator.types.group_sharing_preference_enum
    import capo_bcm_pricing_calculator.types.list_bill_scenarios_filters
    import capo_bcm_pricing_calculator.types.list_bill_scenarios_request
    import capo_bcm_pricing_calculator.types.list_bill_scenarios_response
    import capo_bcm_pricing_calculator.types.max_results
    import capo_bcm_pricing_calculator.types.next_page_token
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.tags
    import capo_bcm_pricing_calculator.types.update_bill_scenario_request
    import capo_bcm_pricing_calculator.types.update_bill_scenario_response
    from capo_bcm_pricing_calculator._services.async_bcm_pricing_calculator import (
        AsyncBCMPricingCalculatorClient,
        AsyncBCMPricingCalculatorClientConfig,
    )
    from capo_bcm_pricing_calculator._services.bcm_pricing_calculator import (
        BCMPricingCalculatorClient,
        BCMPricingCalculatorClientConfig,
    )


class BillScenario:
    def __init__(self, service: BCMPricingCalculatorClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bcm_pricing_calculator.types.tags.Tags"] = None,
        group_sharing_preference: Optional[
            "capo_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "capo_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse":
        """<p> Creates a new bill scenario to model potential changes to Amazon Web Services usage and costs. </p>

        Args:
            name: <p> A descriptive name for the bill scenario. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            tags: <p> The tags to apply to the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>

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
            req: "OperationRequest[capo_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario.create_bill_scenario(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateBillScenario")
        )
        input_: capo_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if group_sharing_preference is not None:
            input_["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input_["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
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
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse":
        """<p> Retrieves details of a specific bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to retrieve. </p>

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
            req: "OperationRequest[capo_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario.get_bill_scenario(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBillScenario")
        )
        input_: capo_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest = {
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
            "capo_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
        group_sharing_preference: Optional[
            "capo_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "capo_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse":
        """<p> Updates an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to update. </p>
            name: <p> The new name for the bill scenario. </p>
            expires_at: <p> The new expiration date for the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>

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
            req: "OperationRequest[capo_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario.update_bill_scenario(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBillScenario")
        )
        input_: capo_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if expires_at is not None:
            input_["expires_at"] = expires_at
        if group_sharing_preference is not None:
            input_["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input_["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
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
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse":
        """<p> Deletes an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to delete. </p>

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
            req: "OperationRequest[capo_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario.delete_bill_scenario(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBillScenario")
        )
        input_: capo_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest = {
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
            "capo_bcm_pricing_calculator.types.list_bill_scenarios_filters.ListBillScenariosFilters"
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
    ) -> "capo_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse":
        """<p> Lists all bill scenarios for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill scenarios. </p>
            created_at_filter: <p> Filter bill scenarios based on the creation date. </p>
            expires_at_filter: <p> Filter bill scenarios based on the expiration date. </p>
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
            req: "OperationRequest[capo_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest]",
        ) -> OperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios

            output, http_response = (
                capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios.list_bill_scenarios(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListBillScenarios")
        )
        input_: capo_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest = {}
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


class AsyncBillScenario:
    def __init__(self, service: AsyncBCMPricingCalculatorClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
        client_token: Optional[
            "capo_bcm_pricing_calculator.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bcm_pricing_calculator.types.tags.Tags"] = None,
        group_sharing_preference: Optional[
            "capo_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "capo_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse":
        """<p> Creates a new bill scenario to model potential changes to Amazon Web Services usage and costs. </p>

        Args:
            name: <p> A descriptive name for the bill scenario. </p>
            client_token: <p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>
            tags: <p> The tags to apply to the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>

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
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.create_bill_scenario_response.CreateBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.create_bill_scenario.async_create_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateBillScenario")
        )
        input_: capo_bcm_pricing_calculator.types.create_bill_scenario_request.CreateBillScenarioRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if group_sharing_preference is not None:
            input_["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input_["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
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
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse":
        """<p> Retrieves details of a specific bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to retrieve. </p>

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
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.get_bill_scenario_response.GetBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.get_bill_scenario.async_get_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetBillScenario")
        )
        input_: capo_bcm_pricing_calculator.types.get_bill_scenario_request.GetBillScenarioRequest = {
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
            "capo_bcm_pricing_calculator.types.bill_scenario_name.BillScenarioName"
        ] = None,
        expires_at: Optional[datetime.datetime] = None,
        group_sharing_preference: Optional[
            "capo_bcm_pricing_calculator.types.group_sharing_preference_enum.GroupSharingPreferenceEnum"
        ] = None,
        cost_category_group_sharing_preference_arn: Optional[
            "capo_bcm_pricing_calculator.types.cost_category_arn.CostCategoryArn"
        ] = None,
    ) -> "capo_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse":
        """<p> Updates an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to update. </p>
            name: <p> The new name for the bill scenario. </p>
            expires_at: <p> The new expiration date for the bill scenario. </p>
            group_sharing_preference: <p>The setting for the reserved instance and savings plan group sharing used in this estimate.</p>
            cost_category_group_sharing_preference_arn: <p>The arn of the cost category used in the reserved and prioritized group sharing.</p>

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
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.update_bill_scenario_response.UpdateBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.update_bill_scenario.async_update_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateBillScenario")
        )
        input_: capo_bcm_pricing_calculator.types.update_bill_scenario_request.UpdateBillScenarioRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if expires_at is not None:
            input_["expires_at"] = expires_at
        if group_sharing_preference is not None:
            input_["group_sharing_preference"] = group_sharing_preference
        if cost_category_group_sharing_preference_arn is not None:
            input_["cost_category_group_sharing_preference_arn"] = (
                cost_category_group_sharing_preference_arn
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
        identifier: "capo_bcm_pricing_calculator.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncBCMPricingCalculatorClientConfig] = None,
    ) -> "capo_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse":
        """<p> Deletes an existing bill scenario. </p>

        Args:
            identifier: <p> The unique identifier of the bill scenario to delete. </p>

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
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.delete_bill_scenario_response.DeleteBillScenarioResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.delete_bill_scenario.async_delete_bill_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteBillScenario")
        )
        input_: capo_bcm_pricing_calculator.types.delete_bill_scenario_request.DeleteBillScenarioRequest = {
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
            "capo_bcm_pricing_calculator.types.list_bill_scenarios_filters.ListBillScenariosFilters"
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
    ) -> "capo_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse":
        """<p> Lists all bill scenarios for the account. </p>

        Args:
            filters: <p> Filters to apply to the list of bill scenarios. </p>
            created_at_filter: <p> Filter bill scenarios based on the creation date. </p>
            expires_at_filter: <p> Filter bill scenarios based on the expiration date. </p>
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
            req: "AsyncOperationRequest[capo_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest]",
        ) -> AsyncOperationResponse[
            "capo_bcm_pricing_calculator.types.list_bill_scenarios_response.ListBillScenariosResponse"
        ]:
            import capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios

            (
                output,
                http_response,
            ) = await capo_bcm_pricing_calculator._operations.awsbcm_pricing_calculator.list_bill_scenarios.async_list_bill_scenarios(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListBillScenarios")
        )
        input_: capo_bcm_pricing_calculator.types.list_bill_scenarios_request.ListBillScenariosRequest = {}
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
