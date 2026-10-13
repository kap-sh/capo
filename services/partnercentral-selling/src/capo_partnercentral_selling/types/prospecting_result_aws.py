"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProspectingResultAws``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.prospecting_insights
    import capo_partnercentral_selling.types.prospecting_result_customer
    import capo_partnercentral_selling.types.prospecting_task_identifier
    import capo_partnercentral_selling.types.task_arn
    import capo_partnercentral_selling.types.task_name


class ProspectingResultAws(TypedDict, closed=True):
    customer: NotRequired[
        "capo_partnercentral_selling.types.prospecting_result_customer.ProspectingResultCustomer"
    ]
    """<p>Contains details about the prospected customer account, including geographic, industry, and segment classifications.</p>"""
    insights: NotRequired[
        "capo_partnercentral_selling.types.prospecting_insights.ProspectingInsights"
    ]
    """<p>Insights that AI generates from the prospecting analysis. These insights include engagement scores and solution fit assessments for the prospected customer.</p>"""
    start_time: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The timestamp when the prospecting result context was created. The format is ISO 8601 (UTC).</p>"""
    end_time: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The timestamp when the prospecting task completed processing. The format is ISO 8601 (UTC).</p>"""
    task_id: NotRequired[
        "capo_partnercentral_selling.types.prospecting_task_identifier.ProspectingTaskIdentifier"
    ]
    """<p>The unique identifier of the prospecting task that generates this result.</p>"""
    task_arn: NotRequired["capo_partnercentral_selling.types.task_arn.TaskArn"]
    """<p>The Amazon Resource Name (ARN) of the prospecting task. Use this ARN to track and manage the task within AWS.</p>"""
    task_name: NotRequired["capo_partnercentral_selling.types.task_name.TaskName"]
    """<p>The name that the user provides for the prospecting task that generates this result.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProspectingResultAws) -> dict:
    out: dict = {}
    if "customer" in value:
        import capo_partnercentral_selling.types.prospecting_result_customer

        out["Customer"] = (
            capo_partnercentral_selling.types.prospecting_result_customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "insights" in value:
        import capo_partnercentral_selling.types.prospecting_insights

        out["Insights"] = (
            capo_partnercentral_selling.types.prospecting_insights.serialize_aws_json_1_0(
                value["insights"]
            )
        )
    if "start_time" in value:
        import capo_partnercentral_selling.types.date_time

        out["StartTime"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_partnercentral_selling.types.date_time

        out["EndTime"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "task_name" in value:
        out["TaskName"] = value["task_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProspectingResultAws:
    out: ProspectingResultAws = {}  # type: ignore[typeddict-item]
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.prospecting_result_customer

        out["customer"] = (
            capo_partnercentral_selling.types.prospecting_result_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if data.get("Insights") is not None:
        import capo_partnercentral_selling.types.prospecting_insights

        out["insights"] = (
            capo_partnercentral_selling.types.prospecting_insights.deserialize_aws_json_1_0(
                data["Insights"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_partnercentral_selling.types.date_time

        out["start_time"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_partnercentral_selling.types.date_time

        out["end_time"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["EndTime"]
            )
        )
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    if data.get("TaskArn") is not None:
        out["task_arn"] = data["TaskArn"]
    if data.get("TaskName") is not None:
        out["task_name"] = data["TaskName"]
    return out


def redact_sensitive(value: ProspectingResultAws) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer" in value:
        import capo_partnercentral_selling.types.prospecting_result_customer

        out["customer"] = (
            capo_partnercentral_selling.types.prospecting_result_customer.redact_sensitive(
                value["customer"]
            )
        )
    return out
