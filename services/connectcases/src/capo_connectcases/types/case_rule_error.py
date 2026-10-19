"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_id


class CaseRuleError(TypedDict, closed=True):
    id: "capo_connectcases.types.case_rule_id.CaseRuleId"
    """<p>The case rule identifier that caused the error.</p>"""
    error_code: "str"
    """<p>Error code from getting a case rule.</p>"""
    message: NotRequired["str"]
    """<p>Error message from getting a case rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleError) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CaseRuleError:
    out: CaseRuleError = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
