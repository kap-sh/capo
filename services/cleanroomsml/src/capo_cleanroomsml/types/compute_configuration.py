"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ComputeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError, SerializationError
from capo_cleanroomsml.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanroomsml.types.worker_compute_configuration


class ComputeConfigurationWorkerMember(TypedDict, closed=True):
    worker: "capo_cleanroomsml.types.worker_compute_configuration.WorkerComputeConfiguration"


ComputeConfiguration: TypeAlias = ComputeConfigurationWorkerMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ComputeConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ComputeConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "worker" in value:
        import capo_cleanroomsml.types.worker_compute_configuration

        return {
            "worker": capo_cleanroomsml.types.worker_compute_configuration.serialize_json(
                value["worker"]
            )
        }
    else:
        raise SerializationError("ComputeConfiguration: no variant present")


def deserialize_json(data: dict) -> ComputeConfiguration:
    if data.get("worker") is not None:
        import capo_cleanroomsml.types.worker_compute_configuration

        return {
            "worker": capo_cleanroomsml.types.worker_compute_configuration.deserialize_json(
                data["worker"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ComputeConfiguration: no recognized variant key")
