"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingSessionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_session_summary

TrainingSessionSummaries: TypeAlias = list[
    "capo_sagemaker.types.training_session_summary.TrainingSessionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingSessionSummaries) -> list:
    import capo_sagemaker.types.training_session_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.training_session_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingSessionSummaries:
    import capo_sagemaker.types.training_session_summary

    out: TrainingSessionSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemaker.types.training_session_summary.deserialize_aws_json_1_1(item)
        )
    return out
