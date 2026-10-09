"""Generated from Smithy shape ``com.amazonaws.billingconductor#AWSBillingConductor``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_billingconductor._auth._signers
import capo_billingconductor._auth._sigv4
from capo_billingconductor._auth._identity import Credentials
from capo_billingconductor._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_billingconductor._auth._zapros_handler import AuthMiddleware
from capo_billingconductor._pagination import resolve_path as _resolve_path
from capo_billingconductor._resources.aws_billing_conductor.billing_group import (
    AsyncBillingGroup,
)
from capo_billingconductor._resources.aws_billing_conductor.custom_line_item import (
    AsyncCustomLineItem,
)
from capo_billingconductor._resources.aws_billing_conductor.pricing_plan import (
    AsyncPricingPlan,
)
from capo_billingconductor._resources.aws_billing_conductor.pricing_rule import (
    AsyncPricingRule,
)
from capo_billingconductor._services._aws_config import aaws_config
from capo_billingconductor._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_billingconductor.types.account_associations_list_element
    import capo_billingconductor.types.account_grouping
    import capo_billingconductor.types.account_id
    import capo_billingconductor.types.account_id_list
    import capo_billingconductor.types.arn
    import capo_billingconductor.types.associate_accounts_input
    import capo_billingconductor.types.associate_accounts_output
    import capo_billingconductor.types.associate_pricing_rules_input
    import capo_billingconductor.types.associate_pricing_rules_output
    import capo_billingconductor.types.auto_transfer_billing_group_creation_preference
    import capo_billingconductor.types.batch_associate_resources_to_custom_line_item_input
    import capo_billingconductor.types.batch_associate_resources_to_custom_line_item_output
    import capo_billingconductor.types.batch_disassociate_resources_from_custom_line_item_input
    import capo_billingconductor.types.batch_disassociate_resources_from_custom_line_item_output
    import capo_billingconductor.types.billing_entity
    import capo_billingconductor.types.billing_group_arn
    import capo_billingconductor.types.billing_group_cost_report_element
    import capo_billingconductor.types.billing_group_cost_report_result_element
    import capo_billingconductor.types.billing_group_description
    import capo_billingconductor.types.billing_group_list_element
    import capo_billingconductor.types.billing_group_name
    import capo_billingconductor.types.billing_group_status
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.billing_period_range
    import capo_billingconductor.types.client_token
    import capo_billingconductor.types.computation_preference
    import capo_billingconductor.types.computation_rule_enum
    import capo_billingconductor.types.create_billing_group_input
    import capo_billingconductor.types.create_billing_group_output
    import capo_billingconductor.types.create_custom_line_item_input
    import capo_billingconductor.types.create_custom_line_item_output
    import capo_billingconductor.types.create_pricing_plan_input
    import capo_billingconductor.types.create_pricing_plan_output
    import capo_billingconductor.types.create_pricing_rule_input
    import capo_billingconductor.types.create_pricing_rule_output
    import capo_billingconductor.types.create_tiering_input
    import capo_billingconductor.types.custom_line_item_arn
    import capo_billingconductor.types.custom_line_item_batch_associations_list
    import capo_billingconductor.types.custom_line_item_batch_disassociations_list
    import capo_billingconductor.types.custom_line_item_billing_period_range
    import capo_billingconductor.types.custom_line_item_charge_details
    import capo_billingconductor.types.custom_line_item_description
    import capo_billingconductor.types.custom_line_item_list_element
    import capo_billingconductor.types.custom_line_item_name
    import capo_billingconductor.types.custom_line_item_version_list_element
    import capo_billingconductor.types.delete_billing_group_input
    import capo_billingconductor.types.delete_billing_group_output
    import capo_billingconductor.types.delete_custom_line_item_input
    import capo_billingconductor.types.delete_custom_line_item_output
    import capo_billingconductor.types.delete_pricing_plan_input
    import capo_billingconductor.types.delete_pricing_plan_output
    import capo_billingconductor.types.delete_pricing_rule_input
    import capo_billingconductor.types.delete_pricing_rule_output
    import capo_billingconductor.types.disassociate_accounts_input
    import capo_billingconductor.types.disassociate_accounts_output
    import capo_billingconductor.types.disassociate_pricing_rules_input
    import capo_billingconductor.types.disassociate_pricing_rules_output
    import capo_billingconductor.types.get_billing_group_cost_report_input
    import capo_billingconductor.types.get_billing_group_cost_report_output
    import capo_billingconductor.types.get_billing_transfer_preference_input
    import capo_billingconductor.types.get_billing_transfer_preference_output
    import capo_billingconductor.types.group_by_attributes_list
    import capo_billingconductor.types.list_account_associations_filter
    import capo_billingconductor.types.list_account_associations_input
    import capo_billingconductor.types.list_account_associations_output
    import capo_billingconductor.types.list_billing_group_cost_reports_filter
    import capo_billingconductor.types.list_billing_group_cost_reports_input
    import capo_billingconductor.types.list_billing_group_cost_reports_output
    import capo_billingconductor.types.list_billing_groups_filter
    import capo_billingconductor.types.list_billing_groups_input
    import capo_billingconductor.types.list_billing_groups_output
    import capo_billingconductor.types.list_custom_line_item_versions_filter
    import capo_billingconductor.types.list_custom_line_item_versions_input
    import capo_billingconductor.types.list_custom_line_item_versions_output
    import capo_billingconductor.types.list_custom_line_items_filter
    import capo_billingconductor.types.list_custom_line_items_input
    import capo_billingconductor.types.list_custom_line_items_output
    import capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input
    import capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output
    import capo_billingconductor.types.list_pricing_plans_filter
    import capo_billingconductor.types.list_pricing_plans_input
    import capo_billingconductor.types.list_pricing_plans_output
    import capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_input
    import capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_output
    import capo_billingconductor.types.list_pricing_rules_filter
    import capo_billingconductor.types.list_pricing_rules_input
    import capo_billingconductor.types.list_pricing_rules_output
    import capo_billingconductor.types.list_resources_associated_to_custom_line_item_filter
    import capo_billingconductor.types.list_resources_associated_to_custom_line_item_input
    import capo_billingconductor.types.list_resources_associated_to_custom_line_item_output
    import capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_element
    import capo_billingconductor.types.list_tags_for_resource_request
    import capo_billingconductor.types.list_tags_for_resource_response
    import capo_billingconductor.types.max_billing_group_cost_report_results
    import capo_billingconductor.types.max_billing_group_results
    import capo_billingconductor.types.max_custom_line_item_results
    import capo_billingconductor.types.max_pricing_plan_results
    import capo_billingconductor.types.max_pricing_rule_results
    import capo_billingconductor.types.modifier_percentage
    import capo_billingconductor.types.operation
    import capo_billingconductor.types.presentation_object
    import capo_billingconductor.types.pricing_plan_arn
    import capo_billingconductor.types.pricing_plan_description
    import capo_billingconductor.types.pricing_plan_list_element
    import capo_billingconductor.types.pricing_plan_name
    import capo_billingconductor.types.pricing_rule_arn
    import capo_billingconductor.types.pricing_rule_arns_input
    import capo_billingconductor.types.pricing_rule_arns_non_empty_input
    import capo_billingconductor.types.pricing_rule_description
    import capo_billingconductor.types.pricing_rule_list_element
    import capo_billingconductor.types.pricing_rule_name
    import capo_billingconductor.types.pricing_rule_scope
    import capo_billingconductor.types.pricing_rule_type
    import capo_billingconductor.types.responsibility_transfer_arn
    import capo_billingconductor.types.service
    import capo_billingconductor.types.tag_key_list
    import capo_billingconductor.types.tag_map
    import capo_billingconductor.types.tag_resource_request
    import capo_billingconductor.types.tag_resource_response
    import capo_billingconductor.types.token
    import capo_billingconductor.types.untag_resource_request
    import capo_billingconductor.types.untag_resource_response
    import capo_billingconductor.types.update_billing_group_account_grouping
    import capo_billingconductor.types.update_billing_group_input
    import capo_billingconductor.types.update_billing_group_output
    import capo_billingconductor.types.update_billing_transfer_preference_input
    import capo_billingconductor.types.update_billing_transfer_preference_output
    import capo_billingconductor.types.update_custom_line_item_charge_details
    import capo_billingconductor.types.update_custom_line_item_input
    import capo_billingconductor.types.update_custom_line_item_output
    import capo_billingconductor.types.update_pricing_plan_input
    import capo_billingconductor.types.update_pricing_plan_output
    import capo_billingconductor.types.update_pricing_rule_input
    import capo_billingconductor.types.update_pricing_rule_output
    import capo_billingconductor.types.update_tiering_input
    import capo_billingconductor.types.usage_type


class AsyncbillingconductorClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncbillingconductorClient:
    """A client for the ``billingconductor`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncbillingconductorClientConfig(
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

        # resources
        self.billing_group = AsyncBillingGroup(self)
        self.custom_line_item = AsyncCustomLineItem(self)
        self.pricing_plan = AsyncPricingPlan(self)
        self.pricing_rule = AsyncPricingRule(self)

    def operation_options(
        self, config_overrides: Optional[AsyncbillingconductorClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncbillingconductorClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def get_billing_group_cost_report(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "capo_billingconductor.types.billing_period_range.BillingPeriodRange"
        ] = None,
        group_by: Optional[
            "capo_billingconductor.types.group_by_attributes_list.GroupByAttributesList"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_billing_group_cost_report_results.MaxBillingGroupCostReportResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.get_billing_group_cost_report_output.GetBillingGroupCostReportOutput":
        """<p>Retrieves the margin summary report, which includes the Amazon Web Services cost and charged amount (pro forma cost) by Amazon Web Services service for a specific billing group.</p>

        Args:
            arn: <p>The Amazon Resource Number (ARN) that uniquely identifies the billing group.</p>
            billing_period_range: <p>A time range for which the margin summary is effective. You can specify up to 12 months.</p>
            group_by: <p>A list of strings that specify the attributes that are used to break down costs in the margin summary reports for the billing group. For example, you can view your costs by the Amazon Web Services service name or the billing period.</p>
            max_results: <p>The maximum number of margin summary reports to retrieve.</p>
            next_token: <p>The pagination token used on subsequent calls to get reports.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.get_billing_group_cost_report_input.GetBillingGroupCostReportInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.get_billing_group_cost_report_output.GetBillingGroupCostReportOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.get_billing_group_cost_report

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.get_billing_group_cost_report.async_get_billing_group_cost_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.get_billing_group_cost_report_input.GetBillingGroupCostReportInput = {
            "arn": arn
        }
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range
        if group_by is not None:
            input_["group_by"] = group_by
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

    async def iter_get_billing_group_cost_report(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "capo_billingconductor.types.billing_period_range.BillingPeriodRange"
        ] = None,
        group_by: Optional[
            "capo_billingconductor.types.group_by_attributes_list.GroupByAttributesList"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_billing_group_cost_report_results.MaxBillingGroupCostReportResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.billing_group_cost_report_result_element.BillingGroupCostReportResultElement]":
        _token = next_token
        while True:
            _response = await self.get_billing_group_cost_report(
                arn,
                config_overrides=config_overrides,
                billing_period_range=billing_period_range,
                group_by=group_by,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("billing_group_cost_report_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_billing_transfer_preference(
        self,
        responsibility_transfer_arn: "capo_billingconductor.types.responsibility_transfer_arn.ResponsibilityTransferArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.get_billing_transfer_preference_output.GetBillingTransferPreferenceOutput":
        """<p>Retrieves the auto billing group creation preference for a billing transfer.</p>

        Args:
            responsibility_transfer_arn: <p>The Amazon Resource Name (ARN) of the billing transfer whose preference you want to retrieve.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.get_billing_transfer_preference_input.GetBillingTransferPreferenceInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.get_billing_transfer_preference_output.GetBillingTransferPreferenceOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.get_billing_transfer_preference

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.get_billing_transfer_preference.async_get_billing_transfer_preference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.get_billing_transfer_preference_input.GetBillingTransferPreferenceInput = {
            "responsibility_transfer_arn": responsibility_transfer_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_account_associations(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "capo_billingconductor.types.list_account_associations_filter.ListAccountAssociationsFilter"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_account_associations_output.ListAccountAssociationsOutput":
        """<p> This is a paginated call to list linked accounts that are linked to the payer account for the specified time period. If no information is provided, the current billing period is used. The response will optionally include the billing group that's associated with the linked account.</p>

        Args:
            billing_period: <p> The preferred billing period to get account associations. </p>
            filters: <p>The filter on the account ID of the linked account, or any of the following:</p> <p> <code>MONITORED</code>: linked accounts that are associated to billing groups.</p> <p> <code>UNMONITORED</code>: linked accounts that aren't associated to billing groups.</p> <p> <code>Billing Group Arn</code>: linked accounts that are associated to the provided billing group Arn. </p>
            next_token: <p> The pagination token that's used on subsequent calls to retrieve accounts. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_account_associations_input.ListAccountAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_account_associations_output.ListAccountAssociationsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_account_associations

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_account_associations.async_list_account_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_account_associations_input.ListAccountAssociationsInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_account_associations(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "capo_billingconductor.types.list_account_associations_filter.ListAccountAssociationsFilter"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.account_associations_list_element.AccountAssociationsListElement]":
        _token = next_token
        while True:
            _response = await self.list_account_associations(
                config_overrides=config_overrides,
                billing_period=billing_period,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("linked_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_billing_group_cost_reports(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_billing_group_cost_reports_filter.ListBillingGroupCostReportsFilter"
        ] = None,
    ) -> "capo_billingconductor.types.list_billing_group_cost_reports_output.ListBillingGroupCostReportsOutput":
        """<p>A paginated call to retrieve a summary report of actual Amazon Web Services charges and the calculated Amazon Web Services charges based on the associated pricing plan of a billing group.</p>

        Args:
            billing_period: <p>The preferred billing period for your report. </p>
            max_results: <p>The maximum number of reports to retrieve. </p>
            next_token: <p>The pagination token that's used on subsequent calls to get reports. </p>
            filters: <p>A <code>ListBillingGroupCostReportsFilter</code> to specify billing groups to retrieve reports from. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_billing_group_cost_reports_input.ListBillingGroupCostReportsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_billing_group_cost_reports_output.ListBillingGroupCostReportsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_billing_group_cost_reports

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_billing_group_cost_reports.async_list_billing_group_cost_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_billing_group_cost_reports_input.ListBillingGroupCostReportsInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_billing_group_cost_reports(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_billing_group_cost_reports_filter.ListBillingGroupCostReportsFilter"
        ] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.billing_group_cost_report_element.BillingGroupCostReportElement]":
        _token = next_token
        while True:
            _response = await self.list_billing_group_cost_reports(
                config_overrides=config_overrides,
                billing_period=billing_period,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("billing_group_cost_reports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_billingconductor.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> A list the tags for a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) that identifies the resource to list the tags. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_billingconductor.types.arn.Arn",
        tags: "capo_billingconductor.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.tag_resource_response.TagResourceResponse":
        """<p> Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource are not specified in the request parameters, they are not changed. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource to which to add tags. </p>
            tags: <p> The tags to add to the resource as a list of key-value pairs. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.tag_resource

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_billingconductor.types.arn.Arn",
        tag_keys: "capo_billingconductor.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.untag_resource_response.UntagResourceResponse":
        """<p> Deletes specified tags from a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource to which to delete tags. </p>
            tag_keys: <p> The tags to delete from the resource as a list of key-value pairs. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.untag_resource

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_billing_transfer_preference(
        self,
        responsibility_transfer_arn: "capo_billingconductor.types.responsibility_transfer_arn.ResponsibilityTransferArn",
        auto_billing_transfer_billing_group_creation: "capo_billingconductor.types.auto_transfer_billing_group_creation_preference.AutoTransferBillingGroupCreationPreference",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_billingconductor.types.update_billing_transfer_preference_output.UpdateBillingTransferPreferenceOutput":
        """<p>Sets the auto billing group creation preference for a billing transfer. When the preference is enabled, Billing Conductor automatically creates an indirect billing transfer billing group in your account, with the pricing plan that you specify, for each account that transfers its bill to the bill source account of this billing transfer. The preference applies only to billing groups that are created after you enable it.</p> <p>Enabling the preference requires the <code>iam:CreateServiceLinkedRole</code> permission. While a pricing plan is specified in an enabled preference, you can't delete that pricing plan.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            responsibility_transfer_arn: <p>The Amazon Resource Name (ARN) of the billing transfer whose preference you want to set.</p>
            auto_billing_transfer_billing_group_creation: <p>The auto billing group creation preference to set for the billing transfer.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.update_billing_transfer_preference_input.UpdateBillingTransferPreferenceInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.update_billing_transfer_preference_output.UpdateBillingTransferPreferenceOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_billing_transfer_preference

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.update_billing_transfer_preference.async_update_billing_transfer_preference(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.update_billing_transfer_preference_input.UpdateBillingTransferPreferenceInput = {
            "responsibility_transfer_arn": responsibility_transfer_arn,
            "auto_billing_transfer_billing_group_creation": auto_billing_transfer_billing_group_creation,
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

    async def create_billing_group(
        self,
        name: "capo_billingconductor.types.billing_group_name.BillingGroupName",
        account_grouping: "capo_billingconductor.types.account_grouping.AccountGrouping",
        computation_preference: "capo_billingconductor.types.computation_preference.ComputationPreference",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        primary_account_id: Optional[
            "capo_billingconductor.types.account_id.AccountId"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
    ) -> "capo_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput":
        """<p> Creates a billing group that resembles a consolidated billing family that Amazon Web Services charges, based off of the predefined pricing plan computation. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The billing group name. The names must be unique. </p>
            account_grouping: <p> The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            primary_account_id: <p> The account ID that serves as the main account in a billing group. </p>
            description: <p>The description of the billing group. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a billing group. This feature isn't available during the beta. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.create_billing_group_input.CreateBillingGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.create_billing_group_output.CreateBillingGroupOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_billing_group

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.create_billing_group.async_create_billing_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.create_billing_group_input.CreateBillingGroupInput = {
            "name": name,
            "account_grouping": account_grouping,
            "computation_preference": computation_preference,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if primary_account_id is not None:
            input_["primary_account_id"] = primary_account_id
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_billing_group(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.billing_group_name.BillingGroupName"
        ] = None,
        status: Optional[
            "capo_billingconductor.types.billing_group_status.BillingGroupStatus"
        ] = None,
        computation_preference: Optional[
            "capo_billingconductor.types.computation_preference.ComputationPreference"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.billing_group_description.BillingGroupDescription"
        ] = None,
        account_grouping: Optional[
            "capo_billingconductor.types.update_billing_group_account_grouping.UpdateBillingGroupAccountGrouping"
        ] = None,
    ) -> "capo_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput":
        """<p>This updates an existing billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group being updated. </p>
            name: <p>The name of the billing group. The names must be unique to each billing group. </p>
            status: <p>The status of the billing group. Only one of the valid values can be used. </p>
            computation_preference: <p> The preferences and settings that will be used to compute the Amazon Web Services charges for a billing group. </p>
            description: <p>A description of the billing group. </p>
            account_grouping: <p>Specifies if the billing group has automatic account association (<code>AutoAssociate</code>) enabled.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.update_billing_group_output.UpdateBillingGroupOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_billing_group

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.update_billing_group.async_update_billing_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.update_billing_group_input.UpdateBillingGroupInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if computation_preference is not None:
            input_["computation_preference"] = computation_preference
        if description is not None:
            input_["description"] = description
        if account_grouping is not None:
            input_["account_grouping"] = account_grouping

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_billing_group(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput":
        """<p> Deletes a billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that you're deleting.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.delete_billing_group_output.DeleteBillingGroupOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_billing_group

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.delete_billing_group.async_delete_billing_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.delete_billing_group_input.DeleteBillingGroupInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_billing_groups(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_billing_groups_filter.ListBillingGroupsFilter"
        ] = None,
    ) -> (
        "capo_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput"
    ):
        """<p>A paginated call to retrieve a list of billing groups for the given billing period. If you don't provide a billing group, the current billing period is used.</p>

        Args:
            billing_period: <p>The preferred billing period to get billing groups. </p>
            max_results: <p>The maximum number of billing groups to retrieve. </p>
            next_token: <p>The pagination token that's used on subsequent calls to get billing groups. </p>
            filters: <p>A <code>ListBillingGroupsFilter</code> that specifies the billing group and pricing plan to retrieve billing group information. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_billing_groups_output.ListBillingGroupsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_billing_groups

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_billing_groups.async_list_billing_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_billing_groups_input.ListBillingGroupsInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_billing_groups(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_billing_group_results.MaxBillingGroupResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_billing_groups_filter.ListBillingGroupsFilter"
        ] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.billing_group_list_element.BillingGroupListElement]":
        _token = next_token
        while True:
            _response = await self.list_billing_groups(
                config_overrides=config_overrides,
                billing_period=billing_period,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("billing_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_accounts(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "capo_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> (
        "capo_billingconductor.types.associate_accounts_output.AssociateAccountsOutput"
    ):
        """<p>Connects an array of account IDs in a consolidated billing family to a predefined billing group. The account IDs must be a part of the consolidated billing family during the current month, and not already associated with another billing group. The maximum number of accounts that can be associated in one call is 30. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the billing group that associates the array of account IDs. </p>
            account_ids: <p> The associating array of account IDs. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.associate_accounts_input.AssociateAccountsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.associate_accounts_output.AssociateAccountsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.associate_accounts

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.associate_accounts.async_associate_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.associate_accounts_input.AssociateAccountsInput = {
            "arn": arn,
            "account_ids": account_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_accounts(
        self,
        arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        account_ids: "capo_billingconductor.types.account_id_list.AccountIdList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput":
        """<p>Removes the specified list of account IDs from the given billing group. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the billing group that the array of account IDs will disassociate from. </p>
            account_ids: <p>The array of account IDs to disassociate. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.disassociate_accounts_output.DisassociateAccountsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.disassociate_accounts

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.disassociate_accounts.async_disassociate_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.disassociate_accounts_input.DisassociateAccountsInput = {
            "arn": arn,
            "account_ids": account_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_line_item(
        self,
        name: "capo_billingconductor.types.custom_line_item_name.CustomLineItemName",
        description: "capo_billingconductor.types.custom_line_item_description.CustomLineItemDescription",
        billing_group_arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn",
        charge_details: "capo_billingconductor.types.custom_line_item_charge_details.CustomLineItemChargeDetails",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        billing_period_range: Optional[
            "capo_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
        account_id: Optional["capo_billingconductor.types.account_id.AccountId"] = None,
        computation_rule: Optional[
            "capo_billingconductor.types.computation_rule_enum.ComputationRuleEnum"
        ] = None,
        presentation_details: Optional[
            "capo_billingconductor.types.presentation_object.PresentationObject"
        ] = None,
    ) -> "capo_billingconductor.types.create_custom_line_item_output.CreateCustomLineItemOutput":
        """<p>Creates a custom line item that can be used to create a one-time fixed charge that can be applied to a single billing group for the current or previous billing period. The one-time fixed charge is either a fee or discount. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The name of the custom line item. </p>
            description: <p> The description of the custom line item. This is shown on the Bills page in association with the charge value. </p>
            billing_group_arn: <p> The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to. </p>
            billing_period_range: <p> A time range for which the custom line item is effective. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a custom line item. </p>
            charge_details: <p> A <code>CustomLineItemChargeDetails</code> that describes the charge details for a custom line item. </p>
            account_id: <p>The Amazon Web Services account in which this custom line item will be applied to.</p>
            computation_rule: <p> Specifies how the custom line item charges are computed. </p>
            presentation_details: <p> Details controlling how the custom line item charges are presented in the bill. Contains specifications for which service the charges will be shown under. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.create_custom_line_item_input.CreateCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.create_custom_line_item_output.CreateCustomLineItemOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_custom_line_item

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.create_custom_line_item.async_create_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.create_custom_line_item_input.CreateCustomLineItemInput = {
            "name": name,
            "description": description,
            "billing_group_arn": billing_group_arn,
            "charge_details": charge_details,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id
        if computation_rule is not None:
            input_["computation_rule"] = computation_rule
        if presentation_details is not None:
            input_["presentation_details"] = presentation_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_custom_line_item(
        self,
        arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.custom_line_item_name.CustomLineItemName"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
        ] = None,
        charge_details: Optional[
            "capo_billingconductor.types.update_custom_line_item_charge_details.UpdateCustomLineItemChargeDetails"
        ] = None,
        billing_period_range: Optional[
            "capo_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "capo_billingconductor.types.update_custom_line_item_output.UpdateCustomLineItemOutput":
        """<p> Update an existing custom line item in the current or previous billing period. </p>

        Args:
            arn: <p> The ARN of the custom line item to be updated. </p>
            name: <p> The new name for the custom line item. </p>
            description: <p> The new line item description of the custom line item. </p>
            charge_details: <p> A <code>ListCustomLineItemChargeDetails</code> containing the new charge details for the custom line item. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.update_custom_line_item_input.UpdateCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.update_custom_line_item_output.UpdateCustomLineItemOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_custom_line_item

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.update_custom_line_item.async_update_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.update_custom_line_item_input.UpdateCustomLineItemInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if charge_details is not None:
            input_["charge_details"] = charge_details
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_line_item(
        self,
        arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "capo_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "capo_billingconductor.types.delete_custom_line_item_output.DeleteCustomLineItemOutput":
        """<p> Deletes the custom line item identified by the given ARN in the current, or previous billing period. </p>

        Args:
            arn: <p> The ARN of the custom line item to be deleted. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.delete_custom_line_item_input.DeleteCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.delete_custom_line_item_output.DeleteCustomLineItemOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_custom_line_item

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.delete_custom_line_item.async_delete_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.delete_custom_line_item_input.DeleteCustomLineItemInput = {
            "arn": arn
        }
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_custom_line_items(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_custom_line_items_filter.ListCustomLineItemsFilter"
        ] = None,
    ) -> "capo_billingconductor.types.list_custom_line_items_output.ListCustomLineItemsOutput":
        """<p> A paginated call to get a list of all custom line items (FFLIs) for the given billing period. If you don't provide a billing period, the current billing period is used. </p>

        Args:
            billing_period: <p> The preferred billing period to get custom line items (FFLIs). </p>
            max_results: <p> The maximum number of billing groups to retrieve. </p>
            next_token: <p> The pagination token that's used on subsequent calls to get custom line items (FFLIs). </p>
            filters: <p>A <code>ListCustomLineItemsFilter</code> that specifies the custom line item names and/or billing group Amazon Resource Names (ARNs) to retrieve FFLI information.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_custom_line_items_input.ListCustomLineItemsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_custom_line_items_output.ListCustomLineItemsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_custom_line_items

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_custom_line_items.async_list_custom_line_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_custom_line_items_input.ListCustomLineItemsInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_custom_line_items(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_custom_line_items_filter.ListCustomLineItemsFilter"
        ] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.custom_line_item_list_element.CustomLineItemListElement]":
        _token = next_token
        while True:
            _response = await self.list_custom_line_items(
                config_overrides=config_overrides,
                billing_period=billing_period,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("custom_line_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_associate_resources_to_custom_line_item(
        self,
        target_arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        resource_arns: "capo_billingconductor.types.custom_line_item_batch_associations_list.CustomLineItemBatchAssociationsList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "capo_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "capo_billingconductor.types.batch_associate_resources_to_custom_line_item_output.BatchAssociateResourcesToCustomLineItemOutput":
        """<p> Associates a batch of resources to a percentage custom line item. </p>

        Args:
            target_arn: <p> A percentage custom line item ARN to associate the resources to. </p>
            resource_arns: <p> A list containing the ARNs of the resources to be associated. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.batch_associate_resources_to_custom_line_item_input.BatchAssociateResourcesToCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.batch_associate_resources_to_custom_line_item_output.BatchAssociateResourcesToCustomLineItemOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.batch_associate_resources_to_custom_line_item

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.batch_associate_resources_to_custom_line_item.async_batch_associate_resources_to_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.batch_associate_resources_to_custom_line_item_input.BatchAssociateResourcesToCustomLineItemInput = {
            "target_arn": target_arn,
            "resource_arns": resource_arns,
        }
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_disassociate_resources_from_custom_line_item(
        self,
        target_arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        resource_arns: "capo_billingconductor.types.custom_line_item_batch_disassociations_list.CustomLineItemBatchDisassociationsList",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period_range: Optional[
            "capo_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
        ] = None,
    ) -> "capo_billingconductor.types.batch_disassociate_resources_from_custom_line_item_output.BatchDisassociateResourcesFromCustomLineItemOutput":
        """<p> Disassociates a batch of resources from a percentage custom line item. </p>

        Args:
            target_arn: <p> A percentage custom line item ARN to disassociate the resources from. </p>
            resource_arns: <p> A list containing the ARNs of resources to be disassociated. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.batch_disassociate_resources_from_custom_line_item_input.BatchDisassociateResourcesFromCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.batch_disassociate_resources_from_custom_line_item_output.BatchDisassociateResourcesFromCustomLineItemOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.batch_disassociate_resources_from_custom_line_item

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.batch_disassociate_resources_from_custom_line_item.async_batch_disassociate_resources_from_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.batch_disassociate_resources_from_custom_line_item_input.BatchDisassociateResourcesFromCustomLineItemInput = {
            "target_arn": target_arn,
            "resource_arns": resource_arns,
        }
        if billing_period_range is not None:
            input_["billing_period_range"] = billing_period_range

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_custom_line_item_versions(
        self,
        arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_custom_line_item_versions_filter.ListCustomLineItemVersionsFilter"
        ] = None,
    ) -> "capo_billingconductor.types.list_custom_line_item_versions_output.ListCustomLineItemVersionsOutput":
        """<p>A paginated call to get a list of all custom line item versions.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for the custom line item.</p>
            max_results: <p>The maximum number of custom line item versions to retrieve.</p>
            next_token: <p>The pagination token that's used on subsequent calls to retrieve custom line item versions.</p>
            filters: <p>A <code>ListCustomLineItemVersionsFilter</code> that specifies the billing period range in which the custom line item versions are applied.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_custom_line_item_versions_input.ListCustomLineItemVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_custom_line_item_versions_output.ListCustomLineItemVersionsOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_custom_line_item_versions

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_custom_line_item_versions.async_list_custom_line_item_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_custom_line_item_versions_input.ListCustomLineItemVersionsInput = {
            "arn": arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_custom_line_item_versions(
        self,
        arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_custom_line_item_versions_filter.ListCustomLineItemVersionsFilter"
        ] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.custom_line_item_version_list_element.CustomLineItemVersionListElement]":
        _token = next_token
        while True:
            _response = await self.list_custom_line_item_versions(
                arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("custom_line_item_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resources_associated_to_custom_line_item(
        self,
        arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_resources_associated_to_custom_line_item_filter.ListResourcesAssociatedToCustomLineItemFilter"
        ] = None,
    ) -> "capo_billingconductor.types.list_resources_associated_to_custom_line_item_output.ListResourcesAssociatedToCustomLineItemOutput":
        """<p> List the resources that are associated to a custom line item. </p>

        Args:
            billing_period: <p> The billing period for which the resource associations will be listed. </p>
            arn: <p> The ARN of the custom line item for which the resource associations will be listed. </p>
            max_results: <p> (Optional) The maximum number of resource associations to be retrieved. </p>
            next_token: <p> (Optional) The pagination token that's returned by a previous request. </p>
            filters: <p> (Optional) A <code>ListResourcesAssociatedToCustomLineItemFilter</code> that can specify the types of resources that should be retrieved. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_resources_associated_to_custom_line_item_input.ListResourcesAssociatedToCustomLineItemInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_resources_associated_to_custom_line_item_output.ListResourcesAssociatedToCustomLineItemOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_resources_associated_to_custom_line_item

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_resources_associated_to_custom_line_item.async_list_resources_associated_to_custom_line_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_resources_associated_to_custom_line_item_input.ListResourcesAssociatedToCustomLineItemInput = {
            "arn": arn
        }
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resources_associated_to_custom_line_item(
        self,
        arn: "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_custom_line_item_results.MaxCustomLineItemResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
        filters: Optional[
            "capo_billingconductor.types.list_resources_associated_to_custom_line_item_filter.ListResourcesAssociatedToCustomLineItemFilter"
        ] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_element.ListResourcesAssociatedToCustomLineItemResponseElement]":
        _token = next_token
        while True:
            _response = await self.list_resources_associated_to_custom_line_item(
                arn,
                config_overrides=config_overrides,
                billing_period=billing_period,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("associated_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_pricing_plan(
        self,
        name: "capo_billingconductor.types.pricing_plan_name.PricingPlanName",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
        pricing_rule_arns: Optional[
            "capo_billingconductor.types.pricing_rule_arns_input.PricingRuleArnsInput"
        ] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
    ) -> (
        "capo_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput"
    ):
        """<p>Creates a pricing plan that is used for computing Amazon Web Services charges for billing groups. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p>The name of the pricing plan. The names must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>
            pricing_rule_arns: <p> A list of Amazon Resource Names (ARNs) that define the pricing plan parameters. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a pricing plan. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.create_pricing_plan_output.CreatePricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_pricing_plan

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.create_pricing_plan.async_create_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.create_pricing_plan_input.CreatePricingPlanInput = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if pricing_rule_arns is not None:
            input_["pricing_rule_arns"] = pricing_rule_arns
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_pricing_plan(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.pricing_plan_name.PricingPlanName"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_plan_description.PricingPlanDescription"
        ] = None,
    ) -> (
        "capo_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput"
    ):
        """<p>This updates an existing pricing plan. </p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're updating. </p>
            name: <p>The name of the pricing plan. The name must be unique to each pricing plan. </p>
            description: <p>The description of the pricing plan. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.update_pricing_plan_output.UpdatePricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_pricing_plan

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.update_pricing_plan.async_update_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.update_pricing_plan_input.UpdatePricingPlanInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_pricing_plan(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> (
        "capo_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput"
    ):
        """<p>Deletes a pricing plan. The pricing plan must not be associated with any billing groups to delete successfully.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the pricing plan that you're deleting. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.delete_pricing_plan_output.DeletePricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_pricing_plan

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.delete_pricing_plan.async_delete_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.delete_pricing_plan_input.DeletePricingPlanInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_pricing_plans(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "capo_billingconductor.types.list_pricing_plans_filter.ListPricingPlansFilter"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput":
        """<p>A paginated call to get pricing plans for the given billing period. If you don't provide a billing period, the current billing period is used. </p>

        Args:
            billing_period: <p>The preferred billing period to get pricing plan. </p>
            filters: <p>A <code>ListPricingPlansFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing plans to retrieve pricing plans information.</p>
            max_results: <p>The maximum number of pricing plans to retrieve.</p>
            next_token: <p>The pagination token that's used on subsequent call to get pricing plans. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_pricing_plans_output.ListPricingPlansOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans.async_list_pricing_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_pricing_plans_input.ListPricingPlansInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_pricing_plans(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "capo_billingconductor.types.list_pricing_plans_filter.ListPricingPlansFilter"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.pricing_plan_list_element.PricingPlanListElement]":
        _token = next_token
        while True:
            _response = await self.list_pricing_plans(
                config_overrides=config_overrides,
                billing_period=billing_period,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pricing_plans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_pricing_rules(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "capo_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput":
        """<p>Connects an array of <code>PricingRuleArns</code> to a defined <code>PricingPlan</code>. The maximum number <code>PricingRuleArn</code> that can be associated in one call is 30. </p>

        Args:
            arn: <p> The <code>PricingPlanArn</code> that the <code>PricingRuleArns</code> are associated with. </p>
            pricing_rule_arns: <p> The <code>PricingRuleArns</code> that are associated with the Pricing Plan. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.associate_pricing_rules_output.AssociatePricingRulesOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.associate_pricing_rules

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.associate_pricing_rules.async_associate_pricing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.associate_pricing_rules_input.AssociatePricingRulesInput = {
            "arn": arn,
            "pricing_rule_arns": pricing_rule_arns,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_pricing_rules(
        self,
        arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        pricing_rule_arns: "capo_billingconductor.types.pricing_rule_arns_non_empty_input.PricingRuleArnsNonEmptyInput",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> "capo_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput":
        """<p> Disassociates a list of pricing rules from a pricing plan. </p>

        Args:
            arn: <p> The pricing plan Amazon Resource Name (ARN) to disassociate pricing rules from. </p>
            pricing_rule_arns: <p> A list containing the Amazon Resource Name (ARN) of the pricing rules that will be disassociated. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.disassociate_pricing_rules_output.DisassociatePricingRulesOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.disassociate_pricing_rules.async_disassociate_pricing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.disassociate_pricing_rules_input.DisassociatePricingRulesInput = {
            "arn": arn,
            "pricing_rule_arns": pricing_rule_arns,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_pricing_plans_associated_with_pricing_rule(
        self,
        pricing_rule_arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput":
        """<p> A list of the pricing plans that are associated with a pricing rule. </p>

        Args:
            billing_period: <p> The pricing plan billing period for which associations will be listed. </p>
            pricing_rule_arn: <p> The pricing rule Amazon Resource Name (ARN) for which associations will be listed. </p>
            max_results: <p> The optional maximum number of pricing rule associations to retrieve. </p>
            next_token: <p> The optional pagination token returned by a previous call. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_output.ListPricingPlansAssociatedWithPricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_pricing_plans_associated_with_pricing_rule.async_list_pricing_plans_associated_with_pricing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_pricing_plans_associated_with_pricing_rule_input.ListPricingPlansAssociatedWithPricingRuleInput = {
            "pricing_rule_arn": pricing_rule_arn
        }
        if billing_period is not None:
            input_["billing_period"] = billing_period
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

    async def iter_list_pricing_plans_associated_with_pricing_rule(
        self,
        pricing_rule_arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.pricing_plan_arn.PricingPlanArn]":
        _token = next_token
        while True:
            _response = await self.list_pricing_plans_associated_with_pricing_rule(
                pricing_rule_arn,
                config_overrides=config_overrides,
                billing_period=billing_period,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pricing_plan_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_pricing_rule(
        self,
        name: "capo_billingconductor.types.pricing_rule_name.PricingRuleName",
        scope: "capo_billingconductor.types.pricing_rule_scope.PricingRuleScope",
        type: "capo_billingconductor.types.pricing_rule_type.PricingRuleType",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        client_token: Optional[
            "capo_billingconductor.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
        ] = None,
        modifier_percentage: Optional[
            "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
        ] = None,
        service: Optional["capo_billingconductor.types.service.Service"] = None,
        tags: Optional["capo_billingconductor.types.tag_map.TagMap"] = None,
        billing_entity: Optional[
            "capo_billingconductor.types.billing_entity.BillingEntity"
        ] = None,
        tiering: Optional[
            "capo_billingconductor.types.create_tiering_input.CreateTieringInput"
        ] = None,
        usage_type: Optional["capo_billingconductor.types.usage_type.UsageType"] = None,
        operation: Optional["capo_billingconductor.types.operation.Operation"] = None,
    ) -> (
        "capo_billingconductor.types.create_pricing_rule_output.CreatePricingRuleOutput"
    ):
        """<p> Creates a pricing rule can be associated to a pricing plan, or a set of pricing plans. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. With an idempotent request, if the original request completes successfully, any subsequent retries complete successfully without performing any further actions.</p>
            name: <p> The pricing rule name. The names must be unique to each pricing rule. </p>
            description: <p> The pricing rule description. </p>
            scope: <p> The scope of pricing rule that indicates if it's globally applicable, or it's service-specific. </p>
            type: <p> The type of pricing rule. </p>
            modifier_percentage: <p>A percentage modifier that's applied on the public pricing rates. Your entry will be rounded to the nearest 2 decimal places.</p>
            service: <p> If the <code>Scope</code> attribute is set to <code>SERVICE</code> or <code>SKU</code>, the attribute indicates which service the <code>PricingRule</code> is applicable for. </p>
            tags: <p> A map that contains tag keys and tag values that are attached to a pricing rule. </p>
            billing_entity: <p> The seller of services provided by Amazon Web Services, their affiliates, or third-party providers selling services via Amazon Web Services Marketplace. </p>
            tiering: <p> The set of tiering configurations for the pricing rule. </p>
            usage_type: <p> Usage type is the unit that each service uses to measure the usage of a specific type of resource.</p> <p>If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which usage type the <code>PricingRule</code> is modifying. For example, <code>USW2-BoxUsage:m2.2xlarge</code> describes an<code> M2 High Memory Double Extra Large</code> instance in the US West (Oregon) Region. </p>
            operation: <p> Operation is the specific Amazon Web Services action covered by this line item. This describes the specific usage of the line item.</p> <p> If the <code>Scope</code> attribute is set to <code>SKU</code>, this attribute indicates which operation the <code>PricingRule</code> is modifying. For example, a value of <code>RunInstances:0202</code> indicates the operation of running an Amazon EC2 instance.</p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.service_limit_exceeded_exception.ServiceLimitExceededException: <p>The request would cause a service limit to exceed. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.create_pricing_rule_input.CreatePricingRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.create_pricing_rule_output.CreatePricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.create_pricing_rule

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.create_pricing_rule.async_create_pricing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.create_pricing_rule_input.CreatePricingRuleInput = {
            "name": name,
            "scope": scope,
            "type": type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if modifier_percentage is not None:
            input_["modifier_percentage"] = modifier_percentage
        if service is not None:
            input_["service"] = service
        if tags is not None:
            input_["tags"] = tags
        if billing_entity is not None:
            input_["billing_entity"] = billing_entity
        if tiering is not None:
            input_["tiering"] = tiering
        if usage_type is not None:
            input_["usage_type"] = usage_type
        if operation is not None:
            input_["operation"] = operation

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_pricing_rule(
        self,
        arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        name: Optional[
            "capo_billingconductor.types.pricing_rule_name.PricingRuleName"
        ] = None,
        description: Optional[
            "capo_billingconductor.types.pricing_rule_description.PricingRuleDescription"
        ] = None,
        type: Optional[
            "capo_billingconductor.types.pricing_rule_type.PricingRuleType"
        ] = None,
        modifier_percentage: Optional[
            "capo_billingconductor.types.modifier_percentage.ModifierPercentage"
        ] = None,
        tiering: Optional[
            "capo_billingconductor.types.update_tiering_input.UpdateTieringInput"
        ] = None,
    ) -> (
        "capo_billingconductor.types.update_pricing_rule_output.UpdatePricingRuleOutput"
    ):
        """<p> Updates an existing pricing rule. </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the pricing rule to update. </p>
            name: <p> The new name of the pricing rule. The name must be unique to each pricing rule. </p>
            description: <p> The new description for the pricing rule. </p>
            type: <p> The new pricing rule type. </p>
            modifier_percentage: <p> The new modifier to show pricing plan rates as a percentage. Your entry will be rounded to the nearest 2 decimal places. </p>
            tiering: <p> The set of tiering configurations for the pricing rule. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.update_pricing_rule_input.UpdatePricingRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.update_pricing_rule_output.UpdatePricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.update_pricing_rule

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.update_pricing_rule.async_update_pricing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.update_pricing_rule_input.UpdatePricingRuleInput = {
            "arn": arn
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if modifier_percentage is not None:
            input_["modifier_percentage"] = modifier_percentage
        if tiering is not None:
            input_["tiering"] = tiering

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_pricing_rule(
        self,
        arn: "capo_billingconductor.types.pricing_rule_arn.PricingRuleArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
    ) -> (
        "capo_billingconductor.types.delete_pricing_rule_output.DeletePricingRuleOutput"
    ):
        """<p> Deletes the pricing rule that's identified by the input Amazon Resource Name (ARN). </p>

        Args:
            arn: <p> The Amazon Resource Name (ARN) of the pricing rule that you are deleting. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.conflict_exception.ConflictException: <p>You can cause an inconsistent state by updating or deleting a resource. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.delete_pricing_rule_input.DeletePricingRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.delete_pricing_rule_output.DeletePricingRuleOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.delete_pricing_rule

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.delete_pricing_rule.async_delete_pricing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.delete_pricing_rule_input.DeletePricingRuleInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_pricing_rules(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "capo_billingconductor.types.list_pricing_rules_filter.ListPricingRulesFilter"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_rules_output.ListPricingRulesOutput":
        """<p> Describes a pricing rule that can be associated to a pricing plan, or set of pricing plans. </p>

        Args:
            billing_period: <p> The preferred billing period to get the pricing plan. </p>
            filters: <p> A <code>DescribePricingRuleFilter</code> that specifies the Amazon Resource Name (ARNs) of pricing rules to retrieve pricing rules information. </p>
            max_results: <p> The maximum number of pricing rules to retrieve. </p>
            next_token: <p> The pagination token that's used on subsequent call to get pricing rules. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_pricing_rules_input.ListPricingRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_pricing_rules_output.ListPricingRulesOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules.async_list_pricing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_pricing_rules_input.ListPricingRulesInput = {}
        if billing_period is not None:
            input_["billing_period"] = billing_period
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_pricing_rules(
        self,
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        filters: Optional[
            "capo_billingconductor.types.list_pricing_rules_filter.ListPricingRulesFilter"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_rule_results.MaxPricingRuleResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.pricing_rule_list_element.PricingRuleListElement]":
        _token = next_token
        while True:
            _response = await self.list_pricing_rules(
                config_overrides=config_overrides,
                billing_period=billing_period,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pricing_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pricing_rules_associated_to_pricing_plan(
        self,
        pricing_plan_arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_output.ListPricingRulesAssociatedToPricingPlanOutput":
        """<p> Lists the pricing rules that are associated with a pricing plan. </p>

        Args:
            billing_period: <p> The billing period for which the pricing rule associations are to be listed. </p>
            pricing_plan_arn: <p> The Amazon Resource Name (ARN) of the pricing plan for which associations are to be listed.</p>
            max_results: <p>The optional maximum number of pricing rule associations to retrieve.</p>
            next_token: <p> The optional pagination token returned by a previous call. </p>

        Raises:
            capo_billingconductor.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. </p>
            capo_billingconductor.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request. </p>
            capo_billingconductor.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist. </p>
            capo_billingconductor.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. </p>
            capo_billingconductor.errors.validation_exception.ValidationException: <p>The input doesn't match with the constraints specified by Amazon Web Services services.</p>
            capo_billingconductor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_input.ListPricingRulesAssociatedToPricingPlanInput]",
        ) -> AsyncOperationResponse[
            "capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_output.ListPricingRulesAssociatedToPricingPlanOutput"
        ]:
            import capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules_associated_to_pricing_plan

            (
                output,
                http_response,
            ) = await capo_billingconductor._operations.aws_billing_conductor.list_pricing_rules_associated_to_pricing_plan.async_list_pricing_rules_associated_to_pricing_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_billingconductor.types.list_pricing_rules_associated_to_pricing_plan_input.ListPricingRulesAssociatedToPricingPlanInput = {
            "pricing_plan_arn": pricing_plan_arn
        }
        if billing_period is not None:
            input_["billing_period"] = billing_period
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

    async def iter_list_pricing_rules_associated_to_pricing_plan(
        self,
        pricing_plan_arn: "capo_billingconductor.types.pricing_plan_arn.PricingPlanArn",
        *,
        config_overrides: Optional[AsyncbillingconductorClientConfig] = None,
        billing_period: Optional[
            "capo_billingconductor.types.billing_period.BillingPeriod"
        ] = None,
        max_results: Optional[
            "capo_billingconductor.types.max_pricing_plan_results.MaxPricingPlanResults"
        ] = None,
        next_token: Optional["capo_billingconductor.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_billingconductor.types.pricing_rule_arn.PricingRuleArn]":
        _token = next_token
        while True:
            _response = await self.list_pricing_rules_associated_to_pricing_plan(
                pricing_plan_arn,
                config_overrides=config_overrides,
                billing_period=billing_period,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("pricing_rule_arns",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
