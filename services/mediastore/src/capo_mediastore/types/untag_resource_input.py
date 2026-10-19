"""Generated from Smithy shape ``com.amazonaws.mediastore#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediastore.types.container_arn
    import capo_mediastore.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource: "capo_mediastore.types.container_arn.ContainerARN"
    """<p>The Amazon Resource Name (ARN) for the container.</p>"""
    tag_keys: "capo_mediastore.types.tag_key_list.TagKeyList"
    """<p>A comma-separated list of keys for tags that you want to remove from the container. For example, if your container has two tags (customer:CompanyA and priority:High) and you want to remove one of the tags (priority:High), you specify the key for the tag that you want to remove (priority).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["Resource"] = value["resource"]
    import capo_mediastore.types.tag_key_list

    out["TagKeys"] = capo_mediastore.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Resource") is not None:
        out["resource"] = data["Resource"]
    else:
        out["resource"] = ""
    if data.get("TagKeys") is not None:
        import capo_mediastore.types.tag_key_list

        out["tag_keys"] = capo_mediastore.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
