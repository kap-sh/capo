"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateProjectInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.environment_configuration_user_parameters_list
    import capo_datazone.types.environment_deployment_details
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.project_id
    import capo_datazone.types.project_name
    import capo_datazone.types.tags


class UpdateProjectInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where a project is being updated.</p>"""
    identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that is to be updated.</p>"""
    name: NotRequired["capo_datazone.types.project_name.ProjectName"]
    """<p>The name to be updated as part of the <code>UpdateProject</code> action.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description to be updated as part of the <code>UpdateProject</code> action.</p>"""
    resource_tags: NotRequired["capo_datazone.types.tags.Tags"]
    """<p>The resource tags of the project.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms to be updated as part of the <code>UpdateProject</code> action.</p>"""
    domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit.</p>"""
    environment_deployment_details: NotRequired[
        "capo_datazone.types.environment_deployment_details.EnvironmentDeploymentDetails"
    ]
    """<p>The environment deployment details of the project.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
    ]
    """<p>The user parameters of the project.</p>"""
    project_profile_version: NotRequired["str"]
    """<p>The project profile version to which the project should be updated. You can only specify the following string for this parameter: <code>latest</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "resource_tags" in value:
        import capo_datazone.types.tags

        out["resourceTags"] = capo_datazone.types.tags.serialize_json(
            value["resource_tags"]
        )
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    if "environment_deployment_details" in value:
        import capo_datazone.types.environment_deployment_details

        out["environmentDeploymentDetails"] = (
            capo_datazone.types.environment_deployment_details.serialize_json(
                value["environment_deployment_details"]
            )
        )
    if "user_parameters" in value:
        import capo_datazone.types.environment_configuration_user_parameters_list

        out["userParameters"] = (
            capo_datazone.types.environment_configuration_user_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "project_profile_version" in value:
        out["projectProfileVersion"] = value["project_profile_version"]
    return out


def deserialize_json(data: dict) -> UpdateProjectInput:
    out: UpdateProjectInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("resourceTags") is not None:
        import capo_datazone.types.tags

        out["resource_tags"] = capo_datazone.types.tags.deserialize_json(
            data["resourceTags"]
        )
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("domainUnitId") is not None:
        out["domain_unit_id"] = data["domainUnitId"]
    if data.get("environmentDeploymentDetails") is not None:
        import capo_datazone.types.environment_deployment_details

        out["environment_deployment_details"] = (
            capo_datazone.types.environment_deployment_details.deserialize_json(
                data["environmentDeploymentDetails"]
            )
        )
    if data.get("userParameters") is not None:
        import capo_datazone.types.environment_configuration_user_parameters_list

        out["user_parameters"] = (
            capo_datazone.types.environment_configuration_user_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if data.get("projectProfileVersion") is not None:
        out["project_profile_version"] = data["projectProfileVersion"]
    return out


def redact_sensitive(value: UpdateProjectInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "user_parameters" in value:
        import capo_datazone.types.environment_configuration_user_parameters_list

        out["user_parameters"] = (
            capo_datazone.types.environment_configuration_user_parameters_list.redact_sensitive(
                value["user_parameters"]
            )
        )
    return out
