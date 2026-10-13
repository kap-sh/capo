"""Generated from Smithy shape ``com.amazonaws.pi#Recommendation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.markdown_string
    import capo_pi.types.string


class Recommendation(TypedDict, closed=True):
    recommendation_id: NotRequired["capo_pi.types.string.String"]
    """<p>The unique identifier for the recommendation.</p>"""
    recommendation_description: NotRequired[
        "capo_pi.types.markdown_string.MarkdownString"
    ]
    """<p>The recommendation details to help resolve the performance issue. For example, <code>Investigate the following SQLs that contributed to 100% of the total DBLoad during that time period: sql-id</code> </p>"""
    recommendation_details: NotRequired["capo_pi.types.markdown_string.MarkdownString"]
    """<p>Detailed information about the recommendation, including steps to resolve the performance issue.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recommendation) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["RecommendationId"] = value["recommendation_id"]
    if "recommendation_description" in value:
        out["RecommendationDescription"] = value["recommendation_description"]
    if "recommendation_details" in value:
        out["RecommendationDetails"] = value["recommendation_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if data.get("RecommendationId") is not None:
        out["recommendation_id"] = data["RecommendationId"]
    if data.get("RecommendationDescription") is not None:
        out["recommendation_description"] = data["RecommendationDescription"]
    if data.get("RecommendationDetails") is not None:
        out["recommendation_details"] = data["RecommendationDetails"]
    return out


def redact_sensitive(value: Recommendation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommendation_description" in value:
        out["recommendation_description"] = "*** Sensitive Data Redacted ***"
    if "recommendation_details" in value:
        out["recommendation_details"] = "*** Sensitive Data Redacted ***"
    return out
