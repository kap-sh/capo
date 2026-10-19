"""Generated from Smithy shape ``com.amazonaws.kendraranking#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra_ranking.types.amazon_resource_name
    import capo_kendra_ranking.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_kendra_ranking.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the rescore execution plan to remove the tag.</p>"""
    tag_keys: "capo_kendra_ranking.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the rescore execution plan. If a tag key does not exist on the resource, it is ignored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_kendra_ranking.types.tag_key_list

    out["TagKeys"] = capo_kendra_ranking.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_kendra_ranking.types.tag_key_list

        out["tag_keys"] = (
            capo_kendra_ranking.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
