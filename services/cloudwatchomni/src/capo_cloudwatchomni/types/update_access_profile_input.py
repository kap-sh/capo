"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateAccessProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.access_profile_name
    import capo_cloudwatchomni.types.profile_id
    import capo_cloudwatchomni.types.space_id


class UpdateAccessProfileInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    profile_id: "capo_cloudwatchomni.types.profile_id.ProfileId"
    """The unique ID of the access profile to update."""
    name: NotRequired["capo_cloudwatchomni.types.access_profile_name.AccessProfileName"]
    """A new name for the access profile. Omit to leave unchanged."""
    description: NotRequired["str"]
    """A new description of the access profile. Omit to leave unchanged."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateAccessProfileInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["profileId"] = value["profile_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> UpdateAccessProfileInput:
    out: UpdateAccessProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
