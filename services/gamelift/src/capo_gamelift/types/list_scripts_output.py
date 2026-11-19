"""Generated from Smithy shape ``com.amazonaws.gamelift#ListScriptsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_empty_string
    import capo_gamelift.types.script_list


class ListScriptsOutput(TypedDict, closed=True):
    scripts: NotRequired["capo_gamelift.types.script_list.ScriptList"]
    """<p>A set of properties describing the requested script.</p>"""
    next_token: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListScriptsOutput) -> dict:
    out: dict = {}
    if "scripts" in value:
        import capo_gamelift.types.script_list

        out["Scripts"] = capo_gamelift.types.script_list.serialize_aws_json_1_1(
            value["scripts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListScriptsOutput:
    out: ListScriptsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Scripts") is not None:
        import capo_gamelift.types.script_list

        out["scripts"] = capo_gamelift.types.script_list.deserialize_aws_json_1_1(
            data["Scripts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListScriptsOutput) -> dict:
    out: dict = {}
    if "scripts" in value:
        import capo_gamelift.types.script_list

        out["Scripts"] = capo_gamelift.types.script_list.serialize_cbor(
            value["scripts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListScriptsOutput:
    out: ListScriptsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Scripts") is not None:
        import capo_gamelift.types.script_list

        out["scripts"] = capo_gamelift.types.script_list.deserialize_cbor(
            data["Scripts"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
