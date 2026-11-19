"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_compute_optimizer_automation.types.tag_list.TagList"]
    """<p> The list of tags associated with the specified resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            capo_compute_optimizer_automation.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = (
            capo_compute_optimizer_automation.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = capo_compute_optimizer_automation.types.tag_list.serialize_cbor(
            value["tags"]
        )
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_compute_optimizer_automation.types.tag_list

        out["tags"] = capo_compute_optimizer_automation.types.tag_list.deserialize_cbor(
            data["tags"]
        )
    return out
