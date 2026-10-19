"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DeleteCentralizationRuleForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.rule_identifier


class DeleteCentralizationRuleForOrganizationInput(TypedDict, closed=True):
    rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier"
    """<p>The identifier (name or ARN) of the organization centralization rule to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCentralizationRuleForOrganizationInput) -> dict:
    out: dict = {}
    out["RuleIdentifier"] = value["rule_identifier"]
    return out


def deserialize_json(data: dict) -> DeleteCentralizationRuleForOrganizationInput:
    out: DeleteCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("RuleIdentifier") is not None:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        out["rule_identifier"] = ""
    return out
