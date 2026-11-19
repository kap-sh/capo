"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeScriptInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.script_id_or_arn


class DescribeScriptInput(TypedDict, closed=True):
    script_id: NotRequired["capo_gamelift.types.script_id_or_arn.ScriptIdOrArn"]
    """<p>A unique identifier for the Realtime script to retrieve properties for. You can use either the script ID or ARN value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScriptInput) -> dict:
    out: dict = {}
    if "script_id" in value:
        out["ScriptId"] = value["script_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScriptInput:
    out: DescribeScriptInput = {}  # type: ignore[typeddict-item]
    if data.get("ScriptId") is not None:
        out["script_id"] = data["ScriptId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeScriptInput) -> dict:
    out: dict = {}
    if "script_id" in value:
        out["ScriptId"] = value["script_id"]
    return out


def deserialize_cbor(data: dict) -> DescribeScriptInput:
    out: DescribeScriptInput = {}  # type: ignore[typeddict-item]
    if data.get("ScriptId") is not None:
        out["script_id"] = data["ScriptId"]
    return out
