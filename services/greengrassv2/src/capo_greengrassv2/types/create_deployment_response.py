"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CreateDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.io_t_job_arn
    import capo_greengrassv2.types.non_empty_string


class CreateDeploymentResponse(TypedDict, closed=True):
    deployment_id: NotRequired[
        "capo_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the deployment.</p>"""
    iot_job_id: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the IoT job that applies the deployment to target devices.</p>"""
    iot_job_arn: NotRequired["capo_greengrassv2.types.io_t_job_arn.IoTJobARN"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the IoT job that applies the deployment to target devices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentResponse) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "iot_job_id" in value:
        out["iotJobId"] = value["iot_job_id"]
    if "iot_job_arn" in value:
        out["iotJobArn"] = value["iot_job_arn"]
    return out


def deserialize_json(data: dict) -> CreateDeploymentResponse:
    out: CreateDeploymentResponse = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    if data.get("iotJobId") is not None:
        out["iot_job_id"] = data["iotJobId"]
    if data.get("iotJobArn") is not None:
        out["iot_job_arn"] = data["iotJobArn"]
    return out
