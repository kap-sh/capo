"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateCentralizationRuleForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.centralization_rule
    import capo_observabilityadmin.types.rule_name
    import capo_observabilityadmin.types.tag_map_input


class CreateCentralizationRuleForOrganizationInput(TypedDict, closed=True):
    rule_name: "capo_observabilityadmin.types.rule_name.RuleName"
    """<p>A unique name for the organization-wide centralization rule being created.</p>"""
    rule: "capo_observabilityadmin.types.centralization_rule.CentralizationRule"
    """<p>The configuration details for the organization-wide centralization rule, including the source configuration and the destination configuration to centralize telemetry data across the organization.</p>"""
    tags: NotRequired["capo_observabilityadmin.types.tag_map_input.TagMapInput"]
    """<p>The key-value pairs to associate with the organization telemetry rule resource for categorization and management purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCentralizationRuleForOrganizationInput) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    import capo_observabilityadmin.types.centralization_rule

    out["Rule"] = capo_observabilityadmin.types.centralization_rule.serialize_json(
        value["rule"]
    )
    if "tags" in value:
        import capo_observabilityadmin.types.tag_map_input

        out["Tags"] = capo_observabilityadmin.types.tag_map_input.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCentralizationRuleForOrganizationInput:
    out: CreateCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    else:
        out["rule_name"] = ""
    if data.get("Rule") is not None:
        import capo_observabilityadmin.types.centralization_rule

        out["rule"] = (
            capo_observabilityadmin.types.centralization_rule.deserialize_json(
                data["Rule"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCentralizationRuleForOrganizationInput.rule required"
        )
    if data.get("Tags") is not None:
        import capo_observabilityadmin.types.tag_map_input

        out["tags"] = capo_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    return out
