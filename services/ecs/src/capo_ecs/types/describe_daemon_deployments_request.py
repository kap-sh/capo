"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string_list


class DescribeDaemonDeploymentsRequest(TypedDict, closed=True):
    daemon_deployment_arns: "capo_ecs.types.string_list.StringList"
    """<p>The ARN of the daemon deployments to describe. You can specify up to 20 ARNs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonDeploymentsRequest) -> dict:
    out: dict = {}
    import capo_ecs.types.string_list

    out["daemonDeploymentArns"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
        value["daemon_deployment_arns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonDeploymentsRequest:
    out: DescribeDaemonDeploymentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("daemonDeploymentArns") is not None:
        import capo_ecs.types.string_list

        out["daemon_deployment_arns"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["daemonDeploymentArns"]
            )
        )
    else:
        out["daemon_deployment_arns"] = []
    return out
