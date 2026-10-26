"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobComputeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_worker_compute_configuration


class _ProtectedJobComputeConfiguration_worker(TypedDict, closed=True):
    worker: "capo_cleanrooms.types.protected_job_worker_compute_configuration.ProtectedJobWorkerComputeConfiguration"


ProtectedJobComputeConfiguration: TypeAlias = (
    _ProtectedJobComputeConfiguration_worker | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobComputeConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProtectedJobComputeConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "worker" in value:
        import capo_cleanrooms.types.protected_job_worker_compute_configuration

        return {
            "worker": capo_cleanrooms.types.protected_job_worker_compute_configuration.serialize_json(
                value["worker"]
            )
        }
    else:
        raise SerializationError("ProtectedJobComputeConfiguration: no variant present")


def deserialize_json(data: dict) -> ProtectedJobComputeConfiguration:
    if data.get("worker") is not None:
        import capo_cleanrooms.types.protected_job_worker_compute_configuration

        return {
            "worker": capo_cleanrooms.types.protected_job_worker_compute_configuration.deserialize_json(
                data["worker"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ProtectedJobComputeConfiguration: no recognized variant key"
        )
