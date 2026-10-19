"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_trustedadvisor.types.account_recommendation_arn
    import capo_trustedadvisor.types.exclusion_status
    import capo_trustedadvisor.types.recommendation_region_code
    import capo_trustedadvisor.types.recommendation_resource_arn
    import capo_trustedadvisor.types.resource_status
    import capo_trustedadvisor.types.string_map


class RecommendationResourceSummary(TypedDict, closed=True):
    id: "str"
    """<p>The ID of the Recommendation Resource</p>"""
    arn: "capo_trustedadvisor.types.recommendation_resource_arn.RecommendationResourceArn"
    """<p>The ARN of the Recommendation Resource</p>"""
    aws_resource_id: "str"
    """<p>The AWS resource identifier. There are certain checks that generate recommendation resources without an awsResourceId.</p>"""
    region_code: (
        "capo_trustedadvisor.types.recommendation_region_code.RecommendationRegionCode"
    )
    """<p>The AWS Region code that the Recommendation Resource is in</p>"""
    status: "capo_trustedadvisor.types.resource_status.ResourceStatus"
    """<p>The current status of the Recommendation Resource</p>"""
    metadata: "capo_trustedadvisor.types.string_map.StringMap"
    """<p>Metadata associated with the Recommendation Resource</p>"""
    last_updated_at: "datetime.datetime"
    """<p>When the Recommendation Resource was last updated</p>"""
    exclusion_status: "capo_trustedadvisor.types.exclusion_status.ExclusionStatus"
    """<p>The exclusion status of the Recommendation Resource</p>"""
    recommendation_arn: (
        "capo_trustedadvisor.types.account_recommendation_arn.AccountRecommendationArn"
    )
    """<p>The Recommendation ARN</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResourceSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["awsResourceId"] = value["aws_resource_id"]
    out["regionCode"] = value["region_code"]
    import capo_trustedadvisor.types.resource_status

    out["status"] = capo_trustedadvisor.types.resource_status.serialize_json(
        value["status"]
    )
    import capo_trustedadvisor.types.string_map

    out["metadata"] = capo_trustedadvisor.types.string_map.serialize_json(
        value["metadata"]
    )
    import capo_trustedadvisor._protocol.serialize

    out["lastUpdatedAt"] = capo_trustedadvisor._protocol.serialize.fmt_date_time(
        value["last_updated_at"]
    )
    import capo_trustedadvisor.types.exclusion_status

    out["exclusionStatus"] = capo_trustedadvisor.types.exclusion_status.serialize_json(
        value.get("exclusion_status", "included")
    )
    out["recommendationArn"] = value["recommendation_arn"]
    return out


def deserialize_json(data: dict) -> RecommendationResourceSummary:
    out: RecommendationResourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("awsResourceId") is not None:
        out["aws_resource_id"] = data["awsResourceId"]
    else:
        out["aws_resource_id"] = ""
    if data.get("regionCode") is not None:
        out["region_code"] = data["regionCode"]
    else:
        out["region_code"] = ""
    if data.get("status") is not None:
        import capo_trustedadvisor.types.resource_status

        out["status"] = capo_trustedadvisor.types.resource_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_trustedadvisor.types.resource_status.ResourceStatus", ""
        )
    if data.get("metadata") is not None:
        import capo_trustedadvisor.types.string_map

        out["metadata"] = capo_trustedadvisor.types.string_map.deserialize_json(
            data["metadata"]
        )
    else:
        out["metadata"] = {}
    if data.get("lastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["lastUpdatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("exclusionStatus") is not None:
        import capo_trustedadvisor.types.exclusion_status

        out["exclusion_status"] = (
            capo_trustedadvisor.types.exclusion_status.deserialize_json(
                data["exclusionStatus"]
            )
        )
    else:
        out["exclusion_status"] = "included"
    if data.get("recommendationArn") is not None:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        out["recommendation_arn"] = ""
    return out
