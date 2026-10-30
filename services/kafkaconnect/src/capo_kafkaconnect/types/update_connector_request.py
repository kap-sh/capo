"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#UpdateConnectorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__boolean
    import capo_kafkaconnect.types.__list_of_plugin_update
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.capacity_update
    import capo_kafkaconnect.types.connector_configuration_update
    import capo_kafkaconnect.types.worker_configuration_update


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
    plugins: NotRequired[
        "capo_kafkaconnect.types.__list_of_plugin_update.__listOfPluginUpdate"
    ]
    """<important> <p>Amazon MSK Connect does not currently support specifying multiple plugins as a list. To use more than one plugin for your connector, you can create a single custom plugin using a ZIP file that bundles multiple plugins together.</p> </important> <p>Specifies which plugin to use for the connector. You must specify a single-element list containing one <code>customPlugin</code> object. If you don't specify this parameter, the connector keeps its current plugin.</p>"""
    worker_configuration: NotRequired[
        "capo_kafkaconnect.types.worker_configuration_update.WorkerConfigurationUpdate"
    ]
    """<p>The worker configuration to use with the connector. Specify the Amazon Resource Name (ARN) and the revision of the worker configuration. You can't specify both <code>workerConfiguration</code> and <code>useDefaultWorkerConfiguration</code> in the same request. If you specify neither parameter, the connector keeps its current worker configuration.</p>"""
    use_default_worker_configuration: NotRequired[
        "capo_kafkaconnect.types.__boolean.__boolean"
    ]
    """<p>Specifies whether to switch the connector to the default worker configuration that Amazon MSK Connect provides. If <code>true</code>, the connector stops using its custom worker configuration and uses the default worker configuration instead. If <code>false</code> or not specified, the connector keeps its current worker configuration. You can't specify both <code>useDefaultWorkerConfiguration</code> and <code>workerConfiguration</code> in the same request.</p>"""


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
    if "plugins" in value:
        import capo_kafkaconnect.types.__list_of_plugin_update

        out["plugins"] = capo_kafkaconnect.types.__list_of_plugin_update.serialize_json(
            value["plugins"]
        )
    if "worker_configuration" in value:
        import capo_kafkaconnect.types.worker_configuration_update

        out["workerConfiguration"] = (
            capo_kafkaconnect.types.worker_configuration_update.serialize_json(
                value["worker_configuration"]
            )
        )
    if "use_default_worker_configuration" in value:
        out["useDefaultWorkerConfiguration"] = value["use_default_worker_configuration"]
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
    if data.get("plugins") is not None:
        import capo_kafkaconnect.types.__list_of_plugin_update

        out["plugins"] = (
            capo_kafkaconnect.types.__list_of_plugin_update.deserialize_json(
                data["plugins"]
            )
        )
    if data.get("workerConfiguration") is not None:
        import capo_kafkaconnect.types.worker_configuration_update

        out["worker_configuration"] = (
            capo_kafkaconnect.types.worker_configuration_update.deserialize_json(
                data["workerConfiguration"]
            )
        )
    if data.get("useDefaultWorkerConfiguration") is not None:
        out["use_default_worker_configuration"] = data["useDefaultWorkerConfiguration"]
    return out


def redact_sensitive(value: UpdateConnectorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connector_configuration" in value:
        out["connector_configuration"] = "*** Sensitive Data Redacted ***"
    return out
