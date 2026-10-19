"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#UpdateTelemetryRuleForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.rule_identifier
    import capo_observabilityadmin.types.telemetry_rule


class UpdateTelemetryRuleForOrganizationInput(TypedDict, closed=True):
    rule_identifier: "capo_observabilityadmin.types.rule_identifier.RuleIdentifier"
    """<p> The identifier (name or ARN) of the organization telemetry rule to update. </p>"""
    rule: "capo_observabilityadmin.types.telemetry_rule.TelemetryRule"
    """<p> The new configuration details for the organization telemetry rule, including resource type, telemetry type, and destination configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTelemetryRuleForOrganizationInput) -> dict:
    out: dict = {}
    out["RuleIdentifier"] = value["rule_identifier"]
    import capo_observabilityadmin.types.telemetry_rule

    out["Rule"] = capo_observabilityadmin.types.telemetry_rule.serialize_json(
        value["rule"]
    )
    return out


def deserialize_json(data: dict) -> UpdateTelemetryRuleForOrganizationInput:
    out: UpdateTelemetryRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("RuleIdentifier") is not None:
        out["rule_identifier"] = data["RuleIdentifier"]
    else:
        out["rule_identifier"] = ""
    if data.get("Rule") is not None:
        import capo_observabilityadmin.types.telemetry_rule

        out["rule"] = capo_observabilityadmin.types.telemetry_rule.deserialize_json(
            data["Rule"]
        )
    else:
        raise DeserializationError(
            "UpdateTelemetryRuleForOrganizationInput.rule required"
        )
    return out
