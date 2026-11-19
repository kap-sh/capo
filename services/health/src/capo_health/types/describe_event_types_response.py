"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.event_type_list
    import capo_health.types.next_token


class DescribeEventTypesResponse(TypedDict, closed=True):
    event_types: NotRequired["capo_health.types.event_type_list.EventTypeList"]
    """<p>A list of event types that match the filter criteria. Event types have a category (<code>issue</code>, <code>accountNotification</code>, or <code>scheduledChange</code>), a service (for example, <code>EC2</code>, <code>RDS</code>, <code>DATAPIPELINE</code>, <code>BILLING</code>), and a code (in the format <code>AWS_<i>SERVICE</i>_<i>DESCRIPTION</i> </code>; for example, <code>AWS_EC2_SYSTEM_MAINTENANCE_EVENT</code>).</p>"""
    next_token: NotRequired["capo_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventTypesResponse) -> dict:
    out: dict = {}
    if "event_types" in value:
        import capo_health.types.event_type_list

        out["eventTypes"] = capo_health.types.event_type_list.serialize_aws_json_1_1(
            value["event_types"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventTypesResponse:
    out: DescribeEventTypesResponse = {}  # type: ignore[typeddict-item]
    if data.get("eventTypes") is not None:
        import capo_health.types.event_type_list

        out["event_types"] = capo_health.types.event_type_list.deserialize_aws_json_1_1(
            data["eventTypes"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEventTypesResponse) -> dict:
    out: dict = {}
    if "event_types" in value:
        import capo_health.types.event_type_list

        out["eventTypes"] = capo_health.types.event_type_list.serialize_cbor(
            value["event_types"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeEventTypesResponse:
    out: DescribeEventTypesResponse = {}  # type: ignore[typeddict-item]
    if data.get("eventTypes") is not None:
        import capo_health.types.event_type_list

        out["event_types"] = capo_health.types.event_type_list.deserialize_cbor(
            data["eventTypes"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
