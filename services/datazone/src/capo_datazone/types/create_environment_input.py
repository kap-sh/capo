"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_configuration_name
    import capo_datazone.types.environment_parameters_list
    import capo_datazone.types.environment_profile_id
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.project_id


class CreateEnvironmentInput(TypedDict, closed=True):
    project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the Amazon DataZone project in which this environment is created.</p>"""
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the environment is created.</p>"""
    description: NotRequired["str"]
    """<p>The description of the Amazon DataZone environment.</p>"""
    name: "str"
    """<p>The name of the Amazon DataZone environment.</p>"""
    environment_profile_identifier: NotRequired[
        "capo_datazone.types.environment_profile_id.EnvironmentProfileId"
    ]
    """<p>The identifier of the environment profile that is used to create this Amazon DataZone environment.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.environment_parameters_list.EnvironmentParametersList"
    ]
    """<p>The user parameters of this Amazon DataZone environment.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms that can be used in this Amazon DataZone environment.</p>"""
    environment_account_identifier: NotRequired["str"]
    """<p>The ID of the account in which the environment is being created.</p>"""
    environment_account_region: NotRequired["str"]
    """<p>The region of the account in which the environment is being created.</p>"""
    environment_blueprint_identifier: NotRequired["str"]
    """<p>The ID of the blueprint with which the environment is being created.</p> <note> <p>This parameter is only valid for V1 domains. If provided for a V2 domain, the service returns a ValidationException.</p> </note>"""
    deployment_order: NotRequired["int"]
    """<p>The deployment order of the environment.</p>"""
    environment_configuration_id: NotRequired["str"]
    """<p>The configuration ID of the environment.</p>"""
    environment_configuration_name: NotRequired[
        "capo_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The configuration name of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentInput) -> dict:
    out: dict = {}
    out["projectIdentifier"] = value["project_identifier"]
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    if "environment_profile_identifier" in value:
        out["environmentProfileIdentifier"] = value["environment_profile_identifier"]
    if "user_parameters" in value:
        import capo_datazone.types.environment_parameters_list

        out["userParameters"] = (
            capo_datazone.types.environment_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "environment_account_identifier" in value:
        out["environmentAccountIdentifier"] = value["environment_account_identifier"]
    if "environment_account_region" in value:
        out["environmentAccountRegion"] = value["environment_account_region"]
    if "environment_blueprint_identifier" in value:
        out["environmentBlueprintIdentifier"] = value[
            "environment_blueprint_identifier"
        ]
    if "deployment_order" in value:
        out["deploymentOrder"] = value["deployment_order"]
    if "environment_configuration_id" in value:
        out["environmentConfigurationId"] = value["environment_configuration_id"]
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentInput:
    out: CreateEnvironmentInput = {}  # type: ignore[typeddict-item]
    if data.get("projectIdentifier") is not None:
        out["project_identifier"] = data["projectIdentifier"]
    else:
        raise DeserializationError("CreateEnvironmentInput.project_identifier required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentInput.name required")
    if data.get("environmentProfileIdentifier") is not None:
        out["environment_profile_identifier"] = data["environmentProfileIdentifier"]
    if data.get("userParameters") is not None:
        import capo_datazone.types.environment_parameters_list

        out["user_parameters"] = (
            capo_datazone.types.environment_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("environmentAccountIdentifier") is not None:
        out["environment_account_identifier"] = data["environmentAccountIdentifier"]
    if data.get("environmentAccountRegion") is not None:
        out["environment_account_region"] = data["environmentAccountRegion"]
    if data.get("environmentBlueprintIdentifier") is not None:
        out["environment_blueprint_identifier"] = data["environmentBlueprintIdentifier"]
    if data.get("deploymentOrder") is not None:
        out["deployment_order"] = data["deploymentOrder"]
    if data.get("environmentConfigurationId") is not None:
        out["environment_configuration_id"] = data["environmentConfigurationId"]
    if data.get("environmentConfigurationName") is not None:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    return out


def redact_sensitive(value: CreateEnvironmentInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environment_configuration_name" in value:
        out["environment_configuration_name"] = "*** Sensitive Data Redacted ***"
    return out
