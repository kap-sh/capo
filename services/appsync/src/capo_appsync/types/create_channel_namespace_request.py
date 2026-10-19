"""Generated from Smithy shape ``com.amazonaws.appsync#CreateChannelNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.auth_modes
    import capo_appsync.types.code
    import capo_appsync.types.handler_configs
    import capo_appsync.types.namespace
    import capo_appsync.types.string
    import capo_appsync.types.tag_map


class CreateChannelNamespaceRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The <code>Api</code> ID.</p>"""
    name: "capo_appsync.types.namespace.Namespace"
    """<p>The name of the <code>ChannelNamespace</code>. This name must be unique within the <code>Api</code> </p>"""
    subscribe_auth_modes: NotRequired["capo_appsync.types.auth_modes.AuthModes"]
    """<p>The authorization mode to use for subscribing to messages on the channel namespace. This configuration overrides the default <code>Api</code> authorization configuration.</p>"""
    publish_auth_modes: NotRequired["capo_appsync.types.auth_modes.AuthModes"]
    """<p>The authorization mode to use for publishing messages on the channel namespace. This configuration overrides the default <code>Api</code> authorization configuration.</p>"""
    code_handlers: NotRequired["capo_appsync.types.code.Code"]
    """<p>The event handler functions that run custom business logic to process published events and subscribe requests.</p>"""
    tags: NotRequired["capo_appsync.types.tag_map.TagMap"]
    handler_configs: NotRequired["capo_appsync.types.handler_configs.HandlerConfigs"]
    """<p>The configuration for the <code>OnPublish</code> and <code>OnSubscribe</code> handlers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelNamespaceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "subscribe_auth_modes" in value:
        import capo_appsync.types.auth_modes

        out["subscribeAuthModes"] = capo_appsync.types.auth_modes.serialize_json(
            value["subscribe_auth_modes"]
        )
    if "publish_auth_modes" in value:
        import capo_appsync.types.auth_modes

        out["publishAuthModes"] = capo_appsync.types.auth_modes.serialize_json(
            value["publish_auth_modes"]
        )
    if "code_handlers" in value:
        out["codeHandlers"] = value["code_handlers"]
    if "tags" in value:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.serialize_json(value["tags"])
    if "handler_configs" in value:
        import capo_appsync.types.handler_configs

        out["handlerConfigs"] = capo_appsync.types.handler_configs.serialize_json(
            value["handler_configs"]
        )
    return out


def deserialize_json(data: dict) -> CreateChannelNamespaceRequest:
    out: CreateChannelNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("subscribeAuthModes") is not None:
        import capo_appsync.types.auth_modes

        out["subscribe_auth_modes"] = capo_appsync.types.auth_modes.deserialize_json(
            data["subscribeAuthModes"]
        )
    if data.get("publishAuthModes") is not None:
        import capo_appsync.types.auth_modes

        out["publish_auth_modes"] = capo_appsync.types.auth_modes.deserialize_json(
            data["publishAuthModes"]
        )
    if data.get("codeHandlers") is not None:
        out["code_handlers"] = data["codeHandlers"]
    if data.get("tags") is not None:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.deserialize_json(data["tags"])
    if data.get("handlerConfigs") is not None:
        import capo_appsync.types.handler_configs

        out["handler_configs"] = capo_appsync.types.handler_configs.deserialize_json(
            data["handlerConfigs"]
        )
    return out
