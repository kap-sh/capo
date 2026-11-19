"""Generated from Smithy shape ``com.amazonaws.keyspaces#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.next_token
    import capo_keyspaces.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_keyspaces.types.next_token.NextToken"]
    """<p>A token to specify where to start paginating. This is the <code>NextToken</code> from a previously truncated response.</p>"""
    tags: NotRequired["capo_keyspaces.types.tag_list.TagList"]
    """<p>A list of tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "tags" in value:
        import capo_keyspaces.types.tag_list

        out["tags"] = capo_keyspaces.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("tags") is not None:
        import capo_keyspaces.types.tag_list

        out["tags"] = capo_keyspaces.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "tags" in value:
        import capo_keyspaces.types.tag_list

        out["tags"] = capo_keyspaces.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("tags") is not None:
        import capo_keyspaces.types.tag_list

        out["tags"] = capo_keyspaces.types.tag_list.deserialize_cbor(data["tags"])
    return out
