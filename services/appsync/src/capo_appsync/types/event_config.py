"""Generated from Smithy shape ``com.amazonaws.appsync#EventConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.auth_modes
    import capo_appsync.types.auth_providers
    import capo_appsync.types.event_log_config


class EventConfig(TypedDict, closed=True):
    auth_providers: "capo_appsync.types.auth_providers.AuthProviders"
    """<p>A list of authorization providers.</p>"""
    connection_auth_modes: "capo_appsync.types.auth_modes.AuthModes"
    """<p>A list of valid authorization modes for the Event API connections.</p>"""
    default_publish_auth_modes: "capo_appsync.types.auth_modes.AuthModes"
    """<p>A list of valid authorization modes for the Event API publishing.</p>"""
    default_subscribe_auth_modes: "capo_appsync.types.auth_modes.AuthModes"
    """<p>A list of valid authorization modes for the Event API subscriptions.</p>"""
    log_config: NotRequired["capo_appsync.types.event_log_config.EventLogConfig"]
    """<p>The CloudWatch Logs configuration for the Event API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventConfig) -> dict:
    out: dict = {}
    import capo_appsync.types.auth_providers

    out["authProviders"] = capo_appsync.types.auth_providers.serialize_json(
        value["auth_providers"]
    )
    import capo_appsync.types.auth_modes

    out["connectionAuthModes"] = capo_appsync.types.auth_modes.serialize_json(
        value["connection_auth_modes"]
    )
    import capo_appsync.types.auth_modes

    out["defaultPublishAuthModes"] = capo_appsync.types.auth_modes.serialize_json(
        value["default_publish_auth_modes"]
    )
    import capo_appsync.types.auth_modes

    out["defaultSubscribeAuthModes"] = capo_appsync.types.auth_modes.serialize_json(
        value["default_subscribe_auth_modes"]
    )
    if "log_config" in value:
        import capo_appsync.types.event_log_config

        out["logConfig"] = capo_appsync.types.event_log_config.serialize_json(
            value["log_config"]
        )
    return out


def deserialize_json(data: dict) -> EventConfig:
    out: EventConfig = {}  # type: ignore[typeddict-item]
    if data.get("authProviders") is not None:
        import capo_appsync.types.auth_providers

        out["auth_providers"] = capo_appsync.types.auth_providers.deserialize_json(
            data["authProviders"]
        )
    else:
        out["auth_providers"] = []
    if data.get("connectionAuthModes") is not None:
        import capo_appsync.types.auth_modes

        out["connection_auth_modes"] = capo_appsync.types.auth_modes.deserialize_json(
            data["connectionAuthModes"]
        )
    else:
        out["connection_auth_modes"] = []
    if data.get("defaultPublishAuthModes") is not None:
        import capo_appsync.types.auth_modes

        out["default_publish_auth_modes"] = (
            capo_appsync.types.auth_modes.deserialize_json(
                data["defaultPublishAuthModes"]
            )
        )
    else:
        out["default_publish_auth_modes"] = []
    if data.get("defaultSubscribeAuthModes") is not None:
        import capo_appsync.types.auth_modes

        out["default_subscribe_auth_modes"] = (
            capo_appsync.types.auth_modes.deserialize_json(
                data["defaultSubscribeAuthModes"]
            )
        )
    else:
        out["default_subscribe_auth_modes"] = []
    if data.get("logConfig") is not None:
        import capo_appsync.types.event_log_config

        out["log_config"] = capo_appsync.types.event_log_config.deserialize_json(
            data["logConfig"]
        )
    return out
