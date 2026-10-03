"""Generated from Smithy shape ``com.amazonaws.costexplorer#AWSInsightsIndexService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cost_explorer._auth._signers
import capo_cost_explorer._auth._sigv4
from capo_cost_explorer._auth._identity import Credentials
from capo_cost_explorer._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cost_explorer._auth._zapros_handler import AuthMiddleware
from capo_cost_explorer._pagination import resolve_path as _resolve_path
from capo_cost_explorer._services._aws_config import aws_config
from capo_cost_explorer._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_cost_explorer.types.account_scope
    import capo_cost_explorer.types.analyses_page_size
    import capo_cost_explorer.types.analysis_id
    import capo_cost_explorer.types.analysis_ids
    import capo_cost_explorer.types.analysis_status
    import capo_cost_explorer.types.analysis_summary
    import capo_cost_explorer.types.anomaly
    import capo_cost_explorer.types.anomaly_date_interval
    import capo_cost_explorer.types.anomaly_feedback_type
    import capo_cost_explorer.types.anomaly_monitor
    import capo_cost_explorer.types.anomaly_subscription
    import capo_cost_explorer.types.anomaly_subscription_frequency
    import capo_cost_explorer.types.approximation_dimension
    import capo_cost_explorer.types.arn
    import capo_cost_explorer.types.billing_view_arn
    import capo_cost_explorer.types.commitment_purchase_analysis_configuration
    import capo_cost_explorer.types.context
    import capo_cost_explorer.types.cost_allocation_tag
    import capo_cost_explorer.types.cost_allocation_tag_backfill_request
    import capo_cost_explorer.types.cost_allocation_tag_key_list
    import capo_cost_explorer.types.cost_allocation_tag_status
    import capo_cost_explorer.types.cost_allocation_tag_status_list
    import capo_cost_explorer.types.cost_allocation_tag_type
    import capo_cost_explorer.types.cost_allocation_tags_max_results
    import capo_cost_explorer.types.cost_and_usage_comparison
    import capo_cost_explorer.types.cost_and_usage_comparisons_max_results
    import capo_cost_explorer.types.cost_category_max_results
    import capo_cost_explorer.types.cost_category_name
    import capo_cost_explorer.types.cost_category_reference
    import capo_cost_explorer.types.cost_category_resource_association
    import capo_cost_explorer.types.cost_category_rule_version
    import capo_cost_explorer.types.cost_category_rules_list
    import capo_cost_explorer.types.cost_category_split_charge_rules_list
    import capo_cost_explorer.types.cost_category_value
    import capo_cost_explorer.types.cost_comparison_driver
    import capo_cost_explorer.types.cost_comparison_drivers_max_results
    import capo_cost_explorer.types.create_anomaly_monitor_request
    import capo_cost_explorer.types.create_anomaly_monitor_response
    import capo_cost_explorer.types.create_anomaly_subscription_request
    import capo_cost_explorer.types.create_anomaly_subscription_response
    import capo_cost_explorer.types.create_cost_category_definition_request
    import capo_cost_explorer.types.create_cost_category_definition_response
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.delete_anomaly_monitor_request
    import capo_cost_explorer.types.delete_anomaly_monitor_response
    import capo_cost_explorer.types.delete_anomaly_subscription_request
    import capo_cost_explorer.types.delete_anomaly_subscription_response
    import capo_cost_explorer.types.delete_cost_category_definition_request
    import capo_cost_explorer.types.delete_cost_category_definition_response
    import capo_cost_explorer.types.describe_cost_category_definition_request
    import capo_cost_explorer.types.describe_cost_category_definition_response
    import capo_cost_explorer.types.dimension
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.generation_status
    import capo_cost_explorer.types.generation_summary
    import capo_cost_explorer.types.generic_string
    import capo_cost_explorer.types.get_anomalies_request
    import capo_cost_explorer.types.get_anomalies_response
    import capo_cost_explorer.types.get_anomaly_monitors_request
    import capo_cost_explorer.types.get_anomaly_monitors_response
    import capo_cost_explorer.types.get_anomaly_subscriptions_request
    import capo_cost_explorer.types.get_anomaly_subscriptions_response
    import capo_cost_explorer.types.get_approximate_usage_records_request
    import capo_cost_explorer.types.get_approximate_usage_records_response
    import capo_cost_explorer.types.get_commitment_purchase_analysis_request
    import capo_cost_explorer.types.get_commitment_purchase_analysis_response
    import capo_cost_explorer.types.get_cost_and_usage_comparisons_request
    import capo_cost_explorer.types.get_cost_and_usage_comparisons_response
    import capo_cost_explorer.types.get_cost_and_usage_request
    import capo_cost_explorer.types.get_cost_and_usage_response
    import capo_cost_explorer.types.get_cost_and_usage_with_resources_request
    import capo_cost_explorer.types.get_cost_and_usage_with_resources_response
    import capo_cost_explorer.types.get_cost_categories_request
    import capo_cost_explorer.types.get_cost_categories_response
    import capo_cost_explorer.types.get_cost_comparison_drivers_request
    import capo_cost_explorer.types.get_cost_comparison_drivers_response
    import capo_cost_explorer.types.get_cost_forecast_request
    import capo_cost_explorer.types.get_cost_forecast_response
    import capo_cost_explorer.types.get_dimension_values_request
    import capo_cost_explorer.types.get_dimension_values_response
    import capo_cost_explorer.types.get_reservation_coverage_request
    import capo_cost_explorer.types.get_reservation_coverage_response
    import capo_cost_explorer.types.get_reservation_purchase_recommendation_request
    import capo_cost_explorer.types.get_reservation_purchase_recommendation_response
    import capo_cost_explorer.types.get_reservation_utilization_request
    import capo_cost_explorer.types.get_reservation_utilization_response
    import capo_cost_explorer.types.get_rightsizing_recommendation_request
    import capo_cost_explorer.types.get_rightsizing_recommendation_response
    import capo_cost_explorer.types.get_savings_plan_purchase_recommendation_details_request
    import capo_cost_explorer.types.get_savings_plan_purchase_recommendation_details_response
    import capo_cost_explorer.types.get_savings_plans_coverage_request
    import capo_cost_explorer.types.get_savings_plans_coverage_response
    import capo_cost_explorer.types.get_savings_plans_purchase_recommendation_request
    import capo_cost_explorer.types.get_savings_plans_purchase_recommendation_response
    import capo_cost_explorer.types.get_savings_plans_utilization_details_request
    import capo_cost_explorer.types.get_savings_plans_utilization_details_response
    import capo_cost_explorer.types.get_savings_plans_utilization_request
    import capo_cost_explorer.types.get_savings_plans_utilization_response
    import capo_cost_explorer.types.get_tags_request
    import capo_cost_explorer.types.get_tags_response
    import capo_cost_explorer.types.get_usage_forecast_request
    import capo_cost_explorer.types.get_usage_forecast_response
    import capo_cost_explorer.types.granularity
    import capo_cost_explorer.types.group_definitions
    import capo_cost_explorer.types.list_commitment_purchase_analyses_request
    import capo_cost_explorer.types.list_commitment_purchase_analyses_response
    import capo_cost_explorer.types.list_cost_allocation_tag_backfill_history_request
    import capo_cost_explorer.types.list_cost_allocation_tag_backfill_history_response
    import capo_cost_explorer.types.list_cost_allocation_tags_request
    import capo_cost_explorer.types.list_cost_allocation_tags_response
    import capo_cost_explorer.types.list_cost_category_definitions_request
    import capo_cost_explorer.types.list_cost_category_definitions_response
    import capo_cost_explorer.types.list_cost_category_resource_associations_request
    import capo_cost_explorer.types.list_cost_category_resource_associations_response
    import capo_cost_explorer.types.list_savings_plans_purchase_recommendation_generation_request
    import capo_cost_explorer.types.list_savings_plans_purchase_recommendation_generation_response
    import capo_cost_explorer.types.list_tags_for_resource_request
    import capo_cost_explorer.types.list_tags_for_resource_response
    import capo_cost_explorer.types.lookback_period_in_days
    import capo_cost_explorer.types.max_results
    import capo_cost_explorer.types.metric
    import capo_cost_explorer.types.metric_name
    import capo_cost_explorer.types.metric_names
    import capo_cost_explorer.types.monitor_arn_list
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.nullable_non_negative_double
    import capo_cost_explorer.types.page_size
    import capo_cost_explorer.types.payment_option
    import capo_cost_explorer.types.prediction_interval_level
    import capo_cost_explorer.types.provide_anomaly_feedback_request
    import capo_cost_explorer.types.provide_anomaly_feedback_response
    import capo_cost_explorer.types.recommendation_detail_id
    import capo_cost_explorer.types.recommendation_id_list
    import capo_cost_explorer.types.recommendations_page_size
    import capo_cost_explorer.types.reservation_purchase_recommendation
    import capo_cost_explorer.types.resource_tag_key_list
    import capo_cost_explorer.types.resource_tag_list
    import capo_cost_explorer.types.resource_types_filter_input
    import capo_cost_explorer.types.rightsizing_recommendation
    import capo_cost_explorer.types.rightsizing_recommendation_configuration
    import capo_cost_explorer.types.savings_plans_data_types
    import capo_cost_explorer.types.search_string
    import capo_cost_explorer.types.service_specification
    import capo_cost_explorer.types.sort_definition
    import capo_cost_explorer.types.sort_definitions
    import capo_cost_explorer.types.start_commitment_purchase_analysis_request
    import capo_cost_explorer.types.start_commitment_purchase_analysis_response
    import capo_cost_explorer.types.start_cost_allocation_tag_backfill_request
    import capo_cost_explorer.types.start_cost_allocation_tag_backfill_response
    import capo_cost_explorer.types.start_savings_plans_purchase_recommendation_generation_request
    import capo_cost_explorer.types.start_savings_plans_purchase_recommendation_generation_response
    import capo_cost_explorer.types.subscribers
    import capo_cost_explorer.types.supported_savings_plans_type
    import capo_cost_explorer.types.tag_key
    import capo_cost_explorer.types.tag_resource_request
    import capo_cost_explorer.types.tag_resource_response
    import capo_cost_explorer.types.term_in_years
    import capo_cost_explorer.types.total_impact_filter
    import capo_cost_explorer.types.untag_resource_request
    import capo_cost_explorer.types.untag_resource_response
    import capo_cost_explorer.types.update_anomaly_monitor_request
    import capo_cost_explorer.types.update_anomaly_monitor_response
    import capo_cost_explorer.types.update_anomaly_subscription_request
    import capo_cost_explorer.types.update_anomaly_subscription_response
    import capo_cost_explorer.types.update_cost_allocation_tags_status_request
    import capo_cost_explorer.types.update_cost_allocation_tags_status_response
    import capo_cost_explorer.types.update_cost_category_definition_request
    import capo_cost_explorer.types.update_cost_category_definition_response
    import capo_cost_explorer.types.usage_services
    import capo_cost_explorer.types.values
    import capo_cost_explorer.types.zoned_date_time


class CostExplorerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class CostExplorerClient:
    """A client for the ``CostExplorer`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = CostExplorerClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[CostExplorerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CostExplorerClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def create_anomaly_monitor(
        self,
        anomaly_monitor: "capo_cost_explorer.types.anomaly_monitor.AnomalyMonitor",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        resource_tags: Optional[
            "capo_cost_explorer.types.resource_tag_list.ResourceTagList"
        ] = None,
    ) -> "capo_cost_explorer.types.create_anomaly_monitor_response.CreateAnomalyMonitorResponse":
        """<p>Creates a new cost anomaly detection monitor with the requested type and monitor specification. </p>

        Args:
            anomaly_monitor: <p>The cost anomaly detection monitor object that you want to create.</p>
            resource_tags: <p>An optional list of tags to associate with the specified <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html"> <code>AnomalyMonitor</code> </a>. You can use resource tags to control access to your <code>monitor</code> using IAM policies.</p> <p>Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:</p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services use</p> </li> <li> <p>The maximum length of a key is 128 characters</p> </li> <li> <p>The maximum length of a value is 256 characters</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code> </p> </li> <li> <p>Keys and values are case sensitive</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces</p> </li> <li> <p>Don’t use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services use</p> </li> </ul>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.create_anomaly_monitor_request.CreateAnomalyMonitorRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.create_anomaly_monitor_response.CreateAnomalyMonitorResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.create_anomaly_monitor

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.create_anomaly_monitor.create_anomaly_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.create_anomaly_monitor_request.CreateAnomalyMonitorRequest = {
            "anomaly_monitor": anomaly_monitor
        }
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_anomaly_subscription(
        self,
        anomaly_subscription: "capo_cost_explorer.types.anomaly_subscription.AnomalySubscription",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        resource_tags: Optional[
            "capo_cost_explorer.types.resource_tag_list.ResourceTagList"
        ] = None,
    ) -> "capo_cost_explorer.types.create_anomaly_subscription_response.CreateAnomalySubscriptionResponse":
        """<p>Adds an alert subscription to a cost anomaly detection monitor. You can use each subscription to define subscribers with email or SNS notifications. Email subscribers can set an absolute or percentage threshold and a time frequency for receiving notifications. </p>

        Args:
            anomaly_subscription: <p>The cost anomaly subscription object that you want to create. </p>
            resource_tags: <p>An optional list of tags to associate with the specified <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html"> <code>AnomalySubscription</code> </a>. You can use resource tags to control access to your <code>subscription</code> using IAM policies.</p> <p>Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:</p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services use</p> </li> <li> <p>The maximum length of a key is 128 characters</p> </li> <li> <p>The maximum length of a value is 256 characters</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code> </p> </li> <li> <p>Keys and values are case sensitive</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces</p> </li> <li> <p>Don’t use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services use</p> </li> </ul>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.unknown_monitor_exception.UnknownMonitorException: <p>The cost anomaly monitor does not exist for the account. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.create_anomaly_subscription_request.CreateAnomalySubscriptionRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.create_anomaly_subscription_response.CreateAnomalySubscriptionResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.create_anomaly_subscription

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.create_anomaly_subscription.create_anomaly_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.create_anomaly_subscription_request.CreateAnomalySubscriptionRequest = {
            "anomaly_subscription": anomaly_subscription
        }
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cost_category_definition(
        self,
        name: "capo_cost_explorer.types.cost_category_name.CostCategoryName",
        rule_version: "capo_cost_explorer.types.cost_category_rule_version.CostCategoryRuleVersion",
        rules: "capo_cost_explorer.types.cost_category_rules_list.CostCategoryRulesList",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        effective_start: Optional[
            "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
        ] = None,
        default_value: Optional[
            "capo_cost_explorer.types.cost_category_value.CostCategoryValue"
        ] = None,
        split_charge_rules: Optional[
            "capo_cost_explorer.types.cost_category_split_charge_rules_list.CostCategorySplitChargeRulesList"
        ] = None,
        resource_tags: Optional[
            "capo_cost_explorer.types.resource_tag_list.ResourceTagList"
        ] = None,
    ) -> "capo_cost_explorer.types.create_cost_category_definition_response.CreateCostCategoryDefinitionResponse":
        """<p>Creates a new cost category with the requested name and rules.</p>

        Args:
            effective_start: <p>The cost category's effective start date. It can only be a billing start date (first day of the month). If the date isn't provided, it's the first day of the current month. Dates can't be before the previous twelve months, or in the future.</p>
            rules: <p>The cost category rules used to categorize costs. For more information, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html">CostCategoryRule</a>.</p>
            split_charge_rules: <p> The split charge rules used to allocate your charges between your cost category values. </p>
            resource_tags: <p>An optional list of tags to associate with the specified <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html"> <code>CostCategory</code> </a>. You can use resource tags to control access to your <code>cost category</code> using IAM policies.</p> <p>Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:</p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services use</p> </li> <li> <p>The maximum length of a key is 128 characters</p> </li> <li> <p>The maximum length of a value is 256 characters</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code> </p> </li> <li> <p>Keys and values are case sensitive</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces</p> </li> <li> <p>Don’t use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services use</p> </li> </ul>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.create_cost_category_definition_request.CreateCostCategoryDefinitionRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.create_cost_category_definition_response.CreateCostCategoryDefinitionResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.create_cost_category_definition

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.create_cost_category_definition.create_cost_category_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.create_cost_category_definition_request.CreateCostCategoryDefinitionRequest = {
            "name": name,
            "rule_version": rule_version,
            "rules": rules,
        }
        if effective_start is not None:
            input_["effective_start"] = effective_start
        if default_value is not None:
            input_["default_value"] = default_value
        if split_charge_rules is not None:
            input_["split_charge_rules"] = split_charge_rules
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_anomaly_monitor(
        self,
        monitor_arn: "capo_cost_explorer.types.generic_string.GenericString",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.delete_anomaly_monitor_response.DeleteAnomalyMonitorResponse":
        """<p>Deletes a cost anomaly monitor. </p>

        Args:
            monitor_arn: <p>The unique identifier of the cost anomaly monitor that you want to delete. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.unknown_monitor_exception.UnknownMonitorException: <p>The cost anomaly monitor does not exist for the account. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.delete_anomaly_monitor_request.DeleteAnomalyMonitorRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.delete_anomaly_monitor_response.DeleteAnomalyMonitorResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.delete_anomaly_monitor

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.delete_anomaly_monitor.delete_anomaly_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.delete_anomaly_monitor_request.DeleteAnomalyMonitorRequest = {
            "monitor_arn": monitor_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_anomaly_subscription(
        self,
        subscription_arn: "capo_cost_explorer.types.generic_string.GenericString",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.delete_anomaly_subscription_response.DeleteAnomalySubscriptionResponse":
        """<p>Deletes a cost anomaly subscription. </p>

        Args:
            subscription_arn: <p>The unique identifier of the cost anomaly subscription that you want to delete. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.unknown_subscription_exception.UnknownSubscriptionException: <p>The cost anomaly subscription does not exist for the account. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.delete_anomaly_subscription_request.DeleteAnomalySubscriptionRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.delete_anomaly_subscription_response.DeleteAnomalySubscriptionResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.delete_anomaly_subscription

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.delete_anomaly_subscription.delete_anomaly_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.delete_anomaly_subscription_request.DeleteAnomalySubscriptionRequest = {
            "subscription_arn": subscription_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cost_category_definition(
        self,
        cost_category_arn: "capo_cost_explorer.types.arn.Arn",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.delete_cost_category_definition_response.DeleteCostCategoryDefinitionResponse":
        """<p>Deletes a cost category. Expenses from this month going forward will no longer be categorized with this cost category.</p>

        Args:
            cost_category_arn: <p>The unique identifier for your cost category. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.delete_cost_category_definition_request.DeleteCostCategoryDefinitionRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.delete_cost_category_definition_response.DeleteCostCategoryDefinitionResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.delete_cost_category_definition

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.delete_cost_category_definition.delete_cost_category_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.delete_cost_category_definition_request.DeleteCostCategoryDefinitionRequest = {
            "cost_category_arn": cost_category_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cost_category_definition(
        self,
        cost_category_arn: "capo_cost_explorer.types.arn.Arn",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        effective_on: Optional[
            "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
        ] = None,
    ) -> "capo_cost_explorer.types.describe_cost_category_definition_response.DescribeCostCategoryDefinitionResponse":
        """<p>Returns the name, Amazon Resource Name (ARN), rules, definition, and effective dates of a cost category that's defined in the account.</p> <p>You have the option to use <code>EffectiveOn</code> to return a cost category that's active on a specific date. If there's no <code>EffectiveOn</code> specified, you see a Cost Category that's effective on the current date. If cost category is still effective, <code>EffectiveEnd</code> is omitted in the response. </p>

        Args:
            cost_category_arn: <p>The unique identifier for your cost category. </p>
            effective_on: <p>The date when the cost category was effective. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.describe_cost_category_definition_request.DescribeCostCategoryDefinitionRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.describe_cost_category_definition_response.DescribeCostCategoryDefinitionResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.describe_cost_category_definition

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.describe_cost_category_definition.describe_cost_category_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.describe_cost_category_definition_request.DescribeCostCategoryDefinitionRequest = {
            "cost_category_arn": cost_category_arn
        }
        if effective_on is not None:
            input_["effective_on"] = effective_on

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_anomalies(
        self,
        date_interval: "capo_cost_explorer.types.anomaly_date_interval.AnomalyDateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        monitor_arn: Optional[
            "capo_cost_explorer.types.generic_string.GenericString"
        ] = None,
        feedback: Optional[
            "capo_cost_explorer.types.anomaly_feedback_type.AnomalyFeedbackType"
        ] = None,
        total_impact: Optional[
            "capo_cost_explorer.types.total_impact_filter.TotalImpactFilter"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.page_size.PageSize"] = None,
    ) -> "capo_cost_explorer.types.get_anomalies_response.GetAnomaliesResponse":
        """<p>Retrieves all of the cost anomalies detected on your account during the time period that's specified by the <code>DateInterval</code> object. Anomalies are available for up to 90 days.</p>

        Args:
            monitor_arn: <p>Retrieves all of the cost anomalies detected for a specific cost anomaly monitor Amazon Resource Name (ARN). </p>
            date_interval: <p>Assigns the start and end dates for retrieving cost anomalies. The returned anomaly object will have an <code>AnomalyEndDate</code> in the specified time range. </p>
            feedback: <p>Filters anomaly results by the feedback field on the anomaly object. </p>
            total_impact: <p>Filters anomaly results by the total impact field on the anomaly object. For example, you can filter anomalies <code>GREATER_THAN 200.00</code> to retrieve anomalies, with an estimated dollar impact greater than 200. </p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>
            max_results: <p>The number of entries a paginated response contains. </p>

        Raises:
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_anomalies_request.GetAnomaliesRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_anomalies_response.GetAnomaliesResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_anomalies

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_anomalies.get_anomalies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_anomalies_request.GetAnomaliesRequest = {
            "date_interval": date_interval
        }
        if monitor_arn is not None:
            input_["monitor_arn"] = monitor_arn
        if feedback is not None:
            input_["feedback"] = feedback
        if total_impact is not None:
            input_["total_impact"] = total_impact
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_anomalies(
        self,
        date_interval: "capo_cost_explorer.types.anomaly_date_interval.AnomalyDateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        monitor_arn: Optional[
            "capo_cost_explorer.types.generic_string.GenericString"
        ] = None,
        feedback: Optional[
            "capo_cost_explorer.types.anomaly_feedback_type.AnomalyFeedbackType"
        ] = None,
        total_impact: Optional[
            "capo_cost_explorer.types.total_impact_filter.TotalImpactFilter"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.page_size.PageSize"] = None,
    ) -> "Iterator[capo_cost_explorer.types.anomaly.Anomaly]":
        _token = next_page_token
        while True:
            _response = self.get_anomalies(
                date_interval,
                config_overrides=config_overrides,
                monitor_arn=monitor_arn,
                feedback=feedback,
                total_impact=total_impact,
                next_page_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("anomalies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def get_anomaly_monitors(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        monitor_arn_list: Optional["capo_cost_explorer.types.values.Values"] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.page_size.PageSize"] = None,
    ) -> "capo_cost_explorer.types.get_anomaly_monitors_response.GetAnomalyMonitorsResponse":
        """<p>Retrieves the cost anomaly monitor definitions for your account. You can filter using a list of cost anomaly monitor Amazon Resource Names (ARNs). </p>

        Args:
            monitor_arn_list: <p>A list of cost anomaly monitor ARNs. </p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>
            max_results: <p>The number of entries that a paginated response contains. </p>

        Raises:
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.unknown_monitor_exception.UnknownMonitorException: <p>The cost anomaly monitor does not exist for the account. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_anomaly_monitors_request.GetAnomalyMonitorsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_anomaly_monitors_response.GetAnomalyMonitorsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_anomaly_monitors

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_anomaly_monitors.get_anomaly_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_anomaly_monitors_request.GetAnomalyMonitorsRequest = {}
        if monitor_arn_list is not None:
            input_["monitor_arn_list"] = monitor_arn_list
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_anomaly_monitors(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        monitor_arn_list: Optional["capo_cost_explorer.types.values.Values"] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.page_size.PageSize"] = None,
    ) -> "Iterator[capo_cost_explorer.types.anomaly_monitor.AnomalyMonitor]":
        _token = next_page_token
        while True:
            _response = self.get_anomaly_monitors(
                config_overrides=config_overrides,
                monitor_arn_list=monitor_arn_list,
                next_page_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("anomaly_monitors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def get_anomaly_subscriptions(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        subscription_arn_list: Optional[
            "capo_cost_explorer.types.values.Values"
        ] = None,
        monitor_arn: Optional[
            "capo_cost_explorer.types.generic_string.GenericString"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.page_size.PageSize"] = None,
    ) -> "capo_cost_explorer.types.get_anomaly_subscriptions_response.GetAnomalySubscriptionsResponse":
        """<p>Retrieves the cost anomaly subscription objects for your account. You can filter using a list of cost anomaly monitor Amazon Resource Names (ARNs). </p>

        Args:
            subscription_arn_list: <p>A list of cost anomaly subscription ARNs. </p>
            monitor_arn: <p>Cost anomaly monitor ARNs. </p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>
            max_results: <p>The number of entries a paginated response contains. </p>

        Raises:
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.unknown_subscription_exception.UnknownSubscriptionException: <p>The cost anomaly subscription does not exist for the account. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_anomaly_subscriptions_request.GetAnomalySubscriptionsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_anomaly_subscriptions_response.GetAnomalySubscriptionsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_anomaly_subscriptions

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_anomaly_subscriptions.get_anomaly_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_anomaly_subscriptions_request.GetAnomalySubscriptionsRequest = {}
        if subscription_arn_list is not None:
            input_["subscription_arn_list"] = subscription_arn_list
        if monitor_arn is not None:
            input_["monitor_arn"] = monitor_arn
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_anomaly_subscriptions(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        subscription_arn_list: Optional[
            "capo_cost_explorer.types.values.Values"
        ] = None,
        monitor_arn: Optional[
            "capo_cost_explorer.types.generic_string.GenericString"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.page_size.PageSize"] = None,
    ) -> "Iterator[capo_cost_explorer.types.anomaly_subscription.AnomalySubscription]":
        _token = next_page_token
        while True:
            _response = self.get_anomaly_subscriptions(
                config_overrides=config_overrides,
                subscription_arn_list=subscription_arn_list,
                monitor_arn=monitor_arn,
                next_page_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("anomaly_subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def get_approximate_usage_records(
        self,
        granularity: "capo_cost_explorer.types.granularity.Granularity",
        approximation_dimension: "capo_cost_explorer.types.approximation_dimension.ApproximationDimension",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        services: Optional[
            "capo_cost_explorer.types.usage_services.UsageServices"
        ] = None,
    ) -> "capo_cost_explorer.types.get_approximate_usage_records_response.GetApproximateUsageRecordsResponse":
        """<p>Retrieves estimated usage records for hourly granularity or resource-level data at daily granularity.</p>

        Args:
            granularity: <p>How granular you want the data to be. You can enable data at hourly or daily granularity.</p>
            services: <p>The service metadata for the service or services you want to query. If not specified, all elements are returned.</p>
            approximation_dimension: <p>The service to evaluate for the usage records. You can choose resource-level data at daily granularity, or hourly granularity with or without resource-level data.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_approximate_usage_records_request.GetApproximateUsageRecordsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_approximate_usage_records_response.GetApproximateUsageRecordsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_approximate_usage_records

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_approximate_usage_records.get_approximate_usage_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_approximate_usage_records_request.GetApproximateUsageRecordsRequest = {
            "granularity": granularity,
            "approximation_dimension": approximation_dimension,
        }
        if services is not None:
            input_["services"] = services

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_commitment_purchase_analysis(
        self,
        analysis_id: "capo_cost_explorer.types.analysis_id.AnalysisId",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.get_commitment_purchase_analysis_response.GetCommitmentPurchaseAnalysisResponse":
        """<p>Retrieves a commitment purchase analysis result based on the <code>AnalysisId</code>.</p>

        Args:
            analysis_id: <p>The analysis ID that's associated with the commitment purchase analysis.</p>

        Raises:
            capo_cost_explorer.errors.analysis_not_found_exception.AnalysisNotFoundException: <p>The requested analysis can't be found.</p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_commitment_purchase_analysis_request.GetCommitmentPurchaseAnalysisRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_commitment_purchase_analysis_response.GetCommitmentPurchaseAnalysisResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_commitment_purchase_analysis

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_commitment_purchase_analysis.get_commitment_purchase_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_commitment_purchase_analysis_request.GetCommitmentPurchaseAnalysisRequest = {
            "analysis_id": analysis_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cost_and_usage(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        granularity: "capo_cost_explorer.types.granularity.Granularity",
        metrics: "capo_cost_explorer.types.metric_names.MetricNames",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.get_cost_and_usage_response.GetCostAndUsageResponse":
        """<p>Retrieves cost and usage metrics for your account. You can specify which cost and usage-related metric that you want the request to return. For example, you can specify <code>BlendedCosts</code> or <code>UsageQuantity</code>. You can also filter and group your data by various dimensions, such as <code>SERVICE</code> or <code>AZ</code>, in a specific time range. For a complete list of valid dimensions, see the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html">GetDimensionValues</a> operation. Management account in an organization in Organizations have access to all member accounts.</p> <p>For information about filter limitations, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html">Quotas and restrictions</a> in the <i>Billing and Cost Management User Guide</i>.</p>

        Args:
            time_period: <p>Sets the start date and end date for retrieving Amazon Web Services costs. The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>.</p>
            granularity: <p>Sets the Amazon Web Services cost granularity to <code>MONTHLY</code> or <code>DAILY</code>, or <code>HOURLY</code>. If <code>Granularity</code> isn't set, the response object doesn't include the <code>Granularity</code>, either <code>MONTHLY</code> or <code>DAILY</code>, or <code>HOURLY</code>. </p>
            filter: <p>Filters Amazon Web Services costs by different dimensions. For example, you can specify <code>SERVICE</code> and <code>LINKED_ACCOUNT</code> and get the costs that are associated with that account's usage of that service. You can nest <code>Expression</code> objects to define any combination of dimension filters. For more information, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a>. </p> <p>Valid values for <code>MatchOptions</code> for <code>Dimensions</code> are <code>EQUALS</code> and <code>CASE_SENSITIVE</code>.</p> <p>Valid values for <code>MatchOptions</code> for <code>CostCategories</code> and <code>Tags</code> are <code>EQUALS</code>, <code>ABSENT</code>, and <code>CASE_SENSITIVE</code>. Default values are <code>EQUALS</code> and <code>CASE_SENSITIVE</code>.</p>
            metrics: <p>Which metrics are returned in the query. For more information about blended and unblended rates, see <a href="http://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/">Why does the "blended" annotation appear on some line items in my bill?</a>. </p> <p>Valid values are <code>AmortizedCost</code>, <code>BlendedCost</code>, <code>NetAmortizedCost</code>, <code>NetUnblendedCost</code>, <code>NormalizedUsageAmount</code>, <code>UnblendedCost</code>, and <code>UsageQuantity</code>. </p> <note> <p>If you return the <code>UsageQuantity</code> metric, the service aggregates all usage numbers without taking into account the units. For example, if you aggregate <code>usageQuantity</code> across all of Amazon EC2, the results aren't meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hours and GB). To get more meaningful <code>UsageQuantity</code> metrics, filter by <code>UsageType</code> or <code>UsageTypeGroups</code>. </p> </note> <p> <code>Metrics</code> is required for <code>GetCostAndUsage</code> requests.</p>
            group_by: <p>You can group Amazon Web Services costs using up to two different groups, either dimensions, tag keys, cost categories, or any two group by types.</p> <p>Valid values for the <code>DIMENSION</code> type are <code>AZ</code>, <code>INSTANCE_TYPE</code>, <code>LEGAL_ENTITY_NAME</code>, <code>INVOICING_ENTITY</code>, <code>LINKED_ACCOUNT</code>, <code>OPERATION</code>, <code>PLATFORM</code>, <code>PURCHASE_TYPE</code>, <code>SERVICE</code>, <code>TENANCY</code>, <code>RECORD_TYPE</code>, and <code>USAGE_TYPE</code>.</p> <p>When you group by the <code>TAG</code> type and include a valid tag key, you get all tag values, including empty strings.</p>
            billing_view_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>

        Raises:
            capo_cost_explorer.errors.bill_expiration_exception.BillExpirationException: <p>The requested report expired. Update the date interval and try again.</p>
            capo_cost_explorer.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> The billing view status must be <code>HEALTHY</code> to perform this action. Try again when the status is <code>HEALTHY</code>. </p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.request_changed_exception.RequestChangedException: <p>Your request parameters changed between pages. Try again with the old parameters or without a pagination token.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_cost_and_usage_request.GetCostAndUsageRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_cost_and_usage_response.GetCostAndUsageResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_cost_and_usage

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_cost_and_usage.get_cost_and_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_cost_and_usage_request.GetCostAndUsageRequest = {
            "time_period": time_period,
            "granularity": granularity,
            "metrics": metrics,
        }
        if filter is not None:
            input_["filter"] = filter
        if group_by is not None:
            input_["group_by"] = group_by
        if billing_view_arn is not None:
            input_["billing_view_arn"] = billing_view_arn
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cost_and_usage_comparisons(
        self,
        baseline_time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        comparison_time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        metric_for_comparison: "capo_cost_explorer.types.metric_name.MetricName",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_and_usage_comparisons_max_results.CostAndUsageComparisonsMaxResults"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.get_cost_and_usage_comparisons_response.GetCostAndUsageComparisonsResponse":
        """<p>Retrieves cost and usage comparisons for your account between two periods within the last 13 months. If you have enabled multi-year data at monthly granularity, you can go back up to 38 months.</p>

        Args:
            billing_view_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>
            baseline_time_period: <p>The reference time period for comparison. This time period serves as the baseline against which other cost and usage data will be compared. The interval must start and end on the first day of a month, with a duration of exactly one month.</p>
            comparison_time_period: <p>The comparison time period for analysis. This time period's cost and usage data will be compared against the baseline time period. The interval must start and end on the first day of a month, with a duration of exactly one month.</p>
            metric_for_comparison: <p>The cost and usage metric to compare. Valid values are <code>AmortizedCost</code>, <code>BlendedCost</code>, <code>NetAmortizedCost</code>, <code>NetUnblendedCost</code>, <code>NormalizedUsageAmount</code>, <code>UnblendedCost</code>, and <code>UsageQuantity</code>.</p>
            group_by: <p>You can group results using the attributes <code>DIMENSION</code>, <code>TAG</code>, and <code>COST_CATEGORY</code>. </p>
            max_results: <p>The maximum number of results that are returned for the request.</p>
            next_page_token: <p>The token to retrieve the next set of paginated results.</p>

        Raises:
            capo_cost_explorer.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> The billing view status must be <code>HEALTHY</code> to perform this action. Try again when the status is <code>HEALTHY</code>. </p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_cost_and_usage_comparisons_request.GetCostAndUsageComparisonsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_cost_and_usage_comparisons_response.GetCostAndUsageComparisonsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_cost_and_usage_comparisons

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_cost_and_usage_comparisons.get_cost_and_usage_comparisons(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_cost_and_usage_comparisons_request.GetCostAndUsageComparisonsRequest = {
            "baseline_time_period": baseline_time_period,
            "comparison_time_period": comparison_time_period,
            "metric_for_comparison": metric_for_comparison,
        }
        if billing_view_arn is not None:
            input_["billing_view_arn"] = billing_view_arn
        if filter is not None:
            input_["filter"] = filter
        if group_by is not None:
            input_["group_by"] = group_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_cost_and_usage_comparisons(
        self,
        baseline_time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        comparison_time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        metric_for_comparison: "capo_cost_explorer.types.metric_name.MetricName",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_and_usage_comparisons_max_results.CostAndUsageComparisonsMaxResults"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.cost_and_usage_comparison.CostAndUsageComparison]":
        _token = next_page_token
        while True:
            _response = self.get_cost_and_usage_comparisons(
                baseline_time_period,
                comparison_time_period,
                metric_for_comparison,
                config_overrides=config_overrides,
                billing_view_arn=billing_view_arn,
                filter=filter,
                group_by=group_by,
                max_results=max_results,
                next_page_token=_token,
            )
            _page = _resolve_path(_response, ("cost_and_usage_comparisons",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def get_cost_and_usage_with_resources(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        granularity: "capo_cost_explorer.types.granularity.Granularity",
        filter: "capo_cost_explorer.types.expression.Expression",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        metrics: Optional["capo_cost_explorer.types.metric_names.MetricNames"] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.get_cost_and_usage_with_resources_response.GetCostAndUsageWithResourcesResponse":
        """<p>Retrieves cost and usage metrics with resources for your account. You can specify which cost and usage-related metric, such as <code>BlendedCosts</code> or <code>UsageQuantity</code>, that you want the request to return. You can also filter and group your data by various dimensions, such as <code>SERVICE</code> or <code>AZ</code>, in a specific time range. For a complete list of valid dimensions, see the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html">GetDimensionValues</a> operation. Management account in an organization in Organizations have access to all member accounts.</p> <p>Hourly granularity is only available for EC2-Instances (Elastic Compute Cloud) resource-level data. All other resource-level data is available at daily granularity.</p> <note> <p>This is an opt-in only feature. You can enable this feature from the Cost Explorer Settings page. For information about how to access the Settings page, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-access.html">Controlling Access for Cost Explorer</a> in the <i>Billing and Cost Management User Guide</i>.</p> </note>

        Args:
            time_period: <p>Sets the start and end dates for retrieving Amazon Web Services costs. The range must be within the last 14 days (the start date cannot be earlier than 14 days ago). The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>.</p>
            granularity: <p>Sets the Amazon Web Services cost granularity to <code>MONTHLY</code>, <code>DAILY</code>, or <code>HOURLY</code>. If <code>Granularity</code> isn't set, the response object doesn't include the <code>Granularity</code>, <code>MONTHLY</code>, <code>DAILY</code>, or <code>HOURLY</code>. </p>
            filter: <p>Filters Amazon Web Services costs by different dimensions. For example, you can specify <code>SERVICE</code> and <code>LINKED_ACCOUNT</code> and get the costs that are associated with that account's usage of that service. You can nest <code>Expression</code> objects to define any combination of dimension filters. For more information, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a>. </p> <p>The <code>GetCostAndUsageWithResources</code> operation requires that you either group by or filter by a <code>ResourceId</code>. It requires the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> <code>"SERVICE = Amazon Elastic Compute Cloud - Compute"</code> in the filter.</p> <p>Valid values for <code>MatchOptions</code> for <code>Dimensions</code> are <code>EQUALS</code> and <code>CASE_SENSITIVE</code>.</p> <p>Valid values for <code>MatchOptions</code> for <code>CostCategories</code> and <code>Tags</code> are <code>EQUALS</code>, <code>ABSENT</code>, and <code>CASE_SENSITIVE</code>. Default values are <code>EQUALS</code> and <code>CASE_SENSITIVE</code>.</p>
            metrics: <p>Which metrics are returned in the query. For more information about blended and unblended rates, see <a href="http://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/">Why does the "blended" annotation appear on some line items in my bill?</a>. </p> <p>Valid values are <code>AmortizedCost</code>, <code>BlendedCost</code>, <code>NetAmortizedCost</code>, <code>NetUnblendedCost</code>, <code>NormalizedUsageAmount</code>, <code>UnblendedCost</code>, and <code>UsageQuantity</code>. </p> <note> <p>If you return the <code>UsageQuantity</code> metric, the service aggregates all usage numbers without taking the units into account. For example, if you aggregate <code>usageQuantity</code> across all of Amazon EC2, the results aren't meaningful because Amazon EC2 compute hours and data transfer are measured in different units (for example, hour or GB). To get more meaningful <code>UsageQuantity</code> metrics, filter by <code>UsageType</code> or <code>UsageTypeGroups</code>. </p> </note> <p> <code>Metrics</code> is required for <code>GetCostAndUsageWithResources</code> requests.</p>
            group_by: <p>You can group Amazon Web Services costs using up to two different groups: <code>DIMENSION</code>, <code>TAG</code>, <code>COST_CATEGORY</code>.</p>
            billing_view_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>

        Raises:
            capo_cost_explorer.errors.bill_expiration_exception.BillExpirationException: <p>The requested report expired. Update the date interval and try again.</p>
            capo_cost_explorer.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> The billing view status must be <code>HEALTHY</code> to perform this action. Try again when the status is <code>HEALTHY</code>. </p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.request_changed_exception.RequestChangedException: <p>Your request parameters changed between pages. Try again with the old parameters or without a pagination token.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_cost_and_usage_with_resources_request.GetCostAndUsageWithResourcesRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_cost_and_usage_with_resources_response.GetCostAndUsageWithResourcesResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_cost_and_usage_with_resources

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_cost_and_usage_with_resources.get_cost_and_usage_with_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_cost_and_usage_with_resources_request.GetCostAndUsageWithResourcesRequest = {
            "time_period": time_period,
            "granularity": granularity,
            "filter": filter,
        }
        if metrics is not None:
            input_["metrics"] = metrics
        if group_by is not None:
            input_["group_by"] = group_by
        if billing_view_arn is not None:
            input_["billing_view_arn"] = billing_view_arn
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cost_categories(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        search_string: Optional[
            "capo_cost_explorer.types.search_string.SearchString"
        ] = None,
        cost_category_name: Optional[
            "capo_cost_explorer.types.cost_category_name.CostCategoryName"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definitions.SortDefinitions"
        ] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.max_results.MaxResults"] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.get_cost_categories_response.GetCostCategoriesResponse":
        """<p>Retrieves an array of cost category names and values incurred cost.</p> <note> <p>If some cost category names and values are not associated with any cost, they will not be returned by this API.</p> </note>

        Args:
            search_string: <p>The value that you want to search the filter values for.</p> <p>If you don't specify a <code>CostCategoryName</code>, <code>SearchString</code> is used to filter cost category names that match the <code>SearchString</code> pattern. If you specify a <code>CostCategoryName</code>, <code>SearchString</code> is used to filter cost category values that match the <code>SearchString</code> pattern.</p>
            sort_by: <p>The value that you sort the data by.</p> <p>The key represents the cost and usage metrics. The following values are supported:</p> <ul> <li> <p> <code>BlendedCost</code> </p> </li> <li> <p> <code>UnblendedCost</code> </p> </li> <li> <p> <code>AmortizedCost</code> </p> </li> <li> <p> <code>NetAmortizedCost</code> </p> </li> <li> <p> <code>NetUnblendedCost</code> </p> </li> <li> <p> <code>UsageQuantity</code> </p> </li> <li> <p> <code>NormalizedUsageAmount</code> </p> </li> </ul> <p>The supported key values for the <code>SortOrder</code> value are <code>ASCENDING</code> and <code>DESCENDING</code>.</p> <p>When you use the <code>SortBy</code> value, the <code>NextPageToken</code> and <code>SearchString</code> key values aren't supported.</p>
            billing_view_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>
            max_results: <p>This field is only used when the <code>SortBy</code> value is provided in the request.</p> <p>The maximum number of objects that are returned for this request. If <code>MaxResults</code> isn't specified with the <code>SortBy</code> value, the request returns 1000 results as the default value for this parameter.</p> <p>For <code>GetCostCategories</code>, MaxResults has an upper quota of 1000.</p>
            next_page_token: <p>If the number of objects that are still available for retrieval exceeds the quota, Amazon Web Services returns a NextPageToken value in the response. To retrieve the next batch of objects, provide the NextPageToken from the previous call in your next request.</p>

        Raises:
            capo_cost_explorer.errors.bill_expiration_exception.BillExpirationException: <p>The requested report expired. Update the date interval and try again.</p>
            capo_cost_explorer.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> The billing view status must be <code>HEALTHY</code> to perform this action. Try again when the status is <code>HEALTHY</code>. </p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.request_changed_exception.RequestChangedException: <p>Your request parameters changed between pages. Try again with the old parameters or without a pagination token.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_cost_categories_request.GetCostCategoriesRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_cost_categories_response.GetCostCategoriesResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_cost_categories

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_cost_categories.get_cost_categories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_cost_categories_request.GetCostCategoriesRequest = {
            "time_period": time_period
        }
        if search_string is not None:
            input_["search_string"] = search_string
        if cost_category_name is not None:
            input_["cost_category_name"] = cost_category_name
        if filter is not None:
            input_["filter"] = filter
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if billing_view_arn is not None:
            input_["billing_view_arn"] = billing_view_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cost_comparison_drivers(
        self,
        baseline_time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        comparison_time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        metric_for_comparison: "capo_cost_explorer.types.metric_name.MetricName",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_comparison_drivers_max_results.CostComparisonDriversMaxResults"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.get_cost_comparison_drivers_response.GetCostComparisonDriversResponse":
        """<p>Retrieves key factors driving cost changes between two time periods within the last 13 months, such as usage changes, discount changes, and commitment-based savings. If you have enabled multi-year data at monthly granularity, you can go back up to 38 months.</p>

        Args:
            billing_view_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>
            baseline_time_period: <p>The reference time period for comparison. This time period serves as the baseline against which other cost and usage data will be compared. The interval must start and end on the first day of a month, with a duration of exactly one month.</p>
            comparison_time_period: <p>The comparison time period for analysis. This time period's cost and usage data will be compared against the baseline time period. The interval must start and end on the first day of a month, with a duration of exactly one month.</p>
            metric_for_comparison: <p>The cost and usage metric to compare. Valid values are <code>AmortizedCost</code>, <code>BlendedCost</code>, <code>NetAmortizedCost</code>, <code>NetUnblendedCost</code>, <code>NormalizedUsageAmount</code>, <code>UnblendedCost</code>, and <code>UsageQuantity</code>.</p>
            group_by: <p>You can group results using the attributes <code>DIMENSION</code>, <code>TAG</code>, and <code>COST_CATEGORY</code>. Note that <code>SERVICE</code> and <code>USAGE_TYPE</code> dimensions are automatically included in the cost comparison drivers analysis.</p>
            max_results: <p>The maximum number of results that are returned for the request.</p>
            next_page_token: <p>The token to retrieve the next set of paginated results.</p>

        Raises:
            capo_cost_explorer.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> The billing view status must be <code>HEALTHY</code> to perform this action. Try again when the status is <code>HEALTHY</code>. </p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_cost_comparison_drivers_request.GetCostComparisonDriversRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_cost_comparison_drivers_response.GetCostComparisonDriversResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_cost_comparison_drivers

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_cost_comparison_drivers.get_cost_comparison_drivers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_cost_comparison_drivers_request.GetCostComparisonDriversRequest = {
            "baseline_time_period": baseline_time_period,
            "comparison_time_period": comparison_time_period,
            "metric_for_comparison": metric_for_comparison,
        }
        if billing_view_arn is not None:
            input_["billing_view_arn"] = billing_view_arn
        if filter is not None:
            input_["filter"] = filter
        if group_by is not None:
            input_["group_by"] = group_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_cost_comparison_drivers(
        self,
        baseline_time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        comparison_time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        metric_for_comparison: "capo_cost_explorer.types.metric_name.MetricName",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_comparison_drivers_max_results.CostComparisonDriversMaxResults"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> (
        "Iterator[capo_cost_explorer.types.cost_comparison_driver.CostComparisonDriver]"
    ):
        _token = next_page_token
        while True:
            _response = self.get_cost_comparison_drivers(
                baseline_time_period,
                comparison_time_period,
                metric_for_comparison,
                config_overrides=config_overrides,
                billing_view_arn=billing_view_arn,
                filter=filter,
                group_by=group_by,
                max_results=max_results,
                next_page_token=_token,
            )
            _page = _resolve_path(_response, ("cost_comparison_drivers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def get_cost_forecast(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        metric: "capo_cost_explorer.types.metric.Metric",
        granularity: "capo_cost_explorer.types.granularity.Granularity",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        prediction_interval_level: Optional[
            "capo_cost_explorer.types.prediction_interval_level.PredictionIntervalLevel"
        ] = None,
    ) -> "capo_cost_explorer.types.get_cost_forecast_response.GetCostForecastResponse":
        """<p>Retrieves a forecast for how much Amazon Web Services predicts that you will spend over the forecast time period that you select, based on your past costs. </p>

        Args:
            time_period: <p>The period of time that you want the forecast to cover. The start date must be equal to or no later than the current date to avoid a validation error.</p>
            metric: <p>Which metric Cost Explorer uses to create your forecast. For more information about blended and unblended rates, see <a href="http://aws.amazon.com/premiumsupport/knowledge-center/blended-rates-intro/">Why does the "blended" annotation appear on some line items in my bill?</a>. </p> <p>Valid values for a <code>GetCostForecast</code> call are the following:</p> <ul> <li> <p>AMORTIZED_COST</p> </li> <li> <p>BLENDED_COST</p> </li> <li> <p>NET_AMORTIZED_COST</p> </li> <li> <p>NET_UNBLENDED_COST</p> </li> <li> <p>UNBLENDED_COST</p> </li> </ul>
            granularity: <p>How granular you want the forecast to be. You can get 3 months of <code>DAILY</code> forecasts or 18 months of <code>MONTHLY</code> forecasts.</p> <p>The <code>GetCostForecast</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>
            filter: <p>The filters that you want to use to filter your forecast. The <code>GetCostForecast</code> API supports filtering by the following dimensions:</p> <ul> <li> <p> <code>AZ</code> </p> </li> <li> <p> <code>INSTANCE_TYPE</code> </p> </li> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>OPERATION</code> </p> </li> <li> <p> <code>PURCHASE_TYPE</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>SERVICE</code> </p> </li> <li> <p> <code>USAGE_TYPE</code> </p> </li> <li> <p> <code>USAGE_TYPE_GROUP</code> </p> </li> <li> <p> <code>RECORD_TYPE</code> </p> </li> <li> <p> <code>OPERATING_SYSTEM</code> </p> </li> <li> <p> <code>TENANCY</code> </p> </li> <li> <p> <code>SCOPE</code> </p> </li> <li> <p> <code>PLATFORM</code> </p> </li> <li> <p> <code>SUBSCRIPTION_ID</code> </p> </li> <li> <p> <code>LEGAL_ENTITY_NAME</code> </p> </li> <li> <p> <code>DEPLOYMENT_OPTION</code> </p> </li> <li> <p> <code>DATABASE_ENGINE</code> </p> </li> <li> <p> <code>INSTANCE_TYPE_FAMILY</code> </p> </li> <li> <p> <code>BILLING_ENTITY</code> </p> </li> <li> <p> <code>RESERVATION_ID</code> </p> </li> <li> <p> <code>SAVINGS_PLAN_ARN</code> </p> </li> </ul>
            billing_view_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>
            prediction_interval_level: <p>Cost Explorer always returns the mean forecast as a single point. You can request a prediction interval around the mean by specifying a confidence level. The higher the confidence level, the more confident Cost Explorer is about the actual value falling in the prediction interval. Higher confidence levels result in wider prediction intervals.</p>

        Raises:
            capo_cost_explorer.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> The billing view status must be <code>HEALTHY</code> to perform this action. Try again when the status is <code>HEALTHY</code>. </p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_cost_forecast_request.GetCostForecastRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_cost_forecast_response.GetCostForecastResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_cost_forecast

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_cost_forecast.get_cost_forecast(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_cost_forecast_request.GetCostForecastRequest = {
            "time_period": time_period,
            "metric": metric,
            "granularity": granularity,
        }
        if filter is not None:
            input_["filter"] = filter
        if billing_view_arn is not None:
            input_["billing_view_arn"] = billing_view_arn
        if prediction_interval_level is not None:
            input_["prediction_interval_level"] = prediction_interval_level

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dimension_values(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        dimension: "capo_cost_explorer.types.dimension.Dimension",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        search_string: Optional[
            "capo_cost_explorer.types.search_string.SearchString"
        ] = None,
        context: Optional["capo_cost_explorer.types.context.Context"] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definitions.SortDefinitions"
        ] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.max_results.MaxResults"] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.get_dimension_values_response.GetDimensionValuesResponse":
        """<p>Retrieves all available filter values for a specified filter over a period of time. You can search the dimension values for an arbitrary string. </p>

        Args:
            search_string: <p>The value that you want to search the filter values for.</p>
            time_period: <p>The start date and end date for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>.</p>
            dimension: <p>The name of the dimension. Each <code>Dimension</code> is available for a different <code>Context</code>. For more information, see <code>Context</code>. <code>LINK_ACCOUNT_NAME</code> and <code>SERVICE_CODE</code> can only be used in <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/AAPI_CostCategoryRule.html">CostCategoryRule</a>. </p>
            context: <p>The context for the call to <code>GetDimensionValues</code>. This can be <code>RESERVATIONS</code> or <code>COST_AND_USAGE</code>. The default value is <code>COST_AND_USAGE</code>. If the context is set to <code>RESERVATIONS</code>, the resulting dimension values can be used in the <code>GetReservationUtilization</code> operation. If the context is set to <code>COST_AND_USAGE</code>, the resulting dimension values can be used in the <code>GetCostAndUsage</code> operation.</p> <p>If you set the context to <code>COST_AND_USAGE</code>, you can use the following dimensions for searching:</p> <ul> <li> <p>AZ - The Availability Zone. An example is <code>us-east-1a</code>.</p> </li> <li> <p>BILLING_ENTITY - The Amazon Web Services seller that your account is with. Possible values are the following:</p> <p>- Amazon Web Services(Amazon Web Services): The entity that sells Amazon Web Services services.</p> <p>- AISPL (Amazon Internet Services Pvt. Ltd.): The local Indian entity that's an acting reseller for Amazon Web Services services in India.</p> <p>- Amazon Web Services Marketplace: The entity that supports the sale of solutions that are built on Amazon Web Services by third-party software providers.</p> </li> <li> <p>CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.</p> </li> <li> <p>DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are <code>SingleAZ</code> and <code>MultiAZ</code>.</p> </li> <li> <p>DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.</p> </li> <li> <p>INSTANCE_TYPE - The type of Amazon EC2 instance. An example is <code>m4.xlarge</code>.</p> </li> <li> <p>INSTANCE_TYPE_FAMILY - A family of instance types optimized to fit different use cases. Examples are <code>Compute Optimized</code> (for example, <code>C4</code>, <code>C5</code>, <code>C6g</code>, and <code>C7g</code>), <code>Memory Optimization</code> (for example, <code>R4</code>, <code>R5n</code>, <code>R5b</code>, and <code>R6g</code>).</p> </li> <li> <p>INVOICING_ENTITY - The name of the entity that issues the Amazon Web Services invoice.</p> </li> <li> <p>LEGAL_ENTITY_NAME - The name of the organization that sells you Amazon Web Services services, such as Amazon Web Services.</p> </li> <li> <p>LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.</p> </li> <li> <p>OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.</p> </li> <li> <p>OPERATION - The action performed. Examples include <code>RunInstance</code> and <code>CreateBucket</code>.</p> </li> <li> <p>PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.</p> </li> <li> <p>PURCHASE_TYPE - The reservation type of the purchase that this usage is related to. Examples include On-Demand Instances and Standard Reserved Instances.</p> </li> <li> <p>RESERVATION_ID - The unique identifier for an Amazon Web Services Reservation Instance.</p> </li> <li> <p>SAVINGS_PLAN_ARN - The unique identifier for your Savings Plans.</p> </li> <li> <p>SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute).</p> </li> <li> <p>SERVICE - The Amazon Web Services service such as Amazon DynamoDB.</p> </li> <li> <p>TENANCY - The tenancy of a resource. Examples are shared or dedicated.</p> </li> <li> <p>USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the <code>GetDimensionValues</code> operation includes a unit attribute. Examples include GB and Hrs.</p> </li> <li> <p>USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch – Alarms. The response for this operation includes a unit attribute.</p> </li> <li> <p>REGION - The Amazon Web Services Region.</p> </li> <li> <p>RECORD_TYPE - The different types of charges such as Reserved Instance (RI) fees, usage costs, tax refunds, and credits.</p> </li> <li> <p>RESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only available for last 14 days for EC2-Compute Service.</p> </li> </ul> <p>If you set the context to <code>RESERVATIONS</code>, you can use the following dimensions for searching:</p> <ul> <li> <p>AZ - The Availability Zone. An example is <code>us-east-1a</code>.</p> </li> <li> <p>CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.</p> </li> <li> <p>DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are <code>SingleAZ</code> and <code>MultiAZ</code>.</p> </li> <li> <p>INSTANCE_TYPE - The type of Amazon EC2 instance. An example is <code>m4.xlarge</code>.</p> </li> <li> <p>LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.</p> </li> <li> <p>PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.</p> </li> <li> <p>REGION - The Amazon Web Services Region.</p> </li> <li> <p>SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.</p> </li> <li> <p>TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).</p> </li> <li> <p>TENANCY - The tenancy of a resource. Examples are shared or dedicated.</p> </li> </ul> <p>If you set the context to <code>SAVINGS_PLANS</code>, you can use the following dimensions for searching:</p> <ul> <li> <p>SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute)</p> </li> <li> <p>PAYMENT_OPTION - The payment option for the given Savings Plans (for example, All Upfront)</p> </li> <li> <p>REGION - The Amazon Web Services Region.</p> </li> <li> <p>INSTANCE_TYPE_FAMILY - The family of instances (For example, <code>m5</code>)</p> </li> <li> <p>LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.</p> </li> <li> <p>SAVINGS_PLAN_ARN - The unique identifier for your Savings Plans.</p> </li> </ul>
            sort_by: <p>The value that you want to sort the data by.</p> <p>The key represents cost and usage metrics. The following values are supported:</p> <ul> <li> <p> <code>BlendedCost</code> </p> </li> <li> <p> <code>UnblendedCost</code> </p> </li> <li> <p> <code>AmortizedCost</code> </p> </li> <li> <p> <code>NetAmortizedCost</code> </p> </li> <li> <p> <code>NetUnblendedCost</code> </p> </li> <li> <p> <code>UsageQuantity</code> </p> </li> <li> <p> <code>NormalizedUsageAmount</code> </p> </li> </ul> <p>The supported values for the <code>SortOrder</code> key are <code>ASCENDING</code> or <code>DESCENDING</code>.</p> <p>When you specify a <code>SortBy</code> paramater, the context must be <code>COST_AND_USAGE</code>. Further, when using <code>SortBy</code>, <code>NextPageToken</code> and <code>SearchString</code> aren't supported.</p>
            billing_view_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>
            max_results: <p>This field is only used when SortBy is provided in the request. The maximum number of objects that are returned for this request. If MaxResults isn't specified with SortBy, the request returns 1000 results as the default value for this parameter.</p> <p>For <code>GetDimensionValues</code>, MaxResults has an upper limit of 1000.</p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>

        Raises:
            capo_cost_explorer.errors.bill_expiration_exception.BillExpirationException: <p>The requested report expired. Update the date interval and try again.</p>
            capo_cost_explorer.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> The billing view status must be <code>HEALTHY</code> to perform this action. Try again when the status is <code>HEALTHY</code>. </p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.request_changed_exception.RequestChangedException: <p>Your request parameters changed between pages. Try again with the old parameters or without a pagination token.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_dimension_values_request.GetDimensionValuesRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_dimension_values_response.GetDimensionValuesResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_dimension_values

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_dimension_values.get_dimension_values(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_dimension_values_request.GetDimensionValuesRequest = {
            "time_period": time_period,
            "dimension": dimension,
        }
        if search_string is not None:
            input_["search_string"] = search_string
        if context is not None:
            input_["context"] = context
        if filter is not None:
            input_["filter"] = filter
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if billing_view_arn is not None:
            input_["billing_view_arn"] = billing_view_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_reservation_coverage(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        granularity: Optional[
            "capo_cost_explorer.types.granularity.Granularity"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        metrics: Optional["capo_cost_explorer.types.metric_names.MetricNames"] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definition.SortDefinition"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.max_results.MaxResults"] = None,
    ) -> "capo_cost_explorer.types.get_reservation_coverage_response.GetReservationCoverageResponse":
        """<p>Retrieves the reservation coverage for your account, which you can use to see how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon Relational Database Service, or Amazon Redshift usage is covered by a reservation. An organization's management account can see the coverage of the associated member accounts. This supports dimensions, cost categories, and nested expressions. For any time period, you can filter data about reservation usage by the following dimensions:</p> <ul> <li> <p>AZ</p> </li> <li> <p>CACHE_ENGINE</p> </li> <li> <p>DATABASE_ENGINE</p> </li> <li> <p>DEPLOYMENT_OPTION</p> </li> <li> <p>INSTANCE_TYPE</p> </li> <li> <p>LINKED_ACCOUNT</p> </li> <li> <p>OPERATING_SYSTEM</p> </li> <li> <p>PLATFORM</p> </li> <li> <p>REGION</p> </li> <li> <p>SERVICE</p> </li> <li> <p>TAG</p> </li> <li> <p>TENANCY</p> </li> </ul> <p>To determine valid values for a dimension, use the <code>GetDimensionValues</code> operation. </p>

        Args:
            time_period: <p>The start and end dates of the period that you want to retrieve data about reservation coverage for. You can retrieve data for a maximum of 13 months: the last 12 months and the current month. The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>. </p>
            group_by: <p>You can group the data by the following attributes:</p> <ul> <li> <p>AZ</p> </li> <li> <p>CACHE_ENGINE</p> </li> <li> <p>DATABASE_ENGINE</p> </li> <li> <p>DEPLOYMENT_OPTION</p> </li> <li> <p>INSTANCE_TYPE</p> </li> <li> <p>INVOICING_ENTITY</p> </li> <li> <p>LINKED_ACCOUNT</p> </li> <li> <p>OPERATING_SYSTEM</p> </li> <li> <p>PLATFORM</p> </li> <li> <p>REGION</p> </li> <li> <p>TENANCY</p> </li> </ul>
            granularity: <p>The granularity of the Amazon Web Services cost data for the reservation. Valid values are <code>MONTHLY</code> and <code>DAILY</code>.</p> <p>If <code>GroupBy</code> is set, <code>Granularity</code> can't be set. If <code>Granularity</code> isn't set, the response object doesn't include <code>Granularity</code>, either <code>MONTHLY</code> or <code>DAILY</code>.</p> <p>The <code>GetReservationCoverage</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>
            filter: <p>Filters utilization data by dimensions. You can filter by the following dimensions:</p> <ul> <li> <p>AZ</p> </li> <li> <p>CACHE_ENGINE</p> </li> <li> <p>DATABASE_ENGINE</p> </li> <li> <p>DEPLOYMENT_OPTION</p> </li> <li> <p>INSTANCE_TYPE</p> </li> <li> <p>LINKED_ACCOUNT</p> </li> <li> <p>OPERATING_SYSTEM</p> </li> <li> <p>PLATFORM</p> </li> <li> <p>REGION</p> </li> <li> <p>SERVICE</p> </li> <li> <p>TAG</p> </li> <li> <p>TENANCY</p> </li> </ul> <p> <code>GetReservationCoverage</code> uses the same <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object as the other operations, but only <code>AND</code> is supported among each dimension. You can nest only one level deep. If there are multiple values for a dimension, they are OR'd together.</p> <p>If you don't provide a <code>SERVICE</code> filter, Cost Explorer defaults to EC2.</p> <p>Cost category is also supported.</p>
            metrics: <p>The measurement that you want your reservation coverage reported in.</p> <p>Valid values are <code>Hour</code>, <code>Unit</code>, and <code>Cost</code>. You can use multiple values in a request.</p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>
            sort_by: <p>The value by which you want to sort the data.</p> <p>The following values are supported for <code>Key</code>:</p> <ul> <li> <p> <code>OnDemandCost</code> </p> </li> <li> <p> <code>CoverageHoursPercentage</code> </p> </li> <li> <p> <code>OnDemandHours</code> </p> </li> <li> <p> <code>ReservedHours</code> </p> </li> <li> <p> <code>TotalRunningHours</code> </p> </li> <li> <p> <code>CoverageNormalizedUnitsPercentage</code> </p> </li> <li> <p> <code>OnDemandNormalizedUnits</code> </p> </li> <li> <p> <code>ReservedNormalizedUnits</code> </p> </li> <li> <p> <code>TotalRunningNormalizedUnits</code> </p> </li> <li> <p> <code>Time</code> </p> </li> </ul> <p>Supported values for <code>SortOrder</code> are <code>ASCENDING</code> or <code>DESCENDING</code>.</p>
            max_results: <p>The maximum number of objects that you returned for this request. If more objects are available, in the response, Amazon Web Services provides a NextPageToken value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_reservation_coverage_request.GetReservationCoverageRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_reservation_coverage_response.GetReservationCoverageResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_reservation_coverage

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_reservation_coverage.get_reservation_coverage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_reservation_coverage_request.GetReservationCoverageRequest = {
            "time_period": time_period
        }
        if group_by is not None:
            input_["group_by"] = group_by
        if granularity is not None:
            input_["granularity"] = granularity
        if filter is not None:
            input_["filter"] = filter
        if metrics is not None:
            input_["metrics"] = metrics
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_reservation_purchase_recommendation(
        self,
        service: "capo_cost_explorer.types.generic_string.GenericString",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        account_id: Optional[
            "capo_cost_explorer.types.generic_string.GenericString"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        account_scope: Optional[
            "capo_cost_explorer.types.account_scope.AccountScope"
        ] = None,
        lookback_period_in_days: Optional[
            "capo_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
        ] = None,
        term_in_years: Optional[
            "capo_cost_explorer.types.term_in_years.TermInYears"
        ] = None,
        payment_option: Optional[
            "capo_cost_explorer.types.payment_option.PaymentOption"
        ] = None,
        service_specification: Optional[
            "capo_cost_explorer.types.service_specification.ServiceSpecification"
        ] = None,
        page_size: Optional[
            "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.get_reservation_purchase_recommendation_response.GetReservationPurchaseRecommendationResponse":
        """<p>Gets recommendations for reservation purchases. These recommendations might help you to reduce your costs. Reservations provide a discounted hourly rate (up to 75%) compared to On-Demand pricing.</p> <p>Amazon Web Services generates your recommendations by identifying your On-Demand usage during a specific time period and collecting your usage into categories that are eligible for a reservation. After Amazon Web Services has these categories, it simulates every combination of reservations in each category of usage to identify the best number of each type of Reserved Instance (RI) to purchase to maximize your estimated savings. </p> <p>For example, Amazon Web Services automatically aggregates your Amazon EC2 Linux, shared tenancy, and c4 family usage in the US West (Oregon) Region and recommends that you buy size-flexible regional reservations to apply to the c4 family usage. Amazon Web Services recommends the smallest size instance in an instance family. This makes it easier to purchase a size-flexible Reserved Instance (RI). Amazon Web Services also shows the equal number of normalized units. This way, you can purchase any instance size that you want. For this example, your RI recommendation is for <code>c4.large</code> because that is the smallest size instance in the c4 instance family.</p>

        Args:
            account_id: <p>The account ID that's associated with the recommendation. </p>
            service: <p>The specific service that you want recommendations for.</p>
            account_scope: <p>The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to <code>PAYER</code>. If the value is <code>LINKED</code>, recommendations are calculated for individual member accounts only.</p>
            lookback_period_in_days: <p>The number of previous days that you want Amazon Web Services to consider when it calculates your recommendations.</p>
            term_in_years: <p>The reservation term that you want recommendations for.</p>
            payment_option: <p>The reservation purchase option that you want recommendations for.</p>
            service_specification: <p>The hardware specifications for the service instances that you want recommendations for, such as standard or convertible Amazon EC2 instances.</p>
            page_size: <p>The number of recommendations that you want returned in a single response object.</p>
            next_page_token: <p>The pagination token that indicates the next set of results that you want to retrieve.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_reservation_purchase_recommendation_request.GetReservationPurchaseRecommendationRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_reservation_purchase_recommendation_response.GetReservationPurchaseRecommendationResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_reservation_purchase_recommendation

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_reservation_purchase_recommendation.get_reservation_purchase_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_reservation_purchase_recommendation_request.GetReservationPurchaseRecommendationRequest = {
            "service": service
        }
        if account_id is not None:
            input_["account_id"] = account_id
        if filter is not None:
            input_["filter"] = filter
        if account_scope is not None:
            input_["account_scope"] = account_scope
        if lookback_period_in_days is not None:
            input_["lookback_period_in_days"] = lookback_period_in_days
        if term_in_years is not None:
            input_["term_in_years"] = term_in_years
        if payment_option is not None:
            input_["payment_option"] = payment_option
        if service_specification is not None:
            input_["service_specification"] = service_specification
        if page_size is not None:
            input_["page_size"] = page_size
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_reservation_purchase_recommendation(
        self,
        service: "capo_cost_explorer.types.generic_string.GenericString",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        account_id: Optional[
            "capo_cost_explorer.types.generic_string.GenericString"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        account_scope: Optional[
            "capo_cost_explorer.types.account_scope.AccountScope"
        ] = None,
        lookback_period_in_days: Optional[
            "capo_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
        ] = None,
        term_in_years: Optional[
            "capo_cost_explorer.types.term_in_years.TermInYears"
        ] = None,
        payment_option: Optional[
            "capo_cost_explorer.types.payment_option.PaymentOption"
        ] = None,
        service_specification: Optional[
            "capo_cost_explorer.types.service_specification.ServiceSpecification"
        ] = None,
        page_size: Optional[
            "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.reservation_purchase_recommendation.ReservationPurchaseRecommendation]":
        _token = next_page_token
        while True:
            _response = self.get_reservation_purchase_recommendation(
                service,
                config_overrides=config_overrides,
                account_id=account_id,
                filter=filter,
                account_scope=account_scope,
                lookback_period_in_days=lookback_period_in_days,
                term_in_years=term_in_years,
                payment_option=payment_option,
                service_specification=service_specification,
                page_size=page_size,
                next_page_token=_token,
            )
            _page = _resolve_path(_response, ("recommendations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def get_reservation_utilization(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        granularity: Optional[
            "capo_cost_explorer.types.granularity.Granularity"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definition.SortDefinition"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.max_results.MaxResults"] = None,
    ) -> "capo_cost_explorer.types.get_reservation_utilization_response.GetReservationUtilizationResponse":
        """<p>Retrieves the reservation utilization for your account. Management account in an organization have access to member accounts. You can filter data by dimensions in a time period. You can use <code>GetDimensionValues</code> to determine the possible dimension values. Currently, you can group only by <code>SUBSCRIPTION_ID</code>. </p>

        Args:
            time_period: <p>Sets the start and end dates for retrieving Reserved Instance (RI) utilization. The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>. </p>
            group_by: <p>Groups only by <code>SUBSCRIPTION_ID</code>. Metadata is included.</p>
            granularity: <p>If <code>GroupBy</code> is set, <code>Granularity</code> can't be set. If <code>Granularity</code> isn't set, the response object doesn't include <code>Granularity</code>, either <code>MONTHLY</code> or <code>DAILY</code>. If both <code>GroupBy</code> and <code>Granularity</code> aren't set, <code>GetReservationUtilization</code> defaults to <code>DAILY</code>.</p> <p>The <code>GetReservationUtilization</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>
            filter: <p>Filters utilization data by dimensions. You can filter by the following dimensions:</p> <ul> <li> <p>AZ</p> </li> <li> <p>CACHE_ENGINE</p> </li> <li> <p>DEPLOYMENT_OPTION</p> </li> <li> <p>INSTANCE_TYPE</p> </li> <li> <p>LINKED_ACCOUNT</p> </li> <li> <p>OPERATING_SYSTEM</p> </li> <li> <p>PLATFORM</p> </li> <li> <p>REGION</p> </li> <li> <p>SERVICE</p> <note> <p>If not specified, the <code>SERVICE</code> filter defaults to Amazon Elastic Compute Cloud - Compute. Supported values for <code>SERVICE</code> are Amazon Elastic Compute Cloud - Compute, Amazon Relational Database Service, Amazon ElastiCache, Amazon Redshift, and Amazon Elasticsearch Service. The value for the <code>SERVICE</code> filter should not exceed "1".</p> </note> </li> <li> <p>SCOPE</p> </li> <li> <p>TENANCY</p> </li> </ul> <p> <code>GetReservationUtilization</code> uses the same <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object as the other operations, but only <code>AND</code> is supported among each dimension, and nesting is supported up to only one level deep. If there are multiple values for a dimension, they are OR'd together.</p>
            sort_by: <p>The value that you want to sort the data by.</p> <p>The following values are supported for <code>Key</code>:</p> <ul> <li> <p> <code>UtilizationPercentage</code> </p> </li> <li> <p> <code>UtilizationPercentageInUnits</code> </p> </li> <li> <p> <code>PurchasedHours</code> </p> </li> <li> <p> <code>PurchasedUnits</code> </p> </li> <li> <p> <code>TotalActualHours</code> </p> </li> <li> <p> <code>TotalActualUnits</code> </p> </li> <li> <p> <code>UnusedHours</code> </p> </li> <li> <p> <code>UnusedUnits</code> </p> </li> <li> <p> <code>OnDemandCostOfRIHoursUsed</code> </p> </li> <li> <p> <code>NetRISavings</code> </p> </li> <li> <p> <code>TotalPotentialRISavings</code> </p> </li> <li> <p> <code>AmortizedUpfrontFee</code> </p> </li> <li> <p> <code>AmortizedRecurringFee</code> </p> </li> <li> <p> <code>TotalAmortizedFee</code> </p> </li> <li> <p> <code>RICostForUnusedHours</code> </p> </li> <li> <p> <code>RealizedSavings</code> </p> </li> <li> <p> <code>UnrealizedSavings</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>
            max_results: <p>The maximum number of objects that you returned for this request. If more objects are available, in the response, Amazon Web Services provides a NextPageToken value that you can use in a subsequent call to get the next batch of objects.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_reservation_utilization_request.GetReservationUtilizationRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_reservation_utilization_response.GetReservationUtilizationResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_reservation_utilization

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_reservation_utilization.get_reservation_utilization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_reservation_utilization_request.GetReservationUtilizationRequest = {
            "time_period": time_period
        }
        if group_by is not None:
            input_["group_by"] = group_by
        if granularity is not None:
            input_["granularity"] = granularity
        if filter is not None:
            input_["filter"] = filter
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_rightsizing_recommendation(
        self,
        service: "capo_cost_explorer.types.generic_string.GenericString",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        configuration: Optional[
            "capo_cost_explorer.types.rightsizing_recommendation_configuration.RightsizingRecommendationConfiguration"
        ] = None,
        page_size: Optional[
            "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.get_rightsizing_recommendation_response.GetRightsizingRecommendationResponse":
        """<p>Creates recommendations that help you save cost by identifying idle and underutilized Amazon EC2 instances.</p> <p>Recommendations are generated to either downsize or terminate instances, along with providing savings detail and metrics. For more information about calculation and function, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-rightsizing.html">Optimizing Your Cost with Rightsizing Recommendations</a> in the <i>Billing and Cost Management User Guide</i>.</p>

        Args:
            configuration: <p>You can use Configuration to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings that are associated with recommendations with consideration of existing Savings Plans or RI benefits, or neither. </p>
            service: <p>The specific service that you want recommendations for. The only valid value for <code>GetRightsizingRecommendation</code> is "<code>AmazonEC2</code>".</p>
            page_size: <p>The number of recommendations that you want returned in a single response object.</p>
            next_page_token: <p>The pagination token that indicates the next set of results that you want to retrieve.</p>

        Raises:
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_rightsizing_recommendation_request.GetRightsizingRecommendationRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_rightsizing_recommendation_response.GetRightsizingRecommendationResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_rightsizing_recommendation

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_rightsizing_recommendation.get_rightsizing_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_rightsizing_recommendation_request.GetRightsizingRecommendationRequest = {
            "service": service
        }
        if filter is not None:
            input_["filter"] = filter
        if configuration is not None:
            input_["configuration"] = configuration
        if page_size is not None:
            input_["page_size"] = page_size
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_rightsizing_recommendation(
        self,
        service: "capo_cost_explorer.types.generic_string.GenericString",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        configuration: Optional[
            "capo_cost_explorer.types.rightsizing_recommendation_configuration.RightsizingRecommendationConfiguration"
        ] = None,
        page_size: Optional[
            "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.rightsizing_recommendation.RightsizingRecommendation]":
        _token = next_page_token
        while True:
            _response = self.get_rightsizing_recommendation(
                service,
                config_overrides=config_overrides,
                filter=filter,
                configuration=configuration,
                page_size=page_size,
                next_page_token=_token,
            )
            _page = _resolve_path(_response, ("rightsizing_recommendations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def get_savings_plan_purchase_recommendation_details(
        self,
        recommendation_detail_id: "capo_cost_explorer.types.recommendation_detail_id.RecommendationDetailId",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.get_savings_plan_purchase_recommendation_details_response.GetSavingsPlanPurchaseRecommendationDetailsResponse":
        """<p>Retrieves the details for a Savings Plan recommendation. These details include the hourly data-points that construct the cost, coverage, and utilization charts.</p>

        Args:
            recommendation_detail_id: <p>The ID that is associated with the Savings Plan recommendation.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_savings_plan_purchase_recommendation_details_request.GetSavingsPlanPurchaseRecommendationDetailsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_savings_plan_purchase_recommendation_details_response.GetSavingsPlanPurchaseRecommendationDetailsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_savings_plan_purchase_recommendation_details

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_savings_plan_purchase_recommendation_details.get_savings_plan_purchase_recommendation_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_savings_plan_purchase_recommendation_details_request.GetSavingsPlanPurchaseRecommendationDetailsRequest = {
            "recommendation_detail_id": recommendation_detail_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_savings_plans_coverage(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        granularity: Optional[
            "capo_cost_explorer.types.granularity.Granularity"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        metrics: Optional["capo_cost_explorer.types.metric_names.MetricNames"] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.max_results.MaxResults"] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definition.SortDefinition"
        ] = None,
    ) -> "capo_cost_explorer.types.get_savings_plans_coverage_response.GetSavingsPlansCoverageResponse":
        """<p>Retrieves the Savings Plans covered for your account. This enables you to see how much of your cost is covered by a Savings Plan. An organization’s management account can see the coverage of the associated member accounts. This supports dimensions, cost categories, and nested expressions. For any time period, you can filter data for Savings Plans usage with the following dimensions:</p> <ul> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>SERVICE</code> </p> </li> <li> <p> <code>INSTANCE_FAMILY</code> </p> </li> </ul> <p>To determine valid values for a dimension, use the <code>GetDimensionValues</code> operation.</p>

        Args:
            time_period: <p>The time period that you want the usage and costs for. The <code>Start</code> date must be within 13 months. The <code>End</code> date must be after the <code>Start</code> date, and before the current date. Future dates can't be used as an <code>End</code> date.</p>
            group_by: <p>You can group the data using the attributes <code>INSTANCE_FAMILY</code>, <code>REGION</code>, or <code>SERVICE</code>.</p>
            granularity: <p>The granularity of the Amazon Web Services cost data for your Savings Plans. <code>Granularity</code> can't be set if <code>GroupBy</code> is set.</p> <p>The <code>GetSavingsPlansCoverage</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>
            filter: <p>Filters Savings Plans coverage data by dimensions. You can filter data for Savings Plans usage with the following dimensions:</p> <ul> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>SERVICE</code> </p> </li> <li> <p> <code>INSTANCE_FAMILY</code> </p> </li> </ul> <p> <code>GetSavingsPlansCoverage</code> uses the same <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object as the other operations, but only <code>AND</code> is supported among each dimension. If there are multiple values for a dimension, they are OR'd together.</p> <p>Cost category is also supported.</p>
            metrics: <p>The measurement that you want your Savings Plans coverage reported in. The only valid value is <code>SpendCoveredBySavingsPlans</code>.</p>
            next_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>
            max_results: <p>The number of items to be returned in a response. The default is <code>20</code>, with a minimum value of <code>1</code>.</p>
            sort_by: <p>The value that you want to sort the data by.</p> <p>The following values are supported for <code>Key</code>:</p> <ul> <li> <p> <code>SpendCoveredBySavingsPlan</code> </p> </li> <li> <p> <code>OnDemandCost</code> </p> </li> <li> <p> <code>CoveragePercentage</code> </p> </li> <li> <p> <code>TotalCost</code> </p> </li> <li> <p> <code>InstanceFamily</code> </p> </li> <li> <p> <code>Region</code> </p> </li> <li> <p> <code>Service</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_savings_plans_coverage_request.GetSavingsPlansCoverageRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_savings_plans_coverage_response.GetSavingsPlansCoverageResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_savings_plans_coverage

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_savings_plans_coverage.get_savings_plans_coverage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_savings_plans_coverage_request.GetSavingsPlansCoverageRequest = {
            "time_period": time_period
        }
        if group_by is not None:
            input_["group_by"] = group_by
        if granularity is not None:
            input_["granularity"] = granularity
        if filter is not None:
            input_["filter"] = filter
        if metrics is not None:
            input_["metrics"] = metrics
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_savings_plans_coverage(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        group_by: Optional[
            "capo_cost_explorer.types.group_definitions.GroupDefinitions"
        ] = None,
        granularity: Optional[
            "capo_cost_explorer.types.granularity.Granularity"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        metrics: Optional["capo_cost_explorer.types.metric_names.MetricNames"] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.max_results.MaxResults"] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definition.SortDefinition"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.get_savings_plans_coverage_response.GetSavingsPlansCoverageResponse]":
        _token = next_token
        while True:
            _response = self.get_savings_plans_coverage(
                time_period,
                config_overrides=config_overrides,
                group_by=group_by,
                granularity=granularity,
                filter=filter,
                metrics=metrics,
                next_token=_token,
                max_results=max_results,
                sort_by=sort_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_savings_plans_purchase_recommendation(
        self,
        savings_plans_type: "capo_cost_explorer.types.supported_savings_plans_type.SupportedSavingsPlansType",
        term_in_years: "capo_cost_explorer.types.term_in_years.TermInYears",
        payment_option: "capo_cost_explorer.types.payment_option.PaymentOption",
        lookback_period_in_days: "capo_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        account_scope: Optional[
            "capo_cost_explorer.types.account_scope.AccountScope"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        page_size: Optional[
            "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
    ) -> "capo_cost_explorer.types.get_savings_plans_purchase_recommendation_response.GetSavingsPlansPurchaseRecommendationResponse":
        """<p>Retrieves the Savings Plans recommendations for your account. First use <code>StartSavingsPlansPurchaseRecommendationGeneration</code> to generate a new set of recommendations, and then use <code>GetSavingsPlansPurchaseRecommendation</code> to retrieve them.</p>

        Args:
            savings_plans_type: <p>The Savings Plans recommendation type that's requested.</p>
            term_in_years: <p>The savings plan recommendation term that's used to generate these recommendations.</p>
            payment_option: <p>The payment option that's used to generate these recommendations.</p>
            account_scope: <p>The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to <code>PAYER</code>. If the value is <code>LINKED</code>, recommendations are calculated for individual member accounts only.</p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>
            page_size: <p>The number of recommendations that you want returned in a single response object.</p>
            lookback_period_in_days: <p>The lookback period that's used to generate the recommendation.</p>
            filter: <p>You can filter your recommendations by Account ID with the <code>LINKED_ACCOUNT</code> dimension. To filter your recommendations by Account ID, specify <code>Key</code> as <code>LINKED_ACCOUNT</code> and <code>Value</code> as the comma-separated Acount ID(s) that you want to see Savings Plans purchase recommendations for.</p> <p>For GetSavingsPlansPurchaseRecommendation, the <code>Filter</code> doesn't include <code>CostCategories</code> or <code>Tags</code>. It only includes <code>Dimensions</code>. With <code>Dimensions</code>, <code>Key</code> must be <code>LINKED_ACCOUNT</code> and <code>Value</code> can be a single Account ID or multiple comma-separated Account IDs that you want to see Savings Plans Purchase Recommendations for. <code>AND</code> and <code>OR</code> operators are not supported.</p>

        Raises:
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_savings_plans_purchase_recommendation_request.GetSavingsPlansPurchaseRecommendationRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_savings_plans_purchase_recommendation_response.GetSavingsPlansPurchaseRecommendationResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_savings_plans_purchase_recommendation

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_savings_plans_purchase_recommendation.get_savings_plans_purchase_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_savings_plans_purchase_recommendation_request.GetSavingsPlansPurchaseRecommendationRequest = {
            "savings_plans_type": savings_plans_type,
            "term_in_years": term_in_years,
            "payment_option": payment_option,
            "lookback_period_in_days": lookback_period_in_days,
        }
        if account_scope is not None:
            input_["account_scope"] = account_scope
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if page_size is not None:
            input_["page_size"] = page_size
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_savings_plans_utilization(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        granularity: Optional[
            "capo_cost_explorer.types.granularity.Granularity"
        ] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definition.SortDefinition"
        ] = None,
    ) -> "capo_cost_explorer.types.get_savings_plans_utilization_response.GetSavingsPlansUtilizationResponse":
        """<p>Retrieves the Savings Plans utilization for your account across date ranges with daily or monthly granularity. Management account in an organization have access to member accounts. You can use <code>GetDimensionValues</code> in <code>SAVINGS_PLANS</code> to determine the possible dimension values.</p> <note> <p>You can't group by any dimension values for <code>GetSavingsPlansUtilization</code>.</p> </note>

        Args:
            time_period: <p>The time period that you want the usage and costs for. The <code>Start</code> date must be within 13 months. The <code>End</code> date must be after the <code>Start</code> date, and before the current date. Future dates can't be used as an <code>End</code> date.</p>
            granularity: <p>The granularity of the Amazon Web Services utillization data for your Savings Plans.</p> <p>The <code>GetSavingsPlansUtilization</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>
            filter: <p>Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can filter data with the following dimensions:</p> <ul> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>SAVINGS_PLAN_ARN</code> </p> </li> <li> <p> <code>SAVINGS_PLANS_TYPE</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>PAYMENT_OPTION</code> </p> </li> <li> <p> <code>INSTANCE_TYPE_FAMILY</code> </p> </li> </ul> <p> <code>GetSavingsPlansUtilization</code> uses the same <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object as the other operations, but only <code>AND</code> is supported among each dimension.</p>
            sort_by: <p>The value that you want to sort the data by.</p> <p>The following values are supported for <code>Key</code>:</p> <ul> <li> <p> <code>UtilizationPercentage</code> </p> </li> <li> <p> <code>TotalCommitment</code> </p> </li> <li> <p> <code>UsedCommitment</code> </p> </li> <li> <p> <code>UnusedCommitment</code> </p> </li> <li> <p> <code>NetSavings</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_savings_plans_utilization_request.GetSavingsPlansUtilizationRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_savings_plans_utilization_response.GetSavingsPlansUtilizationResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_savings_plans_utilization

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_savings_plans_utilization.get_savings_plans_utilization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_savings_plans_utilization_request.GetSavingsPlansUtilizationRequest = {
            "time_period": time_period
        }
        if granularity is not None:
            input_["granularity"] = granularity
        if filter is not None:
            input_["filter"] = filter
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_savings_plans_utilization_details(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        data_type: Optional[
            "capo_cost_explorer.types.savings_plans_data_types.SavingsPlansDataTypes"
        ] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.max_results.MaxResults"] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definition.SortDefinition"
        ] = None,
    ) -> "capo_cost_explorer.types.get_savings_plans_utilization_details_response.GetSavingsPlansUtilizationDetailsResponse":
        """<p>Retrieves attribute data along with aggregate utilization and savings data for a given time period. This doesn't support granular or grouped data (daily/monthly) in response. You can't retrieve data by dates in a single response similar to <code>GetSavingsPlanUtilization</code>, but you have the option to make multiple calls to <code>GetSavingsPlanUtilizationDetails</code> by providing individual dates. You can use <code>GetDimensionValues</code> in <code>SAVINGS_PLANS</code> to determine the possible dimension values.</p> <note> <p> <code>GetSavingsPlanUtilizationDetails</code> internally groups data by <code>SavingsPlansArn</code>.</p> </note>

        Args:
            time_period: <p>The time period that you want the usage and costs for. The <code>Start</code> date must be within 13 months. The <code>End</code> date must be after the <code>Start</code> date, and before the current date. Future dates can't be used as an <code>End</code> date.</p>
            filter: <p>Filters Savings Plans utilization coverage data for active Savings Plans dimensions. You can filter data with the following dimensions:</p> <ul> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>SAVINGS_PLAN_ARN</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>PAYMENT_OPTION</code> </p> </li> <li> <p> <code>INSTANCE_TYPE_FAMILY</code> </p> </li> </ul> <p> <code>GetSavingsPlansUtilizationDetails</code> uses the same <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object as the other operations, but only <code>AND</code> is supported among each dimension.</p>
            data_type: <p>The data type.</p>
            next_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>
            max_results: <p>The number of items to be returned in a response. The default is <code>20</code>, with a minimum value of <code>1</code>.</p>
            sort_by: <p>The value that you want to sort the data by.</p> <p>The following values are supported for <code>Key</code>:</p> <ul> <li> <p> <code>UtilizationPercentage</code> </p> </li> <li> <p> <code>TotalCommitment</code> </p> </li> <li> <p> <code>UsedCommitment</code> </p> </li> <li> <p> <code>UnusedCommitment</code> </p> </li> <li> <p> <code>NetSavings</code> </p> </li> <li> <p> <code>AmortizedRecurringCommitment</code> </p> </li> <li> <p> <code>AmortizedUpfrontCommitment</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_savings_plans_utilization_details_request.GetSavingsPlansUtilizationDetailsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_savings_plans_utilization_details_response.GetSavingsPlansUtilizationDetailsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_savings_plans_utilization_details

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_savings_plans_utilization_details.get_savings_plans_utilization_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_savings_plans_utilization_details_request.GetSavingsPlansUtilizationDetailsRequest = {
            "time_period": time_period
        }
        if filter is not None:
            input_["filter"] = filter
        if data_type is not None:
            input_["data_type"] = data_type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_savings_plans_utilization_details(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        data_type: Optional[
            "capo_cost_explorer.types.savings_plans_data_types.SavingsPlansDataTypes"
        ] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.max_results.MaxResults"] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definition.SortDefinition"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.get_savings_plans_utilization_details_response.GetSavingsPlansUtilizationDetailsResponse]":
        _token = next_token
        while True:
            _response = self.get_savings_plans_utilization_details(
                time_period,
                config_overrides=config_overrides,
                filter=filter,
                data_type=data_type,
                next_token=_token,
                max_results=max_results,
                sort_by=sort_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_tags(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        search_string: Optional[
            "capo_cost_explorer.types.search_string.SearchString"
        ] = None,
        tag_key: Optional["capo_cost_explorer.types.tag_key.TagKey"] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        sort_by: Optional[
            "capo_cost_explorer.types.sort_definitions.SortDefinitions"
        ] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        max_results: Optional["capo_cost_explorer.types.max_results.MaxResults"] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.get_tags_response.GetTagsResponse":
        """<p>Queries for available tag keys and tag values for a specified period. You can search the tag values for an arbitrary string. </p>

        Args:
            search_string: <p>The value that you want to search for.</p>
            time_period: <p>The start and end dates for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>.</p>
            tag_key: <p>The key of the tag that you want to return values for.</p>
            sort_by: <p>The value that you want to sort the data by.</p> <p>The key represents cost and usage metrics. The following values are supported:</p> <ul> <li> <p> <code>BlendedCost</code> </p> </li> <li> <p> <code>UnblendedCost</code> </p> </li> <li> <p> <code>AmortizedCost</code> </p> </li> <li> <p> <code>NetAmortizedCost</code> </p> </li> <li> <p> <code>NetUnblendedCost</code> </p> </li> <li> <p> <code>UsageQuantity</code> </p> </li> <li> <p> <code>NormalizedUsageAmount</code> </p> </li> </ul> <p>The supported values for <code>SortOrder</code> are <code>ASCENDING</code> and <code>DESCENDING</code>.</p> <p>When you use <code>SortBy</code>, <code>NextPageToken</code> and <code>SearchString</code> aren't supported.</p>
            billing_view_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>
            max_results: <p>This field is only used when SortBy is provided in the request. The maximum number of objects that are returned for this request. If MaxResults isn't specified with SortBy, the request returns 1000 results as the default value for this parameter.</p> <p>For <code>GetTags</code>, MaxResults has an upper quota of 1000.</p>
            next_page_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>

        Raises:
            capo_cost_explorer.errors.bill_expiration_exception.BillExpirationException: <p>The requested report expired. Update the date interval and try again.</p>
            capo_cost_explorer.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> The billing view status must be <code>HEALTHY</code> to perform this action. Try again when the status is <code>HEALTHY</code>. </p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.request_changed_exception.RequestChangedException: <p>Your request parameters changed between pages. Try again with the old parameters or without a pagination token.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_tags_request.GetTagsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_tags_response.GetTagsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_tags

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_tags.get_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_tags_request.GetTagsRequest = {
            "time_period": time_period
        }
        if search_string is not None:
            input_["search_string"] = search_string
        if tag_key is not None:
            input_["tag_key"] = tag_key
        if filter is not None:
            input_["filter"] = filter
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if billing_view_arn is not None:
            input_["billing_view_arn"] = billing_view_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_usage_forecast(
        self,
        time_period: "capo_cost_explorer.types.date_interval.DateInterval",
        metric: "capo_cost_explorer.types.metric.Metric",
        granularity: "capo_cost_explorer.types.granularity.Granularity",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        filter: Optional["capo_cost_explorer.types.expression.Expression"] = None,
        billing_view_arn: Optional[
            "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
        ] = None,
        prediction_interval_level: Optional[
            "capo_cost_explorer.types.prediction_interval_level.PredictionIntervalLevel"
        ] = None,
    ) -> (
        "capo_cost_explorer.types.get_usage_forecast_response.GetUsageForecastResponse"
    ):
        """<p>Retrieves a forecast for how much Amazon Web Services predicts that you will use over the forecast time period that you select, based on your past usage. </p>

        Args:
            time_period: <p>The start and end dates of the period that you want to retrieve usage forecast for. The start date is included in the period, but the end date isn't included in the period. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>. The start date must be equal to or later than the current date to avoid a validation error.</p>
            metric: <p>Which metric Cost Explorer uses to create your forecast.</p> <p>Valid values for a <code>GetUsageForecast</code> call are the following:</p> <ul> <li> <p>USAGE_QUANTITY</p> </li> <li> <p>NORMALIZED_USAGE_AMOUNT</p> </li> </ul>
            granularity: <p>How granular you want the forecast to be. You can get 3 months of <code>DAILY</code> forecasts or 18 months of <code>MONTHLY</code> forecasts.</p> <p>The <code>GetUsageForecast</code> operation supports only <code>DAILY</code> and <code>MONTHLY</code> granularities.</p>
            filter: <p>The filters that you want to use to filter your forecast. The <code>GetUsageForecast</code> API supports filtering by the following dimensions:</p> <ul> <li> <p> <code>AZ</code> </p> </li> <li> <p> <code>INSTANCE_TYPE</code> </p> </li> <li> <p> <code>LINKED_ACCOUNT</code> </p> </li> <li> <p> <code>LINKED_ACCOUNT_NAME</code> </p> </li> <li> <p> <code>OPERATION</code> </p> </li> <li> <p> <code>PURCHASE_TYPE</code> </p> </li> <li> <p> <code>REGION</code> </p> </li> <li> <p> <code>SERVICE</code> </p> </li> <li> <p> <code>USAGE_TYPE</code> </p> </li> <li> <p> <code>USAGE_TYPE_GROUP</code> </p> </li> <li> <p> <code>RECORD_TYPE</code> </p> </li> <li> <p> <code>OPERATING_SYSTEM</code> </p> </li> <li> <p> <code>TENANCY</code> </p> </li> <li> <p> <code>SCOPE</code> </p> </li> <li> <p> <code>PLATFORM</code> </p> </li> <li> <p> <code>SUBSCRIPTION_ID</code> </p> </li> <li> <p> <code>LEGAL_ENTITY_NAME</code> </p> </li> <li> <p> <code>DEPLOYMENT_OPTION</code> </p> </li> <li> <p> <code>DATABASE_ENGINE</code> </p> </li> <li> <p> <code>INSTANCE_TYPE_FAMILY</code> </p> </li> <li> <p> <code>BILLING_ENTITY</code> </p> </li> <li> <p> <code>RESERVATION_ID</code> </p> </li> <li> <p> <code>SAVINGS_PLAN_ARN</code> </p> </li> </ul>
            billing_view_arn: <p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>
            prediction_interval_level: <p>Amazon Web Services Cost Explorer always returns the mean forecast as a single point. You can request a prediction interval around the mean by specifying a confidence level. The higher the confidence level, the more confident Cost Explorer is about the actual value falling in the prediction interval. Higher confidence levels result in wider prediction intervals.</p>

        Raises:
            capo_cost_explorer.errors.billing_view_health_status_exception.BillingViewHealthStatusException: <p> The billing view status must be <code>HEALTHY</code> to perform this action. Try again when the status is <code>HEALTHY</code>. </p>
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.unresolvable_usage_unit_exception.UnresolvableUsageUnitException: <p>Cost Explorer was unable to identify the usage unit. Provide <code>UsageType/UsageTypeGroup</code> filter selections that contain matching units, for example: <code>hours</code>.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.get_usage_forecast_request.GetUsageForecastRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.get_usage_forecast_response.GetUsageForecastResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.get_usage_forecast

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.get_usage_forecast.get_usage_forecast(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.get_usage_forecast_request.GetUsageForecastRequest = {
            "time_period": time_period,
            "metric": metric,
            "granularity": granularity,
        }
        if filter is not None:
            input_["filter"] = filter
        if billing_view_arn is not None:
            input_["billing_view_arn"] = billing_view_arn
        if prediction_interval_level is not None:
            input_["prediction_interval_level"] = prediction_interval_level

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_commitment_purchase_analyses(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        analysis_status: Optional[
            "capo_cost_explorer.types.analysis_status.AnalysisStatus"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        page_size: Optional[
            "capo_cost_explorer.types.analyses_page_size.AnalysesPageSize"
        ] = None,
        analysis_ids: Optional[
            "capo_cost_explorer.types.analysis_ids.AnalysisIds"
        ] = None,
    ) -> "capo_cost_explorer.types.list_commitment_purchase_analyses_response.ListCommitmentPurchaseAnalysesResponse":
        """<p>Lists the commitment purchase analyses for your account.</p>

        Args:
            analysis_status: <p>The status of the analysis.</p>
            next_page_token: <p>The token to retrieve the next set of results.</p>
            page_size: <p>The number of analyses that you want returned in a single response object.</p>
            analysis_ids: <p>The analysis IDs associated with the commitment purchase analyses.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.list_commitment_purchase_analyses_request.ListCommitmentPurchaseAnalysesRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.list_commitment_purchase_analyses_response.ListCommitmentPurchaseAnalysesResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.list_commitment_purchase_analyses

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.list_commitment_purchase_analyses.list_commitment_purchase_analyses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.list_commitment_purchase_analyses_request.ListCommitmentPurchaseAnalysesRequest = {}
        if analysis_status is not None:
            input_["analysis_status"] = analysis_status
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if page_size is not None:
            input_["page_size"] = page_size
        if analysis_ids is not None:
            input_["analysis_ids"] = analysis_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_commitment_purchase_analyses(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        analysis_status: Optional[
            "capo_cost_explorer.types.analysis_status.AnalysisStatus"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        page_size: Optional[
            "capo_cost_explorer.types.analyses_page_size.AnalysesPageSize"
        ] = None,
        analysis_ids: Optional[
            "capo_cost_explorer.types.analysis_ids.AnalysisIds"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.analysis_summary.AnalysisSummary]":
        _token = next_page_token
        while True:
            _response = self.list_commitment_purchase_analyses(
                config_overrides=config_overrides,
                analysis_status=analysis_status,
                next_page_token=_token,
                page_size=page_size,
                analysis_ids=analysis_ids,
            )
            _page = _resolve_path(_response, ("analysis_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def list_cost_allocation_tag_backfill_history(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_allocation_tags_max_results.CostAllocationTagsMaxResults"
        ] = None,
    ) -> "capo_cost_explorer.types.list_cost_allocation_tag_backfill_history_response.ListCostAllocationTagBackfillHistoryResponse":
        """<p> Retrieves a list of your historical cost allocation tag backfill requests. </p>

        Args:
            next_token: <p> The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>
            max_results: <p> The maximum number of objects that are returned for this request. </p>

        Raises:
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.list_cost_allocation_tag_backfill_history_request.ListCostAllocationTagBackfillHistoryRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.list_cost_allocation_tag_backfill_history_response.ListCostAllocationTagBackfillHistoryResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.list_cost_allocation_tag_backfill_history

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.list_cost_allocation_tag_backfill_history.list_cost_allocation_tag_backfill_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.list_cost_allocation_tag_backfill_history_request.ListCostAllocationTagBackfillHistoryRequest = {}
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

    def iter_list_cost_allocation_tag_backfill_history(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_allocation_tags_max_results.CostAllocationTagsMaxResults"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.cost_allocation_tag_backfill_request.CostAllocationTagBackfillRequest]":
        _token = next_token
        while True:
            _response = self.list_cost_allocation_tag_backfill_history(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("backfill_requests",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cost_allocation_tags(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        status: Optional[
            "capo_cost_explorer.types.cost_allocation_tag_status.CostAllocationTagStatus"
        ] = None,
        tag_keys: Optional[
            "capo_cost_explorer.types.cost_allocation_tag_key_list.CostAllocationTagKeyList"
        ] = None,
        type: Optional[
            "capo_cost_explorer.types.cost_allocation_tag_type.CostAllocationTagType"
        ] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_allocation_tags_max_results.CostAllocationTagsMaxResults"
        ] = None,
    ) -> "capo_cost_explorer.types.list_cost_allocation_tags_response.ListCostAllocationTagsResponse":
        """<p>Get a list of cost allocation tags. All inputs in the API are optional and serve as filters. By default, all cost allocation tags are returned. </p>

        Args:
            status: <p>The status of cost allocation tag keys that are returned for this request. </p>
            tag_keys: <p>The list of cost allocation tag keys that are returned for this request. </p>
            type: <p>The type of <code>CostAllocationTag</code> object that are returned for this request. The <code>AWSGenerated</code> type tags are tags that Amazon Web Services defines and applies to support Amazon Web Services resources for cost allocation purposes. The <code>UserDefined</code> type tags are tags that you define, create, and apply to resources. </p>
            next_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>
            max_results: <p>The maximum number of objects that are returned for this request. By default, the request returns 100 results. </p>

        Raises:
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.list_cost_allocation_tags_request.ListCostAllocationTagsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.list_cost_allocation_tags_response.ListCostAllocationTagsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.list_cost_allocation_tags

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.list_cost_allocation_tags.list_cost_allocation_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.list_cost_allocation_tags_request.ListCostAllocationTagsRequest = {}
        if status is not None:
            input_["status"] = status
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys
        if type is not None:
            input_["type"] = type
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

    def iter_list_cost_allocation_tags(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        status: Optional[
            "capo_cost_explorer.types.cost_allocation_tag_status.CostAllocationTagStatus"
        ] = None,
        tag_keys: Optional[
            "capo_cost_explorer.types.cost_allocation_tag_key_list.CostAllocationTagKeyList"
        ] = None,
        type: Optional[
            "capo_cost_explorer.types.cost_allocation_tag_type.CostAllocationTagType"
        ] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_allocation_tags_max_results.CostAllocationTagsMaxResults"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.cost_allocation_tag.CostAllocationTag]":
        _token = next_token
        while True:
            _response = self.list_cost_allocation_tags(
                config_overrides=config_overrides,
                status=status,
                tag_keys=tag_keys,
                type=type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("cost_allocation_tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cost_category_definitions(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        effective_on: Optional[
            "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
        ] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_category_max_results.CostCategoryMaxResults"
        ] = None,
        supported_resource_types: Optional[
            "capo_cost_explorer.types.resource_types_filter_input.ResourceTypesFilterInput"
        ] = None,
    ) -> "capo_cost_explorer.types.list_cost_category_definitions_response.ListCostCategoryDefinitionsResponse":
        """<p>Returns the name, Amazon Resource Name (ARN), <code>NumberOfRules</code> and effective dates of all cost categories defined in the account. You have the option to use <code>EffectiveOn</code> and <code>SupportedResourceTypes</code> to return a list of cost categories that were active on a specific date. If there is no <code>EffectiveOn</code> specified, you’ll see cost categories that are effective on the current date. If cost category is still effective, <code>EffectiveEnd</code> is omitted in the response. <code>ListCostCategoryDefinitions</code> supports pagination. The request can have a <code>MaxResults</code> range up to 100.</p>

        Args:
            effective_on: <p>The date when the cost category was effective. </p>
            next_token: <p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>
            max_results: <p>The number of entries a paginated response contains. </p>
            supported_resource_types: <p> Filter cost category definitions that are supported by given resource types based on the latest version. If the filter is present, the result only includes Cost Categories that supports input resource type. If the filter isn't provided, no filtering is applied. The valid values are <code>billing:rispgroupsharing</code> and <code>billing:billingview</code>. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.list_cost_category_definitions_request.ListCostCategoryDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.list_cost_category_definitions_response.ListCostCategoryDefinitionsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.list_cost_category_definitions

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.list_cost_category_definitions.list_cost_category_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.list_cost_category_definitions_request.ListCostCategoryDefinitionsRequest = {}
        if effective_on is not None:
            input_["effective_on"] = effective_on
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if supported_resource_types is not None:
            input_["supported_resource_types"] = supported_resource_types

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_cost_category_definitions(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        effective_on: Optional[
            "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
        ] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_category_max_results.CostCategoryMaxResults"
        ] = None,
        supported_resource_types: Optional[
            "capo_cost_explorer.types.resource_types_filter_input.ResourceTypesFilterInput"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.cost_category_reference.CostCategoryReference]":
        _token = next_token
        while True:
            _response = self.list_cost_category_definitions(
                config_overrides=config_overrides,
                effective_on=effective_on,
                next_token=_token,
                max_results=max_results,
                supported_resource_types=supported_resource_types,
            )
            _page = _resolve_path(_response, ("cost_category_references",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cost_category_resource_associations(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        cost_category_arn: Optional["capo_cost_explorer.types.arn.Arn"] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_category_max_results.CostCategoryMaxResults"
        ] = None,
    ) -> "capo_cost_explorer.types.list_cost_category_resource_associations_response.ListCostCategoryResourceAssociationsResponse":
        """<p>Returns resource associations of all cost categories defined in the account. You have the option to use <code>CostCategoryArn</code> to get the association for a specific cost category. <code>ListCostCategoryResourceAssociations</code> supports pagination. The request can have a <code>MaxResults</code> range up to 100. </p>

        Args:
            cost_category_arn: <p>The unique identifier for your cost category.</p>
            next_token: <p> The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>
            max_results: <p> The number of entries a paginated response contains. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.list_cost_category_resource_associations_request.ListCostCategoryResourceAssociationsRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.list_cost_category_resource_associations_response.ListCostCategoryResourceAssociationsResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.list_cost_category_resource_associations

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.list_cost_category_resource_associations.list_cost_category_resource_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.list_cost_category_resource_associations_request.ListCostCategoryResourceAssociationsRequest = {}
        if cost_category_arn is not None:
            input_["cost_category_arn"] = cost_category_arn
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

    def iter_list_cost_category_resource_associations(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        cost_category_arn: Optional["capo_cost_explorer.types.arn.Arn"] = None,
        next_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
        max_results: Optional[
            "capo_cost_explorer.types.cost_category_max_results.CostCategoryMaxResults"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.cost_category_resource_association.CostCategoryResourceAssociation]":
        _token = next_token
        while True:
            _response = self.list_cost_category_resource_associations(
                config_overrides=config_overrides,
                cost_category_arn=cost_category_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("cost_category_resource_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_savings_plans_purchase_recommendation_generation(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        generation_status: Optional[
            "capo_cost_explorer.types.generation_status.GenerationStatus"
        ] = None,
        recommendation_ids: Optional[
            "capo_cost_explorer.types.recommendation_id_list.RecommendationIdList"
        ] = None,
        page_size: Optional[
            "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "capo_cost_explorer.types.list_savings_plans_purchase_recommendation_generation_response.ListSavingsPlansPurchaseRecommendationGenerationResponse":
        """<p>Retrieves a list of your historical recommendation generations within the past 30 days.</p>

        Args:
            generation_status: <p>The status of the recommendation generation.</p>
            recommendation_ids: <p>The IDs for each specific recommendation.</p>
            page_size: <p>The number of recommendations that you want returned in a single response object.</p>
            next_page_token: <p>The token to retrieve the next set of results.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The pagination token is invalid. Try again without a pagination token.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.list_savings_plans_purchase_recommendation_generation_request.ListSavingsPlansPurchaseRecommendationGenerationRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.list_savings_plans_purchase_recommendation_generation_response.ListSavingsPlansPurchaseRecommendationGenerationResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.list_savings_plans_purchase_recommendation_generation

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.list_savings_plans_purchase_recommendation_generation.list_savings_plans_purchase_recommendation_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.list_savings_plans_purchase_recommendation_generation_request.ListSavingsPlansPurchaseRecommendationGenerationRequest = {}
        if generation_status is not None:
            input_["generation_status"] = generation_status
        if recommendation_ids is not None:
            input_["recommendation_ids"] = recommendation_ids
        if page_size is not None:
            input_["page_size"] = page_size
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_savings_plans_purchase_recommendation_generation(
        self,
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        generation_status: Optional[
            "capo_cost_explorer.types.generation_status.GenerationStatus"
        ] = None,
        recommendation_ids: Optional[
            "capo_cost_explorer.types.recommendation_id_list.RecommendationIdList"
        ] = None,
        page_size: Optional[
            "capo_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
        ] = None,
        next_page_token: Optional[
            "capo_cost_explorer.types.next_page_token.NextPageToken"
        ] = None,
    ) -> "Iterator[capo_cost_explorer.types.generation_summary.GenerationSummary]":
        _token = next_page_token
        while True:
            _response = self.list_savings_plans_purchase_recommendation_generation(
                config_overrides=config_overrides,
                generation_status=generation_status,
                recommendation_ids=recommendation_ids,
                page_size=page_size,
                next_page_token=_token,
            )
            _page = _resolve_path(_response, ("generation_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_cost_explorer.types.arn.Arn",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of resource tags associated with the resource specified by the Amazon Resource Name (ARN). </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. For a list of supported resources, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html">ResourceTag</a>.</p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.list_tags_for_resource

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def provide_anomaly_feedback(
        self,
        anomaly_id: "capo_cost_explorer.types.generic_string.GenericString",
        feedback: "capo_cost_explorer.types.anomaly_feedback_type.AnomalyFeedbackType",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.provide_anomaly_feedback_response.ProvideAnomalyFeedbackResponse":
        """<p>Modifies the feedback property of a given cost anomaly. </p>

        Args:
            anomaly_id: <p>A cost anomaly ID. </p>
            feedback: <p>Describes whether the cost anomaly was a planned activity or you considered it an anomaly. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.provide_anomaly_feedback_request.ProvideAnomalyFeedbackRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.provide_anomaly_feedback_response.ProvideAnomalyFeedbackResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.provide_anomaly_feedback

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.provide_anomaly_feedback.provide_anomaly_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.provide_anomaly_feedback_request.ProvideAnomalyFeedbackRequest = {
            "anomaly_id": anomaly_id,
            "feedback": feedback,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_commitment_purchase_analysis(
        self,
        commitment_purchase_analysis_configuration: "capo_cost_explorer.types.commitment_purchase_analysis_configuration.CommitmentPurchaseAnalysisConfiguration",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.start_commitment_purchase_analysis_response.StartCommitmentPurchaseAnalysisResponse":
        """<p>Specifies the parameters of a planned commitment purchase and starts the generation of the analysis. This enables you to estimate the cost, coverage, and utilization impact of your planned commitment purchases.</p>

        Args:
            commitment_purchase_analysis_configuration: <p>The configuration for the commitment purchase analysis.</p>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.generation_exists_exception.GenerationExistsException: <p>A request to generate a recommendation or analysis is already in progress.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.start_commitment_purchase_analysis_request.StartCommitmentPurchaseAnalysisRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.start_commitment_purchase_analysis_response.StartCommitmentPurchaseAnalysisResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.start_commitment_purchase_analysis

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.start_commitment_purchase_analysis.start_commitment_purchase_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.start_commitment_purchase_analysis_request.StartCommitmentPurchaseAnalysisRequest = {
            "commitment_purchase_analysis_configuration": commitment_purchase_analysis_configuration
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_cost_allocation_tag_backfill(
        self,
        backfill_from: "capo_cost_explorer.types.zoned_date_time.ZonedDateTime",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.start_cost_allocation_tag_backfill_response.StartCostAllocationTagBackfillResponse":
        """<p> Request a cost allocation tag backfill. This will backfill the activation status (either <code>active</code> or <code>inactive</code>) for all tag keys from <code>para:BackfillFrom</code> up to the time this request is made.</p> <p>You can request a backfill once every 24 hours. </p>

        Args:
            backfill_from: <p> The date you want the backfill to start from. The date can only be a first day of the month (a billing start date). Dates can't precede the previous twelve months, or in the future.</p>

        Raises:
            capo_cost_explorer.errors.backfill_limit_exceeded_exception.BackfillLimitExceededException: <p> A request to backfill is already in progress. Once the previous request is complete, you can create another request. </p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.start_cost_allocation_tag_backfill_request.StartCostAllocationTagBackfillRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.start_cost_allocation_tag_backfill_response.StartCostAllocationTagBackfillResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.start_cost_allocation_tag_backfill

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.start_cost_allocation_tag_backfill.start_cost_allocation_tag_backfill(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.start_cost_allocation_tag_backfill_request.StartCostAllocationTagBackfillRequest = {
            "backfill_from": backfill_from
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_savings_plans_purchase_recommendation_generation(
        self, *, config_overrides: Optional[CostExplorerClientConfig] = None
    ) -> "capo_cost_explorer.types.start_savings_plans_purchase_recommendation_generation_response.StartSavingsPlansPurchaseRecommendationGenerationResponse":
        """<p>Requests a Savings Plans recommendation generation. This enables you to calculate a fresh set of Savings Plans recommendations that takes your latest usage data and current Savings Plans inventory into account. You can refresh Savings Plans recommendations up to three times daily for a consolidated billing family.</p> <note> <p> <code>StartSavingsPlansPurchaseRecommendationGeneration</code> has no request syntax because no input parameters are needed to support this operation.</p> </note>

        Raises:
            capo_cost_explorer.errors.data_unavailable_exception.DataUnavailableException: <p>The requested data is unavailable.</p>
            capo_cost_explorer.errors.generation_exists_exception.GenerationExistsException: <p>A request to generate a recommendation or analysis is already in progress.</p>
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.start_savings_plans_purchase_recommendation_generation_request.StartSavingsPlansPurchaseRecommendationGenerationRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.start_savings_plans_purchase_recommendation_generation_response.StartSavingsPlansPurchaseRecommendationGenerationResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.start_savings_plans_purchase_recommendation_generation

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.start_savings_plans_purchase_recommendation_generation.start_savings_plans_purchase_recommendation_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.start_savings_plans_purchase_recommendation_generation_request.StartSavingsPlansPurchaseRecommendationGenerationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_cost_explorer.types.arn.Arn",
        resource_tags: "capo_cost_explorer.types.resource_tag_list.ResourceTagList",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.tag_resource_response.TagResourceResponse":
        """<p>An API operation for adding one or more tags (key-value pairs) to a resource.</p> <p>You can use the <code>TagResource</code> operation with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value you specify replaces the previous value for that tag.</p> <p>Although the maximum number of array members is 200, user-tag maximum is 50. The remaining are reserved for Amazon Web Services use.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. For a list of supported resources, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html">ResourceTag</a>. </p>
            resource_tags: <p> A list of tag key-value pairs to be added to the resource.</p> <p>Each tag consists of a key and a value, and each key must be unique for the resource. The following restrictions apply to resource tags:</p> <ul> <li> <p>Although the maximum number of array members is 200, you can assign a maximum of 50 user-tags to one resource. The remaining are reserved for Amazon Web Services use</p> </li> <li> <p>The maximum length of a key is 128 characters</p> </li> <li> <p>The maximum length of a value is 256 characters</p> </li> <li> <p>Keys and values can only contain alphanumeric characters, spaces, and any of the following: <code>_.:/=+@-</code> </p> </li> <li> <p>Keys and values are case sensitive</p> </li> <li> <p>Keys and values are trimmed for any leading or trailing whitespaces</p> </li> <li> <p>Don’t use <code>aws:</code> as a prefix for your keys. This prefix is reserved for Amazon Web Services use</p> </li> </ul>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.too_many_tags_exception.TooManyTagsException: <p>Can occur if you specify a number of tags for a resource greater than the maximum 50 user tags per resource.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.tag_resource

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "resource_tags": resource_tags,
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
        resource_arn: "capo_cost_explorer.types.arn.Arn",
        resource_tag_keys: "capo_cost_explorer.types.resource_tag_key_list.ResourceTagKeyList",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from a resource. Specify only tag keys in your request. Don't specify the value. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. For a list of supported resources, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html">ResourceTag</a>. </p>
            resource_tag_keys: <p>A list of tag keys associated with tags that need to be removed from the resource. If you specify a tag key that doesn't exist, it's ignored. Although the maximum number of array members is 200, user-tag maximum is 50. The remaining are reserved for Amazon Web Services use. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.untag_resource

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "resource_tag_keys": resource_tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_anomaly_monitor(
        self,
        monitor_arn: "capo_cost_explorer.types.generic_string.GenericString",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        monitor_name: Optional[
            "capo_cost_explorer.types.generic_string.GenericString"
        ] = None,
    ) -> "capo_cost_explorer.types.update_anomaly_monitor_response.UpdateAnomalyMonitorResponse":
        """<p>Updates an existing cost anomaly monitor. The changes made are applied going forward, and doesn't change anomalies detected in the past. </p>

        Args:
            monitor_arn: <p>Cost anomaly monitor Amazon Resource Names (ARNs). </p>
            monitor_name: <p>The new name for the cost anomaly monitor. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.unknown_monitor_exception.UnknownMonitorException: <p>The cost anomaly monitor does not exist for the account. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.update_anomaly_monitor_request.UpdateAnomalyMonitorRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.update_anomaly_monitor_response.UpdateAnomalyMonitorResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.update_anomaly_monitor

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.update_anomaly_monitor.update_anomaly_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.update_anomaly_monitor_request.UpdateAnomalyMonitorRequest = {
            "monitor_arn": monitor_arn
        }
        if monitor_name is not None:
            input_["monitor_name"] = monitor_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_anomaly_subscription(
        self,
        subscription_arn: "capo_cost_explorer.types.generic_string.GenericString",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        threshold: Optional[
            "capo_cost_explorer.types.nullable_non_negative_double.NullableNonNegativeDouble"
        ] = None,
        frequency: Optional[
            "capo_cost_explorer.types.anomaly_subscription_frequency.AnomalySubscriptionFrequency"
        ] = None,
        monitor_arn_list: Optional[
            "capo_cost_explorer.types.monitor_arn_list.MonitorArnList"
        ] = None,
        subscribers: Optional[
            "capo_cost_explorer.types.subscribers.Subscribers"
        ] = None,
        subscription_name: Optional[
            "capo_cost_explorer.types.generic_string.GenericString"
        ] = None,
        threshold_expression: Optional[
            "capo_cost_explorer.types.expression.Expression"
        ] = None,
    ) -> "capo_cost_explorer.types.update_anomaly_subscription_response.UpdateAnomalySubscriptionResponse":
        """<p>Updates an existing cost anomaly subscription. Specify the fields that you want to update. Omitted fields are unchanged.</p> <note> <p>The JSON below describes the generic construct for each type. See <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateAnomalySubscription.html#API_UpdateAnomalySubscription_RequestParameters">Request Parameters</a> for possible values as they apply to <code>AnomalySubscription</code>.</p> </note>

        Args:
            subscription_arn: <p>A cost anomaly subscription Amazon Resource Name (ARN). </p>
            threshold: <p>(deprecated)</p> <p>The update to the threshold value for receiving notifications. </p> <p>This field has been deprecated. To update a threshold, use ThresholdExpression. Continued use of Threshold will be treated as shorthand syntax for a ThresholdExpression.</p> <p>You can specify either Threshold or ThresholdExpression, but not both.</p>
            frequency: <p>The update to the frequency value that subscribers receive notifications. </p>
            monitor_arn_list: <p>A list of cost anomaly monitor ARNs. </p>
            subscribers: <p>The update to the subscriber list. </p>
            subscription_name: <p>The new name of the subscription. </p>
            threshold_expression: <p>The update to the <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html">Expression</a> object used to specify the anomalies that you want to generate alerts for. This supports dimensions and nested expressions. The supported dimensions are <code>ANOMALY_TOTAL_IMPACT_ABSOLUTE</code> and <code>ANOMALY_TOTAL_IMPACT_PERCENTAGE</code>, corresponding to an anomaly’s TotalImpact and TotalImpactPercentage, respectively (see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html">Impact</a> for more details). The supported nested expression types are <code>AND</code> and <code>OR</code>. The match option <code>GREATER_THAN_OR_EQUAL</code> is required. Values must be numbers between 0 and 10,000,000,000 in string format.</p> <p>You can specify either Threshold or ThresholdExpression, but not both.</p> <p>The following are examples of valid ThresholdExpressions:</p> <ul> <li> <p>Absolute threshold: <code>{ "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }</code> </p> </li> <li> <p>Percentage threshold: <code>{ "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }</code> </p> </li> <li> <p> <code>AND</code> two thresholds together: <code>{ "And": [ { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }, { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } } ] }</code> </p> </li> <li> <p> <code>OR</code> two thresholds together: <code>{ "Or": [ { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } }, { "Dimensions": { "Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "100" ] } } ] }</code> </p> </li> </ul>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.unknown_monitor_exception.UnknownMonitorException: <p>The cost anomaly monitor does not exist for the account. </p>
            capo_cost_explorer.errors.unknown_subscription_exception.UnknownSubscriptionException: <p>The cost anomaly subscription does not exist for the account. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.update_anomaly_subscription_request.UpdateAnomalySubscriptionRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.update_anomaly_subscription_response.UpdateAnomalySubscriptionResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.update_anomaly_subscription

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.update_anomaly_subscription.update_anomaly_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.update_anomaly_subscription_request.UpdateAnomalySubscriptionRequest = {
            "subscription_arn": subscription_arn
        }
        if threshold is not None:
            input_["threshold"] = threshold
        if frequency is not None:
            input_["frequency"] = frequency
        if monitor_arn_list is not None:
            input_["monitor_arn_list"] = monitor_arn_list
        if subscribers is not None:
            input_["subscribers"] = subscribers
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if threshold_expression is not None:
            input_["threshold_expression"] = threshold_expression

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cost_allocation_tags_status(
        self,
        cost_allocation_tags_status: "capo_cost_explorer.types.cost_allocation_tag_status_list.CostAllocationTagStatusList",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
    ) -> "capo_cost_explorer.types.update_cost_allocation_tags_status_response.UpdateCostAllocationTagsStatusResponse":
        """<p>Updates status for cost allocation tags in bulk, with maximum batch size of 20. If the tag status that's updated is the same as the existing tag status, the request doesn't fail. Instead, it doesn't have any effect on the tag status (for example, activating the active tag). </p>

        Args:
            cost_allocation_tags_status: <p>The list of <code>CostAllocationTagStatusEntry</code> objects that are used to update cost allocation tags status for this request. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.update_cost_allocation_tags_status_request.UpdateCostAllocationTagsStatusRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.update_cost_allocation_tags_status_response.UpdateCostAllocationTagsStatusResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.update_cost_allocation_tags_status

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.update_cost_allocation_tags_status.update_cost_allocation_tags_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.update_cost_allocation_tags_status_request.UpdateCostAllocationTagsStatusRequest = {
            "cost_allocation_tags_status": cost_allocation_tags_status
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cost_category_definition(
        self,
        cost_category_arn: "capo_cost_explorer.types.arn.Arn",
        rule_version: "capo_cost_explorer.types.cost_category_rule_version.CostCategoryRuleVersion",
        rules: "capo_cost_explorer.types.cost_category_rules_list.CostCategoryRulesList",
        *,
        config_overrides: Optional[CostExplorerClientConfig] = None,
        effective_start: Optional[
            "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
        ] = None,
        default_value: Optional[
            "capo_cost_explorer.types.cost_category_value.CostCategoryValue"
        ] = None,
        split_charge_rules: Optional[
            "capo_cost_explorer.types.cost_category_split_charge_rules_list.CostCategorySplitChargeRulesList"
        ] = None,
    ) -> "capo_cost_explorer.types.update_cost_category_definition_response.UpdateCostCategoryDefinitionResponse":
        """<p>Updates an existing cost category. Changes made to the cost category rules will be used to categorize the current month’s expenses and future expenses. This won’t change categorization for the previous months.</p>

        Args:
            cost_category_arn: <p>The unique identifier for your cost category.</p>
            effective_start: <p>The cost category's effective start date. It can only be a billing start date (first day of the month). If the date isn't provided, it's the first day of the current month. Dates can't be before the previous twelve months, or in the future.</p>
            rules: <p>The <code>Expression</code> object used to categorize costs. For more information, see <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html">CostCategoryRule </a>. </p>
            split_charge_rules: <p> The split charge rules used to allocate your charges between your cost category values. </p>

        Raises:
            capo_cost_explorer.errors.limit_exceeded_exception.LimitExceededException: <p>You made too many calls in a short period of time. Try again later.</p>
            capo_cost_explorer.errors.resource_not_found_exception.ResourceNotFoundException: <p> The specified ARN in the request doesn't exist. </p>
            capo_cost_explorer.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource. </p>
            capo_cost_explorer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cost_explorer.types.update_cost_category_definition_request.UpdateCostCategoryDefinitionRequest]",
        ) -> OperationResponse[
            "capo_cost_explorer.types.update_cost_category_definition_response.UpdateCostCategoryDefinitionResponse"
        ]:
            import capo_cost_explorer._operations.aws_insights_index_service.update_cost_category_definition

            output, http_response = (
                capo_cost_explorer._operations.aws_insights_index_service.update_cost_category_definition.update_cost_category_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cost_explorer.types.update_cost_category_definition_request.UpdateCostCategoryDefinitionRequest = {
            "cost_category_arn": cost_category_arn,
            "rule_version": rule_version,
            "rules": rules,
        }
        if effective_start is not None:
            input_["effective_start"] = effective_start
        if default_value is not None:
            input_["default_value"] = default_value
        if split_charge_rules is not None:
            input_["split_charge_rules"] = split_charge_rules

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
