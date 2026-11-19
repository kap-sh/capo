"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationActor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class InvestigationActor(TypedDict, closed=True):
    access_key_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The access key ID that the identity used.</p>"""
    principal_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the principal.</p>"""
    user_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the user.</p>"""
    user_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the identity, such as <code>IAMUser</code>, <code>AssumedRole</code>, or <code>Root</code>.</p>"""
    user_agent: NotRequired["capo_guardduty.types.string.String"]
    """<p>The user agent that the identity used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationActor) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["accessKeyId"] = value["access_key_id"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "user_type" in value:
        out["userType"] = value["user_type"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    return out


def deserialize_json(data: dict) -> InvestigationActor:
    out: InvestigationActor = {}  # type: ignore[typeddict-item]
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    if data.get("userType") is not None:
        out["user_type"] = data["userType"]
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    return out
