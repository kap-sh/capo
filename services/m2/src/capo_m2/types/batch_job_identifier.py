"""Generated from Smithy shape ``com.amazonaws.m2#BatchJobIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_m2.types.file_batch_job_identifier
    import capo_m2.types.restart_batch_job_identifier
    import capo_m2.types.s3_batch_job_identifier
    import capo_m2.types.script_batch_job_identifier


class BatchJobIdentifierFileBatchJobIdentifierMember(TypedDict, closed=True):
    fileBatchJobIdentifier: (
        "capo_m2.types.file_batch_job_identifier.FileBatchJobIdentifier"
    )


class BatchJobIdentifierScriptBatchJobIdentifierMember(TypedDict, closed=True):
    scriptBatchJobIdentifier: (
        "capo_m2.types.script_batch_job_identifier.ScriptBatchJobIdentifier"
    )


class BatchJobIdentifierS3BatchJobIdentifierMember(TypedDict, closed=True):
    s3BatchJobIdentifier: "capo_m2.types.s3_batch_job_identifier.S3BatchJobIdentifier"


class BatchJobIdentifierRestartBatchJobIdentifierMember(TypedDict, closed=True):
    restartBatchJobIdentifier: (
        "capo_m2.types.restart_batch_job_identifier.RestartBatchJobIdentifier"
    )


BatchJobIdentifier: TypeAlias = (
    BatchJobIdentifierFileBatchJobIdentifierMember
    | BatchJobIdentifierScriptBatchJobIdentifierMember
    | BatchJobIdentifierS3BatchJobIdentifierMember
    | BatchJobIdentifierRestartBatchJobIdentifierMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: BatchJobIdentifier) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BatchJobIdentifier: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fileBatchJobIdentifier" in value:
        import capo_m2.types.file_batch_job_identifier

        return {
            "fileBatchJobIdentifier": capo_m2.types.file_batch_job_identifier.serialize_json(
                value["fileBatchJobIdentifier"]
            )
        }
    elif "scriptBatchJobIdentifier" in value:
        import capo_m2.types.script_batch_job_identifier

        return {
            "scriptBatchJobIdentifier": capo_m2.types.script_batch_job_identifier.serialize_json(
                value["scriptBatchJobIdentifier"]
            )
        }
    elif "s3BatchJobIdentifier" in value:
        import capo_m2.types.s3_batch_job_identifier

        return {
            "s3BatchJobIdentifier": capo_m2.types.s3_batch_job_identifier.serialize_json(
                value["s3BatchJobIdentifier"]
            )
        }
    elif "restartBatchJobIdentifier" in value:
        import capo_m2.types.restart_batch_job_identifier

        return {
            "restartBatchJobIdentifier": capo_m2.types.restart_batch_job_identifier.serialize_json(
                value["restartBatchJobIdentifier"]
            )
        }
    else:
        raise SerializationError("BatchJobIdentifier: no variant present")


def deserialize_json(data: dict) -> BatchJobIdentifier:
    if data.get("fileBatchJobIdentifier") is not None:
        import capo_m2.types.file_batch_job_identifier

        return {
            "fileBatchJobIdentifier": capo_m2.types.file_batch_job_identifier.deserialize_json(
                data["fileBatchJobIdentifier"]
            )
        }
    elif data.get("scriptBatchJobIdentifier") is not None:
        import capo_m2.types.script_batch_job_identifier

        return {
            "scriptBatchJobIdentifier": capo_m2.types.script_batch_job_identifier.deserialize_json(
                data["scriptBatchJobIdentifier"]
            )
        }
    elif data.get("s3BatchJobIdentifier") is not None:
        import capo_m2.types.s3_batch_job_identifier

        return {
            "s3BatchJobIdentifier": capo_m2.types.s3_batch_job_identifier.deserialize_json(
                data["s3BatchJobIdentifier"]
            )
        }
    elif data.get("restartBatchJobIdentifier") is not None:
        import capo_m2.types.restart_batch_job_identifier

        return {
            "restartBatchJobIdentifier": capo_m2.types.restart_batch_job_identifier.deserialize_json(
                data["restartBatchJobIdentifier"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("BatchJobIdentifier: no recognized variant key")
