"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string_list


class DescribeServiceDeploymentsRequest(TypedDict, closed=True):
    service_deployment_arns: "capo_ecs.types.string_list.StringList"
    """<p>The ARN of the service deployment.</p> <p>You can specify a maximum of 20 ARNs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceDeploymentsRequest) -> dict:
    out: dict = {}
    import capo_ecs.types.string_list

    out["serviceDeploymentArns"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
        value["service_deployment_arns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceDeploymentsRequest:
    out: DescribeServiceDeploymentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceDeploymentArns") is not None:
        import capo_ecs.types.string_list

        out["service_deployment_arns"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["serviceDeploymentArns"]
            )
        )
    else:
        out["service_deployment_arns"] = []
    return out
