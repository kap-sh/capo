"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityInsights``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_products_spend_insights_by_source
    import capo_partnercentral_selling.types.engagement_score
    import capo_partnercentral_selling.types.opportunity_quality
    import capo_partnercentral_selling.types.recommendation_list


class AwsOpportunityInsights(TypedDict, closed=True):
    next_best_actions: NotRequired["str"]
    """<p>Provides recommendations from AWS on the next best actions to take in order to move the opportunity forward and increase the likelihood of success.</p>"""
    engagement_score: NotRequired[
        "capo_partnercentral_selling.types.engagement_score.EngagementScore"
    ]
    """<p>Represents a score assigned by AWS to indicate the level of engagement and potential success for the opportunity. This score helps partners prioritize their efforts.</p>"""
    aws_products_spend_insights_by_source: NotRequired[
        "capo_partnercentral_selling.types.aws_products_spend_insights_by_source.AwsProductsSpendInsightsBySource"
    ]
    """<p>Source-separated spend insights that provide independent analysis for AWS recommendations and partner estimates.</p>"""
    opportunity_quality: NotRequired[
        "capo_partnercentral_selling.types.opportunity_quality.OpportunityQuality"
    ]
    """<p>Opportunity quality assessment. Null if not yet scored.</p>"""
    recommendations: NotRequired[
        "capo_partnercentral_selling.types.recommendation_list.RecommendationList"
    ]
    """<p>List of recommendations from various agent-driven sources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunityInsights) -> dict:
    out: dict = {}
    if "next_best_actions" in value:
        out["NextBestActions"] = value["next_best_actions"]
    if "engagement_score" in value:
        import capo_partnercentral_selling.types.engagement_score

        out["EngagementScore"] = (
            capo_partnercentral_selling.types.engagement_score.serialize_aws_json_1_0(
                value["engagement_score"]
            )
        )
    if "aws_products_spend_insights_by_source" in value:
        import capo_partnercentral_selling.types.aws_products_spend_insights_by_source

        out["AwsProductsSpendInsightsBySource"] = (
            capo_partnercentral_selling.types.aws_products_spend_insights_by_source.serialize_aws_json_1_0(
                value["aws_products_spend_insights_by_source"]
            )
        )
    if "opportunity_quality" in value:
        import capo_partnercentral_selling.types.opportunity_quality

        out["OpportunityQuality"] = (
            capo_partnercentral_selling.types.opportunity_quality.serialize_aws_json_1_0(
                value["opportunity_quality"]
            )
        )
    if "recommendations" in value:
        import capo_partnercentral_selling.types.recommendation_list

        out["Recommendations"] = (
            capo_partnercentral_selling.types.recommendation_list.serialize_aws_json_1_0(
                value["recommendations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOpportunityInsights:
    out: AwsOpportunityInsights = {}  # type: ignore[typeddict-item]
    if data.get("NextBestActions") is not None:
        out["next_best_actions"] = data["NextBestActions"]
    if data.get("EngagementScore") is not None:
        import capo_partnercentral_selling.types.engagement_score

        out["engagement_score"] = (
            capo_partnercentral_selling.types.engagement_score.deserialize_aws_json_1_0(
                data["EngagementScore"]
            )
        )
    if data.get("AwsProductsSpendInsightsBySource") is not None:
        import capo_partnercentral_selling.types.aws_products_spend_insights_by_source

        out["aws_products_spend_insights_by_source"] = (
            capo_partnercentral_selling.types.aws_products_spend_insights_by_source.deserialize_aws_json_1_0(
                data["AwsProductsSpendInsightsBySource"]
            )
        )
    if data.get("OpportunityQuality") is not None:
        import capo_partnercentral_selling.types.opportunity_quality

        out["opportunity_quality"] = (
            capo_partnercentral_selling.types.opportunity_quality.deserialize_aws_json_1_0(
                data["OpportunityQuality"]
            )
        )
    if data.get("Recommendations") is not None:
        import capo_partnercentral_selling.types.recommendation_list

        out["recommendations"] = (
            capo_partnercentral_selling.types.recommendation_list.deserialize_aws_json_1_0(
                data["Recommendations"]
            )
        )
    return out


def redact_sensitive(value: AwsOpportunityInsights) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "aws_products_spend_insights_by_source" in value:
        import capo_partnercentral_selling.types.aws_products_spend_insights_by_source

        out["aws_products_spend_insights_by_source"] = (
            capo_partnercentral_selling.types.aws_products_spend_insights_by_source.redact_sensitive(
                value["aws_products_spend_insights_by_source"]
            )
        )
    return out
