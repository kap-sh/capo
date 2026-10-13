"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LifeCycleSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.closed_lost_reason
    import capo_partnercentral_selling.types.date
    import capo_partnercentral_selling.types.pii_string
    import capo_partnercentral_selling.types.review_status
    import capo_partnercentral_selling.types.stage


class LifeCycleSummary(TypedDict, closed=True):
    stage: NotRequired["capo_partnercentral_selling.types.stage.Stage"]
    """<p>Specifies the current stage of the <code>Opportunity</code>'s lifecycle as it maps to Amazon Web Services stages from the current stage in the partner CRM. This field provides a translated value of the stage, and offers insight into the <code>Opportunity</code>'s progression in the sales cycle, according to Amazon Web Services definitions.</p> <note> <p>A lead and a prospect must be further matured to a <code>Qualified</code> opportunity before submission. Opportunities that were closed/lost before submission aren't suitable for submission.</p> </note> <p>The descriptions of each sales stage are:</p> <ul> <li> <p>Prospect: Amazon Web Services identifies the opportunity. It can be active (Comes directly from the end customer through a lead) or latent (Your account team believes it exists based on research, account plans, sales plays).</p> </li> <li> <p>Qualified: Your account team engaged with the customer to discuss viability and understand requirements. The customer agreed that the opportunity is real, of interest, and may solve business/technical needs.</p> </li> <li> <p>Technical Validation: All parties understand the implementation plan.</p> </li> <li> <p>Business Validation: Pricing was proposed, and all parties agree to the steps to close.</p> </li> <li> <p>Committed: The customer signed the contract, but Amazon Web Services hasn't started billing.</p> </li> <li> <p>Launched: The workload is complete, and Amazon Web Services has started billing.</p> </li> <li> <p>Closed Lost: The opportunity is lost, and there are no steps to move forward.</p> </li> </ul>"""
    closed_lost_reason: NotRequired[
        "capo_partnercentral_selling.types.closed_lost_reason.ClosedLostReason"
    ]
    """<p>Specifies the reason code when an opportunity is marked as <i>Closed Lost</i>. When you select an appropriate reason code, you communicate the context for closing the <code>Opportunity</code>, and aid in accurate reports and analysis of opportunity outcomes.</p>"""
    next_steps: NotRequired["capo_partnercentral_selling.types.pii_string.PiiString"]
    """<p>Specifies the upcoming actions or tasks for the <code>Opportunity</code>. This field is utilized to communicate to Amazon Web Services the next actions required for the <code>Opportunity</code>.</p>"""
    target_close_date: NotRequired["capo_partnercentral_selling.types.date.Date"]
    """<p>Specifies the date when Amazon Web Services expects to start significant billing, when the project finishes, and when it moves into production. This field informs the Amazon Web Services seller about when the opportunity launches and starts to incur Amazon Web Services usage.</p> <p>Ensure the <code>Target Close Date</code> isn't in the past.</p>"""
    review_status: NotRequired[
        "capo_partnercentral_selling.types.review_status.ReviewStatus"
    ]
    """<p>Indicates the review status of a partner referred opportunity. This field is read-only and only applicable for partner referrals. Valid values:</p> <ul> <li> <p>Pending Submission: Not submitted for validation (editable).</p> </li> <li> <p>Submitted: Submitted for validation and not yet Amazon Web Services reviewed (read-only).</p> </li> <li> <p>In Review: Undergoing Amazon Web Services validation (read-only).</p> </li> <li> <p>Action Required: Address any issues Amazon Web Services highlights. Use the <code>UpdateOpportunity</code> API action to update the opportunity, and ensure you make all required changes. Only these fields are editable when the <code>Lifecycle.ReviewStatus</code> is <code>Action Required</code>:</p> <ul> <li> <p>Customer.Account.Address.City</p> </li> <li> <p>Customer.Account.Address.CountryCode</p> </li> <li> <p>Customer.Account.Address.PostalCode</p> </li> <li> <p>Customer.Account.Address.StateOrRegion</p> </li> <li> <p>Customer.Account.Address.StreetAddress</p> </li> <li> <p>Customer.Account.WebsiteUrl</p> </li> <li> <p>LifeCycle.TargetCloseDate</p> </li> <li> <p>Project.ExpectedCustomerSpend.Amount</p> </li> <li> <p>Project.ExpectedCustomerSpend.CurrencyCode</p> </li> <li> <p>Project.CustomerBusinessProblem</p> </li> <li> <p>PartnerOpportunityIdentifier</p> </li> </ul> <p>After updates, the opportunity re-enters the validation phase. This process repeats until all issues are resolved, and the opportunity's <code>Lifecycle.ReviewStatus</code> is set to <code>Approved</code> or <code>Rejected</code>.</p> </li> <li> <p>Approved: Validated and converted into the Amazon Web Services seller's pipeline (editable).</p> </li> <li> <p>Rejected: Disqualified (read-only).</p> </li> </ul>"""
    review_comments: NotRequired["str"]
    """<p>Indicates why an opportunity was sent back for further details. Partners must take corrective action based on the <code>ReviewComments</code>.</p>"""
    review_status_reason: NotRequired["str"]
    """<p>Indicates the reason a specific decision was taken during the opportunity review process. This field combines the reasons for both disqualified and action required statuses, and provides clarity for why an opportunity was disqualified or required further action.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifeCycleSummary) -> dict:
    out: dict = {}
    if "stage" in value:
        import capo_partnercentral_selling.types.stage

        out["Stage"] = capo_partnercentral_selling.types.stage.serialize_aws_json_1_0(
            value["stage"]
        )
    if "closed_lost_reason" in value:
        import capo_partnercentral_selling.types.closed_lost_reason

        out["ClosedLostReason"] = (
            capo_partnercentral_selling.types.closed_lost_reason.serialize_aws_json_1_0(
                value["closed_lost_reason"]
            )
        )
    if "next_steps" in value:
        out["NextSteps"] = value["next_steps"]
    if "target_close_date" in value:
        out["TargetCloseDate"] = value["target_close_date"]
    if "review_status" in value:
        import capo_partnercentral_selling.types.review_status

        out["ReviewStatus"] = (
            capo_partnercentral_selling.types.review_status.serialize_aws_json_1_0(
                value["review_status"]
            )
        )
    if "review_comments" in value:
        out["ReviewComments"] = value["review_comments"]
    if "review_status_reason" in value:
        out["ReviewStatusReason"] = value["review_status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LifeCycleSummary:
    out: LifeCycleSummary = {}  # type: ignore[typeddict-item]
    if data.get("Stage") is not None:
        import capo_partnercentral_selling.types.stage

        out["stage"] = capo_partnercentral_selling.types.stage.deserialize_aws_json_1_0(
            data["Stage"]
        )
    if data.get("ClosedLostReason") is not None:
        import capo_partnercentral_selling.types.closed_lost_reason

        out["closed_lost_reason"] = (
            capo_partnercentral_selling.types.closed_lost_reason.deserialize_aws_json_1_0(
                data["ClosedLostReason"]
            )
        )
    if data.get("NextSteps") is not None:
        out["next_steps"] = data["NextSteps"]
    if data.get("TargetCloseDate") is not None:
        out["target_close_date"] = data["TargetCloseDate"]
    if data.get("ReviewStatus") is not None:
        import capo_partnercentral_selling.types.review_status

        out["review_status"] = (
            capo_partnercentral_selling.types.review_status.deserialize_aws_json_1_0(
                data["ReviewStatus"]
            )
        )
    if data.get("ReviewComments") is not None:
        out["review_comments"] = data["ReviewComments"]
    if data.get("ReviewStatusReason") is not None:
        out["review_status_reason"] = data["ReviewStatusReason"]
    return out


def redact_sensitive(value: LifeCycleSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_steps" in value:
        out["next_steps"] = "*** Sensitive Data Redacted ***"
    return out
