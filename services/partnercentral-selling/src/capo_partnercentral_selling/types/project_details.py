"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProjectDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.date
    import capo_partnercentral_selling.types.engagement_customer_business_problem
    import capo_partnercentral_selling.types.expected_customer_spend_list


class ProjectDetails(TypedDict, closed=True):
    business_problem: "capo_partnercentral_selling.types.engagement_customer_business_problem.EngagementCustomerBusinessProblem"
    """<p>Describes the business problem that the project aims to solve. This information is crucial for understanding the project’s goals and objectives.</p>"""
    title: "str"
    """<p>Specifies the title of the project. This title helps partners quickly identify and understand the focus of the project.</p>"""
    target_completion_date: "capo_partnercentral_selling.types.date.Date"
    """<p>Specifies the estimated date of project completion. This field helps track the project timeline and manage expectations.</p>"""
    expected_customer_spend: "capo_partnercentral_selling.types.expected_customer_spend_list.ExpectedCustomerSpendList"
    """<p>Contains revenue estimates for the partner related to the project. This field provides an idea of the financial potential of the opportunity for the partner.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProjectDetails) -> dict:
    out: dict = {}
    out["BusinessProblem"] = value["business_problem"]
    out["Title"] = value["title"]
    out["TargetCompletionDate"] = value["target_completion_date"]
    import capo_partnercentral_selling.types.expected_customer_spend_list

    out["ExpectedCustomerSpend"] = (
        capo_partnercentral_selling.types.expected_customer_spend_list.serialize_aws_json_1_0(
            value["expected_customer_spend"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProjectDetails:
    out: ProjectDetails = {}  # type: ignore[typeddict-item]
    if data.get("BusinessProblem") is not None:
        out["business_problem"] = data["BusinessProblem"]
    else:
        raise DeserializationError("ProjectDetails.business_problem required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("ProjectDetails.title required")
    if data.get("TargetCompletionDate") is not None:
        out["target_completion_date"] = data["TargetCompletionDate"]
    else:
        raise DeserializationError("ProjectDetails.target_completion_date required")
    if data.get("ExpectedCustomerSpend") is not None:
        import capo_partnercentral_selling.types.expected_customer_spend_list

        out["expected_customer_spend"] = (
            capo_partnercentral_selling.types.expected_customer_spend_list.deserialize_aws_json_1_0(
                data["ExpectedCustomerSpend"]
            )
        )
    else:
        raise DeserializationError("ProjectDetails.expected_customer_spend required")
    return out


def redact_sensitive(value: ProjectDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "business_problem" in value:
        out["business_problem"] = "*** Sensitive Data Redacted ***"
    if "expected_customer_spend" in value:
        import capo_partnercentral_selling.types.expected_customer_spend_list

        out["expected_customer_spend"] = (
            capo_partnercentral_selling.types.expected_customer_spend_list.redact_sensitive(
                value["expected_customer_spend"]
            )
        )
    return out
