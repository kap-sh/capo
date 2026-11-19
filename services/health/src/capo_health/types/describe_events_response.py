"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.event_list
    import capo_health.types.next_token


class DescribeEventsResponse(TypedDict, closed=True):
    events: NotRequired["capo_health.types.event_list.EventList"]
    """<p>The events that match the specified filter criteria.</p>"""
    next_token: NotRequired["capo_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsResponse) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_health.types.event_list

        out["events"] = capo_health.types.event_list.serialize_aws_json_1_1(
            value["events"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsResponse:
    out: DescribeEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_health.types.event_list

        out["events"] = capo_health.types.event_list.deserialize_aws_json_1_1(
            data["events"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventsResponse) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_health.types.event_list

        out["events"] = capo_health.types.event_list.serialize_cbor(value["events"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeEventsResponse:
    out: DescribeEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("events") is not None:
        import capo_health.types.event_list

        out["events"] = capo_health.types.event_list.deserialize_cbor(data["events"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
