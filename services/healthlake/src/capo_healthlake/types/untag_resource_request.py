"""Generated from Smithy shape ``com.amazonaws.healthlake#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.amazon_resource_name
    import capo_healthlake.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_healthlake.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the data store from which tags are being removed.</p>"""
    tag_keys: "capo_healthlake.types.tag_key_list.TagKeyList"
    """<p>The keys for the tags to be removed from the data store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_healthlake.types.tag_key_list

    out["TagKeys"] = capo_healthlake.types.tag_key_list.serialize_aws_json_1_0(
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
        import capo_healthlake.types.tag_key_list

        out["tag_keys"] = capo_healthlake.types.tag_key_list.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
