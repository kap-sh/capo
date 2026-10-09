"""Generated from Smithy shape ``com.amazonaws.savingsplans#AWSSavingsPlan``."""

import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_savingsplans._auth._signers
import capo_savingsplans._auth._sigv4
from capo_savingsplans._auth._identity import Credentials
from capo_savingsplans._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_savingsplans._auth._zapros_handler import AuthMiddleware
from capo_savingsplans._services._aws_config import aws_config
from capo_savingsplans._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_savingsplans.types.amount
    import capo_savingsplans.types.client_token
    import capo_savingsplans.types.create_savings_plan_request
    import capo_savingsplans.types.create_savings_plan_response
    import capo_savingsplans.types.currency_list
    import capo_savingsplans.types.date_time
    import capo_savingsplans.types.delete_queued_savings_plan_request
    import capo_savingsplans.types.delete_queued_savings_plan_response
    import capo_savingsplans.types.describe_savings_plan_rates_request
    import capo_savingsplans.types.describe_savings_plan_rates_response
    import capo_savingsplans.types.describe_savings_plans_offering_rates_request
    import capo_savingsplans.types.describe_savings_plans_offering_rates_response
    import capo_savingsplans.types.describe_savings_plans_offerings_request
    import capo_savingsplans.types.describe_savings_plans_offerings_response
    import capo_savingsplans.types.describe_savings_plans_request
    import capo_savingsplans.types.describe_savings_plans_response
    import capo_savingsplans.types.durations_list
    import capo_savingsplans.types.list_tags_for_resource_request
    import capo_savingsplans.types.list_tags_for_resource_response
    import capo_savingsplans.types.max_results
    import capo_savingsplans.types.page_size
    import capo_savingsplans.types.pagination_token
    import capo_savingsplans.types.return_savings_plan_request
    import capo_savingsplans.types.return_savings_plan_response
    import capo_savingsplans.types.savings_plan_arn
    import capo_savingsplans.types.savings_plan_arn_list
    import capo_savingsplans.types.savings_plan_descriptions_list
    import capo_savingsplans.types.savings_plan_filter_list
    import capo_savingsplans.types.savings_plan_id
    import capo_savingsplans.types.savings_plan_id_list
    import capo_savingsplans.types.savings_plan_offering_filters_list
    import capo_savingsplans.types.savings_plan_offering_id
    import capo_savingsplans.types.savings_plan_offering_rate_filters_list
    import capo_savingsplans.types.savings_plan_operation_list
    import capo_savingsplans.types.savings_plan_payment_option_list
    import capo_savingsplans.types.savings_plan_product_type
    import capo_savingsplans.types.savings_plan_product_type_list
    import capo_savingsplans.types.savings_plan_rate_filter_list
    import capo_savingsplans.types.savings_plan_rate_operation_list
    import capo_savingsplans.types.savings_plan_rate_service_code_list
    import capo_savingsplans.types.savings_plan_rate_usage_type_list
    import capo_savingsplans.types.savings_plan_service_code_list
    import capo_savingsplans.types.savings_plan_state_list
    import capo_savingsplans.types.savings_plan_type_list
    import capo_savingsplans.types.savings_plan_usage_type_list
    import capo_savingsplans.types.tag_key_list
    import capo_savingsplans.types.tag_map
    import capo_savingsplans.types.tag_resource_request
    import capo_savingsplans.types.tag_resource_response
    import capo_savingsplans.types.untag_resource_request
    import capo_savingsplans.types.untag_resource_response
    import capo_savingsplans.types.uui_ds


class savingsplansClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class savingsplansClient:
    """A client for the ``savingsplans`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = savingsplansClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[savingsplansClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: savingsplansClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def create_savings_plan(
        self,
        savings_plan_offering_id: "capo_savingsplans.types.savings_plan_offering_id.SavingsPlanOfferingId",
        commitment: "capo_savingsplans.types.amount.Amount",
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
        upfront_payment_amount: Optional[
            "capo_savingsplans.types.amount.Amount"
        ] = None,
        purchase_time: Optional["capo_savingsplans.types.date_time.DateTime"] = None,
        client_token: Optional[
            "capo_savingsplans.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_savingsplans.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_savingsplans.types.create_savings_plan_response.CreateSavingsPlanResponse"
    ):
        """<p>Creates a Savings Plan.</p>

        Args:
            savings_plan_offering_id: <p>The ID of the offering.</p>
            commitment: <p>The hourly commitment, in the same currency of the <code>savingsPlanOfferingId</code>. This is a value between 0.001 and 1 million. You cannot specify more than five digits after the decimal point.</p>
            upfront_payment_amount: <p>The up-front payment amount. This is a whole number between 50 and 99 percent of the total value of the Savings Plan. This parameter is only supported if the payment option is <code>Partial Upfront</code>.</p>
            purchase_time: <p>The purchase time of the Savings Plan in UTC format (YYYY-MM-DDTHH:MM:SSZ).</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            tags: <p>One or more tags.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_savingsplans.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota has been exceeded.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.create_savings_plan_request.CreateSavingsPlanRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.create_savings_plan_response.CreateSavingsPlanResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.create_savings_plan

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.create_savings_plan.create_savings_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.create_savings_plan_request.CreateSavingsPlanRequest = {
            "savings_plan_offering_id": savings_plan_offering_id,
            "commitment": commitment,
        }
        if upfront_payment_amount is not None:
            input_["upfront_payment_amount"] = upfront_payment_amount
        if purchase_time is not None:
            input_["purchase_time"] = purchase_time
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

    def delete_queued_savings_plan(
        self,
        savings_plan_id: "capo_savingsplans.types.savings_plan_id.SavingsPlanId",
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
    ) -> "capo_savingsplans.types.delete_queued_savings_plan_response.DeleteQueuedSavingsPlanResponse":
        """<p>Deletes the queued purchase for the specified Savings Plan.</p>

        Args:
            savings_plan_id: <p>The ID of the Savings Plan.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_savingsplans.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota has been exceeded.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.delete_queued_savings_plan_request.DeleteQueuedSavingsPlanRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.delete_queued_savings_plan_response.DeleteQueuedSavingsPlanResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.delete_queued_savings_plan

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.delete_queued_savings_plan.delete_queued_savings_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.delete_queued_savings_plan_request.DeleteQueuedSavingsPlanRequest = {
            "savings_plan_id": savings_plan_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_savings_plan_rates(
        self,
        savings_plan_id: "capo_savingsplans.types.savings_plan_id.SavingsPlanId",
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
        filters: Optional[
            "capo_savingsplans.types.savings_plan_rate_filter_list.SavingsPlanRateFilterList"
        ] = None,
        next_token: Optional[
            "capo_savingsplans.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_savingsplans.types.max_results.MaxResults"] = None,
    ) -> "capo_savingsplans.types.describe_savings_plan_rates_response.DescribeSavingsPlanRatesResponse":
        """<p>Describes the rates for a specific, existing Savings Plan.</p>

        Args:
            savings_plan_id: <p>The ID of the Savings Plan.</p>
            filters: <p>The filters.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.describe_savings_plan_rates_request.DescribeSavingsPlanRatesRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.describe_savings_plan_rates_response.DescribeSavingsPlanRatesResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.describe_savings_plan_rates

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.describe_savings_plan_rates.describe_savings_plan_rates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.describe_savings_plan_rates_request.DescribeSavingsPlanRatesRequest = {
            "savings_plan_id": savings_plan_id
        }
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

    def describe_savings_plans(
        self,
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
        savings_plan_arns: Optional[
            "capo_savingsplans.types.savings_plan_arn_list.SavingsPlanArnList"
        ] = None,
        savings_plan_ids: Optional[
            "capo_savingsplans.types.savings_plan_id_list.SavingsPlanIdList"
        ] = None,
        next_token: Optional[
            "capo_savingsplans.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_savingsplans.types.max_results.MaxResults"] = None,
        states: Optional[
            "capo_savingsplans.types.savings_plan_state_list.SavingsPlanStateList"
        ] = None,
        filters: Optional[
            "capo_savingsplans.types.savings_plan_filter_list.SavingsPlanFilterList"
        ] = None,
    ) -> "capo_savingsplans.types.describe_savings_plans_response.DescribeSavingsPlansResponse":
        """<p>Describes the specified Savings Plans.</p>

        Args:
            savings_plan_arns: <p>The Amazon Resource Names (ARN) of the Savings Plans.</p>
            savings_plan_ids: <p>The IDs of the Savings Plans.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>
            states: <p>The current states of the Savings Plans.</p>
            filters: <p>The filters.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.describe_savings_plans_request.DescribeSavingsPlansRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.describe_savings_plans_response.DescribeSavingsPlansResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.describe_savings_plans

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.describe_savings_plans.describe_savings_plans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.describe_savings_plans_request.DescribeSavingsPlansRequest = {}
        if savings_plan_arns is not None:
            input_["savings_plan_arns"] = savings_plan_arns
        if savings_plan_ids is not None:
            input_["savings_plan_ids"] = savings_plan_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if states is not None:
            input_["states"] = states
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_savings_plans_offering_rates(
        self,
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
        savings_plan_offering_ids: Optional[
            "capo_savingsplans.types.uui_ds.UUIDs"
        ] = None,
        savings_plan_payment_options: Optional[
            "capo_savingsplans.types.savings_plan_payment_option_list.SavingsPlanPaymentOptionList"
        ] = None,
        savings_plan_types: Optional[
            "capo_savingsplans.types.savings_plan_type_list.SavingsPlanTypeList"
        ] = None,
        products: Optional[
            "capo_savingsplans.types.savings_plan_product_type_list.SavingsPlanProductTypeList"
        ] = None,
        service_codes: Optional[
            "capo_savingsplans.types.savings_plan_rate_service_code_list.SavingsPlanRateServiceCodeList"
        ] = None,
        usage_types: Optional[
            "capo_savingsplans.types.savings_plan_rate_usage_type_list.SavingsPlanRateUsageTypeList"
        ] = None,
        operations: Optional[
            "capo_savingsplans.types.savings_plan_rate_operation_list.SavingsPlanRateOperationList"
        ] = None,
        filters: Optional[
            "capo_savingsplans.types.savings_plan_offering_rate_filters_list.SavingsPlanOfferingRateFiltersList"
        ] = None,
        next_token: Optional[
            "capo_savingsplans.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_savingsplans.types.page_size.PageSize"] = None,
    ) -> "capo_savingsplans.types.describe_savings_plans_offering_rates_response.DescribeSavingsPlansOfferingRatesResponse":
        """<p>Describes the offering rates for Savings Plans you might want to purchase.</p>

        Args:
            savings_plan_offering_ids: <p>The IDs of the offerings.</p>
            savings_plan_payment_options: <p>The payment options.</p>
            savings_plan_types: <p>The plan types.</p>
            products: <p>The Amazon Web Services products.</p>
            service_codes: <p>The services.</p>
            usage_types: <p>The usage details of the line item in the billing report.</p>
            operations: <p>The specific Amazon Web Services operation for the line item in the billing report.</p>
            filters: <p>The filters.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.describe_savings_plans_offering_rates_request.DescribeSavingsPlansOfferingRatesRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.describe_savings_plans_offering_rates_response.DescribeSavingsPlansOfferingRatesResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.describe_savings_plans_offering_rates

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.describe_savings_plans_offering_rates.describe_savings_plans_offering_rates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.describe_savings_plans_offering_rates_request.DescribeSavingsPlansOfferingRatesRequest = {}
        if savings_plan_offering_ids is not None:
            input_["savings_plan_offering_ids"] = savings_plan_offering_ids
        if savings_plan_payment_options is not None:
            input_["savings_plan_payment_options"] = savings_plan_payment_options
        if savings_plan_types is not None:
            input_["savings_plan_types"] = savings_plan_types
        if products is not None:
            input_["products"] = products
        if service_codes is not None:
            input_["service_codes"] = service_codes
        if usage_types is not None:
            input_["usage_types"] = usage_types
        if operations is not None:
            input_["operations"] = operations
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

    def describe_savings_plans_offerings(
        self,
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
        offering_ids: Optional["capo_savingsplans.types.uui_ds.UUIDs"] = None,
        payment_options: Optional[
            "capo_savingsplans.types.savings_plan_payment_option_list.SavingsPlanPaymentOptionList"
        ] = None,
        product_type: Optional[
            "capo_savingsplans.types.savings_plan_product_type.SavingsPlanProductType"
        ] = None,
        plan_types: Optional[
            "capo_savingsplans.types.savings_plan_type_list.SavingsPlanTypeList"
        ] = None,
        durations: Optional[
            "capo_savingsplans.types.durations_list.DurationsList"
        ] = None,
        currencies: Optional[
            "capo_savingsplans.types.currency_list.CurrencyList"
        ] = None,
        descriptions: Optional[
            "capo_savingsplans.types.savings_plan_descriptions_list.SavingsPlanDescriptionsList"
        ] = None,
        service_codes: Optional[
            "capo_savingsplans.types.savings_plan_service_code_list.SavingsPlanServiceCodeList"
        ] = None,
        usage_types: Optional[
            "capo_savingsplans.types.savings_plan_usage_type_list.SavingsPlanUsageTypeList"
        ] = None,
        operations: Optional[
            "capo_savingsplans.types.savings_plan_operation_list.SavingsPlanOperationList"
        ] = None,
        filters: Optional[
            "capo_savingsplans.types.savings_plan_offering_filters_list.SavingsPlanOfferingFiltersList"
        ] = None,
        next_token: Optional[
            "capo_savingsplans.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_savingsplans.types.page_size.PageSize"] = None,
    ) -> "capo_savingsplans.types.describe_savings_plans_offerings_response.DescribeSavingsPlansOfferingsResponse":
        """<p>Describes the offerings for the specified Savings Plans.</p>

        Args:
            offering_ids: <p>The IDs of the offerings.</p>
            payment_options: <p>The payment options.</p>
            product_type: <p>The product type.</p>
            plan_types: <p>The plan types.</p>
            durations: <p>The duration, in seconds.</p>
            currencies: <p>The currencies.</p>
            descriptions: <p>The descriptions.</p>
            service_codes: <p>The services.</p>
            usage_types: <p>The usage details of the line item in the billing report.</p>
            operations: <p>The specific Amazon Web Services operation for the line item in the billing report.</p>
            filters: <p>The filters.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve additional results, make another call with the returned token value.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.describe_savings_plans_offerings_request.DescribeSavingsPlansOfferingsRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.describe_savings_plans_offerings_response.DescribeSavingsPlansOfferingsResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.describe_savings_plans_offerings

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.describe_savings_plans_offerings.describe_savings_plans_offerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.describe_savings_plans_offerings_request.DescribeSavingsPlansOfferingsRequest = {}
        if offering_ids is not None:
            input_["offering_ids"] = offering_ids
        if payment_options is not None:
            input_["payment_options"] = payment_options
        if product_type is not None:
            input_["product_type"] = product_type
        if plan_types is not None:
            input_["plan_types"] = plan_types
        if durations is not None:
            input_["durations"] = durations
        if currencies is not None:
            input_["currencies"] = currencies
        if descriptions is not None:
            input_["descriptions"] = descriptions
        if service_codes is not None:
            input_["service_codes"] = service_codes
        if usage_types is not None:
            input_["usage_types"] = usage_types
        if operations is not None:
            input_["operations"] = operations
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_savingsplans.types.savings_plan_arn.SavingsPlanArn",
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
    ) -> "capo_savingsplans.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.list_tags_for_resource

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def return_savings_plan(
        self,
        savings_plan_id: "capo_savingsplans.types.savings_plan_id.SavingsPlanId",
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
        client_token: Optional[
            "capo_savingsplans.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_savingsplans.types.return_savings_plan_response.ReturnSavingsPlanResponse"
    ):
        """<p>Returns the specified Savings Plan.</p>

        Args:
            savings_plan_id: <p>The ID of the Savings Plan.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_savingsplans.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota has been exceeded.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.return_savings_plan_request.ReturnSavingsPlanRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.return_savings_plan_response.ReturnSavingsPlanResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.return_savings_plan

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.return_savings_plan.return_savings_plan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.return_savings_plan_request.ReturnSavingsPlanRequest = {
            "savings_plan_id": savings_plan_id
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

    def tag_resource(
        self,
        resource_arn: "capo_savingsplans.types.savings_plan_arn.SavingsPlanArn",
        tags: "capo_savingsplans.types.tag_map.TagMap",
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
    ) -> "capo_savingsplans.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>One or more tags. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_savingsplans.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A service quota has been exceeded.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.tag_resource

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_savingsplans.types.savings_plan_arn.SavingsPlanArn",
        tag_keys: "capo_savingsplans.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[savingsplansClientConfig] = None,
    ) -> "capo_savingsplans.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_savingsplans.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred.</p>
            capo_savingsplans.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_savingsplans.errors.validation_exception.ValidationException: <p>One of the input parameters is not valid.</p>
            capo_savingsplans.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_savingsplans.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_savingsplans.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_savingsplans._operations.aws_savings_plan.untag_resource

            output, http_response = (
                capo_savingsplans._operations.aws_savings_plan.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_savingsplans.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
