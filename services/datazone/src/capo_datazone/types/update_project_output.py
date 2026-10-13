"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateProjectOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.environment_configuration_user_parameters_list
    import capo_datazone.types.environment_deployment_details
    import capo_datazone.types.failure_reasons
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.project_id
    import capo_datazone.types.project_name
    import capo_datazone.types.project_profile_id
    import capo_datazone.types.project_status
    import capo_datazone.types.resource_tags


class UpdateProjectOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a project is updated.</p>"""
    id: "capo_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that is to be updated.</p>"""
    name: "capo_datazone.types.project_name.ProjectName"
    """<p>The name of the project that is to be updated.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the project that is to be updated.</p>"""
    project_status: NotRequired["capo_datazone.types.project_status.ProjectStatus"]
    """<p>The status of the project.</p>"""
    failure_reasons: NotRequired["capo_datazone.types.failure_reasons.FailureReasons"]
    """<p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>The Amazon DataZone user who created the project.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the project was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the project was last updated.</p>"""
    resource_tags: NotRequired["capo_datazone.types.resource_tags.ResourceTags"]
    """<p>The resource tags of the project.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms of the project that are to be updated.</p>"""
    domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit.</p>"""
    project_profile_id: NotRequired[
        "capo_datazone.types.project_profile_id.ProjectProfileId"
    ]
    """<p>The ID of the project profile.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
    ]
    """<p>The user parameters of the project.</p>"""
    environment_deployment_details: NotRequired[
        "capo_datazone.types.environment_deployment_details.EnvironmentDeploymentDetails"
    ]
    """<p>The environment deployment details of the project.</p>"""
    project_category: NotRequired["str"]
    """<p>The category of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProjectOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "project_status" in value:
        import capo_datazone.types.project_status

        out["projectStatus"] = capo_datazone.types.project_status.serialize_json(
            value["project_status"]
        )
    if "failure_reasons" in value:
        import capo_datazone.types.failure_reasons

        out["failureReasons"] = capo_datazone.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    out["createdBy"] = value["created_by"]
    if "created_at" in value:
        import capo_datazone._protocol.serialize

        out["createdAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_datazone._protocol.serialize

        out["lastUpdatedAt"] = capo_datazone._protocol.serialize.fmt_date_time(
            value["last_updated_at"]
        )
    if "resource_tags" in value:
        import capo_datazone.types.resource_tags

        out["resourceTags"] = capo_datazone.types.resource_tags.serialize_json(
            value["resource_tags"]
        )
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    if "project_profile_id" in value:
        out["projectProfileId"] = value["project_profile_id"]
    if "user_parameters" in value:
        import capo_datazone.types.environment_configuration_user_parameters_list

        out["userParameters"] = (
            capo_datazone.types.environment_configuration_user_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "environment_deployment_details" in value:
        import capo_datazone.types.environment_deployment_details

        out["environmentDeploymentDetails"] = (
            capo_datazone.types.environment_deployment_details.serialize_json(
                value["environment_deployment_details"]
            )
        )
    if "project_category" in value:
        out["projectCategory"] = value["project_category"]
    return out


def deserialize_json(data: dict) -> UpdateProjectOutput:
    out: UpdateProjectOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("UpdateProjectOutput.domain_id required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateProjectOutput.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateProjectOutput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("projectStatus") is not None:
        import capo_datazone.types.project_status

        out["project_status"] = capo_datazone.types.project_status.deserialize_json(
            data["projectStatus"]
        )
    if data.get("failureReasons") is not None:
        import capo_datazone.types.failure_reasons

        out["failure_reasons"] = capo_datazone.types.failure_reasons.deserialize_json(
            data["failureReasons"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("UpdateProjectOutput.created_by required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("lastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["lastUpdatedAt"].replace("Z", "+00:00")
        )
    if data.get("resourceTags") is not None:
        import capo_datazone.types.resource_tags

        out["resource_tags"] = capo_datazone.types.resource_tags.deserialize_json(
            data["resourceTags"]
        )
    if data.get("glossaryTerms") is not None:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if data.get("domainUnitId") is not None:
        out["domain_unit_id"] = data["domainUnitId"]
    if data.get("projectProfileId") is not None:
        out["project_profile_id"] = data["projectProfileId"]
    if data.get("userParameters") is not None:
        import capo_datazone.types.environment_configuration_user_parameters_list

        out["user_parameters"] = (
            capo_datazone.types.environment_configuration_user_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if data.get("environmentDeploymentDetails") is not None:
        import capo_datazone.types.environment_deployment_details

        out["environment_deployment_details"] = (
            capo_datazone.types.environment_deployment_details.deserialize_json(
                data["environmentDeploymentDetails"]
            )
        )
    if data.get("projectCategory") is not None:
        out["project_category"] = data["projectCategory"]
    return out


def redact_sensitive(value: UpdateProjectOutput) -> dict[str, Any]:
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
