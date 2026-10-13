"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentBlueprintInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.blueprint_category
    import capo_datazone.types.custom_parameter_list
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_blueprint_name
    import capo_datazone.types.provisioning_properties


class CreateEnvironmentBlueprintInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the domain in which this blueprint is created.</p>"""
    name: "capo_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
    """<p>The name of this Amazon DataZone blueprint.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the Amazon DataZone blueprint.</p>"""
    provisioning_properties: (
        "capo_datazone.types.provisioning_properties.ProvisioningProperties"
    )
    """<p>The provisioning properties of this Amazon DataZone blueprint.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters of this Amazon DataZone blueprint.</p>"""
    blueprint_category: NotRequired[
        "capo_datazone.types.blueprint_category.BlueprintCategory"
    ]
    """<p>The category of the Amazon DataZone blueprint. The only valid value is <code>TOOLING</code>, which creates a blueprint that provisions the tooling resources of a project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentBlueprintInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
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


def deserialize_json(data: dict) -> CreateEnvironmentBlueprintInput:
    out: CreateEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentBlueprintInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("provisioningProperties") is not None:
        import capo_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            capo_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEnvironmentBlueprintInput.provisioning_properties required"
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


def redact_sensitive(value: CreateEnvironmentBlueprintInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "user_parameters" in value:
        import capo_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            capo_datazone.types.custom_parameter_list.redact_sensitive(
                value["user_parameters"]
            )
        )
    return out
