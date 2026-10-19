"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateLimitsProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.profile_id
    import capo_quicksight.types.resource_arn


class CreateLimitsProfileResponse(TypedDict, closed=True):
    arn: "capo_quicksight.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the created limits profile.</p>"""
    profile_id: "capo_quicksight.types.profile_id.ProfileId"
    """<p>The unique identifier for the created limits profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLimitsProfileResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["profileId"] = value["profile_id"]
    return out


def deserialize_json(data: dict) -> CreateLimitsProfileResponse:
    out: CreateLimitsProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    return out
