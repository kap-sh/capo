"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfileConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.connector_profile_credentials
    import capo_appflow.types.connector_profile_properties


class ConnectorProfileConfig(TypedDict, closed=True):
    connector_profile_properties: (
        "capo_appflow.types.connector_profile_properties.ConnectorProfileProperties"
    )
    """<p> The connector-specific properties of the profile configuration. </p>"""
    connector_profile_credentials: NotRequired[
        "capo_appflow.types.connector_profile_credentials.ConnectorProfileCredentials"
    ]
    """<p> The connector-specific credentials required by each connector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfileConfig) -> dict:
    out: dict = {}
    import capo_appflow.types.connector_profile_properties

    out["connectorProfileProperties"] = (
        capo_appflow.types.connector_profile_properties.serialize_json(
            value["connector_profile_properties"]
        )
    )
    if "connector_profile_credentials" in value:
        import capo_appflow.types.connector_profile_credentials

        out["connectorProfileCredentials"] = (
            capo_appflow.types.connector_profile_credentials.serialize_json(
                value["connector_profile_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorProfileConfig:
    out: ConnectorProfileConfig = {}  # type: ignore[typeddict-item]
    if data.get("connectorProfileProperties") is not None:
        import capo_appflow.types.connector_profile_properties

        out["connector_profile_properties"] = (
            capo_appflow.types.connector_profile_properties.deserialize_json(
                data["connectorProfileProperties"]
            )
        )
    else:
        raise DeserializationError(
            "ConnectorProfileConfig.connector_profile_properties required"
        )
    if data.get("connectorProfileCredentials") is not None:
        import capo_appflow.types.connector_profile_credentials

        out["connector_profile_credentials"] = (
            capo_appflow.types.connector_profile_credentials.deserialize_json(
                data["connectorProfileCredentials"]
            )
        )
    return out


def redact_sensitive(value: ConnectorProfileConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connector_profile_credentials" in value:
        import capo_appflow.types.connector_profile_credentials

        out["connector_profile_credentials"] = (
            capo_appflow.types.connector_profile_credentials.redact_sensitive(
                value["connector_profile_credentials"]
            )
        )
    return out
