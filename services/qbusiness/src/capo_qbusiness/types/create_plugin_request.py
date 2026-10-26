"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreatePluginRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.custom_plugin_configuration
    import capo_qbusiness.types.plugin_auth_configuration
    import capo_qbusiness.types.plugin_name
    import capo_qbusiness.types.plugin_type
    import capo_qbusiness.types.tags
    import capo_qbusiness.types.url


class CreatePluginRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application that will contain the plugin.</p>"""
    display_name: "capo_qbusiness.types.plugin_name.PluginName"
    """<p>A the name for your plugin.</p>"""
    type: "capo_qbusiness.types.plugin_type.PluginType"
    """<p>The type of plugin you want to create.</p>"""
    auth_configuration: (
        "capo_qbusiness.types.plugin_auth_configuration.PluginAuthConfiguration"
    )
    server_url: NotRequired["capo_qbusiness.types.url.Url"]
    """<p>The source URL used for plugin configuration.</p>"""
    custom_plugin_configuration: NotRequired[
        "capo_qbusiness.types.custom_plugin_configuration.CustomPluginConfiguration"
    ]
    """<p>Contains configuration for a custom plugin.</p>"""
    tags: NotRequired["capo_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create your Amazon Q Business plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePluginRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    import capo_qbusiness.types.plugin_type

    out["type"] = capo_qbusiness.types.plugin_type.serialize_json(value["type"])
    import capo_qbusiness.types.plugin_auth_configuration

    out["authConfiguration"] = (
        capo_qbusiness.types.plugin_auth_configuration.serialize_json(
            value["auth_configuration"]
        )
    )
    if "server_url" in value:
        out["serverUrl"] = value["server_url"]
    if "custom_plugin_configuration" in value:
        import capo_qbusiness.types.custom_plugin_configuration

        out["customPluginConfiguration"] = (
            capo_qbusiness.types.custom_plugin_configuration.serialize_json(
                value["custom_plugin_configuration"]
            )
        )
    if "tags" in value:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePluginRequest:
    out: CreatePluginRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("type") is not None:
        import capo_qbusiness.types.plugin_type

        out["type"] = capo_qbusiness.types.plugin_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_qbusiness.types.plugin_type.PluginType", "")
    if data.get("authConfiguration") is not None:
        import capo_qbusiness.types.plugin_auth_configuration

        out["auth_configuration"] = (
            capo_qbusiness.types.plugin_auth_configuration.deserialize_json(
                data["authConfiguration"]
            )
        )
    else:
        out["auth_configuration"] = {"$unknown": {"name": ""}}
    if data.get("serverUrl") is not None:
        out["server_url"] = data["serverUrl"]
    if data.get("customPluginConfiguration") is not None:
        import capo_qbusiness.types.custom_plugin_configuration

        out["custom_plugin_configuration"] = (
            capo_qbusiness.types.custom_plugin_configuration.deserialize_json(
                data["customPluginConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_qbusiness.types.tags

        out["tags"] = capo_qbusiness.types.tags.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreatePluginRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_plugin_configuration" in value:
        import capo_qbusiness.types.custom_plugin_configuration

        out["custom_plugin_configuration"] = (
            capo_qbusiness.types.custom_plugin_configuration.redact_sensitive(
                value["custom_plugin_configuration"]
            )
        )
    return out
