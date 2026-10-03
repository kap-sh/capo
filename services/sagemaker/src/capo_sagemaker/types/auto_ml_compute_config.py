"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLComputeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.emr_serverless_compute_config


class AutoMLComputeConfig(TypedDict, closed=True):
    emr_serverless_compute_config: NotRequired[
        "capo_sagemaker.types.emr_serverless_compute_config.EmrServerlessComputeConfig"
    ]
    """<p>The configuration for using <a href="https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html"> EMR Serverless</a> to run the AutoML job V2.</p> <p>To allow your AutoML job V2 to automatically initiate a remote job on EMR Serverless when additional compute resources are needed to process large datasets, you need to provide an <code>EmrServerlessComputeConfig</code> object, which includes an <code>ExecutionRoleARN</code> attribute, to the <code>AutoMLComputeConfig</code> of the AutoML job V2 input request.</p> <p>By seamlessly transitioning to EMR Serverless when required, the AutoML job can handle datasets that would otherwise exceed the initially provisioned resources, without any manual intervention from you. </p> <p>EMR Serverless is available for the tabular and time series problem types. We recommend setting up this option for tabular datasets larger than 5 GB and time series datasets larger than 30 GB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLComputeConfig) -> dict:
    out: dict = {}
    if "emr_serverless_compute_config" in value:
        import capo_sagemaker.types.emr_serverless_compute_config

        out["EmrServerlessComputeConfig"] = (
            capo_sagemaker.types.emr_serverless_compute_config.serialize_aws_json_1_1(
                value["emr_serverless_compute_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLComputeConfig:
    out: AutoMLComputeConfig = {}  # type: ignore[typeddict-item]
    if data.get("EmrServerlessComputeConfig") is not None:
        import capo_sagemaker.types.emr_serverless_compute_config

        out["emr_serverless_compute_config"] = (
            capo_sagemaker.types.emr_serverless_compute_config.deserialize_aws_json_1_1(
                data["EmrServerlessComputeConfig"]
            )
        )
    return out
