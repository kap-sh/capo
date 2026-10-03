"""Generated from Smithy shape ``com.amazonaws.mediastore#CreateContainerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediastore.types.container_name
    import capo_mediastore.types.tag_list


class CreateContainerInput(TypedDict, closed=True):
    container_name: "capo_mediastore.types.container_name.ContainerName"
    """<p>The name for the container. The name must be from 1 to 255 characters. Container names must be unique to your AWS account within a specific region. As an example, you could create a container named <code>movies</code> in every region, as long as you don’t have an existing container with that name.</p>"""
    tags: NotRequired["capo_mediastore.types.tag_list.TagList"]
    """<p>An array of key:value pairs that you define. These values can be anything that you want. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each container. For more information about tagging, including naming and usage conventions, see <a href="https://docs.aws.amazon.com/mediastore/latest/ug/tagging.html">Tagging Resources in MediaStore</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContainerInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    if "tags" in value:
        import capo_mediastore.types.tag_list

        out["Tags"] = capo_mediastore.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContainerInput:
    out: CreateContainerInput = {}  # type: ignore[typeddict-item]
    if data.get("ContainerName") is not None:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("CreateContainerInput.container_name required")
    if data.get("Tags") is not None:
        import capo_mediastore.types.tag_list

        out["tags"] = capo_mediastore.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
