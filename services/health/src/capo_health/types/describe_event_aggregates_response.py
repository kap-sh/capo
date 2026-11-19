"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventAggregatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.event_aggregate_list
    import capo_health.types.next_token


class DescribeEventAggregatesResponse(TypedDict, closed=True):
    event_aggregates: NotRequired[
        "capo_health.types.event_aggregate_list.EventAggregateList"
    ]
    """<p>The number of events in each category that meet the optional filter criteria.</p>"""
    next_token: NotRequired["capo_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventAggregatesResponse) -> dict:
    out: dict = {}
    if "event_aggregates" in value:
        import capo_health.types.event_aggregate_list

        out["eventAggregates"] = (
            capo_health.types.event_aggregate_list.serialize_aws_json_1_1(
                value["event_aggregates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventAggregatesResponse:
    out: DescribeEventAggregatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("eventAggregates") is not None:
        import capo_health.types.event_aggregate_list

        out["event_aggregates"] = (
            capo_health.types.event_aggregate_list.deserialize_aws_json_1_1(
                data["eventAggregates"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventAggregatesResponse) -> dict:
    out: dict = {}
    if "event_aggregates" in value:
        import capo_health.types.event_aggregate_list

        out["eventAggregates"] = capo_health.types.event_aggregate_list.serialize_cbor(
            value["event_aggregates"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeEventAggregatesResponse:
    out: DescribeEventAggregatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("eventAggregates") is not None:
        import capo_health.types.event_aggregate_list

        out["event_aggregates"] = (
            capo_health.types.event_aggregate_list.deserialize_cbor(
                data["eventAggregates"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
