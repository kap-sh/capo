"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteVpcIngressConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn


class DeleteVpcIngressConnectionRequest(TypedDict, closed=True):
    vpc_ingress_connection_arn: (
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the App Runner VPC Ingress Connection that you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVpcIngressConnectionRequest) -> dict:
    out: dict = {}
    out["VpcIngressConnectionArn"] = value["vpc_ingress_connection_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVpcIngressConnectionRequest:
    out: DeleteVpcIngressConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("VpcIngressConnectionArn") is not None:
        out["vpc_ingress_connection_arn"] = data["VpcIngressConnectionArn"]
    else:
        out["vpc_ingress_connection_arn"] = ""
    return out
