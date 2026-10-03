"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeFleetEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.timestamp


class DescribeFleetEventsInput(TypedDict, closed=True):
    fleet_id: NotRequired["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"]
    """<p>A unique identifier for the fleet to get event logs for. You can use either the fleet ID or ARN value.</p>"""
    start_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>The earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: "1469498468.057").</p>"""
    end_time: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>The most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: "1469498468.057").</p>"""
    limit: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetEventsInput) -> dict:
    out: dict = {}
    if "fleet_id" in value:
        out["FleetId"] = value["fleet_id"]
    if "start_time" in value:
        import capo_gamelift.types.timestamp

        out["StartTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_gamelift.types.timestamp

        out["EndTime"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetEventsInput:
    out: DescribeFleetEventsInput = {}  # type: ignore[typeddict-item]
    if data.get("FleetId") is not None:
        out["fleet_id"] = data["FleetId"]
    if data.get("StartTime") is not None:
        import capo_gamelift.types.timestamp

        out["start_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_gamelift.types.timestamp

        out["end_time"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
