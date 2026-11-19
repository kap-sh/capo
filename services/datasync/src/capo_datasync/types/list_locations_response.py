"""Generated from Smithy shape ``com.amazonaws.datasync#ListLocationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.location_list
    import capo_datasync.types.next_token


class ListLocationsResponse(TypedDict, closed=True):
    locations: NotRequired["capo_datasync.types.location_list.LocationList"]
    """<p>An array that contains a list of locations.</p>"""
    next_token: NotRequired["capo_datasync.types.next_token.NextToken"]
    """<p>An opaque string that indicates the position at which to begin returning the next list of locations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLocationsResponse) -> dict:
    out: dict = {}
    if "locations" in value:
        import capo_datasync.types.location_list

        out["Locations"] = capo_datasync.types.location_list.serialize_aws_json_1_1(
            value["locations"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLocationsResponse:
    out: ListLocationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Locations") is not None:
        import capo_datasync.types.location_list

        out["locations"] = capo_datasync.types.location_list.deserialize_aws_json_1_1(
            data["Locations"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListLocationsResponse) -> dict:
    out: dict = {}
    if "locations" in value:
        import capo_datasync.types.location_list

        out["Locations"] = capo_datasync.types.location_list.serialize_cbor(
            value["locations"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListLocationsResponse:
    out: ListLocationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Locations") is not None:
        import capo_datasync.types.location_list

        out["locations"] = capo_datasync.types.location_list.deserialize_cbor(
            data["Locations"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
