"""Generated from Smithy shape ``com.amazonaws.codebuild#ListBuildsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_ids
    import capo_codebuild.types.string


class ListBuildsOutput(TypedDict, closed=True):
    ids: NotRequired["capo_codebuild.types.build_ids.BuildIds"]
    """<p>A list of build IDs, with each build ID representing a single build.</p>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>If there are more than 100 items in the list, only the first 100 items are returned, along with a unique string called a <i>nextToken</i>. To get the next batch of items in the list, call this operation again, adding the next token to the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBuildsOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_codebuild.types.build_ids

        out["ids"] = capo_codebuild.types.build_ids.serialize_aws_json_1_1(value["ids"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBuildsOutput:
    out: ListBuildsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_codebuild.types.build_ids

        out["ids"] = capo_codebuild.types.build_ids.deserialize_aws_json_1_1(
            data["ids"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListBuildsOutput) -> dict:
    out: dict = {}
    if "ids" in value:
        import capo_codebuild.types.build_ids

        out["ids"] = capo_codebuild.types.build_ids.serialize_cbor(value["ids"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListBuildsOutput:
    out: ListBuildsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_codebuild.types.build_ids

        out["ids"] = capo_codebuild.types.build_ids.deserialize_cbor(data["ids"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
