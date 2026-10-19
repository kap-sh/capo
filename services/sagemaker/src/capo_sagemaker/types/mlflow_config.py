"""Generated from Smithy shape ``com.amazonaws.sagemaker#MlflowConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ml_flow_resource_arn
    import capo_sagemaker.types.mlflow_experiment_name
    import capo_sagemaker.types.mlflow_run_name


class MlflowConfig(TypedDict, closed=True):
    mlflow_resource_arn: "capo_sagemaker.types.ml_flow_resource_arn.MlFlowResourceArn"
    """<p> The Amazon Resource Name (ARN) of the MLflow resource. </p>"""
    mlflow_experiment_name: NotRequired[
        "capo_sagemaker.types.mlflow_experiment_name.MlflowExperimentName"
    ]
    """<p> The MLflow experiment name used for this job. </p>"""
    mlflow_run_name: NotRequired["capo_sagemaker.types.mlflow_run_name.MlflowRunName"]
    """<p> The MLflow run name used for this job. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MlflowConfig) -> dict:
    out: dict = {}
    out["MlflowResourceArn"] = value["mlflow_resource_arn"]
    if "mlflow_experiment_name" in value:
        out["MlflowExperimentName"] = value["mlflow_experiment_name"]
    if "mlflow_run_name" in value:
        out["MlflowRunName"] = value["mlflow_run_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MlflowConfig:
    out: MlflowConfig = {}  # type: ignore[typeddict-item]
    if data.get("MlflowResourceArn") is not None:
        out["mlflow_resource_arn"] = data["MlflowResourceArn"]
    else:
        out["mlflow_resource_arn"] = ""
    if data.get("MlflowExperimentName") is not None:
        out["mlflow_experiment_name"] = data["MlflowExperimentName"]
    if data.get("MlflowRunName") is not None:
        out["mlflow_run_name"] = data["MlflowRunName"]
    return out
