"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#GetRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.rule_identifier


class GetRuleInput(TypedDict, closed=True):
    rule_identifier: (
        "capo_network_security_manager.types.rule_identifier.RuleIdentifier"
    )
    """<p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRuleInput:
    out: GetRuleInput = {}  # type: ignore[typeddict-item]
    return out
