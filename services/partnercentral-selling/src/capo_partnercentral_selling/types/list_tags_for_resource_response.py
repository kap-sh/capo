"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "capo_partnercentral_selling.types.tag_list.TagList"
    """<p>A map of the key-value pairs for the tag or tags assigned to the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.tag_list

    out["Tags"] = capo_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_partnercentral_selling.types.tag_list

        out["tags"] = (
            capo_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    else:
        out["tags"] = []
    return out
