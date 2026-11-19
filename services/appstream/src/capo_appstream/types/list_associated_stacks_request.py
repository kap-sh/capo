"""Generated from Smithy shape ``com.amazonaws.appstream#ListAssociatedStacksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string


class ListAssociatedStacksRequest(TypedDict, closed=True):
    fleet_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the fleet.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssociatedStacksRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssociatedStacksRequest:
    out: ListAssociatedStacksRequest = {}  # type: ignore[typeddict-item]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAssociatedStacksRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAssociatedStacksRequest:
    out: ListAssociatedStacksRequest = {}  # type: ignore[typeddict-item]
    if data.get("FleetName") is not None:
        out["fleet_name"] = data["FleetName"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
