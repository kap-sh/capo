"""Generated from Smithy shape ``com.amazonaws.codedeploy#StopDeploymentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.message
    import capo_codedeploy.types.stop_status


class StopDeploymentOutput(TypedDict, closed=True):
    status: NotRequired["capo_codedeploy.types.stop_status.StopStatus"]
    """<p>The status of the stop deployment operation:</p> <ul> <li> <p>Pending: The stop operation is pending.</p> </li> <li> <p>Succeeded: The stop operation was successful.</p> </li> </ul>"""
    status_message: NotRequired["capo_codedeploy.types.message.Message"]
    """<p>An accompanying status message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopDeploymentOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_codedeploy.types.stop_status

        out["status"] = capo_codedeploy.types.stop_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopDeploymentOutput:
    out: StopDeploymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codedeploy.types.stop_status

        out["status"] = capo_codedeploy.types.stop_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopDeploymentOutput) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_codedeploy.types.stop_status

        out["status"] = capo_codedeploy.types.stop_status.serialize_cbor(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_cbor(data: dict) -> StopDeploymentOutput:
    out: StopDeploymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codedeploy.types.stop_status

        out["status"] = capo_codedeploy.types.stop_status.deserialize_cbor(
            data["status"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out
