"""Generated from Smithy shape ``com.amazonaws.gamelift#ListBuildsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.build_list
    import capo_gamelift.types.non_empty_string


class ListBuildsOutput(TypedDict, closed=True):
    builds: NotRequired["capo_gamelift.types.build_list.BuildList"]
    """<p>A collection of build resources that match the request.</p>"""
    next_token: NotRequired["capo_gamelift.types.non_empty_string.NonEmptyString"]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildsOutput) -> dict:
    out: dict = {}
    if "builds" in value:
        import capo_gamelift.types.build_list

        out["Builds"] = capo_gamelift.types.build_list.serialize_aws_json_1_1(
            value["builds"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildsOutput:
    out: ListBuildsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Builds") is not None:
        import capo_gamelift.types.build_list

        out["builds"] = capo_gamelift.types.build_list.deserialize_aws_json_1_1(
            data["Builds"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListBuildsOutput) -> dict:
    out: dict = {}
    if "builds" in value:
        import capo_gamelift.types.build_list

        out["Builds"] = capo_gamelift.types.build_list.serialize_cbor(value["builds"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListBuildsOutput:
    out: ListBuildsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Builds") is not None:
        import capo_gamelift.types.build_list

        out["builds"] = capo_gamelift.types.build_list.deserialize_cbor(data["Builds"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
