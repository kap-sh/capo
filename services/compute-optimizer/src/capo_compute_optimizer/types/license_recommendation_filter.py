"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.filter_values
    import capo_compute_optimizer.types.license_recommendation_filter_name


class LicenseRecommendationFilter(TypedDict, closed=True):
    name: NotRequired[
        "capo_compute_optimizer.types.license_recommendation_filter_name.LicenseRecommendationFilterName"
    ]
    """<p>The name of the filter.</p> <p>Specify <code>Finding</code> to return recommendations with a specific finding classification.</p> <p>Specify <code>FindingReasonCode</code> to return recommendations with a specific finding reason code.</p> <p>You can filter your license recommendations by <code>tag:key</code> and <code>tag-key</code> tags.</p> <p>A <code>tag:key</code> is a key and value combination of a tag assigned to your license recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all license recommendations that have a tag with the key of <code>Owner</code> and the value of <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> <p>A <code>tag-key</code> is the key of a tag assigned to your license recommendations. Use this filter to find all of your license recommendations that have a tag with a specific key. This doesn’t consider the tag value. For example, you can find your license recommendations with a tag key value of <code>Owner</code> or without any tag keys assigned.</p>"""
    values: NotRequired["capo_compute_optimizer.types.filter_values.FilterValues"]
    """<p>The value of the filter.</p> <p>The valid values for this parameter are as follows, depending on what you specify for the <code>name</code> parameter:</p> <ul> <li> <p>If you specify the <code>name</code> parameter as <code>Finding</code>, then specify <code>Optimized</code>, <code>NotOptimized</code>, or <code>InsufficentMetrics</code>.</p> </li> <li> <p>If you specify the <code>name</code> parameter as <code>FindingReasonCode</code>, then specify <code>Optimized</code>, <code>LicenseOverprovisioned</code>, <code>InvalidCloudwatchApplicationInsights</code>, or <code>CloudwatchApplicationInsightsError</code>.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendationFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.license_recommendation_filter_name

        out["name"] = (
            capo_compute_optimizer.types.license_recommendation_filter_name.serialize_aws_json_1_0(
                value["name"]
            )
        )
    if "values" in value:
        import capo_compute_optimizer.types.filter_values

        out["values"] = (
            capo_compute_optimizer.types.filter_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LicenseRecommendationFilter:
    out: LicenseRecommendationFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.license_recommendation_filter_name

        out["name"] = (
            capo_compute_optimizer.types.license_recommendation_filter_name.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if data.get("values") is not None:
        import capo_compute_optimizer.types.filter_values

        out["values"] = (
            capo_compute_optimizer.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseRecommendationFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.license_recommendation_filter_name

        out["name"] = (
            capo_compute_optimizer.types.license_recommendation_filter_name.serialize_cbor(
                value["name"]
            )
        )
    if "values" in value:
        import capo_compute_optimizer.types.filter_values

        out["values"] = capo_compute_optimizer.types.filter_values.serialize_cbor(
            value["values"]
        )
    return out


def deserialize_cbor(data: dict) -> LicenseRecommendationFilter:
    out: LicenseRecommendationFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.license_recommendation_filter_name

        out["name"] = (
            capo_compute_optimizer.types.license_recommendation_filter_name.deserialize_cbor(
                data["name"]
            )
        )
    if data.get("values") is not None:
        import capo_compute_optimizer.types.filter_values

        out["values"] = capo_compute_optimizer.types.filter_values.deserialize_cbor(
            data["values"]
        )
    return out
