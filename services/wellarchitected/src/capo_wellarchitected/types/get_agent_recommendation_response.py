"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentRecommendationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.agent_recommendation_remediations
    import capo_wellarchitected.types.cross_pillar_benefits
    import capo_wellarchitected.types.effort
    import capo_wellarchitected.types.highlights
    import capo_wellarchitected.types.impact_category
    import capo_wellarchitected.types.impact_details
    import capo_wellarchitected.types.insight_list
    import capo_wellarchitected.types.pillar
    import capo_wellarchitected.types.priority
    import capo_wellarchitected.types.recommendation_arn
    import capo_wellarchitected.types.recommendation_goals
    import capo_wellarchitected.types.recommendation_source_list
    import capo_wellarchitected.types.recommendation_state
    import capo_wellarchitected.types.recommendation_status
    import capo_wellarchitected.types.recommendation_type
    import capo_wellarchitected.types.remediation_summary
    import capo_wellarchitected.types.roi
    import capo_wellarchitected.types.sensitive_string
    import capo_wellarchitected.types.string_list
    import capo_wellarchitected.types.tags
    import capo_wellarchitected.types.trade_offs
    import capo_wellarchitected.types.uuid


class GetAgentRecommendationResponse(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.recommendation_arn.RecommendationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the recommendation.</p>"""
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the associated profile.</p>"""
    generation_id: NotRequired["capo_wellarchitected.types.uuid.UUID"]
    """<p>The identifier of the generation process that produced this recommendation.</p>"""
    title: "capo_wellarchitected.types.sensitive_string.SensitiveString"
    """<p>The title of the recommendation.</p>"""
    description: "capo_wellarchitected.types.sensitive_string.SensitiveString"
    """<p>A description of the recommendation.</p>"""
    type: "capo_wellarchitected.types.recommendation_type.RecommendationType"
    """<p>The type of the recommendation.</p>"""
    pillar: "capo_wellarchitected.types.pillar.Pillar"
    """<p>The Well-Architected Tool Framework pillar that the recommendation addresses.</p>"""
    priority: "capo_wellarchitected.types.priority.Priority"
    """<p>The priority of the recommendation.</p>"""
    effort: "capo_wellarchitected.types.effort.Effort"
    """<p>The effort required to implement the recommendation.</p>"""
    status: "capo_wellarchitected.types.recommendation_status.RecommendationStatus"
    """<p>The current status of the recommendation.</p>"""
    state: "capo_wellarchitected.types.recommendation_state.RecommendationState"
    """<p>The current state of the recommendation.</p>"""
    update_reason: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The free-text reason associated with the recommendation's most recent status update.</p>"""
    impact: "capo_wellarchitected.types.impact_category.ImpactCategory"
    """<p>The severity of the recommendation's impact.</p>"""
    roi: "capo_wellarchitected.types.roi.Roi"
    """<p>The return on investment estimate for the recommendation.</p>"""
    number_of_resources: NotRequired["int"]
    """<p>The number of Amazon Web Services resources this recommendation affects.</p>"""
    aws_services: NotRequired["capo_wellarchitected.types.string_list.StringList"]
    """<p>The Amazon Web Services services that the recommendation applies to.</p>"""
    business_units: NotRequired["capo_wellarchitected.types.string_list.StringList"]
    """<p>The business units that own the affected resources.</p>"""
    applications: NotRequired["capo_wellarchitected.types.string_list.StringList"]
    """<p>The applications that the recommendation targets.</p>"""
    impact_details: "capo_wellarchitected.types.impact_details.ImpactDetails"
    """<p>Detailed impact information for the recommendation.</p>"""
    insights: "capo_wellarchitected.types.insight_list.InsightList"
    """<p>A list of insights about the recommendation.</p>"""
    highlights: "capo_wellarchitected.types.highlights.Highlights"
    """<p>Highlights describing what was detected.</p>"""
    remediation_summary: (
        "capo_wellarchitected.types.remediation_summary.RemediationSummary"
    )
    """<p>A high-level summary of the recommended remediation.</p>"""
    cross_pillar_benefits: NotRequired[
        "capo_wellarchitected.types.cross_pillar_benefits.CrossPillarBenefits"
    ]
    """<p>Cross-pillar benefits of acting on the recommendation.</p>"""
    trade_offs: NotRequired["capo_wellarchitected.types.trade_offs.TradeOffs"]
    """<p>Trade-offs of acting on the recommendation.</p>"""
    sources: NotRequired[
        "capo_wellarchitected.types.recommendation_source_list.RecommendationSourceList"
    ]
    """<p>Sources that generated this recommendation.</p>"""
    goals: NotRequired[
        "capo_wellarchitected.types.recommendation_goals.RecommendationGoals"
    ]
    """<p>Goals that this recommendation targets.</p>"""
    tags: NotRequired["capo_wellarchitected.types.tags.Tags"]
    """<p>A set of key-value pairs associated with the recommendation, used for cost allocation and access control.</p>"""
    created_by: "str"
    """<p>The identifier of the user or system that created this recommendation.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the recommendation was created.</p>"""
    last_modified_by: NotRequired["str"]
    """<p>The identifier of the user or system that last modified this recommendation.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the recommendation was last modified.</p>"""
    remediations: NotRequired[
        "capo_wellarchitected.types.agent_recommendation_remediations.AgentRecommendationRemediations"
    ]
    """<p>A list of remediations for the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRecommendationResponse) -> dict:
    out: dict = {}
    out["recommendationArn"] = value["recommendation_arn"]
    out["profileArn"] = value["profile_arn"]
    if "generation_id" in value:
        out["generationId"] = value["generation_id"]
    out["title"] = value["title"]
    out["description"] = value["description"]
    import capo_wellarchitected.types.recommendation_type

    out["type"] = capo_wellarchitected.types.recommendation_type.serialize_json(
        value["type"]
    )
    import capo_wellarchitected.types.pillar

    out["pillar"] = capo_wellarchitected.types.pillar.serialize_json(value["pillar"])
    import capo_wellarchitected.types.priority

    out["priority"] = capo_wellarchitected.types.priority.serialize_json(
        value["priority"]
    )
    import capo_wellarchitected.types.effort

    out["effort"] = capo_wellarchitected.types.effort.serialize_json(value["effort"])
    import capo_wellarchitected.types.recommendation_status

    out["status"] = capo_wellarchitected.types.recommendation_status.serialize_json(
        value["status"]
    )
    import capo_wellarchitected.types.recommendation_state

    out["state"] = capo_wellarchitected.types.recommendation_state.serialize_json(
        value["state"]
    )
    if "update_reason" in value:
        out["updateReason"] = value["update_reason"]
    import capo_wellarchitected.types.impact_category

    out["impact"] = capo_wellarchitected.types.impact_category.serialize_json(
        value["impact"]
    )
    import capo_wellarchitected.types.roi

    out["roi"] = capo_wellarchitected.types.roi.serialize_json(value["roi"])
    if "number_of_resources" in value:
        out["numberOfResources"] = value["number_of_resources"]
    if "aws_services" in value:
        import capo_wellarchitected.types.string_list

        out["awsServices"] = capo_wellarchitected.types.string_list.serialize_json(
            value["aws_services"]
        )
    if "business_units" in value:
        import capo_wellarchitected.types.string_list

        out["businessUnits"] = capo_wellarchitected.types.string_list.serialize_json(
            value["business_units"]
        )
    if "applications" in value:
        import capo_wellarchitected.types.string_list

        out["applications"] = capo_wellarchitected.types.string_list.serialize_json(
            value["applications"]
        )
    import capo_wellarchitected.types.impact_details

    out["impactDetails"] = capo_wellarchitected.types.impact_details.serialize_json(
        value["impact_details"]
    )
    import capo_wellarchitected.types.insight_list

    out["insights"] = capo_wellarchitected.types.insight_list.serialize_json(
        value["insights"]
    )
    import capo_wellarchitected.types.highlights

    out["highlights"] = capo_wellarchitected.types.highlights.serialize_json(
        value["highlights"]
    )
    import capo_wellarchitected.types.remediation_summary

    out["remediationSummary"] = (
        capo_wellarchitected.types.remediation_summary.serialize_json(
            value["remediation_summary"]
        )
    )
    if "cross_pillar_benefits" in value:
        import capo_wellarchitected.types.cross_pillar_benefits

        out["crossPillarBenefits"] = (
            capo_wellarchitected.types.cross_pillar_benefits.serialize_json(
                value["cross_pillar_benefits"]
            )
        )
    if "trade_offs" in value:
        import capo_wellarchitected.types.trade_offs

        out["tradeOffs"] = capo_wellarchitected.types.trade_offs.serialize_json(
            value["trade_offs"]
        )
    if "sources" in value:
        import capo_wellarchitected.types.recommendation_source_list

        out["sources"] = (
            capo_wellarchitected.types.recommendation_source_list.serialize_json(
                value["sources"]
            )
        )
    if "goals" in value:
        import capo_wellarchitected.types.recommendation_goals

        out["goals"] = capo_wellarchitected.types.recommendation_goals.serialize_json(
            value["goals"]
        )
    if "tags" in value:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.serialize_json(value["tags"])
    out["createdBy"] = value["created_by"]
    import capo_wellarchitected._protocol.serialize

    out["createdAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "last_modified_at" in value:
        import capo_wellarchitected._protocol.serialize

        out["lastModifiedAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
            value["last_modified_at"]
        )
    if "remediations" in value:
        import capo_wellarchitected.types.agent_recommendation_remediations

        out["remediations"] = (
            capo_wellarchitected.types.agent_recommendation_remediations.serialize_json(
                value["remediations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAgentRecommendationResponse:
    out: GetAgentRecommendationResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendationArn") is not None:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        raise DeserializationError(
            "GetAgentRecommendationResponse.recommendation_arn required"
        )
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    else:
        raise DeserializationError(
            "GetAgentRecommendationResponse.profile_arn required"
        )
    if data.get("generationId") is not None:
        out["generation_id"] = data["generationId"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        raise DeserializationError("GetAgentRecommendationResponse.title required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError(
            "GetAgentRecommendationResponse.description required"
        )
    if data.get("type") is not None:
        import capo_wellarchitected.types.recommendation_type

        out["type"] = capo_wellarchitected.types.recommendation_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.type required")
    if data.get("pillar") is not None:
        import capo_wellarchitected.types.pillar

        out["pillar"] = capo_wellarchitected.types.pillar.deserialize_json(
            data["pillar"]
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.pillar required")
    if data.get("priority") is not None:
        import capo_wellarchitected.types.priority

        out["priority"] = capo_wellarchitected.types.priority.deserialize_json(
            data["priority"]
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.priority required")
    if data.get("effort") is not None:
        import capo_wellarchitected.types.effort

        out["effort"] = capo_wellarchitected.types.effort.deserialize_json(
            data["effort"]
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.effort required")
    if data.get("status") is not None:
        import capo_wellarchitected.types.recommendation_status

        out["status"] = (
            capo_wellarchitected.types.recommendation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.status required")
    if data.get("state") is not None:
        import capo_wellarchitected.types.recommendation_state

        out["state"] = capo_wellarchitected.types.recommendation_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.state required")
    if data.get("updateReason") is not None:
        out["update_reason"] = data["updateReason"]
    if data.get("impact") is not None:
        import capo_wellarchitected.types.impact_category

        out["impact"] = capo_wellarchitected.types.impact_category.deserialize_json(
            data["impact"]
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.impact required")
    if data.get("roi") is not None:
        import capo_wellarchitected.types.roi

        out["roi"] = capo_wellarchitected.types.roi.deserialize_json(data["roi"])
    else:
        raise DeserializationError("GetAgentRecommendationResponse.roi required")
    if data.get("numberOfResources") is not None:
        out["number_of_resources"] = data["numberOfResources"]
    if data.get("awsServices") is not None:
        import capo_wellarchitected.types.string_list

        out["aws_services"] = capo_wellarchitected.types.string_list.deserialize_json(
            data["awsServices"]
        )
    if data.get("businessUnits") is not None:
        import capo_wellarchitected.types.string_list

        out["business_units"] = capo_wellarchitected.types.string_list.deserialize_json(
            data["businessUnits"]
        )
    if data.get("applications") is not None:
        import capo_wellarchitected.types.string_list

        out["applications"] = capo_wellarchitected.types.string_list.deserialize_json(
            data["applications"]
        )
    if data.get("impactDetails") is not None:
        import capo_wellarchitected.types.impact_details

        out["impact_details"] = (
            capo_wellarchitected.types.impact_details.deserialize_json(
                data["impactDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetAgentRecommendationResponse.impact_details required"
        )
    if data.get("insights") is not None:
        import capo_wellarchitected.types.insight_list

        out["insights"] = capo_wellarchitected.types.insight_list.deserialize_json(
            data["insights"]
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.insights required")
    if data.get("highlights") is not None:
        import capo_wellarchitected.types.highlights

        out["highlights"] = capo_wellarchitected.types.highlights.deserialize_json(
            data["highlights"]
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.highlights required")
    if data.get("remediationSummary") is not None:
        import capo_wellarchitected.types.remediation_summary

        out["remediation_summary"] = (
            capo_wellarchitected.types.remediation_summary.deserialize_json(
                data["remediationSummary"]
            )
        )
    else:
        raise DeserializationError(
            "GetAgentRecommendationResponse.remediation_summary required"
        )
    if data.get("crossPillarBenefits") is not None:
        import capo_wellarchitected.types.cross_pillar_benefits

        out["cross_pillar_benefits"] = (
            capo_wellarchitected.types.cross_pillar_benefits.deserialize_json(
                data["crossPillarBenefits"]
            )
        )
    if data.get("tradeOffs") is not None:
        import capo_wellarchitected.types.trade_offs

        out["trade_offs"] = capo_wellarchitected.types.trade_offs.deserialize_json(
            data["tradeOffs"]
        )
    if data.get("sources") is not None:
        import capo_wellarchitected.types.recommendation_source_list

        out["sources"] = (
            capo_wellarchitected.types.recommendation_source_list.deserialize_json(
                data["sources"]
            )
        )
    if data.get("goals") is not None:
        import capo_wellarchitected.types.recommendation_goals

        out["goals"] = capo_wellarchitected.types.recommendation_goals.deserialize_json(
            data["goals"]
        )
    if data.get("tags") is not None:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.deserialize_json(data["tags"])
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetAgentRecommendationResponse.created_by required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("GetAgentRecommendationResponse.created_at required")
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("lastModifiedAt") is not None:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromisoformat(
            data["lastModifiedAt"].replace("Z", "+00:00")
        )
    if data.get("remediations") is not None:
        import capo_wellarchitected.types.agent_recommendation_remediations

        out["remediations"] = (
            capo_wellarchitected.types.agent_recommendation_remediations.deserialize_json(
                data["remediations"]
            )
        )
    return out


def redact_sensitive(value: GetAgentRecommendationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "update_reason" in value:
        out["update_reason"] = "*** Sensitive Data Redacted ***"
    if "remediations" in value:
        import capo_wellarchitected.types.agent_recommendation_remediations

        out["remediations"] = (
            capo_wellarchitected.types.agent_recommendation_remediations.redact_sensitive(
                value["remediations"]
            )
        )
    return out
