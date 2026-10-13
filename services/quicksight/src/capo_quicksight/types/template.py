"""Generated from Smithy shape ``com.amazonaws.quicksight#Template``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.template_name
    import capo_quicksight.types.template_version
    import capo_quicksight.types.timestamp


class Template(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    name: NotRequired["capo_quicksight.types.template_name.TemplateName"]
    """<p>The display name of the template.</p>"""
    version: NotRequired["capo_quicksight.types.template_version.TemplateVersion"]
    """<p>A structure describing the versions of the template.</p>"""
    template_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the template. This is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>Time when this was last updated.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>Time when this was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Template) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        import capo_quicksight.types.template_version

        out["Version"] = capo_quicksight.types.template_version.serialize_json(
            value["version"]
        )
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    return out


def deserialize_json(data: dict) -> Template:
    out: Template = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Version") is not None:
        import capo_quicksight.types.template_version

        out["version"] = capo_quicksight.types.template_version.deserialize_json(
            data["Version"]
        )
    if data.get("TemplateId") is not None:
        out["template_id"] = data["TemplateId"]
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    return out


def redact_sensitive(value: Template) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "version" in value:
        import capo_quicksight.types.template_version

        out["version"] = capo_quicksight.types.template_version.redact_sensitive(
            value["version"]
        )
    return out
