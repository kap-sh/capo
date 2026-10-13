"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#GetConfigurationManagerOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ssm_quicksetup.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_ssm_quicksetup.types.configuration_definitions_list
    import capo_ssm_quicksetup.types.status_summaries_list
    import capo_ssm_quicksetup.types.tags_map


class GetConfigurationManagerOutput(TypedDict, closed=True):
    manager_arn: "str"
    """<p>The ARN of the configuration manager.</p>"""
    description: NotRequired["str"]
    """<p>The description of the configuration manager.</p>"""
    name: NotRequired["str"]
    """<p>The name of the configuration manager.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The datetime stamp when the configuration manager was created.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The datetime stamp when the configuration manager was last updated.</p>"""
    status_summaries: NotRequired[
        "capo_ssm_quicksetup.types.status_summaries_list.StatusSummariesList"
    ]
    """<p>A summary of the state of the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.</p>"""
    configuration_definitions: NotRequired[
        "capo_ssm_quicksetup.types.configuration_definitions_list.ConfigurationDefinitionsList"
    ]
    """<p>The configuration definitions association with the configuration manager.</p>"""
    tags: NotRequired["capo_ssm_quicksetup.types.tags_map.TagsMap"]
    """<p>Key-value pairs of metadata to assign to the configuration manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationManagerOutput) -> dict:
    out: dict = {}
    out["ManagerArn"] = value["manager_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_at" in value:
        import capo_ssm_quicksetup._protocol.serialize

        out["CreatedAt"] = capo_ssm_quicksetup._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "last_modified_at" in value:
        import capo_ssm_quicksetup._protocol.serialize

        out["LastModifiedAt"] = capo_ssm_quicksetup._protocol.serialize.fmt_date_time(
            value["last_modified_at"]
        )
    if "status_summaries" in value:
        import capo_ssm_quicksetup.types.status_summaries_list

        out["StatusSummaries"] = (
            capo_ssm_quicksetup.types.status_summaries_list.serialize_json(
                value["status_summaries"]
            )
        )
    if "configuration_definitions" in value:
        import capo_ssm_quicksetup.types.configuration_definitions_list

        out["ConfigurationDefinitions"] = (
            capo_ssm_quicksetup.types.configuration_definitions_list.serialize_json(
                value["configuration_definitions"]
            )
        )
    if "tags" in value:
        import capo_ssm_quicksetup.types.tags_map

        out["Tags"] = capo_ssm_quicksetup.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetConfigurationManagerOutput:
    out: GetConfigurationManagerOutput = {}  # type: ignore[typeddict-item]
    if data.get("ManagerArn") is not None:
        out["manager_arn"] = data["ManagerArn"]
    else:
        raise DeserializationError("GetConfigurationManagerOutput.manager_arn required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["CreatedAt"].replace("Z", "+00:00")
        )
    if data.get("LastModifiedAt") is not None:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromisoformat(
            data["LastModifiedAt"].replace("Z", "+00:00")
        )
    if data.get("StatusSummaries") is not None:
        import capo_ssm_quicksetup.types.status_summaries_list

        out["status_summaries"] = (
            capo_ssm_quicksetup.types.status_summaries_list.deserialize_json(
                data["StatusSummaries"]
            )
        )
    if data.get("ConfigurationDefinitions") is not None:
        import capo_ssm_quicksetup.types.configuration_definitions_list

        out["configuration_definitions"] = (
            capo_ssm_quicksetup.types.configuration_definitions_list.deserialize_json(
                data["ConfigurationDefinitions"]
            )
        )
    if data.get("Tags") is not None:
        import capo_ssm_quicksetup.types.tags_map

        out["tags"] = capo_ssm_quicksetup.types.tags_map.deserialize_json(data["Tags"])
    return out


def redact_sensitive(value: GetConfigurationManagerOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
