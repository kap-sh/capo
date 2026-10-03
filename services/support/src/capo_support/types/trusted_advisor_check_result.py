"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorCheckResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_support.errors import DeserializationError

if TYPE_CHECKING:
    import capo_support.types.string
    import capo_support.types.trusted_advisor_category_specific_summary
    import capo_support.types.trusted_advisor_resource_detail_list
    import capo_support.types.trusted_advisor_resources_summary


class TrustedAdvisorCheckResult(TypedDict, closed=True):
    check_id: "capo_support.types.string.String"
    """<p>The unique identifier for the Trusted Advisor check.</p>"""
    timestamp: "capo_support.types.string.String"
    """<p>The time of the last refresh of the check.</p>"""
    status: "capo_support.types.string.String"
    """<p>The alert status of the check: "ok" (green), "warning" (yellow), "error" (red), or "not_available".</p>"""
    resources_summary: "capo_support.types.trusted_advisor_resources_summary.TrustedAdvisorResourcesSummary"
    category_specific_summary: "capo_support.types.trusted_advisor_category_specific_summary.TrustedAdvisorCategorySpecificSummary"
    """<p>Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.</p>"""
    flagged_resources: "capo_support.types.trusted_advisor_resource_detail_list.TrustedAdvisorResourceDetailList"
    """<p>The details about each resource listed in the check result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorCheckResult) -> dict:
    out: dict = {}
    out["checkId"] = value["check_id"]
    out["timestamp"] = value["timestamp"]
    out["status"] = value["status"]
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
    import capo_support.types.trusted_advisor_resource_detail_list

    out["flaggedResources"] = (
        capo_support.types.trusted_advisor_resource_detail_list.serialize_aws_json_1_1(
            value["flagged_resources"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorCheckResult:
    out: TrustedAdvisorCheckResult = {}  # type: ignore[typeddict-item]
    if data.get("checkId") is not None:
        out["check_id"] = data["checkId"]
    else:
        raise DeserializationError("TrustedAdvisorCheckResult.check_id required")
    if data.get("timestamp") is not None:
        out["timestamp"] = data["timestamp"]
    else:
        raise DeserializationError("TrustedAdvisorCheckResult.timestamp required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("TrustedAdvisorCheckResult.status required")
    if data.get("resourcesSummary") is not None:
        import capo_support.types.trusted_advisor_resources_summary

        out["resources_summary"] = (
            capo_support.types.trusted_advisor_resources_summary.deserialize_aws_json_1_1(
                data["resourcesSummary"]
            )
        )
    else:
        raise DeserializationError(
            "TrustedAdvisorCheckResult.resources_summary required"
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
            "TrustedAdvisorCheckResult.category_specific_summary required"
        )
    if data.get("flaggedResources") is not None:
        import capo_support.types.trusted_advisor_resource_detail_list

        out["flagged_resources"] = (
            capo_support.types.trusted_advisor_resource_detail_list.deserialize_aws_json_1_1(
                data["flaggedResources"]
            )
        )
    else:
        raise DeserializationError(
            "TrustedAdvisorCheckResult.flagged_resources required"
        )
    return out
