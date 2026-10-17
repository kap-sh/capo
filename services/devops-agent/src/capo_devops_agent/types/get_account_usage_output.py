"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAccountUsageOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.date_time
    import capo_devops_agent.types.usage_metric


class GetAccountUsageOutput(TypedDict, closed=True):
    monthly_account_investigation_hours: NotRequired[
        "capo_devops_agent.types.usage_metric.UsageMetric"
    ]
    """<p>Monthly investigation hours usage and limit for an account</p>"""
    monthly_account_evaluation_hours: NotRequired[
        "capo_devops_agent.types.usage_metric.UsageMetric"
    ]
    """<p>Monthly evaluation hours usage and limit for an account</p>"""
    monthly_account_system_learning_hours: NotRequired[
        "capo_devops_agent.types.usage_metric.UsageMetric"
    ]
    """<p>Monthly system learning hours usage and limit for an account</p>"""
    monthly_account_on_demand_hours: NotRequired[
        "capo_devops_agent.types.usage_metric.UsageMetric"
    ]
    """<p>Monthly on-demand hours usage and limit for an account</p>"""
    usage_period_start_time: "capo_devops_agent.types.date_time.DateTime"
    """<p>The start time of the usage tracking period</p>"""
    usage_period_end_time: "capo_devops_agent.types.date_time.DateTime"
    """<p>The end time of the usage tracking period</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountUsageOutput) -> dict:
    out: dict = {}
    if "monthly_account_investigation_hours" in value:
        import capo_devops_agent.types.usage_metric

        out["monthlyAccountInvestigationHours"] = (
            capo_devops_agent.types.usage_metric.serialize_json(
                value["monthly_account_investigation_hours"]
            )
        )
    if "monthly_account_evaluation_hours" in value:
        import capo_devops_agent.types.usage_metric

        out["monthlyAccountEvaluationHours"] = (
            capo_devops_agent.types.usage_metric.serialize_json(
                value["monthly_account_evaluation_hours"]
            )
        )
    if "monthly_account_system_learning_hours" in value:
        import capo_devops_agent.types.usage_metric

        out["monthlyAccountSystemLearningHours"] = (
            capo_devops_agent.types.usage_metric.serialize_json(
                value["monthly_account_system_learning_hours"]
            )
        )
    if "monthly_account_on_demand_hours" in value:
        import capo_devops_agent.types.usage_metric

        out["monthlyAccountOnDemandHours"] = (
            capo_devops_agent.types.usage_metric.serialize_json(
                value["monthly_account_on_demand_hours"]
            )
        )
    import capo_devops_agent.types.date_time

    out["usagePeriodStartTime"] = capo_devops_agent.types.date_time.serialize_json(
        value["usage_period_start_time"]
    )
    import capo_devops_agent.types.date_time

    out["usagePeriodEndTime"] = capo_devops_agent.types.date_time.serialize_json(
        value["usage_period_end_time"]
    )
    return out


def deserialize_json(data: dict) -> GetAccountUsageOutput:
    out: GetAccountUsageOutput = {}  # type: ignore[typeddict-item]
    if data.get("monthlyAccountInvestigationHours") is not None:
        import capo_devops_agent.types.usage_metric

        out["monthly_account_investigation_hours"] = (
            capo_devops_agent.types.usage_metric.deserialize_json(
                data["monthlyAccountInvestigationHours"]
            )
        )
    if data.get("monthlyAccountEvaluationHours") is not None:
        import capo_devops_agent.types.usage_metric

        out["monthly_account_evaluation_hours"] = (
            capo_devops_agent.types.usage_metric.deserialize_json(
                data["monthlyAccountEvaluationHours"]
            )
        )
    if data.get("monthlyAccountSystemLearningHours") is not None:
        import capo_devops_agent.types.usage_metric

        out["monthly_account_system_learning_hours"] = (
            capo_devops_agent.types.usage_metric.deserialize_json(
                data["monthlyAccountSystemLearningHours"]
            )
        )
    if data.get("monthlyAccountOnDemandHours") is not None:
        import capo_devops_agent.types.usage_metric

        out["monthly_account_on_demand_hours"] = (
            capo_devops_agent.types.usage_metric.deserialize_json(
                data["monthlyAccountOnDemandHours"]
            )
        )
    if data.get("usagePeriodStartTime") is not None:
        import capo_devops_agent.types.date_time

        out["usage_period_start_time"] = (
            capo_devops_agent.types.date_time.deserialize_json(
                data["usagePeriodStartTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetAccountUsageOutput.usage_period_start_time required"
        )
    if data.get("usagePeriodEndTime") is not None:
        import capo_devops_agent.types.date_time

        out["usage_period_end_time"] = (
            capo_devops_agent.types.date_time.deserialize_json(
                data["usagePeriodEndTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetAccountUsageOutput.usage_period_end_time required"
        )
    return out
