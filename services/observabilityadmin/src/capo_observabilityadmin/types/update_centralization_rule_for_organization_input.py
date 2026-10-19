"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#UpdateCentralizationRuleForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.centralization_rule
    import capo_observabilityadmin.types.rule_identifier


class UpdateCentralizationRuleForOrganizationInput(TypedDict, closed=True):
    rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier"
    """<p>The identifier (name or ARN) of the organization centralization rule to update.</p>"""
    rule: "capo_observabilityadmin.types.centralization_rule.CentralizationRule"
    """<p>The configuration details for the organization-wide centralization rule, including the source configuration and the destination configuration to centralize telemetry data across the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCentralizationRuleForOrganizationInput) -> dict:
    out: dict = {}
    out["RuleIdentifier"] = value["rule_identifier"]
    import capo_observabilityadmin.types.centralization_rule

    out["Rule"] = capo_observabilityadmin.types.centralization_rule.serialize_json(
        value["rule"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCentralizationRuleForOrganizationInput:
    out: UpdateCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("RuleIdentifier") is not None:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        out["rule_identifier"] = ""
    if data.get("Rule") is not None:
        import capo_observabilityadmin.types.centralization_rule

        out["rule"] = (
            capo_observabilityadmin.types.centralization_rule.deserialize_json(
                data["Rule"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCentralizationRuleForOrganizationInput.rule required"
        )
    return out
