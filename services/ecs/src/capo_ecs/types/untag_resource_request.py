"""Generated from Smithy shape ``com.amazonaws.ecs#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource to delete tags from. Currently, the supported resources are Amazon ECS capacity providers, tasks, services, task definitions, clusters, and container instances.</p>"""
    tag_keys: "capo_ecs.types.tag_keys.TagKeys"
    """<p>The keys of the tags to be removed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_ecs.types.tag_keys

    out["tagKeys"] = capo_ecs.types.tag_keys.serialize_aws_json_1_1(value["tag_keys"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_ecs.types.tag_keys

        out["tag_keys"] = capo_ecs.types.tag_keys.deserialize_aws_json_1_1(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
