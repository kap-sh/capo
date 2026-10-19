"""Generated from Smithy shape ``com.amazonaws.appflow#UpdateConnectorProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.client_token
    import capo_appflow.types.connection_mode
    import capo_appflow.types.connector_profile_config
    import capo_appflow.types.connector_profile_name


class UpdateConnectorProfileRequest(TypedDict, closed=True):
    connector_profile_name: (
        "capo_appflow.types.connector_profile_name.ConnectorProfileName"
    )
    """<p> The name of the connector profile and is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account. </p>"""
    connection_mode: "capo_appflow.types.connection_mode.ConnectionMode"
    """<p> Indicates the connection mode and if it is public or private. </p>"""
    connector_profile_config: (
        "capo_appflow.types.connector_profile_config.ConnectorProfileConfig"
    )
    """<p> Defines the connector-specific profile configuration and credentials. </p>"""
    client_token: NotRequired["capo_appflow.types.client_token.ClientToken"]
    """<p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>UpdateConnectorProfile</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>UpdateConnectorProfile</code>. The token is active for 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorProfileRequest) -> dict:
    out: dict = {}
    out["connectorProfileName"] = value["connector_profile_name"]
    import capo_appflow.types.connection_mode

    out["connectionMode"] = capo_appflow.types.connection_mode.serialize_json(
        value["connection_mode"]
    )
    import capo_appflow.types.connector_profile_config

    out["connectorProfileConfig"] = (
        capo_appflow.types.connector_profile_config.serialize_json(
            value["connector_profile_config"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateConnectorProfileRequest:
    out: UpdateConnectorProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectorProfileName") is not None:
        out["connector_profile_name"] = data["connectorProfileName"]
    else:
        out["connector_profile_name"] = ""
    if data.get("connectionMode") is not None:
        import capo_appflow.types.connection_mode

        out["connection_mode"] = capo_appflow.types.connection_mode.deserialize_json(
            data["connectionMode"]
        )
    else:
        import typing

        out["connection_mode"] = typing.cast(
            "capo_appflow.types.connection_mode.ConnectionMode", ""
        )
    if data.get("connectorProfileConfig") is not None:
        import capo_appflow.types.connector_profile_config

        out["connector_profile_config"] = (
            capo_appflow.types.connector_profile_config.deserialize_json(
                data["connectorProfileConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectorProfileRequest.connector_profile_config required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: UpdateConnectorProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connector_profile_config" in value:
        import capo_appflow.types.connector_profile_config

        out["connector_profile_config"] = (
            capo_appflow.types.connector_profile_config.redact_sensitive(
                value["connector_profile_config"]
            )
        )
    return out
