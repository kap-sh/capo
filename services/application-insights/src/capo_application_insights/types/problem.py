"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Problem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.affected_resource
    import capo_application_insights.types.end_time
    import capo_application_insights.types.feedback
    import capo_application_insights.types.insights
    import capo_application_insights.types.last_recurrence_time
    import capo_application_insights.types.problem_id
    import capo_application_insights.types.recurring_count
    import capo_application_insights.types.resolution_method
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.severity_level
    import capo_application_insights.types.short_name
    import capo_application_insights.types.start_time
    import capo_application_insights.types.status
    import capo_application_insights.types.title
    import capo_application_insights.types.visibility


class Problem(TypedDict, closed=True):
    id: NotRequired["capo_application_insights.types.problem_id.ProblemId"]
    """<p>The ID of the problem.</p>"""
    title: NotRequired["capo_application_insights.types.title.Title"]
    """<p>The name of the problem.</p>"""
    short_name: NotRequired["capo_application_insights.types.short_name.ShortName"]
    """<p> The short name of the problem associated with the SNS notification. </p>"""
    insights: NotRequired["capo_application_insights.types.insights.Insights"]
    """<p>A detailed analysis of the problem using machine learning.</p>"""
    status: NotRequired["capo_application_insights.types.status.Status"]
    """<p>The status of the problem.</p>"""
    affected_resource: NotRequired[
        "capo_application_insights.types.affected_resource.AffectedResource"
    ]
    """<p>The resource affected by the problem.</p>"""
    start_time: NotRequired["capo_application_insights.types.start_time.StartTime"]
    """<p>The time when the problem started, in epoch seconds.</p>"""
    end_time: NotRequired["capo_application_insights.types.end_time.EndTime"]
    """<p>The time when the problem ended, in epoch seconds.</p>"""
    severity_level: NotRequired[
        "capo_application_insights.types.severity_level.SeverityLevel"
    ]
    """<p>A measure of the level of impact of the problem.</p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the owner of the resource group affected by the problem.</p>"""
    resource_group_name: NotRequired[
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group affected by the problem.</p>"""
    feedback: NotRequired["capo_application_insights.types.feedback.Feedback"]
    """<p>Feedback provided by the user about the problem.</p>"""
    recurring_count: NotRequired[
        "capo_application_insights.types.recurring_count.RecurringCount"
    ]
    """<p> The number of times that the same problem reoccurred after the first time it was resolved. </p>"""
    last_recurrence_time: NotRequired[
        "capo_application_insights.types.last_recurrence_time.LastRecurrenceTime"
    ]
    """<p> The last time that the problem reoccurred after its last resolution. </p>"""
    visibility: NotRequired["capo_application_insights.types.visibility.Visibility"]
    """<p>Specifies whether or not you can view the problem. Updates to ignored problems do not generate notifications.</p>"""
    resolution_method: NotRequired[
        "capo_application_insights.types.resolution_method.ResolutionMethod"
    ]
    """<p>Specifies how the problem was resolved. If the value is <code>AUTOMATIC</code>, the system resolved the problem. If the value is <code>MANUAL</code>, the user resolved the problem. If the value is <code>UNRESOLVED</code>, then the problem is not resolved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Problem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "short_name" in value:
        out["ShortName"] = value["short_name"]
    if "insights" in value:
        out["Insights"] = value["insights"]
    if "status" in value:
        import capo_application_insights.types.status

        out["Status"] = capo_application_insights.types.status.serialize_aws_json_1_1(
            value["status"]
        )
    if "affected_resource" in value:
        out["AffectedResource"] = value["affected_resource"]
    if "start_time" in value:
        import capo_application_insights.types.start_time

        out["StartTime"] = (
            capo_application_insights.types.start_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_application_insights.types.end_time

        out["EndTime"] = (
            capo_application_insights.types.end_time.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "severity_level" in value:
        import capo_application_insights.types.severity_level

        out["SeverityLevel"] = (
            capo_application_insights.types.severity_level.serialize_aws_json_1_1(
                value["severity_level"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "feedback" in value:
        import capo_application_insights.types.feedback

        out["Feedback"] = (
            capo_application_insights.types.feedback.serialize_aws_json_1_1(
                value["feedback"]
            )
        )
    if "recurring_count" in value:
        out["RecurringCount"] = value["recurring_count"]
    if "last_recurrence_time" in value:
        import capo_application_insights.types.last_recurrence_time

        out["LastRecurrenceTime"] = (
            capo_application_insights.types.last_recurrence_time.serialize_aws_json_1_1(
                value["last_recurrence_time"]
            )
        )
    if "visibility" in value:
        import capo_application_insights.types.visibility

        out["Visibility"] = (
            capo_application_insights.types.visibility.serialize_aws_json_1_1(
                value["visibility"]
            )
        )
    if "resolution_method" in value:
        import capo_application_insights.types.resolution_method

        out["ResolutionMethod"] = (
            capo_application_insights.types.resolution_method.serialize_aws_json_1_1(
                value["resolution_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Problem:
    out: Problem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("ShortName") is not None:
        out["short_name"] = data["ShortName"]
    if data.get("Insights") is not None:
        out["insights"] = data["Insights"]
    if data.get("Status") is not None:
        import capo_application_insights.types.status

        out["status"] = capo_application_insights.types.status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("AffectedResource") is not None:
        out["affected_resource"] = data["AffectedResource"]
    if data.get("StartTime") is not None:
        import capo_application_insights.types.start_time

        out["start_time"] = (
            capo_application_insights.types.start_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_application_insights.types.end_time

        out["end_time"] = (
            capo_application_insights.types.end_time.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if data.get("SeverityLevel") is not None:
        import capo_application_insights.types.severity_level

        out["severity_level"] = (
            capo_application_insights.types.severity_level.deserialize_aws_json_1_1(
                data["SeverityLevel"]
            )
        )
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("Feedback") is not None:
        import capo_application_insights.types.feedback

        out["feedback"] = (
            capo_application_insights.types.feedback.deserialize_aws_json_1_1(
                data["Feedback"]
            )
        )
    if data.get("RecurringCount") is not None:
        out["recurring_count"] = data["RecurringCount"]
    if data.get("LastRecurrenceTime") is not None:
        import capo_application_insights.types.last_recurrence_time

        out["last_recurrence_time"] = (
            capo_application_insights.types.last_recurrence_time.deserialize_aws_json_1_1(
                data["LastRecurrenceTime"]
            )
        )
    if data.get("Visibility") is not None:
        import capo_application_insights.types.visibility

        out["visibility"] = (
            capo_application_insights.types.visibility.deserialize_aws_json_1_1(
                data["Visibility"]
            )
        )
    if data.get("ResolutionMethod") is not None:
        import capo_application_insights.types.resolution_method

        out["resolution_method"] = (
            capo_application_insights.types.resolution_method.deserialize_aws_json_1_1(
                data["ResolutionMethod"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Problem) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "short_name" in value:
        out["ShortName"] = value["short_name"]
    if "insights" in value:
        out["Insights"] = value["insights"]
    if "status" in value:
        import capo_application_insights.types.status

        out["Status"] = capo_application_insights.types.status.serialize_cbor(
            value["status"]
        )
    if "affected_resource" in value:
        out["AffectedResource"] = value["affected_resource"]
    if "start_time" in value:
        import capo_application_insights.types.start_time

        out["StartTime"] = capo_application_insights.types.start_time.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_application_insights.types.end_time

        out["EndTime"] = capo_application_insights.types.end_time.serialize_cbor(
            value["end_time"]
        )
    if "severity_level" in value:
        import capo_application_insights.types.severity_level

        out["SeverityLevel"] = (
            capo_application_insights.types.severity_level.serialize_cbor(
                value["severity_level"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "feedback" in value:
        import capo_application_insights.types.feedback

        out["Feedback"] = capo_application_insights.types.feedback.serialize_cbor(
            value["feedback"]
        )
    if "recurring_count" in value:
        out["RecurringCount"] = value["recurring_count"]
    if "last_recurrence_time" in value:
        import capo_application_insights.types.last_recurrence_time

        out["LastRecurrenceTime"] = (
            capo_application_insights.types.last_recurrence_time.serialize_cbor(
                value["last_recurrence_time"]
            )
        )
    if "visibility" in value:
        import capo_application_insights.types.visibility

        out["Visibility"] = capo_application_insights.types.visibility.serialize_cbor(
            value["visibility"]
        )
    if "resolution_method" in value:
        import capo_application_insights.types.resolution_method

        out["ResolutionMethod"] = (
            capo_application_insights.types.resolution_method.serialize_cbor(
                value["resolution_method"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Problem:
    out: Problem = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("ShortName") is not None:
        out["short_name"] = data["ShortName"]
    if data.get("Insights") is not None:
        out["insights"] = data["Insights"]
    if data.get("Status") is not None:
        import capo_application_insights.types.status

        out["status"] = capo_application_insights.types.status.deserialize_cbor(
            data["Status"]
        )
    if data.get("AffectedResource") is not None:
        out["affected_resource"] = data["AffectedResource"]
    if data.get("StartTime") is not None:
        import capo_application_insights.types.start_time

        out["start_time"] = capo_application_insights.types.start_time.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_application_insights.types.end_time

        out["end_time"] = capo_application_insights.types.end_time.deserialize_cbor(
            data["EndTime"]
        )
    if data.get("SeverityLevel") is not None:
        import capo_application_insights.types.severity_level

        out["severity_level"] = (
            capo_application_insights.types.severity_level.deserialize_cbor(
                data["SeverityLevel"]
            )
        )
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("Feedback") is not None:
        import capo_application_insights.types.feedback

        out["feedback"] = capo_application_insights.types.feedback.deserialize_cbor(
            data["Feedback"]
        )
    if data.get("RecurringCount") is not None:
        out["recurring_count"] = data["RecurringCount"]
    if data.get("LastRecurrenceTime") is not None:
        import capo_application_insights.types.last_recurrence_time

        out["last_recurrence_time"] = (
            capo_application_insights.types.last_recurrence_time.deserialize_cbor(
                data["LastRecurrenceTime"]
            )
        )
    if data.get("Visibility") is not None:
        import capo_application_insights.types.visibility

        out["visibility"] = capo_application_insights.types.visibility.deserialize_cbor(
            data["Visibility"]
        )
    if data.get("ResolutionMethod") is not None:
        import capo_application_insights.types.resolution_method

        out["resolution_method"] = (
            capo_application_insights.types.resolution_method.deserialize_cbor(
                data["ResolutionMethod"]
            )
        )
    return out
