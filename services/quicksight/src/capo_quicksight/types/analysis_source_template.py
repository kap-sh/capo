"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisSourceTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.data_set_reference_list
    import capo_quicksight.types.topic_reference_list


class AnalysisSourceTemplate(TypedDict, closed=True):
    data_set_references: (
        "capo_quicksight.types.data_set_reference_list.DataSetReferenceList"
    )
    """<p>The dataset references of the source template of an analysis.</p>"""
    topic_references: NotRequired[
        "capo_quicksight.types.topic_reference_list.TopicReferenceList"
    ]
    """<p>The topic references of the source template of an analysis.</p>"""
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the source template of an analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisSourceTemplate) -> dict:
    out: dict = {}
    import capo_quicksight.types.data_set_reference_list

    out["DataSetReferences"] = (
        capo_quicksight.types.data_set_reference_list.serialize_json(
            value["data_set_references"]
        )
    )
    if "topic_references" in value:
        import capo_quicksight.types.topic_reference_list

        out["TopicReferences"] = (
            capo_quicksight.types.topic_reference_list.serialize_json(
                value["topic_references"]
            )
        )
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AnalysisSourceTemplate:
    out: AnalysisSourceTemplate = {}  # type: ignore[typeddict-item]
    if data.get("DataSetReferences") is not None:
        import capo_quicksight.types.data_set_reference_list

        out["data_set_references"] = (
            capo_quicksight.types.data_set_reference_list.deserialize_json(
                data["DataSetReferences"]
            )
        )
    else:
        out["data_set_references"] = []
    if data.get("TopicReferences") is not None:
        import capo_quicksight.types.topic_reference_list

        out["topic_references"] = (
            capo_quicksight.types.topic_reference_list.deserialize_json(
                data["TopicReferences"]
            )
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
