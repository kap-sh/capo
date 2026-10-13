"""Generated from Smithy shape ``com.amazonaws.quicksight#QAResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dashboard_visual_result
    import capo_quicksight.types.generated_answer_result
    import capo_quicksight.types.qa_result_type


class QAResult(TypedDict, closed=True):
    result_type: NotRequired["capo_quicksight.types.qa_result_type.QAResultType"]
    """<p>The type of QA result.</p>"""
    dashboard_visual: NotRequired[
        "capo_quicksight.types.dashboard_visual_result.DashboardVisualResult"
    ]
    """<p>The representation of a dashboard visual result.</p>"""
    generated_answer: NotRequired[
        "capo_quicksight.types.generated_answer_result.GeneratedAnswerResult"
    ]
    """<p>The representation of a generated answer result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QAResult) -> dict:
    out: dict = {}
    if "result_type" in value:
        import capo_quicksight.types.qa_result_type

        out["ResultType"] = capo_quicksight.types.qa_result_type.serialize_json(
            value["result_type"]
        )
    if "dashboard_visual" in value:
        import capo_quicksight.types.dashboard_visual_result

        out["DashboardVisual"] = (
            capo_quicksight.types.dashboard_visual_result.serialize_json(
                value["dashboard_visual"]
            )
        )
    if "generated_answer" in value:
        import capo_quicksight.types.generated_answer_result

        out["GeneratedAnswer"] = (
            capo_quicksight.types.generated_answer_result.serialize_json(
                value["generated_answer"]
            )
        )
    return out


def deserialize_json(data: dict) -> QAResult:
    out: QAResult = {}  # type: ignore[typeddict-item]
    if data.get("ResultType") is not None:
        import capo_quicksight.types.qa_result_type

        out["result_type"] = capo_quicksight.types.qa_result_type.deserialize_json(
            data["ResultType"]
        )
    if data.get("DashboardVisual") is not None:
        import capo_quicksight.types.dashboard_visual_result

        out["dashboard_visual"] = (
            capo_quicksight.types.dashboard_visual_result.deserialize_json(
                data["DashboardVisual"]
            )
        )
    if data.get("GeneratedAnswer") is not None:
        import capo_quicksight.types.generated_answer_result

        out["generated_answer"] = (
            capo_quicksight.types.generated_answer_result.deserialize_json(
                data["GeneratedAnswer"]
            )
        )
    return out


def redact_sensitive(value: QAResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "generated_answer" in value:
        import capo_quicksight.types.generated_answer_result

        out["generated_answer"] = (
            capo_quicksight.types.generated_answer_result.redact_sensitive(
                value["generated_answer"]
            )
        )
    return out
