"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.example_count_by_field_condition_list


class ListDatasetsFilter(TypedDict, closed=True):
    example_count_by_field: NotRequired[
        "capo_bedrock_agentcore_control.types.example_count_by_field_condition_list.ExampleCountByFieldConditionList"
    ]
    """<p> Returns only datasets whose DRAFT example counts meet at least one of these conditions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsFilter) -> dict:
    out: dict = {}
    if "example_count_by_field" in value:
        import capo_bedrock_agentcore_control.types.example_count_by_field_condition_list

        out["exampleCountByField"] = (
            capo_bedrock_agentcore_control.types.example_count_by_field_condition_list.serialize_json(
                value["example_count_by_field"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDatasetsFilter:
    out: ListDatasetsFilter = {}  # type: ignore[typeddict-item]
    if data.get("exampleCountByField") is not None:
        import capo_bedrock_agentcore_control.types.example_count_by_field_condition_list

        out["example_count_by_field"] = (
            capo_bedrock_agentcore_control.types.example_count_by_field_condition_list.deserialize_json(
                data["exampleCountByField"]
            )
        )
    return out
