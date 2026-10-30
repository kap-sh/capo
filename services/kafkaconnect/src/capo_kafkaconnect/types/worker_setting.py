"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__boolean
    import capo_kafkaconnect.types.__list_of_plugin_description
    import capo_kafkaconnect.types.capacity_description
    import capo_kafkaconnect.types.worker_configuration_description


class WorkerSetting(TypedDict, closed=True):
    capacity: NotRequired[
        "capo_kafkaconnect.types.capacity_description.CapacityDescription"
    ]
    """<p>Specifies the compute capacity settings of the connector.</p>"""
    plugins: NotRequired[
        "capo_kafkaconnect.types.__list_of_plugin_description.__listOfPluginDescription"
    ]
    """<p>Specifies which plugins the connector uses.</p>"""
    worker_configuration: NotRequired[
        "capo_kafkaconnect.types.worker_configuration_description.WorkerConfigurationDescription"
    ]
    """<p>Specifies which worker configuration the connector uses.</p>"""
    use_default_worker_configuration: "capo_kafkaconnect.types.__boolean.__boolean"
    """<p>Specifies whether the connector uses the default worker configuration instead of a custom worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerSetting) -> dict:
    out: dict = {}
    if "capacity" in value:
        import capo_kafkaconnect.types.capacity_description

        out["capacity"] = capo_kafkaconnect.types.capacity_description.serialize_json(
            value["capacity"]
        )
    if "plugins" in value:
        import capo_kafkaconnect.types.__list_of_plugin_description

        out["plugins"] = (
            capo_kafkaconnect.types.__list_of_plugin_description.serialize_json(
                value["plugins"]
            )
        )
    if "worker_configuration" in value:
        import capo_kafkaconnect.types.worker_configuration_description

        out["workerConfiguration"] = (
            capo_kafkaconnect.types.worker_configuration_description.serialize_json(
                value["worker_configuration"]
            )
        )
    out["useDefaultWorkerConfiguration"] = value.get(
        "use_default_worker_configuration", False
    )
    return out


def deserialize_json(data: dict) -> WorkerSetting:
    out: WorkerSetting = {}  # type: ignore[typeddict-item]
    if data.get("capacity") is not None:
        import capo_kafkaconnect.types.capacity_description

        out["capacity"] = capo_kafkaconnect.types.capacity_description.deserialize_json(
            data["capacity"]
        )
    if data.get("plugins") is not None:
        import capo_kafkaconnect.types.__list_of_plugin_description

        out["plugins"] = (
            capo_kafkaconnect.types.__list_of_plugin_description.deserialize_json(
                data["plugins"]
            )
        )
    if data.get("workerConfiguration") is not None:
        import capo_kafkaconnect.types.worker_configuration_description

        out["worker_configuration"] = (
            capo_kafkaconnect.types.worker_configuration_description.deserialize_json(
                data["workerConfiguration"]
            )
        )
    if data.get("useDefaultWorkerConfiguration") is not None:
        out["use_default_worker_configuration"] = data["useDefaultWorkerConfiguration"]
    else:
        out["use_default_worker_configuration"] = False
    return out
