"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateVersion``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.data_set_configuration_list
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.sheet_list
    import capo_quicksight.types.template_error_list
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.topic_configuration_list
    import capo_quicksight.types.version_description
    import capo_quicksight.types.version_number


class TemplateVersion(TypedDict, closed=True):
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this template version was created.</p>"""
    errors: NotRequired["capo_quicksight.types.template_error_list.TemplateErrorList"]
    """<p>Errors associated with this template version.</p>"""
    version_number: NotRequired["capo_quicksight.types.version_number.VersionNumber"]
    """<p>The version number of the template version.</p>"""
    status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The status that is associated with the template.</p> <ul> <li> <p> <code>CREATION_IN_PROGRESS</code> </p> </li> <li> <p> <code>CREATION_SUCCESSFUL</code> </p> </li> <li> <p> <code>CREATION_FAILED</code> </p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> </p> </li> <li> <p> <code>UPDATE_FAILED</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> </ul>"""
    data_set_configurations: NotRequired[
        "capo_quicksight.types.data_set_configuration_list.DataSetConfigurationList"
    ]
    """<p>Schema of the dataset identified by the placeholder. Any dashboard created from this template should be bound to new datasets matching the same schema described through this API operation.</p>"""
    topic_configurations: NotRequired[
        "capo_quicksight.types.topic_configuration_list.TopicConfigurationList"
    ]
    """<p>Schema of the topic identified by the placeholder. Any dashboard created from this template should be bound to new topics matching the same schema described through this API operation.</p>"""
    description: NotRequired[
        "capo_quicksight.types.version_description.VersionDescription"
    ]
    """<p>The description of the template.</p>"""
    source_entity_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of an analysis or template that was used to create this template.</p>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme associated with this version of the template.</p>"""
    sheets: NotRequired["capo_quicksight.types.sheet_list.SheetList"]
    """<p>A list of the associated sheets with the unique identifier and name of each sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateVersion) -> dict:
    out: dict = {}
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "errors" in value:
        import capo_quicksight.types.template_error_list

        out["Errors"] = capo_quicksight.types.template_error_list.serialize_json(
            value["errors"]
        )
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "status" in value:
        import capo_quicksight.types.resource_status

        out["Status"] = capo_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "data_set_configurations" in value:
        import capo_quicksight.types.data_set_configuration_list

        out["DataSetConfigurations"] = (
            capo_quicksight.types.data_set_configuration_list.serialize_json(
                value["data_set_configurations"]
            )
        )
    if "topic_configurations" in value:
        import capo_quicksight.types.topic_configuration_list

        out["TopicConfigurations"] = (
            capo_quicksight.types.topic_configuration_list.serialize_json(
                value["topic_configurations"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "source_entity_arn" in value:
        out["SourceEntityArn"] = value["source_entity_arn"]
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "sheets" in value:
        import capo_quicksight.types.sheet_list

        out["Sheets"] = capo_quicksight.types.sheet_list.serialize_json(value["sheets"])
    return out


def deserialize_json(data: dict) -> TemplateVersion:
    out: TemplateVersion = {}  # type: ignore[typeddict-item]
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("Errors") is not None:
        import capo_quicksight.types.template_error_list

        out["errors"] = capo_quicksight.types.template_error_list.deserialize_json(
            data["Errors"]
        )
    if data.get("VersionNumber") is not None:
        out["version_number"] = data["VersionNumber"]
    if data.get("Status") is not None:
        import capo_quicksight.types.resource_status

        out["status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if data.get("DataSetConfigurations") is not None:
        import capo_quicksight.types.data_set_configuration_list

        out["data_set_configurations"] = (
            capo_quicksight.types.data_set_configuration_list.deserialize_json(
                data["DataSetConfigurations"]
            )
        )
    if data.get("TopicConfigurations") is not None:
        import capo_quicksight.types.topic_configuration_list

        out["topic_configurations"] = (
            capo_quicksight.types.topic_configuration_list.deserialize_json(
                data["TopicConfigurations"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SourceEntityArn") is not None:
        out["source_entity_arn"] = data["SourceEntityArn"]
    if data.get("ThemeArn") is not None:
        out["theme_arn"] = data["ThemeArn"]
    if data.get("Sheets") is not None:
        import capo_quicksight.types.sheet_list

        out["sheets"] = capo_quicksight.types.sheet_list.deserialize_json(
            data["Sheets"]
        )
    return out


def redact_sensitive(value: TemplateVersion) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sheets" in value:
        import capo_quicksight.types.sheet_list

        out["sheets"] = capo_quicksight.types.sheet_list.redact_sensitive(
            value["sheets"]
        )
    return out
