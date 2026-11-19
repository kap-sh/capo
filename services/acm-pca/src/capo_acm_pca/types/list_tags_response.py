"""Generated from Smithy shape ``com.amazonaws.acmpca#ListTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.next_token
    import capo_acm_pca.types.tag_list


class ListTagsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_acm_pca.types.next_token.NextToken"]
    """<p>When the list is truncated, this value is present and should be used for the <b>NextToken</b> parameter in a subsequent pagination request. </p>"""
    tags: NotRequired["capo_acm_pca.types.tag_list.TagList"]
    """<p>The tags associated with your private CA.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tags" in value:
        import capo_acm_pca.types.tag_list

        out["Tags"] = capo_acm_pca.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Tags") is not None:
        import capo_acm_pca.types.tag_list

        out["tags"] = capo_acm_pca.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tags" in value:
        import capo_acm_pca.types.tag_list

        out["Tags"] = capo_acm_pca.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Tags") is not None:
        import capo_acm_pca.types.tag_list

        out["tags"] = capo_acm_pca.types.tag_list.deserialize_cbor(data["Tags"])
    return out
