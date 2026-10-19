"""Generated from Smithy shape ``com.amazonaws.memorydb#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.key_list
    import capo_memorydb.types.string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_memorydb.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource to which the tags are to be removed.</p>"""
    tag_keys: "capo_memorydb.types.key_list.KeyList"
    """<p>The list of keys of the tags that are to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_memorydb.types.key_list

    out["TagKeys"] = capo_memorydb.types.key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_memorydb.types.key_list

        out["tag_keys"] = capo_memorydb.types.key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
