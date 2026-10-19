"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelImportJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.imported_model_arn
    import capo_bedrock.types.imported_model_name
    import capo_bedrock.types.job_name
    import capo_bedrock.types.model_import_job_arn
    import capo_bedrock.types.model_import_job_status
    import capo_bedrock.types.timestamp


class ModelImportJobSummary(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.model_import_job_arn.ModelImportJobArn"
    """<p>The Amazon Resource Name (ARN) of the import job.</p>"""
    job_name: "capo_bedrock.types.job_name.JobName"
    """<p>The name of the import job.</p>"""
    status: "capo_bedrock.types.model_import_job_status.ModelImportJobStatus"
    """<p>The status of the imported job. </p>"""
    last_modified_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time when the import job was last modified.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The time import job was created.</p>"""
    end_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time when import job ended.</p>"""
    imported_model_arn: NotRequired[
        "capo_bedrock.types.imported_model_arn.ImportedModelArn"
    ]
    """<p>The Amazon resource Name (ARN) of the imported model.</p>"""
    imported_model_name: NotRequired[
        "capo_bedrock.types.imported_model_name.ImportedModelName"
    ]
    """<p>The name of the imported model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelImportJobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    import capo_bedrock.types.model_import_job_status

    out["status"] = capo_bedrock.types.model_import_job_status.serialize_json(
        value["status"]
    )
    if "last_modified_time" in value:
        import capo_bedrock.types.timestamp

        out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "end_time" in value:
        import capo_bedrock.types.timestamp

        out["endTime"] = capo_bedrock.types.timestamp.serialize_json(value["end_time"])
    if "imported_model_arn" in value:
        out["importedModelArn"] = value["imported_model_arn"]
    if "imported_model_name" in value:
        out["importedModelName"] = value["imported_model_name"]
    return out


def deserialize_json(data: dict) -> ModelImportJobSummary:
    out: ModelImportJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("status") is not None:
        import capo_bedrock.types.model_import_job_status

        out["status"] = capo_bedrock.types.model_import_job_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.model_import_job_status.ModelImportJobStatus", ""
        )
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    if data.get("creationTime") is not None:
        import capo_bedrock.types.timestamp

        out["creation_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("endTime") is not None:
        import capo_bedrock.types.timestamp

        out["end_time"] = capo_bedrock.types.timestamp.deserialize_json(data["endTime"])
    if data.get("importedModelArn") is not None:
        out["imported_model_arn"] = data["importedModelArn"]
    if data.get("importedModelName") is not None:
        out["imported_model_name"] = data["importedModelName"]
    return out
