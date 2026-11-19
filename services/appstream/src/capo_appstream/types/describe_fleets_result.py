"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeFleetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.fleet_list
    import capo_appstream.types.string


class DescribeFleetsResult(TypedDict, closed=True):
    fleets: NotRequired["capo_appstream.types.fleet_list.FleetList"]
    """<p>Information about the fleets.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetsResult) -> dict:
    out: dict = {}
    if "fleets" in value:
        import capo_appstream.types.fleet_list

        out["Fleets"] = capo_appstream.types.fleet_list.serialize_aws_json_1_1(
            value["fleets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetsResult:
    out: DescribeFleetsResult = {}  # type: ignore[typeddict-item]
    if data.get("Fleets") is not None:
        import capo_appstream.types.fleet_list

        out["fleets"] = capo_appstream.types.fleet_list.deserialize_aws_json_1_1(
            data["Fleets"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeFleetsResult) -> dict:
    out: dict = {}
    if "fleets" in value:
        import capo_appstream.types.fleet_list

        out["Fleets"] = capo_appstream.types.fleet_list.serialize_cbor(value["fleets"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeFleetsResult:
    out: DescribeFleetsResult = {}  # type: ignore[typeddict-item]
    if data.get("Fleets") is not None:
        import capo_appstream.types.fleet_list

        out["fleets"] = capo_appstream.types.fleet_list.deserialize_cbor(data["Fleets"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
