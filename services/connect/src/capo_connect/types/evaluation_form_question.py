"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.evaluation_form_item_enablement_configuration
    import capo_connect.types.evaluation_form_item_weight
    import capo_connect.types.evaluation_form_metric_configuration
    import capo_connect.types.evaluation_form_question_instructions
    import capo_connect.types.evaluation_form_question_scoring_configuration
    import capo_connect.types.evaluation_form_question_title
    import capo_connect.types.evaluation_form_question_type
    import capo_connect.types.evaluation_form_question_type_properties
    import capo_connect.types.reference_id


class EvaluationFormQuestion(TypedDict, closed=True):
    title: (
        "capo_connect.types.evaluation_form_question_title.EvaluationFormQuestionTitle"
    )
    """<p>The title of the question.</p>"""
    instructions: NotRequired[
        "capo_connect.types.evaluation_form_question_instructions.EvaluationFormQuestionInstructions"
    ]
    """<p>The instructions of the section.</p>"""
    ref_id: "capo_connect.types.reference_id.ReferenceId"
    """<p>The identifier of the question. An identifier must be unique within the evaluation form.</p>"""
    not_applicable_enabled: "capo_connect.types.boolean.Boolean"
    """<p>The flag to enable not applicable answers to the question.</p>"""
    question_type: (
        "capo_connect.types.evaluation_form_question_type.EvaluationFormQuestionType"
    )
    """<p>The type of the question.</p>"""
    question_type_properties: NotRequired[
        "capo_connect.types.evaluation_form_question_type_properties.EvaluationFormQuestionTypeProperties"
    ]
    """<p>The properties of the type of question. Text questions do not have to define question type properties.</p>"""
    enablement: NotRequired[
        "capo_connect.types.evaluation_form_item_enablement_configuration.EvaluationFormItemEnablementConfiguration"
    ]
    """<p>A question conditional enablement.</p>"""
    weight: "capo_connect.types.evaluation_form_item_weight.EvaluationFormItemWeight"
    """<p>The scoring weight of the section.</p>"""
    scoring_configuration: NotRequired[
        "capo_connect.types.evaluation_form_question_scoring_configuration.EvaluationFormQuestionScoringConfiguration"
    ]
    """<p>The scoring configuration of the question.</p>"""
    metric_configuration: NotRequired[
        "capo_connect.types.evaluation_form_metric_configuration.EvaluationFormMetricConfiguration"
    ]
    """<p>The metric configuration for the question. Use this to associate a business outcome metric with the question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormQuestion) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    if "instructions" in value:
        out["Instructions"] = value["instructions"]
    out["RefId"] = value["ref_id"]
    out["NotApplicableEnabled"] = value.get("not_applicable_enabled", False)
    import capo_connect.types.evaluation_form_question_type

    out["QuestionType"] = (
        capo_connect.types.evaluation_form_question_type.serialize_json(
            value["question_type"]
        )
    )
    if "question_type_properties" in value:
        import capo_connect.types.evaluation_form_question_type_properties

        out["QuestionTypeProperties"] = (
            capo_connect.types.evaluation_form_question_type_properties.serialize_json(
                value["question_type_properties"]
            )
        )
    if "enablement" in value:
        import capo_connect.types.evaluation_form_item_enablement_configuration

        out["Enablement"] = (
            capo_connect.types.evaluation_form_item_enablement_configuration.serialize_json(
                value["enablement"]
            )
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
    if "scoring_configuration" in value:
        import capo_connect.types.evaluation_form_question_scoring_configuration

        out["ScoringConfiguration"] = (
            capo_connect.types.evaluation_form_question_scoring_configuration.serialize_json(
                value["scoring_configuration"]
            )
        )
    if "metric_configuration" in value:
        import capo_connect.types.evaluation_form_metric_configuration

        out["MetricConfiguration"] = (
            capo_connect.types.evaluation_form_metric_configuration.serialize_json(
                value["metric_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormQuestion:
    out: EvaluationFormQuestion = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("Instructions") is not None:
        out["instructions"] = data["Instructions"]
    if data.get("RefId") is not None:
        out["ref_id"] = data["RefId"]
    else:
        out["ref_id"] = ""
    if data.get("NotApplicableEnabled") is not None:
        out["not_applicable_enabled"] = data["NotApplicableEnabled"]
    else:
        out["not_applicable_enabled"] = False
    if data.get("QuestionType") is not None:
        import capo_connect.types.evaluation_form_question_type

        out["question_type"] = (
            capo_connect.types.evaluation_form_question_type.deserialize_json(
                data["QuestionType"]
            )
        )
    else:
        import typing

        out["question_type"] = typing.cast(
            "capo_connect.types.evaluation_form_question_type.EvaluationFormQuestionType",
            "",
        )
    if data.get("QuestionTypeProperties") is not None:
        import capo_connect.types.evaluation_form_question_type_properties

        out["question_type_properties"] = (
            capo_connect.types.evaluation_form_question_type_properties.deserialize_json(
                data["QuestionTypeProperties"]
            )
        )
    if data.get("Enablement") is not None:
        import capo_connect.types.evaluation_form_item_enablement_configuration

        out["enablement"] = (
            capo_connect.types.evaluation_form_item_enablement_configuration.deserialize_json(
                data["Enablement"]
            )
        )
    if data.get("Weight") is not None:
        out["weight"] = float(data["Weight"])
    else:
        out["weight"] = 0
    if data.get("ScoringConfiguration") is not None:
        import capo_connect.types.evaluation_form_question_scoring_configuration

        out["scoring_configuration"] = (
            capo_connect.types.evaluation_form_question_scoring_configuration.deserialize_json(
                data["ScoringConfiguration"]
            )
        )
    if data.get("MetricConfiguration") is not None:
        import capo_connect.types.evaluation_form_metric_configuration

        out["metric_configuration"] = (
            capo_connect.types.evaluation_form_metric_configuration.deserialize_json(
                data["MetricConfiguration"]
            )
        )
    return out
