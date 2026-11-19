"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListDeploymentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployments_list
    import capo_codedeploy.types.next_token


class ListDeploymentsOutput(TypedDict, closed=True):
    deployments: NotRequired["capo_codedeploy.types.deployments_list.DeploymentsList"]
    """<p>A list of deployment IDs.</p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list deployments call to return the next set of deployments in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeploymentsOutput) -> dict:
    out: dict = {}
    if "deployments" in value:
        import capo_codedeploy.types.deployments_list

        out["deployments"] = (
            capo_codedeploy.types.deployments_list.serialize_aws_json_1_1(
                value["deployments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeploymentsOutput:
    out: ListDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deployments") is not None:
        import capo_codedeploy.types.deployments_list

        out["deployments"] = (
            capo_codedeploy.types.deployments_list.deserialize_aws_json_1_1(
                data["deployments"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDeploymentsOutput) -> dict:
    out: dict = {}
    if "deployments" in value:
        import capo_codedeploy.types.deployments_list

        out["deployments"] = capo_codedeploy.types.deployments_list.serialize_cbor(
            value["deployments"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDeploymentsOutput:
    out: ListDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deployments") is not None:
        import capo_codedeploy.types.deployments_list

        out["deployments"] = capo_codedeploy.types.deployments_list.deserialize_cbor(
            data["deployments"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
