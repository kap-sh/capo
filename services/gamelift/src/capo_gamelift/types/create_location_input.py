"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateLocationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.custom_input_location_string_model
    import capo_gamelift.types.tag_list


class CreateLocationInput(TypedDict, closed=True):
    location_name: NotRequired[
        "capo_gamelift.types.custom_input_location_string_model.CustomInputLocationStringModel"
    ]
    """<p>A descriptive name for the custom location.</p>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of labels to assign to the new resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources are useful for resource management, access management, and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Rareference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationInput) -> dict:
    out: dict = {}
    if "location_name" in value:
        out["LocationName"] = value["location_name"]
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationInput:
    out: CreateLocationInput = {}  # type: ignore[typeddict-item]
    if data.get("LocationName") is not None:
        out["location_name"] = data["LocationName"]
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
