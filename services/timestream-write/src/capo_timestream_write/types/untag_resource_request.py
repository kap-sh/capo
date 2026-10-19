"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.amazon_resource_name
    import capo_timestream_write.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_timestream_write.types.amazon_resource_name.AmazonResourceName"
    """<p> The Timestream resource that the tags will be removed from. This value is an Amazon Resource Name (ARN). </p>"""
    tag_keys: "capo_timestream_write.types.tag_key_list.TagKeyList"
    """<p> A list of tags keys. Existing tags of the resource whose keys are members of this list will be removed from the Timestream resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_timestream_write.types.tag_key_list

    out["TagKeys"] = capo_timestream_write.types.tag_key_list.serialize_aws_json_1_0(
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
        import capo_timestream_write.types.tag_key_list

        out["tag_keys"] = (
            capo_timestream_write.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
