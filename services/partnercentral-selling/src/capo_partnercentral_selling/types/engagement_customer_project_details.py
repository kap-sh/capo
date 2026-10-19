"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementCustomerProjectDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_customer_business_problem
    import capo_partnercentral_selling.types.engagement_customer_project_title


class EngagementCustomerProjectDetails(TypedDict, closed=True):
    title: "capo_partnercentral_selling.types.engagement_customer_project_title.EngagementCustomerProjectTitle"
    """<p>The title of the project.</p>"""
    business_problem: "capo_partnercentral_selling.types.engagement_customer_business_problem.EngagementCustomerBusinessProblem"
    """<p>A description of the business problem the project aims to solve.</p>"""
    target_completion_date: "str"
    """<p>The target completion date for the customer's project.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementCustomerProjectDetails) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    out["BusinessProblem"] = value["business_problem"]
    out["TargetCompletionDate"] = value["target_completion_date"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementCustomerProjectDetails:
    out: EngagementCustomerProjectDetails = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("BusinessProblem") is not None:
        out["business_problem"] = data["BusinessProblem"]
    else:
        out["business_problem"] = ""
    if data.get("TargetCompletionDate") is not None:
        out["target_completion_date"] = data["TargetCompletionDate"]
    else:
        out["target_completion_date"] = ""
    return out


def redact_sensitive(value: EngagementCustomerProjectDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "business_problem" in value:
        out["business_problem"] = "*** Sensitive Data Redacted ***"
    return out
