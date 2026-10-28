"""Generated from Smithy shape ``com.amazonaws.m2#BatchJobDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_m2.types.file_batch_job_definition
    import capo_m2.types.script_batch_job_definition


class BatchJobDefinitionFileBatchJobDefinitionMember(TypedDict, closed=True):
    fileBatchJobDefinition: (
        "capo_m2.types.file_batch_job_definition.FileBatchJobDefinition"
    )


class BatchJobDefinitionScriptBatchJobDefinitionMember(TypedDict, closed=True):
    scriptBatchJobDefinition: (
        "capo_m2.types.script_batch_job_definition.ScriptBatchJobDefinition"
    )


BatchJobDefinition: TypeAlias = (
    BatchJobDefinitionFileBatchJobDefinitionMember
    | BatchJobDefinitionScriptBatchJobDefinitionMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: BatchJobDefinition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BatchJobDefinition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fileBatchJobDefinition" in value:
        import capo_m2.types.file_batch_job_definition

        return {
            "fileBatchJobDefinition": capo_m2.types.file_batch_job_definition.serialize_json(
                value["fileBatchJobDefinition"]
            )
        }
    elif "scriptBatchJobDefinition" in value:
        import capo_m2.types.script_batch_job_definition

        return {
            "scriptBatchJobDefinition": capo_m2.types.script_batch_job_definition.serialize_json(
                value["scriptBatchJobDefinition"]
            )
        }
    else:
        raise SerializationError("BatchJobDefinition: no variant present")


def deserialize_json(data: dict) -> BatchJobDefinition:
    if data.get("fileBatchJobDefinition") is not None:
        import capo_m2.types.file_batch_job_definition

        return {
            "fileBatchJobDefinition": capo_m2.types.file_batch_job_definition.deserialize_json(
                data["fileBatchJobDefinition"]
            )
        }
    elif data.get("scriptBatchJobDefinition") is not None:
        import capo_m2.types.script_batch_job_definition

        return {
            "scriptBatchJobDefinition": capo_m2.types.script_batch_job_definition.deserialize_json(
                data["scriptBatchJobDefinition"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("BatchJobDefinition: no recognized variant key")
