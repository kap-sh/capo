"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.instances_list
    import capo_codedeploy.types.next_token


class ListDeploymentInstancesOutput(TypedDict, closed=True):
    instances_list: NotRequired["capo_codedeploy.types.instances_list.InstancesList"]
    """<p>A list of instance IDs.</p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployment instances call to return the next set of deployment instances in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentInstancesOutput) -> dict:
    out: dict = {}
    if "instances_list" in value:
        import capo_codedeploy.types.instances_list

        out["instancesList"] = (
            capo_codedeploy.types.instances_list.serialize_aws_json_1_1(
                value["instances_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentInstancesOutput:
    out: ListDeploymentInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("instancesList") is not None:
        import capo_codedeploy.types.instances_list

        out["instances_list"] = (
            capo_codedeploy.types.instances_list.deserialize_aws_json_1_1(
                data["instancesList"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDeploymentInstancesOutput) -> dict:
    out: dict = {}
    if "instances_list" in value:
        import capo_codedeploy.types.instances_list

        out["instancesList"] = capo_codedeploy.types.instances_list.serialize_cbor(
            value["instances_list"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDeploymentInstancesOutput:
    out: ListDeploymentInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("instancesList") is not None:
        import capo_codedeploy.types.instances_list

        out["instances_list"] = capo_codedeploy.types.instances_list.deserialize_cbor(
            data["instancesList"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
