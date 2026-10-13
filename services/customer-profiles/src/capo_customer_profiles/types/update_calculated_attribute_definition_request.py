"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateCalculatedAttributeDefinitionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.conditions
    import capo_customer_profiles.types.display_name
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.type_name


class UpdateCalculatedAttributeDefinitionRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the calculated attribute.</p>"""
    display_name: NotRequired["capo_customer_profiles.types.display_name.displayName"]
    """<p>The display name of the calculated attribute.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the calculated attribute.</p>"""
    conditions: NotRequired["capo_customer_profiles.types.conditions.Conditions"]
    """<p>The conditions including range, object count, and threshold for the calculated attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCalculatedAttributeDefinitionRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "conditions" in value:
        import capo_customer_profiles.types.conditions

        out["Conditions"] = capo_customer_profiles.types.conditions.serialize_json(
            value["conditions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCalculatedAttributeDefinitionRequest:
    out: UpdateCalculatedAttributeDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Conditions") is not None:
        import capo_customer_profiles.types.conditions

        out["conditions"] = capo_customer_profiles.types.conditions.deserialize_json(
            data["Conditions"]
        )
    return out


def redact_sensitive(
    value: UpdateCalculatedAttributeDefinitionRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "conditions" in value:
        out["conditions"] = "*** Sensitive Data Redacted ***"
    return out
