"""Generated from Smithy shape ``com.amazonaws.gamelift#ListFleetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.fleet_id_list
    import capo_gamelift.types.non_zero_and_max_string


class ListFleetsOutput(TypedDict, closed=True):
    fleet_ids: NotRequired["capo_gamelift.types.fleet_id_list.FleetIdList"]
    """<p>A set of fleet IDs that match the list request.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFleetsOutput) -> dict:
    out: dict = {}
    if "fleet_ids" in value:
        import capo_gamelift.types.fleet_id_list

        out["FleetIds"] = capo_gamelift.types.fleet_id_list.serialize_aws_json_1_1(
            value["fleet_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFleetsOutput:
    out: ListFleetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetIds") is not None:
        import capo_gamelift.types.fleet_id_list

        out["fleet_ids"] = capo_gamelift.types.fleet_id_list.deserialize_aws_json_1_1(
            data["FleetIds"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListFleetsOutput) -> dict:
    out: dict = {}
    if "fleet_ids" in value:
        import capo_gamelift.types.fleet_id_list

        out["FleetIds"] = capo_gamelift.types.fleet_id_list.serialize_cbor(
            value["fleet_ids"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListFleetsOutput:
    out: ListFleetsOutput = {}  # type: ignore[typeddict-item]
    if data.get("FleetIds") is not None:
        import capo_gamelift.types.fleet_id_list

        out["fleet_ids"] = capo_gamelift.types.fleet_id_list.deserialize_cbor(
            data["FleetIds"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
