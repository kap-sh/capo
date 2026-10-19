"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.description
    import capo_appconfig.types.monitor_list
    import capo_appconfig.types.name
    import capo_appconfig.types.tag_map


class CreateEnvironmentRequest(TypedDict, closed=True):
    application_id: "capo_appconfig.types.name.Name"
    """<p>The application ID.</p>"""
    name: "capo_appconfig.types.name.Name"
    """<p>A name for the environment.</p>"""
    description: NotRequired["capo_appconfig.types.description.Description"]
    """<p>A description of the environment.</p>"""
    monitors: NotRequired["capo_appconfig.types.monitor_list.MonitorList"]
    """<p>Amazon CloudWatch alarms to monitor during the deployment process.</p>"""
    tags: NotRequired["capo_appconfig.types.tag_map.TagMap"]
    """<p>Metadata to assign to the environment. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "monitors" in value:
        import capo_appconfig.types.monitor_list

        out["Monitors"] = capo_appconfig.types.monitor_list.serialize_json(
            value["monitors"]
        )
    if "tags" in value:
        import capo_appconfig.types.tag_map

        out["Tags"] = capo_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEnvironmentRequest:
    out: CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Monitors") is not None:
        import capo_appconfig.types.monitor_list

        out["monitors"] = capo_appconfig.types.monitor_list.deserialize_json(
            data["Monitors"]
        )
    if data.get("Tags") is not None:
        import capo_appconfig.types.tag_map

        out["tags"] = capo_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out
