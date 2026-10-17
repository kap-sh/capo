"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingSessionOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_session_s3_location


class TrainingSessionOutputConfig(TypedDict, closed=True):
    s3_location: NotRequired[
        "capo_sagemaker.types.training_session_s3_location.TrainingSessionS3Location"
    ]
    """<p>The Amazon S3 location where training session outputs, including checkpoints and model artifacts, are stored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingSessionOutputConfig) -> dict:
    out: dict = {}
    if "s3_location" in value:
        import capo_sagemaker.types.training_session_s3_location

        out["S3Location"] = (
            capo_sagemaker.types.training_session_s3_location.serialize_aws_json_1_1(
                value["s3_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingSessionOutputConfig:
    out: TrainingSessionOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Location") is not None:
        import capo_sagemaker.types.training_session_s3_location

        out["s3_location"] = (
            capo_sagemaker.types.training_session_s3_location.deserialize_aws_json_1_1(
                data["S3Location"]
            )
        )
    return out
