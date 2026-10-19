"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicReviewedAnswer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.answer_id
    import capo_quicksight.types.arn
    import capo_quicksight.types.limited_sensitive_string
    import capo_quicksight.types.topic_ir
    import capo_quicksight.types.topic_template
    import capo_quicksight.types.topic_visual


class TopicReviewedAnswer(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the reviewed answer.</p>"""
    answer_id: "capo_quicksight.types.answer_id.AnswerId"
    """<p>The answer ID of the reviewed answer.</p>"""
    dataset_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Dataset ARN for the <code>TopicReviewedAnswer</code>.</p>"""
    question: "capo_quicksight.types.limited_sensitive_string.LimitedSensitiveString"
    """<p>The question for the <code>TopicReviewedAnswer</code>.</p>"""
    mir: NotRequired["capo_quicksight.types.topic_ir.TopicIR"]
    """<p>The mir for the <code>TopicReviewedAnswer</code>.</p>"""
    primary_visual: NotRequired["capo_quicksight.types.topic_visual.TopicVisual"]
    """<p>The primary visual for the <code>TopicReviewedAnswer</code>.</p>"""
    template: NotRequired["capo_quicksight.types.topic_template.TopicTemplate"]
    """<p>The template for the <code>TopicReviewedAnswer</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicReviewedAnswer) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    out["AnswerId"] = value["answer_id"]
    out["DatasetArn"] = value["dataset_arn"]
    out["Question"] = value["question"]
    if "mir" in value:
        import capo_quicksight.types.topic_ir

        out["Mir"] = capo_quicksight.types.topic_ir.serialize_json(value["mir"])
    if "primary_visual" in value:
        import capo_quicksight.types.topic_visual

        out["PrimaryVisual"] = capo_quicksight.types.topic_visual.serialize_json(
            value["primary_visual"]
        )
    if "template" in value:
        import capo_quicksight.types.topic_template

        out["Template"] = capo_quicksight.types.topic_template.serialize_json(
            value["template"]
        )
    return out


def deserialize_json(data: dict) -> TopicReviewedAnswer:
    out: TopicReviewedAnswer = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AnswerId") is not None:
        out["answer_id"] = data["AnswerId"]
    else:
        out["answer_id"] = ""
    if data.get("DatasetArn") is not None:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        out["dataset_arn"] = ""
    if data.get("Question") is not None:
        out["question"] = data["Question"]
    else:
        out["question"] = ""
    if data.get("Mir") is not None:
        import capo_quicksight.types.topic_ir

        out["mir"] = capo_quicksight.types.topic_ir.deserialize_json(data["Mir"])
    if data.get("PrimaryVisual") is not None:
        import capo_quicksight.types.topic_visual

        out["primary_visual"] = capo_quicksight.types.topic_visual.deserialize_json(
            data["PrimaryVisual"]
        )
    if data.get("Template") is not None:
        import capo_quicksight.types.topic_template

        out["template"] = capo_quicksight.types.topic_template.deserialize_json(
            data["Template"]
        )
    return out


def redact_sensitive(value: TopicReviewedAnswer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "question" in value:
        out["question"] = "*** Sensitive Data Redacted ***"
    if "mir" in value:
        import capo_quicksight.types.topic_ir

        out["mir"] = capo_quicksight.types.topic_ir.redact_sensitive(value["mir"])
    if "primary_visual" in value:
        import capo_quicksight.types.topic_visual

        out["primary_visual"] = capo_quicksight.types.topic_visual.redact_sensitive(
            value["primary_visual"]
        )
    return out
