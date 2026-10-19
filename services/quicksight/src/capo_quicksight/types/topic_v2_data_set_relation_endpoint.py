"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicV2DataSetRelationEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.topic_v2_data_set_relation_column_names


class TopicV2DataSetRelationEndpoint(TypedDict, closed=True):
    data_set_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data set at this endpoint of the relation.</p>"""
    column_names: "capo_quicksight.types.topic_v2_data_set_relation_column_names.TopicV2DataSetRelationColumnNames"
    """<p>The names of the columns that are used in the data set relation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicV2DataSetRelationEndpoint) -> dict:
    out: dict = {}
    out["DataSetArn"] = value["data_set_arn"]
    import capo_quicksight.types.topic_v2_data_set_relation_column_names

    out["ColumnNames"] = (
        capo_quicksight.types.topic_v2_data_set_relation_column_names.serialize_json(
            value["column_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> TopicV2DataSetRelationEndpoint:
    out: TopicV2DataSetRelationEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("DataSetArn") is not None:
        out["data_set_arn"] = data["DataSetArn"]
    else:
        out["data_set_arn"] = ""
    if data.get("ColumnNames") is not None:
        import capo_quicksight.types.topic_v2_data_set_relation_column_names

        out["column_names"] = (
            capo_quicksight.types.topic_v2_data_set_relation_column_names.deserialize_json(
                data["ColumnNames"]
            )
        )
    else:
        out["column_names"] = []
    return out
