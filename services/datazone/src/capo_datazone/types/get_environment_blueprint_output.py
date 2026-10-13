"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentBlueprintOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.blueprint_category
    import capo_datazone.types.custom_parameter_list
    import capo_datazone.types.deployment_properties
    import capo_datazone.types.description
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.environment_blueprint_name
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.provisioning_properties


class GetEnvironmentBlueprintOutput(TypedDict, closed=True):
    id: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The ID of this Amazon DataZone blueprint.</p>"""
    name: "capo_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
    """<p>The name of this Amazon DataZone blueprint.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of this Amazon DataZone blueprint.</p>"""
    provider: "str"
    """<p>The provider of this Amazon DataZone blueprint.</p>"""
    provisioning_properties: (
        "capo_datazone.types.provisioning_properties.ProvisioningProperties"
    )
    """<p>The provisioning properties of this Amazon DataZone blueprint.</p>"""
    deployment_properties: NotRequired[
        "capo_datazone.types.deployment_properties.DeploymentProperties"
    ]
    """<p>The deployment properties of this Amazon DataZone blueprint.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters of this blueprint.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms attached to this Amazon DataZone blueprint.</p>"""
    blueprint_category: NotRequired[
        "capo_datazone.types.blueprint_category.BlueprintCategory"
    ]
    """<p>The category of this Amazon DataZone blueprint. The only valid value is <code>TOOLING</code>, which indicates a blueprint that provisions the tooling resources of a project.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>A timestamp of when this blueprint was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when this blueprint was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentBlueprintOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["provider"] = value["provider"]
    import capo_datazone.types.provisioning_properties

    out["provisioningProperties"] = (
        capo_datazone.types.provisioning_properties.serialize_json(
            value["provisioning_properties"]
        )
    )
    if "deployment_properties" in value:
        import capo_datazone.types.deployment_properties

        out["deploymentProperties"] = (
            capo_datazone.types.deployment_properties.serialize_json(
                value["deployment_properties"]
            )
        )
    if "user_parameters" in value:
        import capo_datazone.types.custom_parameter_list

        out["userParameters"] = (
            capo_datazone.types.custom_parameter_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "blueprint_category" in value:
        import capo_datazone.types.blueprint_category

        out["blueprintCategory"] = (
            capo_datazone.types.blueprint_category.serialize_json(
                value["blueprint_category"]
            )
        )
    if "created_at" in value:
        import capo_datazone._protocol.serialize

        out["createdAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone._protocol.serialize

        out["updatedAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetEnvironmentBlueprintOutput:
    out: GetEnvironmentBlueprintOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetEnvironmentBlueprintOutput.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetEnvironmentBlueprintOutput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("GetEnvironmentBlueprintOutput.provider required")
    if data.get("provisioningProperties") is not None:
        import capo_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            capo_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnvironmentBlueprintOutput.provisioning_properties required"
        )
    if data.get("deploymentProperties") is not None:
        import capo_datazone.types.deployment_properties

        out["deployment_properties"] = (
            capo_datazone.types.deployment_properties.deserialize_json(
                data["deploymentProperties"]
            )
        )
    if data.get("userParameters") is not None:
        import capo_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            capo_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("blueprintCategory") is not None:
        import capo_datazone.types.blueprint_category

        out["blueprint_category"] = (
            capo_datazone.types.blueprint_category.deserialize_json(
                data["blueprintCategory"]
            )
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: GetEnvironmentBlueprintOutput) -> dict[str, Any]:
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
