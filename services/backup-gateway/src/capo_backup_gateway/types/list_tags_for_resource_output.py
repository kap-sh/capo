"""Generated from Smithy shape ``com.amazonaws.backupgateway#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.resource_arn
    import capo_backup_gateway.types.tags


class ListTagsForResourceOutput(TypedDict, closed=True):
    resource_arn: NotRequired["capo_backup_gateway.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource's tags that you listed.</p>"""
    tags: NotRequired["capo_backup_gateway.types.tags.Tags"]
    """<p>A list of the resource's tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import capo_backup_gateway.types.tags

        out["Tags"] = capo_backup_gateway.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Tags") is not None:
        import capo_backup_gateway.types.tags

        out["tags"] = capo_backup_gateway.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import capo_backup_gateway.types.tags

        out["Tags"] = capo_backup_gateway.types.tags.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Tags") is not None:
        import capo_backup_gateway.types.tags

        out["tags"] = capo_backup_gateway.types.tags.deserialize_cbor(data["Tags"])
    return out
