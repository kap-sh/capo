"""Generated from Smithy shape ``com.amazonaws.codedeploy#MinimumHealthyHosts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.minimum_healthy_hosts_type
    import capo_codedeploy.types.minimum_healthy_hosts_value


class MinimumHealthyHosts(TypedDict, closed=True):
    type: NotRequired[
        "capo_codedeploy.types.minimum_healthy_hosts_type.MinimumHealthyHostsType"
    ]
    """<p>The minimum healthy instance type:</p> <ul> <li> <p> <code>HOST_COUNT</code>: The minimum number of healthy instances as an absolute value.</p> </li> <li> <p> <code>FLEET_PERCENT</code>: The minimum number of healthy instances as a percentage of the total number of instances in the deployment.</p> </li> </ul> <p>In an example of nine instances, if a HOST_COUNT of six is specified, deploy to up to three instances at a time. The deployment is successful if six or more instances are deployed to successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to five instances at a time. The deployment is successful if four or more instances are deployed to successfully. Otherwise, the deployment fails.</p> <note> <p>In a call to the <code>GetDeploymentConfig</code>, CodeDeployDefault.OneAtATime returns a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, CodeDeploy attempts to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment is still successful.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html">CodeDeploy Instance Health</a> in the <i>CodeDeploy User Guide</i>.</p>"""
    value: "capo_codedeploy.types.minimum_healthy_hosts_value.MinimumHealthyHostsValue"
    """<p>The minimum healthy instance value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MinimumHealthyHosts) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_codedeploy.types.minimum_healthy_hosts_type

        out["type"] = (
            capo_codedeploy.types.minimum_healthy_hosts_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> MinimumHealthyHosts:
    out: MinimumHealthyHosts = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codedeploy.types.minimum_healthy_hosts_type

        out["type"] = (
            capo_codedeploy.types.minimum_healthy_hosts_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = 0
    return out
