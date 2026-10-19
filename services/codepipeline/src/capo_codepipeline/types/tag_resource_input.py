"""Generated from Smithy shape ``com.amazonaws.codepipeline#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.resource_arn
    import capo_codepipeline.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_codepipeline.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource you want to add tags to.</p>"""
    tags: "capo_codepipeline.types.tag_list.TagList"
    """<p>The tags you want to modify or add to the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_codepipeline.types.tag_list

    out["tags"] = capo_codepipeline.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_codepipeline.types.tag_list

        out["tags"] = capo_codepipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
