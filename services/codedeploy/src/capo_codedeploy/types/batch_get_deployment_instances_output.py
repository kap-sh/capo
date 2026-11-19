"""Generated from Smithy shape ``com.amazonaws.codedeploy#BatchGetDeploymentInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.error_message
    import capo_codedeploy.types.instance_summary_list


class BatchGetDeploymentInstancesOutput(TypedDict, closed=True):
    instances_summary: NotRequired[
        "capo_codedeploy.types.instance_summary_list.InstanceSummaryList"
    ]
    """<p>Information about the instance.</p>"""
    error_message: NotRequired["capo_codedeploy.types.error_message.ErrorMessage"]
    """<p>Information about errors that might have occurred during the API call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetDeploymentInstancesOutput) -> dict:
    out: dict = {}
    if "instances_summary" in value:
        import capo_codedeploy.types.instance_summary_list

        out["instancesSummary"] = (
            capo_codedeploy.types.instance_summary_list.serialize_aws_json_1_1(
                value["instances_summary"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetDeploymentInstancesOutput:
    out: BatchGetDeploymentInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("instancesSummary") is not None:
        import capo_codedeploy.types.instance_summary_list

        out["instances_summary"] = (
            capo_codedeploy.types.instance_summary_list.deserialize_aws_json_1_1(
                data["instancesSummary"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetDeploymentInstancesOutput) -> dict:
    out: dict = {}
    if "instances_summary" in value:
        import capo_codedeploy.types.instance_summary_list

        out["instancesSummary"] = (
            capo_codedeploy.types.instance_summary_list.serialize_cbor(
                value["instances_summary"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> BatchGetDeploymentInstancesOutput:
    out: BatchGetDeploymentInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("instancesSummary") is not None:
        import capo_codedeploy.types.instance_summary_list

        out["instances_summary"] = (
            capo_codedeploy.types.instance_summary_list.deserialize_cbor(
                data["instancesSummary"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
