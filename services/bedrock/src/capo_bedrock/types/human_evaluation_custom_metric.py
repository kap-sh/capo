"""Generated from Smithy shape ``com.amazonaws.bedrock#HumanEvaluationCustomMetric``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_metric_description
    import capo_bedrock.types.evaluation_metric_name
    import capo_bedrock.types.evaluation_rating_method


class HumanEvaluationCustomMetric(TypedDict, closed=True):
    name: "capo_bedrock.types.evaluation_metric_name.EvaluationMetricName"
    """<p>The name of the metric. Your human evaluators will see this name in the evaluation UI.</p>"""
    description: NotRequired[
        "capo_bedrock.types.evaluation_metric_description.EvaluationMetricDescription"
    ]
    """<p>An optional description of the metric. Use this parameter to provide more details about the metric.</p>"""
    rating_method: "capo_bedrock.types.evaluation_rating_method.EvaluationRatingMethod"
    """<p>Choose how you want your human workers to evaluation your model. Valid values for rating methods are <code>ThumbsUpDown</code>, <code>IndividualLikertScale</code>,<code>ComparisonLikertScale</code>, <code>ComparisonChoice</code>, and <code>ComparisonRank</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanEvaluationCustomMetric) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["ratingMethod"] = value["rating_method"]
    return out


def deserialize_json(data: dict) -> HumanEvaluationCustomMetric:
    out: HumanEvaluationCustomMetric = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("ratingMethod") is not None:
        out["rating_method"] = data["ratingMethod"]
    else:
        out["rating_method"] = ""
    return out


def redact_sensitive(value: HumanEvaluationCustomMetric) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
