"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.uuid


class CreateProfileResponse(TypedDict, closed=True):
    profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of a customer profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileResponse) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_json(data: dict) -> CreateProfileResponse:
    out: CreateProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    return out
