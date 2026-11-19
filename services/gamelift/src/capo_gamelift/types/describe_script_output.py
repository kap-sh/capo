"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeScriptOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.script


class DescribeScriptOutput(TypedDict, closed=True):
    script: NotRequired["capo_gamelift.types.script.Script"]
    """<p>A set of properties describing the requested script.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeScriptOutput) -> dict:
    out: dict = {}
    if "script" in value:
        import capo_gamelift.types.script

        out["Script"] = capo_gamelift.types.script.serialize_aws_json_1_1(
            value["script"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeScriptOutput:
    out: DescribeScriptOutput = {}  # type: ignore[typeddict-item]
    if data.get("Script") is not None:
        import capo_gamelift.types.script

        out["script"] = capo_gamelift.types.script.deserialize_aws_json_1_1(
            data["Script"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeScriptOutput) -> dict:
    out: dict = {}
    if "script" in value:
        import capo_gamelift.types.script

        out["Script"] = capo_gamelift.types.script.serialize_cbor(value["script"])
    return out


def deserialize_cbor(data: dict) -> DescribeScriptOutput:
    out: DescribeScriptOutput = {}  # type: ignore[typeddict-item]
    if data.get("Script") is not None:
        import capo_gamelift.types.script

        out["script"] = capo_gamelift.types.script.deserialize_cbor(data["Script"])
    return out
