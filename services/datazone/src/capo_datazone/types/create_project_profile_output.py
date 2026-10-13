"""Generated from Smithy shape ``com.amazonaws.datazone#CreateProjectProfileOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.created_by
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.environment_configurations_list
    import capo_datazone.types.project_profile_id
    import capo_datazone.types.project_profile_name
    import capo_datazone.types.project_resource_tag_parameters
    import capo_datazone.types.status


class CreateProjectProfileOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where a project profile is created.</p>"""
    id: "capo_datazone.types.project_profile_id.ProjectProfileId"
    """<p>Project profile ID.</p>"""
    name: "capo_datazone.types.project_profile_name.ProjectProfileName"
    """<p>Project profile name.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>A project profile description.</p>"""
    status: NotRequired["capo_datazone.types.status.Status"]
    """<p>Project profile status.</p>"""
    project_resource_tags: NotRequired[
        "capo_datazone.types.project_resource_tag_parameters.ProjectResourceTagParameters"
    ]
    """<p>The resource tags of the project profile.</p>"""
    allow_custom_project_resource_tags: NotRequired["bool"]
    """<p>Specifies whether custom project resource tags are supported.</p>"""
    project_resource_tags_description: NotRequired[
        "capo_datazone.types.description.Description"
    ]
    """<p>Field viewable through the UI that provides a project user with the allowed resource tag specifications.</p>"""
    environment_configurations: NotRequired[
        "capo_datazone.types.environment_configurations_list.EnvironmentConfigurationsList"
    ]
    """<p>Environment configurations of a project profile.</p>"""
    created_by: "capo_datazone.types.created_by.CreatedBy"
    """<p>A user who created a project profile.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>A timestamp at which a project profile is created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>A timestamp when a project profile was last updated.</p>"""
    domain_unit_id: NotRequired["capo_datazone.types.domain_unit_id.DomainUnitId"]
    """<p>The ID of the domain unit where a project profile is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectProfileOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import capo_datazone.types.status

        out["status"] = capo_datazone.types.status.serialize_json(value["status"])
    if "project_resource_tags" in value:
        import capo_datazone.types.project_resource_tag_parameters

        out["projectResourceTags"] = (
            capo_datazone.types.project_resource_tag_parameters.serialize_json(
                value["project_resource_tags"]
            )
        )
    if "allow_custom_project_resource_tags" in value:
        out["allowCustomProjectResourceTags"] = value[
            "allow_custom_project_resource_tags"
        ]
    if "project_resource_tags_description" in value:
        out["projectResourceTagsDescription"] = value[
            "project_resource_tags_description"
        ]
    if "environment_configurations" in value:
        import capo_datazone.types.environment_configurations_list

        out["environmentConfigurations"] = (
            capo_datazone.types.environment_configurations_list.serialize_json(
                value["environment_configurations"]
            )
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
    if "domain_unit_id" in value:
        out["domainUnitId"] = value["domain_unit_id"]
    return out


def deserialize_json(data: dict) -> CreateProjectProfileOutput:
    out: CreateProjectProfileOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("CreateProjectProfileOutput.domain_id required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateProjectProfileOutput.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateProjectProfileOutput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_datazone.types.status

        out["status"] = capo_datazone.types.status.deserialize_json(data["status"])
    if data.get("projectResourceTags") is not None:
        import capo_datazone.types.project_resource_tag_parameters

        out["project_resource_tags"] = (
            capo_datazone.types.project_resource_tag_parameters.deserialize_json(
                data["projectResourceTags"]
            )
        )
    if data.get("allowCustomProjectResourceTags") is not None:
        out["allow_custom_project_resource_tags"] = data[
            "allowCustomProjectResourceTags"
        ]
    if data.get("projectResourceTagsDescription") is not None:
        out["project_resource_tags_description"] = data[
            "projectResourceTagsDescription"
        ]
    if data.get("environmentConfigurations") is not None:
        import capo_datazone.types.environment_configurations_list

        out["environment_configurations"] = (
            capo_datazone.types.environment_configurations_list.deserialize_json(
                data["environmentConfigurations"]
            )
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("CreateProjectProfileOutput.created_by required")
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
    if data.get("domainUnitId") is not None:
        out["domain_unit_id"] = data["domainUnitId"]
    return out


def redact_sensitive(value: CreateProjectProfileOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "project_resource_tags_description" in value:
        out["project_resource_tags_description"] = "*** Sensitive Data Redacted ***"
    if "environment_configurations" in value:
        import capo_datazone.types.environment_configurations_list

        out["environment_configurations"] = (
            capo_datazone.types.environment_configurations_list.redact_sensitive(
                value["environment_configurations"]
            )
        )
    return out
