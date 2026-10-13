"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LifeCycle``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.closed_lost_reason
    import capo_partnercentral_selling.types.date
    import capo_partnercentral_selling.types.next_steps_histories
    import capo_partnercentral_selling.types.pii_string
    import capo_partnercentral_selling.types.review_status
    import capo_partnercentral_selling.types.stage


class LifeCycle(TypedDict, closed=True):
    stage: NotRequired["capo_partnercentral_selling.types.stage.Stage"]
    """<p>Specifies the current stage of the <code>Opportunity</code>'s lifecycle as it maps to Amazon Web Services stages from the current stage in the partner CRM. This field provides a translated value of the stage, and offers insight into the <code>Opportunity</code>'s progression in the sales cycle, according to Amazon Web Services definitions.</p> <note> <p>A lead and a prospect must be further matured to a <code>Qualified</code> opportunity before submission. Opportunities that were closed/lost before submission aren't suitable for submission.</p> </note> <p>The descriptions of each sales stage are:</p> <ul> <li> <p>Prospect: Amazon Web Services identifies the opportunity. It can be active (Comes directly from the end customer through a lead) or latent (Your account team believes it exists based on research, account plans, sales plays).</p> </li> <li> <p>Qualified: Your account team engaged with the customer to discuss viability and requirements. The customer agreed that the opportunity is real, of interest, and may solve business/technical needs.</p> </li> <li> <p>Technical Validation: All parties understand the implementation plan.</p> </li> <li> <p>Business Validation: Pricing was proposed, and all parties agree to the steps to close.</p> </li> <li> <p>Committed: The customer signed the contract, but Amazon Web Services hasn't started billing.</p> </li> <li> <p>Launched: The workload is complete, and Amazon Web Services has started billing.</p> </li> <li> <p>Closed Lost: The opportunity is lost, and there are no steps to move forward.</p> </li> </ul>"""
    closed_lost_reason: NotRequired[
        "capo_partnercentral_selling.types.closed_lost_reason.ClosedLostReason"
    ]
    """<p>Specifies the reason code when an opportunity is marked as <i>Closed Lost</i>. When you select an appropriate reason code, you communicate the context for closing the <code>Opportunity</code>, and aid in accurate reports and analysis of opportunity outcomes. The possible values are:</p> <ul> <li> <p>Customer Deficiency: The customer lacked necessary resources or capabilities.</p> </li> <li> <p>Delay/Cancellation of Project: The project was delayed or canceled.</p> </li> <li> <p>Legal/Tax/Regulatory: Legal, tax, or regulatory issues prevented progress.</p> </li> <li> <p>Lost to Competitor—Google: The opportunity was lost to Google.</p> </li> <li> <p>Lost to Competitor—Microsoft: The opportunity was lost to Microsoft.</p> </li> <li> <p>Lost to Competitor—SoftLayer: The opportunity was lost to SoftLayer.</p> </li> <li> <p>Lost to Competitor—VMWare: The opportunity was lost to VMWare.</p> </li> <li> <p>Lost to Competitor—Other: The opportunity was lost to a competitor not listed above.</p> </li> <li> <p>No Opportunity: There was no opportunity to pursue.</p> </li> <li> <p>On Premises Deployment: The customer chose an on-premises solution.</p> </li> <li> <p>Partner Gap: The partner lacked necessary resources or capabilities.</p> </li> <li> <p>Price: The price was not competitive or acceptable to the customer.</p> </li> <li> <p>Security/Compliance: Security or compliance issues prevented progress.</p> </li> <li> <p>Technical Limitations: Technical limitations prevented progress.</p> </li> <li> <p>Customer Experience: Issues related to the customer's experience impacted the decision.</p> </li> <li> <p>Other: Any reason not covered by the other values.</p> </li> <li> <p>People/Relationship/Governance: Issues related to people, relationships, or governance.</p> </li> <li> <p>Product/Technology: Issues related to the product or technology.</p> </li> <li> <p>Financial/Commercial: Financial or commercial issues impacted the decision.</p> </li> </ul>"""
    next_steps: NotRequired["capo_partnercentral_selling.types.pii_string.PiiString"]
    """<p>Specifies the upcoming actions or tasks for the <code>Opportunity</code>. Use this field to communicate with Amazon Web Services about the next actions required for the <code>Opportunity</code>.</p>"""
    target_close_date: NotRequired["capo_partnercentral_selling.types.date.Date"]
    """<p>Specifies the date when Amazon Web Services expects to start significant billing, when the project finishes, and when it moves into production. This field informs the Amazon Web Services seller about when the opportunity launches and starts to incur Amazon Web Services usage.</p> <p>Ensure the <code>Target Close Date</code> isn't in the past.</p>"""
    review_status: NotRequired[
        "capo_partnercentral_selling.types.review_status.ReviewStatus"
    ]
    """<p>Indicates the review status of an opportunity referred by a partner. This field is read-only and only applicable for partner referrals. The possible values are:</p> <ul> <li> <p>Pending Submission: Not submitted for validation (editable).</p> </li> <li> <p>Submitted: Submitted for validation, and Amazon Web Services hasn't reviewed it (read-only).</p> </li> <li> <p>In Review: Amazon Web Services is validating (read-only).</p> </li> <li> <p>Action Required: Issues that Amazon Web Services highlights need to be addressed. Partners should use the <code>UpdateOpportunity</code> API action to update the opportunity and helps to ensure that all required changes are made. Only the following fields are editable when the <code>Lifecycle.ReviewStatus</code> is <code>Action Required</code>:</p> <ul> <li> <p>Customer.Account.Address.City</p> </li> <li> <p>Customer.Account.Address.CountryCode</p> </li> <li> <p>Customer.Account.Address.PostalCode</p> </li> <li> <p>Customer.Account.Address.StateOrRegion</p> </li> <li> <p>Customer.Account.Address.StreetAddress</p> </li> <li> <p>Customer.Account.WebsiteUrl</p> </li> <li> <p>LifeCycle.TargetCloseDate</p> </li> <li> <p>Project.ExpectedMonthlyAWSRevenue.Amount</p> </li> <li> <p>Project.ExpectedMonthlyAWSRevenue.CurrencyCode</p> </li> <li> <p>Project.CustomerBusinessProblem</p> </li> <li> <p>PartnerOpportunityIdentifier</p> </li> </ul> <p>After updates, the opportunity re-enters the validation phase. This process repeats until all issues are resolved, and the opportunity's <code>Lifecycle.ReviewStatus</code> is set to <code>Approved</code> or <code>Rejected</code>.</p> </li> <li> <p>Approved: Validated and converted into the Amazon Web Services seller's pipeline (editable).</p> </li> <li> <p>Rejected: Disqualified (read-only).</p> </li> </ul>"""
    review_comments: NotRequired["str"]
    """<p>Contains detailed feedback from Amazon Web Services when requesting additional information from partners. Provides specific guidance on what partners need to provide or clarify for opportunity validation, complementing the <code>ReviewStatusReason</code> field.</p>"""
    review_status_reason: NotRequired["str"]
    """<p>Code indicating the validation decision during the Amazon Web Services opportunity review. Applies when status is <code>Rejected</code> or <code>Action Required</code>. Used to document validation results for AWS Partner Referrals and indicate when additional information is needed from partners as part of the APN Customer Engagement (ACE) program.</p>"""
    next_steps_history: NotRequired[
        "capo_partnercentral_selling.types.next_steps_histories.NextStepsHistories"
    ]
    """<p>Captures a chronological record of the next steps or actions planned or taken for the current opportunity, along with the timestamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LifeCycle) -> dict:
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
    if "next_steps_history" in value:
        import capo_partnercentral_selling.types.next_steps_histories

        out["NextStepsHistory"] = (
            capo_partnercentral_selling.types.next_steps_histories.serialize_aws_json_1_0(
                value["next_steps_history"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LifeCycle:
    out: LifeCycle = {}  # type: ignore[typeddict-item]
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
    if data.get("NextStepsHistory") is not None:
        import capo_partnercentral_selling.types.next_steps_histories

        out["next_steps_history"] = (
            capo_partnercentral_selling.types.next_steps_histories.deserialize_aws_json_1_0(
                data["NextStepsHistory"]
            )
        )
    return out


def redact_sensitive(value: LifeCycle) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_steps" in value:
        out["next_steps"] = "*** Sensitive Data Redacted ***"
    return out
