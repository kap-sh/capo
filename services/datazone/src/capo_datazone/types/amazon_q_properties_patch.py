"""Generated from Smithy shape ``com.amazonaws.datazone#AmazonQPropertiesPatch``."""

from typing_extensions import NotRequired, TypedDict


class AmazonQPropertiesPatch(TypedDict, closed=True):
    is_enabled: "bool"
    """<p>Specifies whether Amazon Q is enabled for the connection.</p>"""
    profile_arn: NotRequired["str"]
    """<p>The profile ARN of the connection's Amazon Q properties.</p>"""
    auth_mode: NotRequired["str"]
    """<p>The authentication mode of the connection's Amazon Q properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmazonQPropertiesPatch) -> dict:
    out: dict = {}
    out["isEnabled"] = value["is_enabled"]
    if "profile_arn" in value:
        out["profileArn"] = value["profile_arn"]
    if "auth_mode" in value:
        out["authMode"] = value["auth_mode"]
    return out


def deserialize_json(data: dict) -> AmazonQPropertiesPatch:
    out: AmazonQPropertiesPatch = {}  # type: ignore[typeddict-item]
    if data.get("isEnabled") is not None:
        out["is_enabled"] = data["isEnabled"]
    else:
        out["is_enabled"] = False
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    if data.get("authMode") is not None:
        out["auth_mode"] = data["authMode"]
    return out
