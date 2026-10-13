"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductsSpendInsightsBySource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_product_insights


class AwsProductsSpendInsightsBySource(TypedDict, closed=True):
    partner: NotRequired[
        "capo_partnercentral_selling.types.aws_product_insights.AwsProductInsights"
    ]
    """<p>Partner-sourced insights derived from Pricing Calculator URLs.</p>"""
    aws: NotRequired[
        "capo_partnercentral_selling.types.aws_product_insights.AwsProductInsights"
    ]
    """<p>AI-generated insights including recommended products from AWS.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductsSpendInsightsBySource) -> dict:
    out: dict = {}
    if "partner" in value:
        import capo_partnercentral_selling.types.aws_product_insights

        out["Partner"] = (
            capo_partnercentral_selling.types.aws_product_insights.serialize_aws_json_1_0(
                value["partner"]
            )
        )
    if "aws" in value:
        import capo_partnercentral_selling.types.aws_product_insights

        out["AWS"] = (
            capo_partnercentral_selling.types.aws_product_insights.serialize_aws_json_1_0(
                value["aws"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsProductsSpendInsightsBySource:
    out: AwsProductsSpendInsightsBySource = {}  # type: ignore[typeddict-item]
    if data.get("Partner") is not None:
        import capo_partnercentral_selling.types.aws_product_insights

        out["partner"] = (
            capo_partnercentral_selling.types.aws_product_insights.deserialize_aws_json_1_0(
                data["Partner"]
            )
        )
    if data.get("AWS") is not None:
        import capo_partnercentral_selling.types.aws_product_insights

        out["aws"] = (
            capo_partnercentral_selling.types.aws_product_insights.deserialize_aws_json_1_0(
                data["AWS"]
            )
        )
    return out


def redact_sensitive(value: AwsProductsSpendInsightsBySource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "partner" in value:
        import capo_partnercentral_selling.types.aws_product_insights

        out["partner"] = (
            capo_partnercentral_selling.types.aws_product_insights.redact_sensitive(
                value["partner"]
            )
        )
    if "aws" in value:
        import capo_partnercentral_selling.types.aws_product_insights

        out["aws"] = (
            capo_partnercentral_selling.types.aws_product_insights.redact_sensitive(
                value["aws"]
            )
        )
    return out
