"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesResourceFieldsUpdateV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.resource_criticality


class AutomationRulesResourceFieldsUpdateV2(TypedDict, closed=True):
    criticality: NotRequired[
        "capo_securityhub.types.resource_criticality.ResourceCriticality"
    ]
    """<p>The criticality level to be assigned to resources that match the automation rule criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesResourceFieldsUpdateV2) -> dict:
    out: dict = {}
    if "criticality" in value:
        import capo_securityhub.types.resource_criticality

        out["Criticality"] = capo_securityhub.types.resource_criticality.serialize_json(
            value["criticality"]
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesResourceFieldsUpdateV2:
    out: AutomationRulesResourceFieldsUpdateV2 = {}  # type: ignore[typeddict-item]
    if data.get("Criticality") is not None:
        import capo_securityhub.types.resource_criticality

        out["criticality"] = (
            capo_securityhub.types.resource_criticality.deserialize_json(
                data["Criticality"]
            )
        )
    return out
