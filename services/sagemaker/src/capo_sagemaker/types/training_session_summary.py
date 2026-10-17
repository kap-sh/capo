"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingSessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_session_arn
    import capo_sagemaker.types.training_session_status


class TrainingSessionSummary(TypedDict, closed=True):
    training_session_arn: NotRequired[
        "capo_sagemaker.types.training_session_arn.TrainingSessionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training session.</p>"""
    training_session_status: NotRequired[
        "capo_sagemaker.types.training_session_status.TrainingSessionStatus"
    ]
    """<p>The current status of the training session.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the training session was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the training session was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingSessionSummary) -> dict:
    out: dict = {}
    if "training_session_arn" in value:
        out["TrainingSessionArn"] = value["training_session_arn"]
    if "training_session_status" in value:
        import capo_sagemaker.types.training_session_status

        out["TrainingSessionStatus"] = (
            capo_sagemaker.types.training_session_status.serialize_aws_json_1_1(
                value["training_session_status"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingSessionSummary:
    out: TrainingSessionSummary = {}  # type: ignore[typeddict-item]
    if data.get("TrainingSessionArn") is not None:
        out["training_session_arn"] = data["TrainingSessionArn"]
    if data.get("TrainingSessionStatus") is not None:
        import capo_sagemaker.types.training_session_status

        out["training_session_status"] = (
            capo_sagemaker.types.training_session_status.deserialize_aws_json_1_1(
                data["TrainingSessionStatus"]
            )
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
