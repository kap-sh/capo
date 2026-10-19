"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.space_id


class GetSpaceInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSpaceInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    return out


def deserialize_cbor(data: dict) -> GetSpaceInput:
    out: GetSpaceInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    return out
