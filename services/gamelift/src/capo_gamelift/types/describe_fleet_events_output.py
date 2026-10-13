"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetEventsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.event_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeFleetEventsOutput(TypedDict, closed=True):
    events: NotRequired["capo_gamelift.types.event_list.EventList"]
    """<p>A collection of objects containing event log entries for the specified fleet.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetEventsOutput) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_gamelift.types.event_list

        out["Events"] = capo_gamelift.types.event_list.serialize_aws_json_1_1(
            value["events"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetEventsOutput:
    out: DescribeFleetEventsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Events") is not None:
        import capo_gamelift.types.event_list

        out["events"] = capo_gamelift.types.event_list.deserialize_aws_json_1_1(
            data["Events"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeFleetEventsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "events" in value:
        import capo_gamelift.types.event_list

        out["events"] = capo_gamelift.types.event_list.redact_sensitive(value["events"])
    return out
