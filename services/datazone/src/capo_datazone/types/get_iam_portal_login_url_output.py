"""Generated from Smithy shape ``com.amazonaws.datazone#GetIamPortalLoginUrlOutput``."""

from typing_extensions import NotRequired, TypedDict


class GetIamPortalLoginUrlOutput(TypedDict, closed=True):
    auth_code_url: NotRequired["str"]
    """<p>The data portal URL of the specified Amazon DataZone domain.</p>"""
    user_profile_id: "str"
    """<p>The ID of the user profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIamPortalLoginUrlOutput) -> dict:
    out: dict = {}
    if "auth_code_url" in value:
        out["authCodeUrl"] = value["auth_code_url"]
    out["userProfileId"] = value["user_profile_id"]
    return out


def deserialize_json(data: dict) -> GetIamPortalLoginUrlOutput:
    out: GetIamPortalLoginUrlOutput = {}  # type: ignore[typeddict-item]
    if data.get("authCodeUrl") is not None:
        out["auth_code_url"] = data["authCodeUrl"]
    if data.get("userProfileId") is not None:
        out["user_profile_id"] = data["userProfileId"]
    else:
        out["user_profile_id"] = ""
    return out
