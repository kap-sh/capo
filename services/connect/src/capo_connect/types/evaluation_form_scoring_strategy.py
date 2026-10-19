"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormScoringStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_score_threshold_list
    import capo_connect.types.evaluation_form_scoring_mode
    import capo_connect.types.evaluation_form_scoring_status


class EvaluationFormScoringStrategy(TypedDict, closed=True):
    mode: "capo_connect.types.evaluation_form_scoring_mode.EvaluationFormScoringMode"
    """<p>The scoring mode of the evaluation form.</p>"""
    status: (
        "capo_connect.types.evaluation_form_scoring_status.EvaluationFormScoringStatus"
    )
    """<p>The scoring status of the evaluation form.</p>"""
    score_thresholds: NotRequired[
        "capo_connect.types.evaluation_form_score_threshold_list.EvaluationFormScoreThresholdList"
    ]
    """<p>The score thresholds for performance categories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormScoringStrategy) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_scoring_mode

    out["Mode"] = capo_connect.types.evaluation_form_scoring_mode.serialize_json(
        value["mode"]
    )
    import capo_connect.types.evaluation_form_scoring_status

    out["Status"] = capo_connect.types.evaluation_form_scoring_status.serialize_json(
        value["status"]
    )
    if "score_thresholds" in value:
        import capo_connect.types.evaluation_form_score_threshold_list

        out["ScoreThresholds"] = (
            capo_connect.types.evaluation_form_score_threshold_list.serialize_json(
                value["score_thresholds"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormScoringStrategy:
    out: EvaluationFormScoringStrategy = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_connect.types.evaluation_form_scoring_mode

        out["mode"] = capo_connect.types.evaluation_form_scoring_mode.deserialize_json(
            data["Mode"]
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_connect.types.evaluation_form_scoring_mode.EvaluationFormScoringMode",
            "",
        )
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_form_scoring_status

        out["status"] = (
            capo_connect.types.evaluation_form_scoring_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connect.types.evaluation_form_scoring_status.EvaluationFormScoringStatus",
            "",
        )
    if data.get("ScoreThresholds") is not None:
        import capo_connect.types.evaluation_form_score_threshold_list

        out["score_thresholds"] = (
            capo_connect.types.evaluation_form_score_threshold_list.deserialize_json(
                data["ScoreThresholds"]
            )
        )
    return out
