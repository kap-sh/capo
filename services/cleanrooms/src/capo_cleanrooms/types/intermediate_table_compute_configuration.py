"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableComputeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_compute_configuration
    import capo_cleanrooms.types.worker_compute_configuration


class IntermediateTableComputeConfigurationQueryComputeConfigurationMember(
    TypedDict, closed=True
):
    queryComputeConfiguration: (
        "capo_cleanrooms.types.worker_compute_configuration.WorkerComputeConfiguration"
    )


class IntermediateTableComputeConfigurationJobComputeConfigurationMember(
    TypedDict, closed=True
):
    jobComputeConfiguration: "capo_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"


IntermediateTableComputeConfiguration: TypeAlias = (
    IntermediateTableComputeConfigurationQueryComputeConfigurationMember
    | IntermediateTableComputeConfigurationJobComputeConfigurationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableComputeConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IntermediateTableComputeConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "queryComputeConfiguration" in value:
        import capo_cleanrooms.types.worker_compute_configuration

        return {
            "queryComputeConfiguration": capo_cleanrooms.types.worker_compute_configuration.serialize_json(
                value["queryComputeConfiguration"]
            )
        }
    elif "jobComputeConfiguration" in value:
        import capo_cleanrooms.types.protected_job_compute_configuration

        return {
            "jobComputeConfiguration": capo_cleanrooms.types.protected_job_compute_configuration.serialize_json(
                value["jobComputeConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "IntermediateTableComputeConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> IntermediateTableComputeConfiguration:
    if data.get("queryComputeConfiguration") is not None:
        import capo_cleanrooms.types.worker_compute_configuration

        return {
            "queryComputeConfiguration": capo_cleanrooms.types.worker_compute_configuration.deserialize_json(
                data["queryComputeConfiguration"]
            )
        }
    elif data.get("jobComputeConfiguration") is not None:
        import capo_cleanrooms.types.protected_job_compute_configuration

        return {
            "jobComputeConfiguration": capo_cleanrooms.types.protected_job_compute_configuration.deserialize_json(
                data["jobComputeConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "IntermediateTableComputeConfiguration: no recognized variant key"
        )
