"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetRequestHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.describe_spot_fleet_request_history_max_results
    import capo_ec2.types.event_type
    import capo_ec2.types.spot_fleet_request_id
    import capo_ec2.types.string


class DescribeSpotFleetRequestHistoryRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_fleet_request_id: NotRequired[
        "capo_ec2.types.spot_fleet_request_id.SpotFleetRequestId"
    ]
    """<p>The ID of the Spot Fleet request.</p>"""
    event_type: NotRequired["capo_ec2.types.event_type.EventType"]
    """<p>The type of events to describe. By default, all events are described.</p>"""
    start_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The starting date and time for the events, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_spot_fleet_request_history_max_results.DescribeSpotFleetRequestHistoryMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotFleetRequestHistoryRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "spot_fleet_request_id" in value:
        pairs.append(
            (f"{key_prefix}SpotFleetRequestId", str(value["spot_fleet_request_id"]))
        )
    if "event_type" in value:
        import capo_ec2.types.event_type

        capo_ec2.types.event_type.serialize_ec2_query(
            value["event_type"], pairs, f"{key_prefix}EventType"
        )
    if "start_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeSpotFleetRequestHistoryRequest:
    out: DescribeSpotFleetRequestHistoryRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_spot_fleet_request_id = el.find("spotFleetRequestId")
    if child_spot_fleet_request_id is not None:
        out["spot_fleet_request_id"] = str(child_spot_fleet_request_id.text or "")
    child_event_type = el.find("eventType")
    if child_event_type is not None:
        import capo_ec2.types.event_type

        out["event_type"] = capo_ec2.types.event_type.deserialize_ec2_query(
            child_event_type
        )
    child_start_time = el.find("startTime")
    if child_start_time is not None:
        import capo_ec2.types.date_time

        out["start_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_start_time
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("maxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
