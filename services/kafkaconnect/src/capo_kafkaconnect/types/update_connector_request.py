"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#UpdateConnectorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.capacity_update
    import capo_kafkaconnect.types.connector_configuration_update


class UpdateConnectorRequest(TypedDict, closed=True):
    capacity: NotRequired["capo_kafkaconnect.types.capacity_update.CapacityUpdate"]
    """<p>The target capacity.</p>"""
    connector_configuration: NotRequired[
        "capo_kafkaconnect.types.connector_configuration_update.ConnectorConfigurationUpdate"
    ]
    """<p>A map of keys to values that represent the configuration for the connector.</p>"""
    connector_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the connector that you want to update.</p>"""
    current_version: "capo_kafkaconnect.types.__string.__string"
    """<p>The current version of the connector that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorRequest) -> dict:
    out: dict = {}
    if "capacity" in value:
        import capo_kafkaconnect.types.capacity_update

        out["capacity"] = capo_kafkaconnect.types.capacity_update.serialize_json(
            value["capacity"]
        )
    if "connector_configuration" in value:
        import capo_kafkaconnect.types.connector_configuration_update

        out["connectorConfiguration"] = (
            capo_kafkaconnect.types.connector_configuration_update.serialize_json(
                value["connector_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConnectorRequest:
    out: UpdateConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("capacity") is not None:
        import capo_kafkaconnect.types.capacity_update

        out["capacity"] = capo_kafkaconnect.types.capacity_update.deserialize_json(
            data["capacity"]
        )
    if data.get("connectorConfiguration") is not None:
        import capo_kafkaconnect.types.connector_configuration_update

        out["connector_configuration"] = (
            capo_kafkaconnect.types.connector_configuration_update.deserialize_json(
                data["connectorConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateConnectorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connector_configuration" in value:
        out["connector_configuration"] = "*** Sensitive Data Redacted ***"
    return out
