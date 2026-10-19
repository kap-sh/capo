"""Generated from Smithy shape ``com.amazonaws.ecs#EBSTagSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.ebs_resource_type
    import capo_ecs.types.propagate_tags
    import capo_ecs.types.tags


class EBSTagSpecification(TypedDict, closed=True):
    resource_type: "capo_ecs.types.ebs_resource_type.EBSResourceType"
    """<p>The type of volume resource.</p>"""
    tags: NotRequired["capo_ecs.types.tags.Tags"]
    """<p>The tags applied to this Amazon EBS volume. <code>AmazonECSCreated</code> and <code>AmazonECSManaged</code> are reserved tags that can't be used.</p>"""
    propagate_tags: NotRequired["capo_ecs.types.propagate_tags.PropagateTags"]
    """<p>Determines whether to propagate the tags from the task definition to the Amazon EBS volume. Tags can only propagate to a <code>SERVICE</code> specified in <code>ServiceVolumeConfiguration</code>. If no value is specified, the tags aren't propagated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EBSTagSpecification) -> dict:
    out: dict = {}
    import capo_ecs.types.ebs_resource_type

    out["resourceType"] = capo_ecs.types.ebs_resource_type.serialize_aws_json_1_1(
        value["resource_type"]
    )
    if "tags" in value:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.serialize_aws_json_1_1(value["tags"])
    if "propagate_tags" in value:
        import capo_ecs.types.propagate_tags

        out["propagateTags"] = capo_ecs.types.propagate_tags.serialize_aws_json_1_1(
            value["propagate_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EBSTagSpecification:
    out: EBSTagSpecification = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_ecs.types.ebs_resource_type

        out["resource_type"] = (
            capo_ecs.types.ebs_resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_ecs.types.ebs_resource_type.EBSResourceType", ""
        )
    if data.get("tags") is not None:
        import capo_ecs.types.tags

        out["tags"] = capo_ecs.types.tags.deserialize_aws_json_1_1(data["tags"])
    if data.get("propagateTags") is not None:
        import capo_ecs.types.propagate_tags

        out["propagate_tags"] = capo_ecs.types.propagate_tags.deserialize_aws_json_1_1(
            data["propagateTags"]
        )
    return out
