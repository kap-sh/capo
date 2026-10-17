"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingSessionModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.base_model_arn
    import capo_sagemaker.types.java_boolean


class TrainingSessionModelConfig(TypedDict, closed=True):
    base_model_arn: NotRequired["capo_sagemaker.types.base_model_arn.BaseModelArn"]
    """<p>The Amazon Resource Name (ARN) of the base foundation model from SageMaker Hub.</p>"""
    accept_eula: NotRequired["capo_sagemaker.types.java_boolean.JavaBoolean"]
    """<p>Specifies whether you accept the end-user license agreement (EULA) for gated models.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingSessionModelConfig) -> dict:
    out: dict = {}
    if "base_model_arn" in value:
        out["BaseModelArn"] = value["base_model_arn"]
    if "accept_eula" in value:
        out["AcceptEula"] = value["accept_eula"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingSessionModelConfig:
    out: TrainingSessionModelConfig = {}  # type: ignore[typeddict-item]
    if data.get("BaseModelArn") is not None:
        out["base_model_arn"] = data["BaseModelArn"]
    if data.get("AcceptEula") is not None:
        out["accept_eula"] = data["AcceptEula"]
    return out
