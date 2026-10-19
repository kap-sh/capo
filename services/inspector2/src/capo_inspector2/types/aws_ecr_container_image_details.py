"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEcrContainerImageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.image_hash
    import capo_inspector2.types.image_tag_list
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.platform


class AwsEcrContainerImageDetails(TypedDict, closed=True):
    repository_name: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The name of the repository the Amazon ECR container image resides in.</p>"""
    image_tags: NotRequired["capo_inspector2.types.image_tag_list.ImageTagList"]
    """<p>The image tags attached to the Amazon ECR container image.</p>"""
    pushed_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the Amazon ECR container image was pushed.</p>"""
    author: NotRequired["str"]
    """<p>The image author of the Amazon ECR container image.</p>"""
    architecture: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The architecture of the Amazon ECR container image.</p>"""
    image_hash: "capo_inspector2.types.image_hash.ImageHash"
    """<p>The image hash of the Amazon ECR container image.</p>"""
    registry: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The registry for the Amazon ECR container image.</p>"""
    platform: NotRequired["capo_inspector2.types.platform.Platform"]
    """<p>The platform of the Amazon ECR container image.</p>"""
    last_in_use_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.</p>"""
    in_use_count: NotRequired["int"]
    """<p>The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrContainerImageDetails) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "image_tags" in value:
        import capo_inspector2.types.image_tag_list

        out["imageTags"] = capo_inspector2.types.image_tag_list.serialize_json(
            value["image_tags"]
        )
    if "pushed_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["pushedAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["pushed_at"]
        )
    if "author" in value:
        out["author"] = value["author"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    out["imageHash"] = value["image_hash"]
    out["registry"] = value["registry"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "last_in_use_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["lastInUseAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["last_in_use_at"]
        )
    if "in_use_count" in value:
        out["inUseCount"] = value["in_use_count"]
    return out


def deserialize_json(data: dict) -> AwsEcrContainerImageDetails:
    out: AwsEcrContainerImageDetails = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("imageTags") is not None:
        import capo_inspector2.types.image_tag_list

        out["image_tags"] = capo_inspector2.types.image_tag_list.deserialize_json(
            data["imageTags"]
        )
    if data.get("pushedAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["pushed_at"] = capo_inspector2.types.date_time_timestamp.deserialize_json(
            data["pushedAt"]
        )
    if data.get("author") is not None:
        out["author"] = data["author"]
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    if data.get("imageHash") is not None:
        out["image_hash"] = data["imageHash"]
    else:
        out["image_hash"] = ""
    if data.get("registry") is not None:
        out["registry"] = data["registry"]
    else:
        out["registry"] = ""
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("lastInUseAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["last_in_use_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastInUseAt"]
            )
        )
    if data.get("inUseCount") is not None:
        out["in_use_count"] = data["inUseCount"]
    return out
