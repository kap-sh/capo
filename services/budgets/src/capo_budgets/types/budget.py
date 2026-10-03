"""Generated from Smithy shape ``com.amazonaws.budgets#Budget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.auto_adjust_data
    import capo_budgets.types.billing_view_arn
    import capo_budgets.types.budget_name
    import capo_budgets.types.budget_type
    import capo_budgets.types.calculated_spend
    import capo_budgets.types.cost_filters
    import capo_budgets.types.cost_types
    import capo_budgets.types.expression
    import capo_budgets.types.generic_timestamp
    import capo_budgets.types.health_status
    import capo_budgets.types.metrics
    import capo_budgets.types.planned_budget_limits
    import capo_budgets.types.spend
    import capo_budgets.types.time_period
    import capo_budgets.types.time_unit


class Budget(TypedDict, closed=True):
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    r"""<p>The name of a budget. The name must be unique within an account. The <code>:</code> and <code>\</code> characters, and the "/action/" substring, aren't allowed in <code>BudgetName</code>.</p> <p>Budget names are validated for content. Names that contain phone numbers, URLs, or email addresses combined with certain terms may be rejected.</p>"""
    budget_limit: NotRequired["capo_budgets.types.spend.Spend"]
    """<p>The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage that you want to track with your budget.</p> <p> <code>BudgetLimit</code> is required for cost or usage budgets, but optional for RI or Savings Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default to <code>100</code>. This is the only valid value for RI or Savings Plans utilization or coverage budgets. You can't use <code>BudgetLimit</code> with <code>PlannedBudgetLimits</code> for <code>CreateBudget</code> and <code>UpdateBudget</code> actions. </p>"""
    planned_budget_limits: NotRequired[
        "capo_budgets.types.planned_budget_limits.PlannedBudgetLimits"
    ]
    """<p>A map containing multiple <code>BudgetLimit</code>, including current or future limits.</p> <p> <code>PlannedBudgetLimits</code> is available for cost or usage budget and supports both monthly and quarterly <code>TimeUnit</code>. </p> <p>For monthly budgets, provide 12 months of <code>PlannedBudgetLimits</code> values. This must start from the current month and include the next 11 months. The <code>key</code> is the start of the month, <code>UTC</code> in epoch seconds. </p> <p>For quarterly budgets, provide four quarters of <code>PlannedBudgetLimits</code> value entries in standard calendar quarter increments. This must start from the current quarter and include the next three quarters. The <code>key</code> is the start of the quarter, <code>UTC</code> in epoch seconds. </p> <p>If the planned budget expires before 12 months for monthly or four quarters for quarterly, provide the <code>PlannedBudgetLimits</code> values only for the remaining periods.</p> <p>If the budget begins at a date in the future, provide <code>PlannedBudgetLimits</code> values from the start date of the budget. </p> <p>After all of the <code>BudgetLimit</code> values in <code>PlannedBudgetLimits</code> are used, the budget continues to use the last limit as the <code>BudgetLimit</code>. At that point, the planned budget provides the same experience as a fixed budget. </p> <p> <code>DescribeBudget</code> and <code>DescribeBudgets</code> response along with <code>PlannedBudgetLimits</code> also contain <code>BudgetLimit</code> representing the current month or quarter limit present in <code>PlannedBudgetLimits</code>. This only applies to budgets that are created with <code>PlannedBudgetLimits</code>. Budgets that are created without <code>PlannedBudgetLimits</code> only contain <code>BudgetLimit</code>. They don't contain <code>PlannedBudgetLimits</code>.</p>"""
    cost_filters: NotRequired["capo_budgets.types.cost_filters.CostFilters"]
    """<p>The cost filters, such as <code>Region</code>, <code>Service</code>, <code>LinkedAccount</code>, <code>Tag</code>, or <code>CostCategory</code>, that are applied to a budget.</p> <p>Amazon Web Services Budgets supports the following services as a <code>Service</code> filter for RI budgets:</p> <ul> <li> <p>Amazon EC2</p> </li> <li> <p>Amazon Redshift</p> </li> <li> <p>Amazon Relational Database Service</p> </li> <li> <p>Amazon ElastiCache</p> </li> <li> <p>Amazon OpenSearch Service</p> </li> </ul>"""
    cost_types: NotRequired["capo_budgets.types.cost_types.CostTypes"]
    """<p>The types of costs that are included in this <code>COST</code> budget.</p> <p> <code>USAGE</code>, <code>RI_UTILIZATION</code>, <code>RI_COVERAGE</code>, <code>SAVINGS_PLANS_UTILIZATION</code>, and <code>SAVINGS_PLANS_COVERAGE</code> budgets do not have <code>CostTypes</code>.</p>"""
    time_unit: "capo_budgets.types.time_unit.TimeUnit"
    """<p>The length of time until a budget resets the actual and forecasted spend.</p>"""
    time_period: NotRequired["capo_budgets.types.time_period.TimePeriod"]
    """<p>The period of time that's covered by a budget. You set the start date and end date. The start date must come before the end date. The end date must come before <code>06/15/87 00:00 UTC</code>. </p> <p>If you create your budget and don't specify a start date, Amazon Web Services defaults to the start of your chosen time period (DAILY, MONTHLY, QUARTERLY, ANNUALLY, or CUSTOM). For example, if you created your budget on January 24, 2018, chose <code>DAILY</code>, and didn't set a start date, Amazon Web Services set your start date to <code>01/24/18 00:00 UTC</code>. If you chose <code>MONTHLY</code>, Amazon Web Services set your start date to <code>01/01/18 00:00 UTC</code>. If you didn't specify an end date, Amazon Web Services set your end date to <code>06/15/87 00:00 UTC</code>. The defaults are the same for the Billing and Cost Management console and the API. </p> <p>You can change either date with the <code>UpdateBudget</code> operation.</p> <p>After the end date, Amazon Web Services deletes the budget and all the associated notifications and subscribers.</p>"""
    calculated_spend: NotRequired["capo_budgets.types.calculated_spend.CalculatedSpend"]
    """<p>The actual and forecasted cost or usage that the budget tracks.</p>"""
    budget_type: "capo_budgets.types.budget_type.BudgetType"
    """<p>Specifies whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage.</p>"""
    last_updated_time: NotRequired[
        "capo_budgets.types.generic_timestamp.GenericTimestamp"
    ]
    """<p>The last time that you updated this budget.</p>"""
    auto_adjust_data: NotRequired["capo_budgets.types.auto_adjust_data.AutoAdjustData"]
    """<p>The parameters that determine the budget amount for an auto-adjusting budget.</p>"""
    filter_expression: NotRequired["capo_budgets.types.expression.Expression"]
    """<p>The filtering dimensions for the budget and their corresponding values.</p>"""
    metrics: NotRequired["capo_budgets.types.metrics.Metrics"]
    """<p>The definition for how the budget data is aggregated.</p>"""
    billing_view_arn: NotRequired["capo_budgets.types.billing_view_arn.BillingViewArn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    health_status: NotRequired["capo_budgets.types.health_status.HealthStatus"]
    """<p>The current operational state of a Billing View derived resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Budget) -> dict:
    out: dict = {}
    out["BudgetName"] = value["budget_name"]
    if "budget_limit" in value:
        import capo_budgets.types.spend

        out["BudgetLimit"] = capo_budgets.types.spend.serialize_aws_json_1_1(
            value["budget_limit"]
        )
    if "planned_budget_limits" in value:
        import capo_budgets.types.planned_budget_limits

        out["PlannedBudgetLimits"] = (
            capo_budgets.types.planned_budget_limits.serialize_aws_json_1_1(
                value["planned_budget_limits"]
            )
        )
    if "cost_filters" in value:
        import capo_budgets.types.cost_filters

        out["CostFilters"] = capo_budgets.types.cost_filters.serialize_aws_json_1_1(
            value["cost_filters"]
        )
    if "cost_types" in value:
        import capo_budgets.types.cost_types

        out["CostTypes"] = capo_budgets.types.cost_types.serialize_aws_json_1_1(
            value["cost_types"]
        )
    import capo_budgets.types.time_unit

    out["TimeUnit"] = capo_budgets.types.time_unit.serialize_aws_json_1_1(
        value["time_unit"]
    )
    if "time_period" in value:
        import capo_budgets.types.time_period

        out["TimePeriod"] = capo_budgets.types.time_period.serialize_aws_json_1_1(
            value["time_period"]
        )
    if "calculated_spend" in value:
        import capo_budgets.types.calculated_spend

        out["CalculatedSpend"] = (
            capo_budgets.types.calculated_spend.serialize_aws_json_1_1(
                value["calculated_spend"]
            )
        )
    import capo_budgets.types.budget_type

    out["BudgetType"] = capo_budgets.types.budget_type.serialize_aws_json_1_1(
        value["budget_type"]
    )
    if "last_updated_time" in value:
        import capo_budgets.types.generic_timestamp

        out["LastUpdatedTime"] = (
            capo_budgets.types.generic_timestamp.serialize_aws_json_1_1(
                value["last_updated_time"]
            )
        )
    if "auto_adjust_data" in value:
        import capo_budgets.types.auto_adjust_data

        out["AutoAdjustData"] = (
            capo_budgets.types.auto_adjust_data.serialize_aws_json_1_1(
                value["auto_adjust_data"]
            )
        )
    if "filter_expression" in value:
        import capo_budgets.types.expression

        out["FilterExpression"] = capo_budgets.types.expression.serialize_aws_json_1_1(
            value["filter_expression"]
        )
    if "metrics" in value:
        import capo_budgets.types.metrics

        out["Metrics"] = capo_budgets.types.metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    if "health_status" in value:
        import capo_budgets.types.health_status

        out["HealthStatus"] = capo_budgets.types.health_status.serialize_aws_json_1_1(
            value["health_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Budget:
    out: Budget = {}  # type: ignore[typeddict-item]
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("Budget.budget_name required")
    if data.get("BudgetLimit") is not None:
        import capo_budgets.types.spend

        out["budget_limit"] = capo_budgets.types.spend.deserialize_aws_json_1_1(
            data["BudgetLimit"]
        )
    if data.get("PlannedBudgetLimits") is not None:
        import capo_budgets.types.planned_budget_limits

        out["planned_budget_limits"] = (
            capo_budgets.types.planned_budget_limits.deserialize_aws_json_1_1(
                data["PlannedBudgetLimits"]
            )
        )
    if data.get("CostFilters") is not None:
        import capo_budgets.types.cost_filters

        out["cost_filters"] = capo_budgets.types.cost_filters.deserialize_aws_json_1_1(
            data["CostFilters"]
        )
    if data.get("CostTypes") is not None:
        import capo_budgets.types.cost_types

        out["cost_types"] = capo_budgets.types.cost_types.deserialize_aws_json_1_1(
            data["CostTypes"]
        )
    if data.get("TimeUnit") is not None:
        import capo_budgets.types.time_unit

        out["time_unit"] = capo_budgets.types.time_unit.deserialize_aws_json_1_1(
            data["TimeUnit"]
        )
    else:
        raise DeserializationError("Budget.time_unit required")
    if data.get("TimePeriod") is not None:
        import capo_budgets.types.time_period

        out["time_period"] = capo_budgets.types.time_period.deserialize_aws_json_1_1(
            data["TimePeriod"]
        )
    if data.get("CalculatedSpend") is not None:
        import capo_budgets.types.calculated_spend

        out["calculated_spend"] = (
            capo_budgets.types.calculated_spend.deserialize_aws_json_1_1(
                data["CalculatedSpend"]
            )
        )
    if data.get("BudgetType") is not None:
        import capo_budgets.types.budget_type

        out["budget_type"] = capo_budgets.types.budget_type.deserialize_aws_json_1_1(
            data["BudgetType"]
        )
    else:
        raise DeserializationError("Budget.budget_type required")
    if data.get("LastUpdatedTime") is not None:
        import capo_budgets.types.generic_timestamp

        out["last_updated_time"] = (
            capo_budgets.types.generic_timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedTime"]
            )
        )
    if data.get("AutoAdjustData") is not None:
        import capo_budgets.types.auto_adjust_data

        out["auto_adjust_data"] = (
            capo_budgets.types.auto_adjust_data.deserialize_aws_json_1_1(
                data["AutoAdjustData"]
            )
        )
    if data.get("FilterExpression") is not None:
        import capo_budgets.types.expression

        out["filter_expression"] = (
            capo_budgets.types.expression.deserialize_aws_json_1_1(
                data["FilterExpression"]
            )
        )
    if data.get("Metrics") is not None:
        import capo_budgets.types.metrics

        out["metrics"] = capo_budgets.types.metrics.deserialize_aws_json_1_1(
            data["Metrics"]
        )
    if data.get("BillingViewArn") is not None:
        out["billing_view_arn"] = data["BillingViewArn"]
    if data.get("HealthStatus") is not None:
        import capo_budgets.types.health_status

        out["health_status"] = (
            capo_budgets.types.health_status.deserialize_aws_json_1_1(
                data["HealthStatus"]
            )
        )
    return out
