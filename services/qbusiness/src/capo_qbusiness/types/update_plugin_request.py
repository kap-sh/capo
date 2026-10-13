"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdatePluginRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.custom_plugin_configuration
    import capo_qbusiness.types.plugin_auth_configuration
    import capo_qbusiness.types.plugin_id
    import capo_qbusiness.types.plugin_name
    import capo_qbusiness.types.plugin_state
    import capo_qbusiness.types.url


class UpdatePluginRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application the plugin is attached to.</p>"""
    plugin_id: "capo_qbusiness.types.plugin_id.PluginId"
    """<p>The identifier of the plugin.</p>"""
    display_name: NotRequired["capo_qbusiness.types.plugin_name.PluginName"]
    """<p>The name of the plugin.</p>"""
    state: NotRequired["capo_qbusiness.types.plugin_state.PluginState"]
    """<p>The status of the plugin. </p>"""
    server_url: NotRequired["capo_qbusiness.types.url.Url"]
    """<p>The source URL used for plugin configuration.</p>"""
    custom_plugin_configuration: NotRequired[
        "capo_qbusiness.types.custom_plugin_configuration.CustomPluginConfiguration"
    ]
    """<p>The configuration for a custom plugin.</p>"""
    auth_configuration: NotRequired[
        "capo_qbusiness.types.plugin_auth_configuration.PluginAuthConfiguration"
    ]
    """<p>The authentication configuration the plugin is using.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePluginRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "state" in value:
        import capo_qbusiness.types.plugin_state

        out["state"] = capo_qbusiness.types.plugin_state.serialize_json(value["state"])
    if "server_url" in value:
        out["serverUrl"] = value["server_url"]
    if "custom_plugin_configuration" in value:
        import capo_qbusiness.types.custom_plugin_configuration

        out["customPluginConfiguration"] = (
            capo_qbusiness.types.custom_plugin_configuration.serialize_json(
                value["custom_plugin_configuration"]
            )
        )
    if "auth_configuration" in value:
        import capo_qbusiness.types.plugin_auth_configuration

        out["authConfiguration"] = (
            capo_qbusiness.types.plugin_auth_configuration.serialize_json(
                value["auth_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePluginRequest:
    out: UpdatePluginRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("state") is not None:
        import capo_qbusiness.types.plugin_state

        out["state"] = capo_qbusiness.types.plugin_state.deserialize_json(data["state"])
    if data.get("serverUrl") is not None:
        out["server_url"] = data["serverUrl"]
    if data.get("customPluginConfiguration") is not None:
        import capo_qbusiness.types.custom_plugin_configuration

        out["custom_plugin_configuration"] = (
            capo_qbusiness.types.custom_plugin_configuration.deserialize_json(
                data["customPluginConfiguration"]
            )
        )
    if data.get("authConfiguration") is not None:
        import capo_qbusiness.types.plugin_auth_configuration

        out["auth_configuration"] = (
            capo_qbusiness.types.plugin_auth_configuration.deserialize_json(
                data["authConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdatePluginRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_plugin_configuration" in value:
        import capo_qbusiness.types.custom_plugin_configuration

        out["custom_plugin_configuration"] = (
            capo_qbusiness.types.custom_plugin_configuration.redact_sensitive(
                value["custom_plugin_configuration"]
            )
        )
    return out
