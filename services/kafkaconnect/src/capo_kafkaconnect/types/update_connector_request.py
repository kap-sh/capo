"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#UpdateConnectorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__boolean
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
    skip_health_validation: NotRequired["capo_kafkaconnect.types.__boolean.__boolean"]
    """<p>Specifies whether the update bypasses connector-level and task-level health checks. If <code>true</code>, the update skips the health checks. The update stays in effect even if the connector or its tasks are unhealthy, and Amazon MSK Connect doesn't roll it back. If <code>false</code> or not specified, the health checks run. If they fail, MSK Connect automatically rolls the connector back to its previous configuration, and the update doesn't take effect. To update a connector that is in the <code>PAUSED</code> state, you must set this parameter to <code>true</code>.</p>"""
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
    if "skip_health_validation" in value:
        out["skipHealthValidation"] = value["skip_health_validation"]
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
    if data.get("skipHealthValidation") is not None:
        out["skip_health_validation"] = data["skipHealthValidation"]
    return out


def redact_sensitive(value: UpdateConnectorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connector_configuration" in value:
        out["connector_configuration"] = "*** Sensitive Data Redacted ***"
    return out
