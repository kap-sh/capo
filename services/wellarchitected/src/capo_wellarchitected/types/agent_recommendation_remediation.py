"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AgentRecommendationRemediation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.recommendation_arn
    import capo_wellarchitected.types.remediation_steps
    import capo_wellarchitected.types.remediation_type
    import capo_wellarchitected.types.resource_links


class AgentRecommendationRemediation(TypedDict, closed=True):
    recommendation_arn: (
        "capo_wellarchitected.types.recommendation_arn.RecommendationArn"
    )
    """<p>The ARN of the recommendation that this remediation belongs to.</p>"""
    type: "capo_wellarchitected.types.remediation_type.RemediationType"
    """<p>The remediation method.</p>"""
    steps: "capo_wellarchitected.types.remediation_steps.RemediationSteps"
    """<p>The procedural steps to perform the remediation.</p>"""
    resource_links: NotRequired[
        "capo_wellarchitected.types.resource_links.ResourceLinks"
    ]
    """<p>External references associated with the steps.</p>"""
    created_by: "str"
    """<p>The identifier of the user or system that created this remediation.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the remediation was created.</p>"""
    last_modified_by: NotRequired["str"]
    """<p>The identifier of the user or system that last modified this remediation.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the remediation was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentRecommendationRemediation) -> dict:
    out: dict = {}
    out["recommendationArn"] = value["recommendation_arn"]
    import capo_wellarchitected.types.remediation_type

    out["type"] = capo_wellarchitected.types.remediation_type.serialize_json(
        value["type"]
    )
    import capo_wellarchitected.types.remediation_steps

    out["steps"] = capo_wellarchitected.types.remediation_steps.serialize_json(
        value["steps"]
    )
    if "resource_links" in value:
        import capo_wellarchitected.types.resource_links

        out["resourceLinks"] = capo_wellarchitected.types.resource_links.serialize_json(
            value["resource_links"]
        )
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
    return out


def deserialize_json(data: dict) -> AgentRecommendationRemediation:
    out: AgentRecommendationRemediation = {}  # type: ignore[typeddict-item]
    if data.get("recommendationArn") is not None:
        out["recommendation_arn"] = data["recommendationArn"]
    else:
        out["recommendation_arn"] = ""
    if data.get("type") is not None:
        import capo_wellarchitected.types.remediation_type

        out["type"] = capo_wellarchitected.types.remediation_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_wellarchitected.types.remediation_type.RemediationType", ""
        )
    if data.get("steps") is not None:
        import capo_wellarchitected.types.remediation_steps

        out["steps"] = capo_wellarchitected.types.remediation_steps.deserialize_json(
            data["steps"]
        )
    else:
        out["steps"] = []
    if data.get("resourceLinks") is not None:
        import capo_wellarchitected.types.resource_links

        out["resource_links"] = (
            capo_wellarchitected.types.resource_links.deserialize_json(
                data["resourceLinks"]
            )
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("lastModifiedAt") is not None:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromisoformat(
            data["lastModifiedAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: AgentRecommendationRemediation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "steps" in value:
        import capo_wellarchitected.types.remediation_steps

        out["steps"] = capo_wellarchitected.types.remediation_steps.redact_sensitive(
            value["steps"]
        )
    return out
