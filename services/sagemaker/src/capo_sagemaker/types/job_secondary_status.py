"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobSecondaryStatus``."""

from typing import Literal, TypeAlias, cast

JobSecondaryStatus: TypeAlias = Literal[
    "Starting",
    "Downloading",
    "Training",
    "Uploading",
    "Stopping",
    "Stopped",
    "MaxRuntimeExceeded",
    "Interrupted",
    "Failed",
    "Completed",
    "Restarting",
    "Pending",
    "Generating",
    "PartialGeneration",
    "Evaluating",
    "Validating",
    "Preparing",
    "Executing",
    "Publishing",
    "Finalizing",
    "Transforming",
    "Deleting",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobSecondaryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobSecondaryStatus:
    return cast(JobSecondaryStatus, data)
