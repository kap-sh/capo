"""Generated from Smithy shape ``com.amazonaws.timestreamquery#UpdateScheduledQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name
    import capo_timestream_query.types.scheduled_query_state


class UpdateScheduledQueryRequest(TypedDict, closed=True):
    scheduled_query_arn: (
        "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>ARN of the scheuled query.</p>"""
    state: "capo_timestream_query.types.scheduled_query_state.ScheduledQueryState"
    """<p>State of the scheduled query. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateScheduledQueryRequest) -> dict:
    out: dict = {}
    out["ScheduledQueryArn"] = value["scheduled_query_arn"]
    import capo_timestream_query.types.scheduled_query_state

    out["State"] = (
        capo_timestream_query.types.scheduled_query_state.serialize_aws_json_1_0(
            value["state"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateScheduledQueryRequest:
    out: UpdateScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScheduledQueryArn") is not None:
        out["scheduled_query_arn"] = data["ScheduledQueryArn"]
    else:
        out["scheduled_query_arn"] = ""
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
    return out
