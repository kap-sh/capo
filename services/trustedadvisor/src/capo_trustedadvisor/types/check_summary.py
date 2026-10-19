"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#CheckSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_trustedadvisor.types.check_arn
    import capo_trustedadvisor.types.recommendation_aws_service_list
    import capo_trustedadvisor.types.recommendation_pillar_list
    import capo_trustedadvisor.types.recommendation_source
    import capo_trustedadvisor.types.string_list
    import capo_trustedadvisor.types.string_map


class CheckSummary(TypedDict, closed=True):
    id: "str"
    """<p>The unique identifier of the AWS Trusted Advisor Check</p>"""
    arn: "capo_trustedadvisor.types.check_arn.CheckArn"
    """<p>The ARN of the AWS Trusted Advisor Check</p>"""
    name: "str"
    """<p>The name of the AWS Trusted Advisor Check</p>"""
    description: "str"
    """<p>A description of what the AWS Trusted Advisor Check is monitoring</p>"""
    pillars: (
        "capo_trustedadvisor.types.recommendation_pillar_list.RecommendationPillarList"
    )
    """<p>The Recommendation pillars that the AWS Trusted Advisor Check falls under</p>"""
    aws_services: "capo_trustedadvisor.types.recommendation_aws_service_list.RecommendationAwsServiceList"
    """<p>The AWS Services that the Check applies to</p>"""
    source: "capo_trustedadvisor.types.recommendation_source.RecommendationSource"
    """<p>The source of the Recommendation</p>"""
    metadata: "capo_trustedadvisor.types.string_map.StringMap"
    """<p>The column headings for the metadata returned in the resource</p>"""
    resource_arn_queryable: "bool"
    """<p>Indicates whether this check is supported by the ListRecommendationsForResource API.</p>"""
    aws_resource_types: "capo_trustedadvisor.types.string_list.StringList"
    """<p>The AWS resource types that this check evaluates (for example, AWS::EC2::Instance).</p>"""
    check_granularity: NotRequired["str"]
    """<p>The granularity level at which the check operates: resource, account, or account_region.</p>"""
    recommendation_id: NotRequired["str"]
    """<p>The recommendation identifier associated with the check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_trustedadvisor.types.recommendation_pillar_list

    out["pillars"] = (
        capo_trustedadvisor.types.recommendation_pillar_list.serialize_json(
            value["pillars"]
        )
    )
    import capo_trustedadvisor.types.recommendation_aws_service_list

    out["awsServices"] = (
        capo_trustedadvisor.types.recommendation_aws_service_list.serialize_json(
            value["aws_services"]
        )
    )
    import capo_trustedadvisor.types.recommendation_source

    out["source"] = capo_trustedadvisor.types.recommendation_source.serialize_json(
        value["source"]
    )
    import capo_trustedadvisor.types.string_map

    out["metadata"] = capo_trustedadvisor.types.string_map.serialize_json(
        value["metadata"]
    )
    out["resourceArnQueryable"] = value.get("resource_arn_queryable", False)
    import capo_trustedadvisor.types.string_list

    out["awsResourceTypes"] = capo_trustedadvisor.types.string_list.serialize_json(
        value.get("aws_resource_types", [])
    )
    if "check_granularity" in value:
        out["checkGranularity"] = value["check_granularity"]
    if "recommendation_id" in value:
        out["recommendationId"] = value["recommendation_id"]
    return out


def deserialize_json(data: dict) -> CheckSummary:
    out: CheckSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("pillars") is not None:
        import capo_trustedadvisor.types.recommendation_pillar_list

        out["pillars"] = (
            capo_trustedadvisor.types.recommendation_pillar_list.deserialize_json(
                data["pillars"]
            )
        )
    else:
        out["pillars"] = []
    if data.get("awsServices") is not None:
        import capo_trustedadvisor.types.recommendation_aws_service_list

        out["aws_services"] = (
            capo_trustedadvisor.types.recommendation_aws_service_list.deserialize_json(
                data["awsServices"]
            )
        )
    else:
        out["aws_services"] = []
    if data.get("source") is not None:
        import capo_trustedadvisor.types.recommendation_source

        out["source"] = (
            capo_trustedadvisor.types.recommendation_source.deserialize_json(
                data["source"]
            )
        )
    else:
        import typing

        out["source"] = typing.cast(
            "capo_trustedadvisor.types.recommendation_source.RecommendationSource", ""
        )
    if data.get("metadata") is not None:
        import capo_trustedadvisor.types.string_map

        out["metadata"] = capo_trustedadvisor.types.string_map.deserialize_json(
            data["metadata"]
        )
    else:
        out["metadata"] = {}
    if data.get("resourceArnQueryable") is not None:
        out["resource_arn_queryable"] = data["resourceArnQueryable"]
    else:
        out["resource_arn_queryable"] = False
    if data.get("awsResourceTypes") is not None:
        import capo_trustedadvisor.types.string_list

        out["aws_resource_types"] = (
            capo_trustedadvisor.types.string_list.deserialize_json(
                data["awsResourceTypes"]
            )
        )
    else:
        out["aws_resource_types"] = []
    if data.get("checkGranularity") is not None:
        out["check_granularity"] = data["checkGranularity"]
    if data.get("recommendationId") is not None:
        out["recommendation_id"] = data["recommendationId"]
    return out
