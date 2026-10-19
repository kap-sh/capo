"""Generated from Smithy shape ``com.amazonaws.datazone#CreateProjectProfileInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.environment_configurations_list
    import capo_datazone.types.project_profile_name
    import capo_datazone.types.project_resource_tag_parameters
    import capo_datazone.types.status


class CreateProjectProfileInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>A domain ID of the project profile.</p>"""
    name: "capo_datazone.types.project_profile_name.ProjectProfileName"
    """<p>Project profile name.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>A description of a project profile.</p>"""
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
    """<p>Environment configurations of the project profile.</p>"""
    domain_unit_identifier: NotRequired[
        "capo_datazone.types.domain_unit_id.DomainUnitId"
    ]
    """<p>A domain unit ID of the project profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectProfileInput) -> dict:
    out: dict = {}
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
    if "domain_unit_identifier" in value:
        out["domainUnitIdentifier"] = value["domain_unit_identifier"]
    return out


def deserialize_json(data: dict) -> CreateProjectProfileInput:
    out: CreateProjectProfileInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
    if data.get("domainUnitIdentifier") is not None:
        out["domain_unit_identifier"] = data["domainUnitIdentifier"]
    return out


def redact_sensitive(value: CreateProjectProfileInput) -> dict[str, Any]:
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
