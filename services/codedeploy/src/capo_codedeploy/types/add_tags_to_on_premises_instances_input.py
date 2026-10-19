"""Generated from Smithy shape ``com.amazonaws.codedeploy#AddTagsToOnPremisesInstancesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_name_list
    import capo_codedeploy.types.tag_list


class AddTagsToOnPremisesInstancesInput(TypedDict, closed=True):
    tags: "capo_codedeploy.types.tag_list.TagList"
    """<p>The tag key-value pairs to add to the on-premises instances.</p> <p>Keys and values are both required. Keys cannot be null or empty strings. Value-only tags are not allowed.</p>"""
    instance_names: "capo_codedeploy.types.instance_name_list.InstanceNameList"
    """<p>The names of the on-premises instances to which to add tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToOnPremisesInstancesInput) -> dict:
    out: dict = {}
    import capo_codedeploy.types.tag_list

    out["tags"] = capo_codedeploy.types.tag_list.serialize_aws_json_1_1(value["tags"])
    import capo_codedeploy.types.instance_name_list

    out["instanceNames"] = (
        capo_codedeploy.types.instance_name_list.serialize_aws_json_1_1(
            value["instance_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToOnPremisesInstancesInput:
    out: AddTagsToOnPremisesInstancesInput = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_codedeploy.types.tag_list

        out["tags"] = capo_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    if data.get("instanceNames") is not None:
        import capo_codedeploy.types.instance_name_list

        out["instance_names"] = (
            capo_codedeploy.types.instance_name_list.deserialize_aws_json_1_1(
                data["instanceNames"]
            )
        )
    else:
        out["instance_names"] = []
    return out
