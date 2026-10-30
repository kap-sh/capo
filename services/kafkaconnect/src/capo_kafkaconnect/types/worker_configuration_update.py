"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__long_min1
    import capo_kafkaconnect.types.__string


class WorkerConfigurationUpdate(TypedDict, closed=True):
    revision: "capo_kafkaconnect.types.__long_min1.__longMin1"
    """<p>The revision of the worker configuration.</p>"""
    worker_configuration_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerConfigurationUpdate) -> dict:
    out: dict = {}
    out["revision"] = value["revision"]
    out["workerConfigurationArn"] = value["worker_configuration_arn"]
    return out


def deserialize_json(data: dict) -> WorkerConfigurationUpdate:
    out: WorkerConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    if data.get("workerConfigurationArn") is not None:
        out["worker_configuration_arn"] = data["workerConfigurationArn"]
    else:
        out["worker_configuration_arn"] = ""
    return out
