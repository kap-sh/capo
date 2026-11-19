"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentConfigsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployment_configs_list
    import capo_codedeploy.types.next_token


class ListDeploymentConfigsOutput(TypedDict, closed=True):
    deployment_configs_list: NotRequired[
        "capo_codedeploy.types.deployment_configs_list.DeploymentConfigsList"
    ]
    """<p>A list of deployment configurations, including built-in configurations such as <code>CodeDeployDefault.OneAtATime</code>.</p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment configurations call to return the next set of deployment configurations in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentConfigsOutput) -> dict:
    out: dict = {}
    if "deployment_configs_list" in value:
        import capo_codedeploy.types.deployment_configs_list

        out["deploymentConfigsList"] = (
            capo_codedeploy.types.deployment_configs_list.serialize_aws_json_1_1(
                value["deployment_configs_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentConfigsOutput:
    out: ListDeploymentConfigsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentConfigsList") is not None:
        import capo_codedeploy.types.deployment_configs_list

        out["deployment_configs_list"] = (
            capo_codedeploy.types.deployment_configs_list.deserialize_aws_json_1_1(
                data["deploymentConfigsList"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDeploymentConfigsOutput) -> dict:
    out: dict = {}
    if "deployment_configs_list" in value:
        import capo_codedeploy.types.deployment_configs_list

        out["deploymentConfigsList"] = (
            capo_codedeploy.types.deployment_configs_list.serialize_cbor(
                value["deployment_configs_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDeploymentConfigsOutput:
    out: ListDeploymentConfigsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentConfigsList") is not None:
        import capo_codedeploy.types.deployment_configs_list

        out["deployment_configs_list"] = (
            capo_codedeploy.types.deployment_configs_list.deserialize_cbor(
                data["deploymentConfigsList"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
