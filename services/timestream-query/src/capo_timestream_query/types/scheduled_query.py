"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name
    import capo_timestream_query.types.error_report_configuration
    import capo_timestream_query.types.scheduled_query_name
    import capo_timestream_query.types.scheduled_query_run_status
    import capo_timestream_query.types.scheduled_query_state
    import capo_timestream_query.types.target_destination
    import capo_timestream_query.types.time


class ScheduledQuery(TypedDict, closed=True):
    arn: "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name.</p>"""
    name: "capo_timestream_query.types.scheduled_query_name.ScheduledQueryName"
    """<p>The name of the scheduled query.</p>"""
    creation_time: NotRequired["capo_timestream_query.types.time.Time"]
    """<p>The creation time of the scheduled query.</p>"""
    state: "capo_timestream_query.types.scheduled_query_state.ScheduledQueryState"
    """<p>State of scheduled query. </p>"""
    previous_invocation_time: NotRequired["capo_timestream_query.types.time.Time"]
    """<p>The last time the scheduled query was run.</p>"""
    next_invocation_time: NotRequired["capo_timestream_query.types.time.Time"]
    """<p>The next time the scheduled query is to be run.</p>"""
    error_report_configuration: NotRequired[
        "capo_timestream_query.types.error_report_configuration.ErrorReportConfiguration"
    ]
    """<p>Configuration for scheduled query error reporting.</p>"""
    target_destination: NotRequired[
        "capo_timestream_query.types.target_destination.TargetDestination"
    ]
    """<p>Target data source where final scheduled query result will be written.</p>"""
    last_run_status: NotRequired[
        "capo_timestream_query.types.scheduled_query_run_status.ScheduledQueryRunStatus"
    ]
    """<p>Status of the last scheduled query run.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledQuery) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    if "creation_time" in value:
        import capo_timestream_query.types.time

        out["CreationTime"] = capo_timestream_query.types.time.serialize_aws_json_1_0(
            value["creation_time"]
        )
    import capo_timestream_query.types.scheduled_query_state

    out["State"] = (
        capo_timestream_query.types.scheduled_query_state.serialize_aws_json_1_0(
            value["state"]
        )
    )
    if "previous_invocation_time" in value:
        import capo_timestream_query.types.time

        out["PreviousInvocationTime"] = (
            capo_timestream_query.types.time.serialize_aws_json_1_0(
                value["previous_invocation_time"]
            )
        )
    if "next_invocation_time" in value:
        import capo_timestream_query.types.time

        out["NextInvocationTime"] = (
            capo_timestream_query.types.time.serialize_aws_json_1_0(
                value["next_invocation_time"]
            )
        )
    if "error_report_configuration" in value:
        import capo_timestream_query.types.error_report_configuration

        out["ErrorReportConfiguration"] = (
            capo_timestream_query.types.error_report_configuration.serialize_aws_json_1_0(
                value["error_report_configuration"]
            )
        )
    if "target_destination" in value:
        import capo_timestream_query.types.target_destination

        out["TargetDestination"] = (
            capo_timestream_query.types.target_destination.serialize_aws_json_1_0(
                value["target_destination"]
            )
        )
    if "last_run_status" in value:
        import capo_timestream_query.types.scheduled_query_run_status

        out["LastRunStatus"] = (
            capo_timestream_query.types.scheduled_query_run_status.serialize_aws_json_1_0(
                value["last_run_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledQuery:
    out: ScheduledQuery = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("CreationTime") is not None:
        import capo_timestream_query.types.time

        out["creation_time"] = (
            capo_timestream_query.types.time.deserialize_aws_json_1_0(
                data["CreationTime"]
            )
        )
    if data.get("State") is not None:
        import capo_timestream_query.types.scheduled_query_state

        out["state"] = (
            capo_timestream_query.types.scheduled_query_state.deserialize_aws_json_1_0(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_timestream_query.types.scheduled_query_state.ScheduledQueryState", ""
        )
    if data.get("PreviousInvocationTime") is not None:
        import capo_timestream_query.types.time

        out["previous_invocation_time"] = (
            capo_timestream_query.types.time.deserialize_aws_json_1_0(
                data["PreviousInvocationTime"]
            )
        )
    if data.get("NextInvocationTime") is not None:
        import capo_timestream_query.types.time

        out["next_invocation_time"] = (
            capo_timestream_query.types.time.deserialize_aws_json_1_0(
                data["NextInvocationTime"]
            )
        )
    if data.get("ErrorReportConfiguration") is not None:
        import capo_timestream_query.types.error_report_configuration

        out["error_report_configuration"] = (
            capo_timestream_query.types.error_report_configuration.deserialize_aws_json_1_0(
                data["ErrorReportConfiguration"]
            )
        )
    if data.get("TargetDestination") is not None:
        import capo_timestream_query.types.target_destination

        out["target_destination"] = (
            capo_timestream_query.types.target_destination.deserialize_aws_json_1_0(
                data["TargetDestination"]
            )
        )
    if data.get("LastRunStatus") is not None:
        import capo_timestream_query.types.scheduled_query_run_status

        out["last_run_status"] = (
            capo_timestream_query.types.scheduled_query_run_status.deserialize_aws_json_1_0(
                data["LastRunStatus"]
            )
        )
    return out
