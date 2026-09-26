"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#RuleReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.rule_identifier


class RuleReference(TypedDict, closed=True):
    rule_identifier: (
        "capo_network_security_manager.types.rule_identifier.RuleIdentifier"
    )
    """<p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleReference) -> dict:
    out: dict = {}
    out["ruleIdentifier"] = value["rule_identifier"]
    return out


def deserialize_json(data: dict) -> RuleReference:
    out: RuleReference = {}  # type: ignore[typeddict-item]
    if data.get("ruleIdentifier") is not None:
        out["rule_identifier"] = data["ruleIdentifier"]
    else:
        raise DeserializationError("RuleReference.rule_identifier required")
    return out
