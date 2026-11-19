"""Generated from Smithy shape ``com.amazonaws.gamelift#ListAliasesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.alias_list
    import capo_gamelift.types.non_empty_string


class ListAliasesOutput(TypedDict, closed=True):
    aliases: NotRequired["capo_gamelift.types.alias_list.AliasList"]
    """<p>A collection of alias resources that match the request parameters.</p>"""
    next_token: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesOutput) -> dict:
    out: dict = {}
    if "aliases" in value:
        import capo_gamelift.types.alias_list

        out["Aliases"] = capo_gamelift.types.alias_list.serialize_aws_json_1_1(
            value["aliases"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesOutput:
    out: ListAliasesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Aliases") is not None:
        import capo_gamelift.types.alias_list

        out["aliases"] = capo_gamelift.types.alias_list.deserialize_aws_json_1_1(
            data["Aliases"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAliasesOutput) -> dict:
    out: dict = {}
    if "aliases" in value:
        import capo_gamelift.types.alias_list

        out["Aliases"] = capo_gamelift.types.alias_list.serialize_cbor(value["aliases"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAliasesOutput:
    out: ListAliasesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Aliases") is not None:
        import capo_gamelift.types.alias_list

        out["aliases"] = capo_gamelift.types.alias_list.deserialize_cbor(
            data["Aliases"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
