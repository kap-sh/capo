"""Generated from Smithy shape ``com.amazonaws.glue#EvaluationMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.find_matches_metrics
    import capo_glue.types.transform_type


class EvaluationMetrics(TypedDict, closed=True):
    transform_type: "capo_glue.types.transform_type.TransformType"
    """<p>The type of machine learning transform.</p>"""
    find_matches_metrics: NotRequired[
        "capo_glue.types.find_matches_metrics.FindMatchesMetrics"
    ]
    """<p>The evaluation metrics for the find matches algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationMetrics) -> dict:
    out: dict = {}
    import capo_glue.types.transform_type

    out["TransformType"] = capo_glue.types.transform_type.serialize_aws_json_1_1(
        value["transform_type"]
    )
    if "find_matches_metrics" in value:
        import capo_glue.types.find_matches_metrics

        out["FindMatchesMetrics"] = (
            capo_glue.types.find_matches_metrics.serialize_aws_json_1_1(
                value["find_matches_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationMetrics:
    out: EvaluationMetrics = {}  # type: ignore[typeddict-item]
    if data.get("TransformType") is not None:
        import capo_glue.types.transform_type

        out["transform_type"] = capo_glue.types.transform_type.deserialize_aws_json_1_1(
            data["TransformType"]
        )
    else:
        import typing

        out["transform_type"] = typing.cast(
            "capo_glue.types.transform_type.TransformType", ""
        )
    if data.get("FindMatchesMetrics") is not None:
        import capo_glue.types.find_matches_metrics

        out["find_matches_metrics"] = (
            capo_glue.types.find_matches_metrics.deserialize_aws_json_1_1(
                data["FindMatchesMetrics"]
            )
        )
    return out
