"""Generated from Smithy shape ``com.amazonaws.glue#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.glue_resource_arn
    import capo_glue.types.tags_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_glue.types.glue_resource_arn.GlueResourceArn"
    """<p>The ARN of the Glue resource to which to add the tags. For more information about Glue resource ARNs, see the <a href="https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-common.html#aws-glue-api-regex-aws-glue-arn-id">Glue ARN string pattern</a>.</p>"""
    tags_to_add: "capo_glue.types.tags_map.TagsMap"
    """<p>Tags to add to this resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_glue.types.tags_map

    out["TagsToAdd"] = capo_glue.types.tags_map.serialize_aws_json_1_1(
        value["tags_to_add"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if data.get("TagsToAdd") is not None:
        import capo_glue.types.tags_map

        out["tags_to_add"] = capo_glue.types.tags_map.deserialize_aws_json_1_1(
            data["TagsToAdd"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags_to_add required")
    return out
