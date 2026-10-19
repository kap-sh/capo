"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.evaluation_form_item_weight
    import capo_connect.types.evaluation_form_items_list
    import capo_connect.types.evaluation_form_question_instructions
    import capo_connect.types.evaluation_form_score_threshold_list
    import capo_connect.types.evaluation_form_section_title
    import capo_connect.types.reference_id


class EvaluationFormSection(TypedDict, closed=True):
    title: "capo_connect.types.evaluation_form_section_title.EvaluationFormSectionTitle"
    """<p>The title of the section.</p>"""
    ref_id: "capo_connect.types.reference_id.ReferenceId"
    """<p>The identifier of the section. An identifier must be unique within the evaluation form.</p>"""
    instructions: NotRequired[
        "capo_connect.types.evaluation_form_question_instructions.EvaluationFormQuestionInstructions"
    ]
    """<p>The instructions of the section.</p>"""
    items: "capo_connect.types.evaluation_form_items_list.EvaluationFormItemsList"
    """<p>The items of the section.</p>"""
    weight: "capo_connect.types.evaluation_form_item_weight.EvaluationFormItemWeight"
    """<p>The scoring weight of the section.</p>"""
    is_excluded_from_scoring: "capo_connect.types.boolean.Boolean"
    """<p>The flag to exclude the section from scoring.</p>"""
    score_thresholds: NotRequired[
        "capo_connect.types.evaluation_form_score_threshold_list.EvaluationFormScoreThresholdList"
    ]
    """<p>The score thresholds for performance categories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSection) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    out["RefId"] = value["ref_id"]
    if "instructions" in value:
        out["Instructions"] = value["instructions"]
    import capo_connect.types.evaluation_form_items_list

    out["Items"] = capo_connect.types.evaluation_form_items_list.serialize_json(
        value["items"]
    )
    out["Weight"] = (
        "NaN"
        if value.get("weight", 0) != value.get("weight", 0)
        else "Infinity"
        if value.get("weight", 0) == float("inf")
        else "-Infinity"
        if value.get("weight", 0) == float("-inf")
        else value.get("weight", 0)
    )
    out["IsExcludedFromScoring"] = value.get("is_excluded_from_scoring", False)
    if "score_thresholds" in value:
        import capo_connect.types.evaluation_form_score_threshold_list

        out["ScoreThresholds"] = (
            capo_connect.types.evaluation_form_score_threshold_list.serialize_json(
                value["score_thresholds"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormSection:
    out: EvaluationFormSection = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("RefId") is not None:
        out["ref_id"] = data["RefId"]
    else:
        out["ref_id"] = ""
    if data.get("Instructions") is not None:
        out["instructions"] = data["Instructions"]
    if data.get("Items") is not None:
        import capo_connect.types.evaluation_form_items_list

        out["items"] = capo_connect.types.evaluation_form_items_list.deserialize_json(
            data["Items"]
        )
    else:
        out["items"] = []
    if data.get("Weight") is not None:
        out["weight"] = float(data["Weight"])
    else:
        out["weight"] = 0
    if data.get("IsExcludedFromScoring") is not None:
        out["is_excluded_from_scoring"] = data["IsExcludedFromScoring"]
    else:
        out["is_excluded_from_scoring"] = False
    if data.get("ScoreThresholds") is not None:
        import capo_connect.types.evaluation_form_score_threshold_list

        out["score_thresholds"] = (
            capo_connect.types.evaluation_form_score_threshold_list.deserialize_json(
                data["ScoreThresholds"]
            )
        )
    return out
