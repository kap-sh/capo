"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentBlueprintOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

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


class UpdateEnvironmentBlueprintOutput(TypedDict, closed=True):
    id: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The identifier of the blueprint to be updated.</p>"""
    name: "capo_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
    """<p>The name to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    provider: "str"
    """<p>The provider of the blueprint to be udpated.</p>"""
    provisioning_properties: (
        "capo_datazone.types.provisioning_properties.ProvisioningProperties"
    )
    """<p>The provisioning properties to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    deployment_properties: NotRequired[
        "capo_datazone.types.deployment_properties.DeploymentProperties"
    ]
    """<p>The deployment properties to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    blueprint_category: NotRequired[
        "capo_datazone.types.blueprint_category.BlueprintCategory"
    ]
    """<p>The category of the environment blueprint. The only valid value is <code>TOOLING</code>.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment blueprint was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the blueprint was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentBlueprintOutput) -> dict:
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


def deserialize_json(data: dict) -> UpdateEnvironmentBlueprintOutput:
    out: UpdateEnvironmentBlueprintOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("provisioningProperties") is not None:
        import capo_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            capo_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    else:
        out["provisioning_properties"] = {"$unknown": {"name": ""}}
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


def redact_sensitive(value: UpdateEnvironmentBlueprintOutput) -> dict[str, Any]:
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
