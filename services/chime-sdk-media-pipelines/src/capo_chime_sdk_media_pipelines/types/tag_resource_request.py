"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.amazon_resource_name
    import capo_chime_sdk_media_pipelines.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_chime_sdk_media_pipelines.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the media pipeline associated with any tags. The ARN consists of the pipeline's endpoint region, resource ID, and pipeline ID.</p>"""
    tags: "capo_chime_sdk_media_pipelines.types.tag_list.TagList"
    """<p>The tags associated with the specified media pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_chime_sdk_media_pipelines.types.tag_list

    out["Tags"] = capo_chime_sdk_media_pipelines.types.tag_list.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["tags"] = capo_chime_sdk_media_pipelines.types.tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
