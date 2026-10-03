"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCheckSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_support.errors import DeserializationError

if TYPE_CHECKING:
    import capo_support.types.boolean
    import capo_support.types.string
    import capo_support.types.trusted_advisor_category_specific_summary
    import capo_support.types.trusted_advisor_resources_summary


class TrustedAdvisorCheckSummary(TypedDict, closed=True):
    check_id: "capo_support.types.string.String"
    """<p>The unique identifier for the Trusted Advisor check.</p>"""
    timestamp: "capo_support.types.string.String"
    """<p>The time of the last refresh of the check.</p>"""
    status: "capo_support.types.string.String"
    """<p>The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or "not_available".</p>"""
    has_flagged_resources: "capo_support.types.boolean.Boolean"
    """<p>Specifies whether the Trusted Advisor check has flagged resources.</p>"""
    resources_summary: "capo_support.types.trusted_advisor_resources_summary.TrustedAdvisorResourcesSummary"
    category_specific_summary: "capo_support.types.trusted_advisor_category_specific_summary.TrustedAdvisorCategorySpecificSummary"
    """<p>Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCheckSummary) -> dict:
    out: dict = {}
    out["checkId"] = value["check_id"]
    out["timestamp"] = value["timestamp"]
    out["status"] = value["status"]
    out["hasFlaggedResources"] = value.get("has_flagged_resources", False)
    import capo_support.types.trusted_advisor_resources_summary

    out["resourcesSummary"] = (
        capo_support.types.trusted_advisor_resources_summary.serialize_aws_json_1_1(
            value["resources_summary"]
        )
    )
    import capo_support.types.trusted_advisor_category_specific_summary

    out["categorySpecificSummary"] = (
        capo_support.types.trusted_advisor_category_specific_summary.serialize_aws_json_1_1(
            value["category_specific_summary"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorCheckSummary:
    out: TrustedAdvisorCheckSummary = {}  # type: ignore[typeddict-item]
    if data.get("checkId") is not None:
        out["check_id"] = data["checkId"]
    else:
        raise DeserializationError("TrustedAdvisorCheckSummary.check_id required")
    if data.get("timestamp") is not None:
        out["timestamp"] = data["timestamp"]
    else:
        raise DeserializationError("TrustedAdvisorCheckSummary.timestamp required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("TrustedAdvisorCheckSummary.status required")
    if data.get("hasFlaggedResources") is not None:
        out["has_flagged_resources"] = data["hasFlaggedResources"]
    else:
        out["has_flagged_resources"] = False
    if data.get("resourcesSummary") is not None:
        import capo_support.types.trusted_advisor_resources_summary

        out["resources_summary"] = (
            capo_support.types.trusted_advisor_resources_summary.deserialize_aws_json_1_1(
                data["resourcesSummary"]
            )
        )
    else:
        raise DeserializationError(
            "TrustedAdvisorCheckSummary.resources_summary required"
        )
    if data.get("categorySpecificSummary") is not None:
        import capo_support.types.trusted_advisor_category_specific_summary

        out["category_specific_summary"] = (
            capo_support.types.trusted_advisor_category_specific_summary.deserialize_aws_json_1_1(
                data["categorySpecificSummary"]
            )
        )
    else:
        raise DeserializationError(
            "TrustedAdvisorCheckSummary.category_specific_summary required"
        )
    return out
