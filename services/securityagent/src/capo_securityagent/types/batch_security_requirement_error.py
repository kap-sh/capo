"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchSecurityRequirementError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_name


class BatchSecurityRequirementError(TypedDict, closed=True):
    security_requirement_name: (
        "capo_securityagent.types.security_requirement_name.SecurityRequirementName"
    )
    """<p>The name of the security requirement that caused the error.</p>"""
    code: "str"
    """<p>The error code.</p>"""
    message: "str"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchSecurityRequirementError) -> dict:
    out: dict = {}
    out["securityRequirementName"] = value["security_requirement_name"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchSecurityRequirementError:
    out: BatchSecurityRequirementError = {}  # type: ignore[typeddict-item]
    if data.get("securityRequirementName") is not None:
        out["security_requirement_name"] = data["securityRequirementName"]
    else:
        out["security_requirement_name"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
