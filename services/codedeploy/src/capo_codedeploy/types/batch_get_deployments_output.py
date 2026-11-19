"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.deployments_info_list


class BatchGetDeploymentsOutput(TypedDict, closed=True):
    deployments_info: NotRequired[
        "capo_codedeploy.types.deployments_info_list.DeploymentsInfoList"
    ]
    """<p> Information about the deployments. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentsOutput) -> dict:
    out: dict = {}
    if "deployments_info" in value:
        import capo_codedeploy.types.deployments_info_list

        out["deploymentsInfo"] = (
            capo_codedeploy.types.deployments_info_list.serialize_aws_json_1_1(
                value["deployments_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentsOutput:
    out: BatchGetDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentsInfo") is not None:
        import capo_codedeploy.types.deployments_info_list

        out["deployments_info"] = (
            capo_codedeploy.types.deployments_info_list.deserialize_aws_json_1_1(
                data["deploymentsInfo"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetDeploymentsOutput) -> dict:
    out: dict = {}
    if "deployments_info" in value:
        import capo_codedeploy.types.deployments_info_list

        out["deploymentsInfo"] = (
            capo_codedeploy.types.deployments_info_list.serialize_cbor(
                value["deployments_info"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetDeploymentsOutput:
    out: BatchGetDeploymentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentsInfo") is not None:
        import capo_codedeploy.types.deployments_info_list

        out["deployments_info"] = (
            capo_codedeploy.types.deployments_info_list.deserialize_cbor(
                data["deploymentsInfo"]
            )
        )
    return out
