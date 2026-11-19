"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.next_token
    import capo_codepipeline.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_codepipeline.types.tag_list.TagList"]
    """<p>The tags for the resource.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>If the amount of returned information is significantly large, an identifier is also returned and can be used in a subsequent API call to return the next page of the list. The ListTagsforResource call lists all available tags in one call and does not use pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.serialize_cbor(value["tags"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.deserialize_cbor(data["tags"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
