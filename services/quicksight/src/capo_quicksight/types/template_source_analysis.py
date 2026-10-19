"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateSourceAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.data_set_reference_list
    import capo_quicksight.types.topic_reference_list


class TemplateSourceAnalysis(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    data_set_references: (
        "capo_quicksight.types.data_set_reference_list.DataSetReferenceList"
    )
    """<p>A structure containing information about the dataset references used as placeholders in the template.</p>"""
    topic_references: NotRequired[
        "capo_quicksight.types.topic_reference_list.TopicReferenceList"
    ]
    """<p>A structure containing information about the topic references used as placeholders in the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSourceAnalysis) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
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
    return out


def deserialize_json(data: dict) -> TemplateSourceAnalysis:
    out: TemplateSourceAnalysis = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
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
    return out
