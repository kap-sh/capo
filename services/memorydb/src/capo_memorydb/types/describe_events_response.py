"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.event_list
    import capo_memorydb.types.string


class DescribeEventsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    events: NotRequired["capo_memorydb.types.event_list.EventList"]
    """<p>A list of events. Each element in the list contains detailed information about one event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "events" in value:
        import capo_memorydb.types.event_list

        out["Events"] = capo_memorydb.types.event_list.serialize_aws_json_1_1(
            value["events"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsResponse:
    out: DescribeEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Events") is not None:
        import capo_memorydb.types.event_list

        out["events"] = capo_memorydb.types.event_list.deserialize_aws_json_1_1(
            data["Events"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "events" in value:
        import capo_memorydb.types.event_list

        out["Events"] = capo_memorydb.types.event_list.serialize_cbor(value["events"])
    return out


def deserialize_cbor(data: dict) -> DescribeEventsResponse:
    out: DescribeEventsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Events") is not None:
        import capo_memorydb.types.event_list

        out["events"] = capo_memorydb.types.event_list.deserialize_cbor(data["Events"])
    return out
