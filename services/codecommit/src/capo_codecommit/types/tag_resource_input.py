"""Generated from Smithy shape ``com.amazonaws.codecommit#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.resource_arn
    import capo_codecommit.types.tags_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_codecommit.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to which you want to add or update tags.</p>"""
    tags: "capo_codecommit.types.tags_map.TagsMap"
    """<p>The key-value pair to use when tagging this repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_codecommit.types.tags_map

    out["tags"] = capo_codecommit.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_codecommit.types.tags_map

        out["tags"] = capo_codecommit.types.tags_map.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
