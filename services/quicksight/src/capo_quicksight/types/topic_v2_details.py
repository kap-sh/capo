"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2Details``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.resource_name
    import capo_quicksight.types.topic_v2_data_set_references
    import capo_quicksight.types.topic_v2_data_set_relation_list


class TopicV2Details(TypedDict, closed=True):
    name: "capo_quicksight.types.resource_name.ResourceName"
    """<p>The name of the topic.</p>"""
    description: NotRequired["capo_quicksight.types.limited_string.LimitedString"]
    """<p>The description of the topic.</p>"""
    data_sets: NotRequired[
        "capo_quicksight.types.topic_v2_data_set_references.TopicV2DataSetReferences"
    ]
    """<p>The data sets that the topic is associated with.</p>"""
    data_set_relations: NotRequired[
        "capo_quicksight.types.topic_v2_data_set_relation_list.TopicV2DataSetRelationList"
    ]
    """<p>The relations between the data sets that the topic is associated with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2Details) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "data_sets" in value:
        import capo_quicksight.types.topic_v2_data_set_references

        out["DataSets"] = (
            capo_quicksight.types.topic_v2_data_set_references.serialize_json(
                value["data_sets"]
            )
        )
    if "data_set_relations" in value:
        import capo_quicksight.types.topic_v2_data_set_relation_list

        out["DataSetRelations"] = (
            capo_quicksight.types.topic_v2_data_set_relation_list.serialize_json(
                value["data_set_relations"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicV2Details:
    out: TopicV2Details = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DataSets") is not None:
        import capo_quicksight.types.topic_v2_data_set_references

        out["data_sets"] = (
            capo_quicksight.types.topic_v2_data_set_references.deserialize_json(
                data["DataSets"]
            )
        )
    if data.get("DataSetRelations") is not None:
        import capo_quicksight.types.topic_v2_data_set_relation_list

        out["data_set_relations"] = (
            capo_quicksight.types.topic_v2_data_set_relation_list.deserialize_json(
                data["DataSetRelations"]
            )
        )
    return out
