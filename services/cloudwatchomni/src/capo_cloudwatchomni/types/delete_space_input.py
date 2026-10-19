"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DeleteSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.space_id


class DeleteSpaceInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space to delete."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteSpaceInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteSpaceInput:
    out: DeleteSpaceInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    return out
