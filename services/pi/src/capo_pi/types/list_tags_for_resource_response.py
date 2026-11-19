"""Generated from Smithy shape ``com.amazonaws.pi#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_pi.types.tag_list.TagList"]
    """<p>The metadata assigned to an Amazon RDS resource consisting of a key-value pair.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_pi.types.tag_list

        out["Tags"] = capo_pi.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_pi.types.tag_list

        out["tags"] = capo_pi.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_pi.types.tag_list

        out["Tags"] = capo_pi.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_pi.types.tag_list

        out["tags"] = capo_pi.types.tag_list.deserialize_cbor(data["Tags"])
    return out
