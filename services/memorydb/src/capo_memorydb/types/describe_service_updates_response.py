"""Generated from Smithy shape ``com.amazonaws.memorydb#DescribeServiceUpdatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.service_update_list
    import capo_memorydb.types.string


class DescribeServiceUpdatesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_memorydb.types.string.String"]
    """<p>An optional argument to pass in case the total number of records exceeds the value of MaxResults. If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""
    service_updates: NotRequired[
        "capo_memorydb.types.service_update_list.ServiceUpdateList"
    ]
    """<p>A list of service updates</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceUpdatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "service_updates" in value:
        import capo_memorydb.types.service_update_list

        out["ServiceUpdates"] = (
            capo_memorydb.types.service_update_list.serialize_aws_json_1_1(
                value["service_updates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceUpdatesResponse:
    out: DescribeServiceUpdatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ServiceUpdates") is not None:
        import capo_memorydb.types.service_update_list

        out["service_updates"] = (
            capo_memorydb.types.service_update_list.deserialize_aws_json_1_1(
                data["ServiceUpdates"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeServiceUpdatesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "service_updates" in value:
        import capo_memorydb.types.service_update_list

        out["ServiceUpdates"] = capo_memorydb.types.service_update_list.serialize_cbor(
            value["service_updates"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeServiceUpdatesResponse:
    out: DescribeServiceUpdatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ServiceUpdates") is not None:
        import capo_memorydb.types.service_update_list

        out["service_updates"] = (
            capo_memorydb.types.service_update_list.deserialize_cbor(
                data["ServiceUpdates"]
            )
        )
    return out
