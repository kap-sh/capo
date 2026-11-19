"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_application_insights.types.tag_list.TagList"]
    """<p>An array that lists all the tags that are associated with the application. Each tag consists of a required tag key (<code>Key</code>) and an associated tag value (<code>Value</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_application_insights.types.tag_list

        out["Tags"] = capo_application_insights.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_application_insights.types.tag_list

        out["tags"] = capo_application_insights.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_application_insights.types.tag_list

        out["Tags"] = capo_application_insights.types.tag_list.serialize_cbor(
            value["tags"]
        )
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_application_insights.types.tag_list

        out["tags"] = capo_application_insights.types.tag_list.deserialize_cbor(
            data["Tags"]
        )
    return out
