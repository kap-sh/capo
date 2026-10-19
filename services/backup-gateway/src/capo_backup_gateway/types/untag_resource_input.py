"""Generated from Smithy shape ``com.amazonaws.backupgateway#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.resource_arn
    import capo_backup_gateway.types.tag_keys


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_backup_gateway.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>"""
    tag_keys: "capo_backup_gateway.types.tag_keys.TagKeys"
    """<p>The list of tag keys specifying which tags to remove.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_backup_gateway.types.tag_keys

    out["TagKeys"] = capo_backup_gateway.types.tag_keys.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_backup_gateway.types.tag_keys

        out["tag_keys"] = capo_backup_gateway.types.tag_keys.deserialize_aws_json_1_0(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
