"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CidrAuthorizationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string


class CidrAuthorizationContext(TypedDict, closed=True):
    message: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The plain-text authorization message for the prefix and account.</p>"""
    signature: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The signed authorization message for the prefix and account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CidrAuthorizationContext) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    out["Signature"] = value["signature"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CidrAuthorizationContext:
    out: CidrAuthorizationContext = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Signature") is not None:
        out["signature"] = data["Signature"]
    else:
        out["signature"] = ""
    return out
