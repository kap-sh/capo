"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetAccessProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.profile_id
    import capo_cloudwatchomni.types.space_id


class GetAccessProfileInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    profile_id: "capo_cloudwatchomni.types.profile_id.ProfileId"
    """The unique ID of the access profile."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAccessProfileInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["profileId"] = value["profile_id"]
    return out


def deserialize_cbor(data: dict) -> GetAccessProfileInput:
    out: GetAccessProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    return out
