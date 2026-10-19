"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_id


class CaseRuleIdentifier(TypedDict, closed=True):
    id: "capo_connectcases.types.case_rule_id.CaseRuleId"
    """<p>Unique identifier of a case rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleIdentifier) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CaseRuleIdentifier:
    out: CaseRuleIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
