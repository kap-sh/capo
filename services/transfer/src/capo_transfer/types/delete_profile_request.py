"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.profile_id


class DeleteProfileRequest(TypedDict, closed=True):
    profile_id: "capo_transfer.types.profile_id.ProfileId"
    """<p>The identifier of the profile that you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProfileRequest:
    out: DeleteProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    return out
