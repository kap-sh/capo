"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_blank_and_length_constraint_string
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.routing_strategy
    import capo_gamelift.types.tag_list


class CreateAliasInput(TypedDict, closed=True):
    name: NotRequired[
        "capo_gamelift.types.non_blank_and_length_constraint_string.NonBlankAndLengthConstraintString"
    ]
    """<p>A descriptive label that is associated with an alias. Alias names do not need to be unique.</p>"""
    description: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A human-readable description of the alias.</p>"""
    routing_strategy: NotRequired[
        "capo_gamelift.types.routing_strategy.RoutingStrategy"
    ]
    """<p>The routing configuration, including routing type and fleet target, for the alias. </p>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of labels to assign to the new alias resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAliasInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "routing_strategy" in value:
        import capo_gamelift.types.routing_strategy

        out["RoutingStrategy"] = (
            capo_gamelift.types.routing_strategy.serialize_aws_json_1_1(
                value["routing_strategy"]
            )
        )
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAliasInput:
    out: CreateAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoutingStrategy") is not None:
        import capo_gamelift.types.routing_strategy

        out["routing_strategy"] = (
            capo_gamelift.types.routing_strategy.deserialize_aws_json_1_1(
                data["RoutingStrategy"]
            )
        )
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
