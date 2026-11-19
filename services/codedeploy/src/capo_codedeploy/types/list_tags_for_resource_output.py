"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.next_token
    import capo_codedeploy.types.tag_list


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: NotRequired["capo_codedeploy.types.tag_list.TagList"]
    """<p> A list of tags returned by <code>ListTagsForResource</code>. The tags are associated with the resource identified by the input <code>ResourceArn</code> parameter. </p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent list application revisions call to return the next set of application revisions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codedeploy.types.tag_list

        out["Tags"] = capo_codedeploy.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_codedeploy.types.tag_list

        out["Tags"] = capo_codedeploy.types.tag_list.serialize_cbor(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.deserialize_cbor(data["Tags"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
