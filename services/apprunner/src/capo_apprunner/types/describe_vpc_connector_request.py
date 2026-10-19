"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeVpcConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn


class DescribeVpcConnectorRequest(TypedDict, closed=True):
    vpc_connector_arn: (
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the App Runner VPC connector that you want a description for.</p> <p>The ARN must be a full VPC connector ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeVpcConnectorRequest) -> dict:
    out: dict = {}
    out["VpcConnectorArn"] = value["vpc_connector_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeVpcConnectorRequest:
    out: DescribeVpcConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("VpcConnectorArn") is not None:
        out["vpc_connector_arn"] = data["VpcConnectorArn"]
    else:
        out["vpc_connector_arn"] = ""
    return out
