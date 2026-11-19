"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution_id
    import capo_codepipeline.types.action_name


class ActionContext(TypedDict, closed=True):
    name: NotRequired["capo_codepipeline.types.action_name.ActionName"]
    """<p>The name of the action in the context of a job.</p>"""
    action_execution_id: NotRequired[
        "capo_codepipeline.types.action_execution_id.ActionExecutionId"
    ]
    """<p>The system-generated unique ID that corresponds to an action's execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionContext) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "action_execution_id" in value:
        out["actionExecutionId"] = value["action_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionContext:
    out: ActionContext = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("actionExecutionId") is not None:
        out["action_execution_id"] = data["actionExecutionId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionContext) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "action_execution_id" in value:
        out["actionExecutionId"] = value["action_execution_id"]
    return out


def deserialize_cbor(data: dict) -> ActionContext:
    out: ActionContext = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("actionExecutionId") is not None:
        out["action_execution_id"] = data["actionExecutionId"]
    return out
