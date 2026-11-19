"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployTargetEventContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.string


class DeployTargetEventContext(TypedDict, closed=True):
    ssm_command_id: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The command ID for the event for the deploy action.</p>"""
    message: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The context message for the event for the deploy action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployTargetEventContext) -> dict:
    out: dict = {}
    if "ssm_command_id" in value:
        out["ssmCommandId"] = value["ssm_command_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployTargetEventContext:
    out: DeployTargetEventContext = {}  # type: ignore[typeddict-item]
    if data.get("ssmCommandId") is not None:
        out["ssm_command_id"] = data["ssmCommandId"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeployTargetEventContext) -> dict:
    out: dict = {}
    if "ssm_command_id" in value:
        out["ssmCommandId"] = value["ssm_command_id"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> DeployTargetEventContext:
    out: DeployTargetEventContext = {}  # type: ignore[typeddict-item]
    if data.get("ssmCommandId") is not None:
        out["ssm_command_id"] = data["ssmCommandId"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
