"""Generated from Smithy shape ``com.amazonaws.licensemanager#ScriptRuleStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class ScriptRuleStatement(TypedDict, closed=True):
    key_to_match: "capo_license_manager.types.string.String"
    """<p>Key name to match against in the script rule evaluation.</p>"""
    script: "capo_license_manager.types.string.String"
    """<p>Script code used to evaluate the rule condition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScriptRuleStatement) -> dict:
    out: dict = {}
    out["KeyToMatch"] = value["key_to_match"]
    out["Script"] = value["script"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScriptRuleStatement:
    out: ScriptRuleStatement = {}  # type: ignore[typeddict-item]
    if data.get("KeyToMatch") is not None:
        out["key_to_match"] = data["KeyToMatch"]
    else:
        out["key_to_match"] = ""
    if data.get("Script") is not None:
        out["script"] = data["Script"]
    else:
        out["script"] = ""
    return out
