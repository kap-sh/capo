"""Generated from Smithy shape ``com.amazonaws.transfer#CreateProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.profile_id


class CreateProfileResponse(TypedDict, closed=True):
    profile_id: "capo_transfer.types.profile_id.ProfileId"
    """<p>The unique identifier for the AS2 profile, returned after the API call succeeds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProfileResponse) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProfileResponse:
    out: CreateProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    return out
