"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListDatasetExamplesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dataset_generation_id_list
    import capo_bedrock_agentcore_control.types.example_field_condition_list


class ListDatasetExamplesFilter(TypedDict, closed=True):
    generation_ids: NotRequired[
        "capo_bedrock_agentcore_control.types.dataset_generation_id_list.DatasetGenerationIdList"
    ]
    """<p> Returns only examples created by this dataset generation. Specify one ID. </p>"""
    example_fields: NotRequired[
        "capo_bedrock_agentcore_control.types.example_field_condition_list.ExampleFieldConditionList"
    ]
    """<p> Returns only examples that meet at least one of these conditions. Examples last written before example field filtering was available never match. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetExamplesFilter) -> dict:
    out: dict = {}
    if "generation_ids" in value:
        import capo_bedrock_agentcore_control.types.dataset_generation_id_list

        out["generationIds"] = (
            capo_bedrock_agentcore_control.types.dataset_generation_id_list.serialize_json(
                value["generation_ids"]
            )
        )
    if "example_fields" in value:
        import capo_bedrock_agentcore_control.types.example_field_condition_list

        out["exampleFields"] = (
            capo_bedrock_agentcore_control.types.example_field_condition_list.serialize_json(
                value["example_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDatasetExamplesFilter:
    out: ListDatasetExamplesFilter = {}  # type: ignore[typeddict-item]
    if data.get("generationIds") is not None:
        import capo_bedrock_agentcore_control.types.dataset_generation_id_list

        out["generation_ids"] = (
            capo_bedrock_agentcore_control.types.dataset_generation_id_list.deserialize_json(
                data["generationIds"]
            )
        )
    if data.get("exampleFields") is not None:
        import capo_bedrock_agentcore_control.types.example_field_condition_list

        out["example_fields"] = (
            capo_bedrock_agentcore_control.types.example_field_condition_list.deserialize_json(
                data["exampleFields"]
            )
        )
    return out
