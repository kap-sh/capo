"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetPluginResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.custom_plugin_configuration
    import capo_qbusiness.types.plugin_arn
    import capo_qbusiness.types.plugin_auth_configuration
    import capo_qbusiness.types.plugin_build_status
    import capo_qbusiness.types.plugin_id
    import capo_qbusiness.types.plugin_name
    import capo_qbusiness.types.plugin_state
    import capo_qbusiness.types.plugin_type
    import capo_qbusiness.types.timestamp
    import capo_qbusiness.types.url


class GetPluginResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the application which contains the plugin.</p>"""
    plugin_id: NotRequired["capo_qbusiness.types.plugin_id.PluginId"]
    """<p>The identifier of the plugin.</p>"""
    display_name: NotRequired["capo_qbusiness.types.plugin_name.PluginName"]
    """<p>The name of the plugin.</p>"""
    type: NotRequired["capo_qbusiness.types.plugin_type.PluginType"]
    """<p>The type of the plugin.</p>"""
    server_url: NotRequired["capo_qbusiness.types.url.Url"]
    """<p>The source URL used for plugin configuration.</p>"""
    auth_configuration: NotRequired[
        "capo_qbusiness.types.plugin_auth_configuration.PluginAuthConfiguration"
    ]
    custom_plugin_configuration: NotRequired[
        "capo_qbusiness.types.custom_plugin_configuration.CustomPluginConfiguration"
    ]
    """<p>Configuration information required to create a custom plugin.</p>"""
    build_status: NotRequired[
        "capo_qbusiness.types.plugin_build_status.PluginBuildStatus"
    ]
    """<p>The current status of a plugin. A plugin is modified asynchronously.</p>"""
    plugin_arn: NotRequired["capo_qbusiness.types.plugin_arn.PluginArn"]
    """<p>The Amazon Resource Name (ARN) of the role with permission to access resources needed to create the plugin.</p>"""
    state: NotRequired["capo_qbusiness.types.plugin_state.PluginState"]
    """<p>The current state of the plugin.</p>"""
    created_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp for when the plugin was created.</p>"""
    updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp for when the plugin was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPluginResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "plugin_id" in value:
        out["pluginId"] = value["plugin_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "type" in value:
        import capo_qbusiness.types.plugin_type

        out["type"] = capo_qbusiness.types.plugin_type.serialize_json(value["type"])
    if "server_url" in value:
        out["serverUrl"] = value["server_url"]
    if "auth_configuration" in value:
        import capo_qbusiness.types.plugin_auth_configuration

        out["authConfiguration"] = (
            capo_qbusiness.types.plugin_auth_configuration.serialize_json(
                value["auth_configuration"]
            )
        )
    if "custom_plugin_configuration" in value:
        import capo_qbusiness.types.custom_plugin_configuration

        out["customPluginConfiguration"] = (
            capo_qbusiness.types.custom_plugin_configuration.serialize_json(
                value["custom_plugin_configuration"]
            )
        )
    if "build_status" in value:
        import capo_qbusiness.types.plugin_build_status

        out["buildStatus"] = capo_qbusiness.types.plugin_build_status.serialize_json(
            value["build_status"]
        )
    if "plugin_arn" in value:
        out["pluginArn"] = value["plugin_arn"]
    if "state" in value:
        import capo_qbusiness.types.plugin_state

        out["state"] = capo_qbusiness.types.plugin_state.serialize_json(value["state"])
    if "created_at" in value:
        import capo_qbusiness.types.timestamp

        out["createdAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["updatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetPluginResponse:
    out: GetPluginResponse = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    if data.get("pluginId") is not None:
        out["plugin_id"] = data["pluginId"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("type") is not None:
        import capo_qbusiness.types.plugin_type

        out["type"] = capo_qbusiness.types.plugin_type.deserialize_json(data["type"])
    if data.get("serverUrl") is not None:
        out["server_url"] = data["serverUrl"]
    if data.get("authConfiguration") is not None:
        import capo_qbusiness.types.plugin_auth_configuration

        out["auth_configuration"] = (
            capo_qbusiness.types.plugin_auth_configuration.deserialize_json(
                data["authConfiguration"]
            )
        )
    if data.get("customPluginConfiguration") is not None:
        import capo_qbusiness.types.custom_plugin_configuration

        out["custom_plugin_configuration"] = (
            capo_qbusiness.types.custom_plugin_configuration.deserialize_json(
                data["customPluginConfiguration"]
            )
        )
    if data.get("buildStatus") is not None:
        import capo_qbusiness.types.plugin_build_status

        out["build_status"] = capo_qbusiness.types.plugin_build_status.deserialize_json(
            data["buildStatus"]
        )
    if data.get("pluginArn") is not None:
        out["plugin_arn"] = data["pluginArn"]
    if data.get("state") is not None:
        import capo_qbusiness.types.plugin_state

        out["state"] = capo_qbusiness.types.plugin_state.deserialize_json(data["state"])
    if data.get("createdAt") is not None:
        import capo_qbusiness.types.timestamp

        out["created_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_qbusiness.types.timestamp

        out["updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out


def redact_sensitive(value: GetPluginResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_plugin_configuration" in value:
        import capo_qbusiness.types.custom_plugin_configuration

        out["custom_plugin_configuration"] = (
            capo_qbusiness.types.custom_plugin_configuration.redact_sensitive(
                value["custom_plugin_configuration"]
            )
        )
    return out
