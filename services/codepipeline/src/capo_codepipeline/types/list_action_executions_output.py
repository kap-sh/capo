"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListActionExecutionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution_detail_list
    import capo_codepipeline.types.next_token


class ListActionExecutionsOutput(TypedDict, closed=True):
    action_execution_details: NotRequired[
        "capo_codepipeline.types.action_execution_detail_list.ActionExecutionDetailList"
    ]
    """<p>The details for a list of recent executions, such as action execution ID.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent <code>ListActionExecutions</code> call to return the next set of action executions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListActionExecutionsOutput) -> dict:
    out: dict = {}
    if "action_execution_details" in value:
        import capo_codepipeline.types.action_execution_detail_list

        out["actionExecutionDetails"] = (
            capo_codepipeline.types.action_execution_detail_list.serialize_aws_json_1_1(
                value["action_execution_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListActionExecutionsOutput:
    out: ListActionExecutionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("actionExecutionDetails") is not None:
        import capo_codepipeline.types.action_execution_detail_list

        out["action_execution_details"] = (
            capo_codepipeline.types.action_execution_detail_list.deserialize_aws_json_1_1(
                data["actionExecutionDetails"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListActionExecutionsOutput) -> dict:
    out: dict = {}
    if "action_execution_details" in value:
        import capo_codepipeline.types.action_execution_detail_list

        out["actionExecutionDetails"] = (
            capo_codepipeline.types.action_execution_detail_list.serialize_cbor(
                value["action_execution_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListActionExecutionsOutput:
    out: ListActionExecutionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("actionExecutionDetails") is not None:
        import capo_codepipeline.types.action_execution_detail_list

        out["action_execution_details"] = (
            capo_codepipeline.types.action_execution_detail_list.deserialize_cbor(
                data["actionExecutionDetails"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
