"""Generated from Smithy shape ``com.amazonaws.sagemaker#EmrServerlessComputeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.role_arn


class EmrServerlessComputeConfig(TypedDict, closed=True):
    execution_role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role granting the AutoML job V2 the necessary permissions access policies to list, connect to, or manage EMR Serverless jobs. For detailed information about the required permissions of this role, see "How to configure AutoML to initiate a remote job on EMR Serverless for large datasets" in <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html">Create a regression or classification job for tabular data using the AutoML API</a> or <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-timeseries-forecasting.html#timeseries-forecasting-api-optional-params">Create an AutoML job for time-series forecasting using the API</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmrServerlessComputeConfig) -> dict:
    out: dict = {}
    if "execution_role_arn" in value:
        out["ExecutionRoleARN"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EmrServerlessComputeConfig:
    out: EmrServerlessComputeConfig = {}  # type: ignore[typeddict-item]
    if data.get("ExecutionRoleARN") is not None:
        out["execution_role_arn"] = data["ExecutionRoleARN"]
    return out
