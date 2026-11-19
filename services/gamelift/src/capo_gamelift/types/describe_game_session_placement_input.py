"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameSessionPlacementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.id_string_model


class DescribeGameSessionPlacementInput(TypedDict, closed=True):
    placement_id: NotRequired["capo_gamelift.types.id_string_model.IdStringModel"]
    """<p>A unique identifier for a game session placement to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameSessionPlacementInput) -> dict:
    out: dict = {}
    if "placement_id" in value:
        out["PlacementId"] = value["placement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameSessionPlacementInput:
    out: DescribeGameSessionPlacementInput = {}  # type: ignore[typeddict-item]
    if data.get("PlacementId") is not None:
        out["placement_id"] = data["PlacementId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeGameSessionPlacementInput) -> dict:
    out: dict = {}
    if "placement_id" in value:
        out["PlacementId"] = value["placement_id"]
    return out


def deserialize_cbor(data: dict) -> DescribeGameSessionPlacementInput:
    out: DescribeGameSessionPlacementInput = {}  # type: ignore[typeddict-item]
    if data.get("PlacementId") is not None:
        out["placement_id"] = data["PlacementId"]
    return out
