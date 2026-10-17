"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_action_type_v2
    import capo_securityhub.types.automation_rules_finding_fields_update_v2
    import capo_securityhub.types.external_integration_configuration


class AutomationRulesActionV2(TypedDict, closed=True):
    type: NotRequired[
        "capo_securityhub.types.automation_rules_action_type_v2.AutomationRulesActionTypeV2"
    ]
    """<p>The category of action to be executed by the automation rule.</p>"""
    finding_fields_update: NotRequired[
        "capo_securityhub.types.automation_rules_finding_fields_update_v2.AutomationRulesFindingFieldsUpdateV2"
    ]
    """<p>The changes to be applied to fields in a security finding when an automation rule is triggered.</p>"""
    external_integration_configuration: NotRequired[
        "capo_securityhub.types.external_integration_configuration.ExternalIntegrationConfiguration"
    ]
    """<p>The settings for integrating automation rule actions with external systems or service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesActionV2) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_securityhub.types.automation_rules_action_type_v2

        out["Type"] = (
            capo_securityhub.types.automation_rules_action_type_v2.serialize_json(
                value["type"]
            )
        )
    if "finding_fields_update" in value:
        import capo_securityhub.types.automation_rules_finding_fields_update_v2

        out["FindingFieldsUpdate"] = (
            capo_securityhub.types.automation_rules_finding_fields_update_v2.serialize_json(
                value["finding_fields_update"]
            )
        )
    if "external_integration_configuration" in value:
        import capo_securityhub.types.external_integration_configuration

        out["ExternalIntegrationConfiguration"] = (
            capo_securityhub.types.external_integration_configuration.serialize_json(
                value["external_integration_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesActionV2:
    out: AutomationRulesActionV2 = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_securityhub.types.automation_rules_action_type_v2

        out["type"] = (
            capo_securityhub.types.automation_rules_action_type_v2.deserialize_json(
                data["Type"]
            )
        )
    if data.get("FindingFieldsUpdate") is not None:
        import capo_securityhub.types.automation_rules_finding_fields_update_v2

        out["finding_fields_update"] = (
            capo_securityhub.types.automation_rules_finding_fields_update_v2.deserialize_json(
                data["FindingFieldsUpdate"]
            )
        )
    if data.get("ExternalIntegrationConfiguration") is not None:
        import capo_securityhub.types.external_integration_configuration

        out["external_integration_configuration"] = (
            capo_securityhub.types.external_integration_configuration.deserialize_json(
                data["ExternalIntegrationConfiguration"]
            )
        )
    return out
