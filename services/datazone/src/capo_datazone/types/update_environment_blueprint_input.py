"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentBlueprintInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.blueprint_category
    import capo_datazone.types.custom_parameter_list
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.provisioning_properties


class UpdateEnvironmentBlueprintInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which an environment blueprint is to be updated.</p>"""
    identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The identifier of the environment blueprint to be updated.</p>"""
    description: NotRequired["str"]
    """<p>The description to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    provisioning_properties: NotRequired[
        "capo_datazone.types.provisioning_properties.ProvisioningProperties"
    ]
    """<p>The provisioning properties to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    blueprint_category: NotRequired[
        "capo_datazone.types.blueprint_category.BlueprintCategory"
    ]
    """<p>The category to update. The only valid value is <code>TOOLING</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentBlueprintInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "provisioning_properties" in value:
        import capo_datazone.types.provisioning_properties

        out["provisioningProperties"] = (
            capo_datazone.types.provisioning_properties.serialize_json(
                value["provisioning_properties"]
            )
        )
    if "user_parameters" in value:
        import capo_datazone.types.custom_parameter_list

        out["userParameters"] = (
            capo_datazone.types.custom_parameter_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "blueprint_category" in value:
        import capo_datazone.types.blueprint_category

        out["blueprintCategory"] = (
            capo_datazone.types.blueprint_category.serialize_json(
                value["blueprint_category"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentBlueprintInput:
    out: UpdateEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("provisioningProperties") is not None:
        import capo_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            capo_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    if data.get("userParameters") is not None:
        import capo_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            capo_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    if data.get("blueprintCategory") is not None:
        import capo_datazone.types.blueprint_category

        out["blueprint_category"] = (
            capo_datazone.types.blueprint_category.deserialize_json(
                data["blueprintCategory"]
            )
        )
    return out


def redact_sensitive(value: UpdateEnvironmentBlueprintInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_parameters" in value:
        import capo_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            capo_datazone.types.custom_parameter_list.redact_sensitive(
                value["user_parameters"]
            )
        )
    return out
