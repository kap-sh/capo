"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationForResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_trustedadvisor.types.account_recommendation_arn
    import capo_trustedadvisor.types.aws_resource_arn
    import capo_trustedadvisor.types.check_arn
    import capo_trustedadvisor.types.exclusion_status
    import capo_trustedadvisor.types.recommendation_pillar_list
    import capo_trustedadvisor.types.resource_status
    import capo_trustedadvisor.types.string_map


class RecommendationForResourceSummary(TypedDict, closed=True):
    check_arn: "capo_trustedadvisor.types.check_arn.CheckArn"
    """<p>The Check ARN</p>"""
    recommendation_arn: (
        "capo_trustedadvisor.types.account_recommendation_arn.AccountRecommendationArn"
    )
    """<p>The Recommendation ARN</p>"""
    aws_resource_arn: "capo_trustedadvisor.types.aws_resource_arn.AwsResourceArn"
    """<p>The AWS Resource ARN</p>"""
    status: "capo_trustedadvisor.types.resource_status.ResourceStatus"
    """<p>The current status of the recommendation</p>"""
    last_updated_at: "datetime.datetime"
    """<p>When the recommendation was last updated</p>"""
    exclusion_status: "capo_trustedadvisor.types.exclusion_status.ExclusionStatus"
    """<p>The exclusion status of the recommendation</p>"""
    metadata: "capo_trustedadvisor.types.string_map.StringMap"
    """<p>Metadata associated with the recommendation</p>"""
    pillars: (
        "capo_trustedadvisor.types.recommendation_pillar_list.RecommendationPillarList"
    )
    """<p>The Pillars that the Recommendation is optimizing</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationForResourceSummary) -> dict:
    out: dict = {}
    out["checkArn"] = value["check_arn"]
    out["recommendationArn"] = value["recommendation_arn"]
    out["awsResourceArn"] = value["aws_resource_arn"]
    import capo_trustedadvisor.types.resource_status

    out["status"] = capo_trustedadvisor.types.resource_status.serialize_json(
        value["status"]
    )
    import capo_trustedadvisor._protocol.serialize

    out["lastUpdatedAt"] = capo_trustedadvisor._protocol.serialize.fmt_date_time(
        value["last_updated_at"]
    )
    import capo_trustedadvisor.types.exclusion_status

    out["exclusionStatus"] = capo_trustedadvisor.types.exclusion_status.serialize_json(
        value["exclusion_status"]
    )
    import capo_trustedadvisor.types.string_map

    out["metadata"] = capo_trustedadvisor.types.string_map.serialize_json(
        value["metadata"]
    )
    import capo_trustedadvisor.types.recommendation_pillar_list

    out["pillars"] = (
        capo_trustedadvisor.types.recommendation_pillar_list.serialize_json(
            value["pillars"]
        )
    )
    return out


def deserialize_json(data: dict) -> RecommendationForResourceSummary:
    out: RecommendationForResourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("checkArn") is not None:
        out["check_arn"] = data["checkArn"]
    else:
        out["check_arn"] = ""
    if data.get("recommendationArn") is not None:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        out["recommendation_arn"] = ""
    if data.get("awsResourceArn") is not None:
        out["aws_resource_arn"] = data["awsResourceArn"]
    else:
        out["aws_resource_arn"] = ""
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
        import typing

        out["exclusion_status"] = typing.cast(
            "capo_trustedadvisor.types.exclusion_status.ExclusionStatus", ""
        )
    if data.get("metadata") is not None:
        import capo_trustedadvisor.types.string_map

        out["metadata"] = capo_trustedadvisor.types.string_map.deserialize_json(
            data["metadata"]
        )
    else:
        out["metadata"] = {}
    if data.get("pillars") is not None:
        import capo_trustedadvisor.types.recommendation_pillar_list

        out["pillars"] = (
            capo_trustedadvisor.types.recommendation_pillar_list.deserialize_json(
                data["pillars"]
            )
        )
    else:
        out["pillars"] = []
    return out
