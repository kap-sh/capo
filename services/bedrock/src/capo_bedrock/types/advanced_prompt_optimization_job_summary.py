"""Generated from Smithy shape ``com.amazonaws.bedrock#AdvancedPromptOptimizationJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_job_arn
    import capo_bedrock.types.advanced_prompt_optimization_job_name
    import capo_bedrock.types.advanced_prompt_optimization_job_status
    import capo_bedrock.types.timestamp


class AdvancedPromptOptimizationJobSummary(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.advanced_prompt_optimization_job_arn.AdvancedPromptOptimizationJobArn"
    """<p>The Amazon Resource Name (ARN) of the job.</p>"""
    job_name: "capo_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName"
    """<p>The name of the job.</p>"""
    job_status: "capo_bedrock.types.advanced_prompt_optimization_job_status.AdvancedPromptOptimizationJobStatus"
    """<p>The status of the job.</p>"""
    creation_time: "capo_bedrock.types.timestamp.Timestamp"
    """<p>The time at which the job was created.</p>"""
    last_modified_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the job was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedPromptOptimizationJobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    out["jobName"] = value["job_name"]
    import capo_bedrock.types.advanced_prompt_optimization_job_status

    out["jobStatus"] = (
        capo_bedrock.types.advanced_prompt_optimization_job_status.serialize_json(
            value["job_status"]
        )
    )
    import capo_bedrock.types.timestamp

    out["creationTime"] = capo_bedrock.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "last_modified_time" in value:
        import capo_bedrock.types.timestamp

        out["lastModifiedTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    return out


def deserialize_json(data: dict) -> AdvancedPromptOptimizationJobSummary:
    out: AdvancedPromptOptimizationJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("jobStatus") is not None:
        import capo_bedrock.types.advanced_prompt_optimization_job_status

        out["job_status"] = (
            capo_bedrock.types.advanced_prompt_optimization_job_status.deserialize_json(
                data["jobStatus"]
            )
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_bedrock.types.advanced_prompt_optimization_job_status.AdvancedPromptOptimizationJobStatus",
            "",
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
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock.types.timestamp

        out["last_modified_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["lastModifiedTime"]
        )
    return out
