"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeleteRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.rule_identifier


class DeleteRuleInput(TypedDict, closed=True):
    rule_identifier: (
        "capo_network_security_manager.types.rule_identifier.RuleIdentifier"
    )
    """<p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRuleInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRuleInput:
    out: DeleteRuleInput = {}  # type: ignore[typeddict-item]
    return out
