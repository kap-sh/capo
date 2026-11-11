"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#DescribeAgreementOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.acceptor
    import capo_marketplace_agreement.types.agreement_status
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.end_time_behavior
    import capo_marketplace_agreement.types.estimated_charges
    import capo_marketplace_agreement.types.free_trial_summary
    import capo_marketplace_agreement.types.proposal_summary
    import capo_marketplace_agreement.types.proposer
    import capo_marketplace_agreement.types.resource_id
    import capo_marketplace_agreement.types.timestamp


class DescribeAgreementOutput(TypedDict, closed=True):
    agreement_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the agreement.</p>"""
    acceptor: NotRequired["capo_marketplace_agreement.types.acceptor.Acceptor"]
    """<p>The details of the party accepting the agreement terms. This is commonly the buyer for <code>PurchaseAgreement</code>.</p>"""
    proposer: NotRequired["capo_marketplace_agreement.types.proposer.Proposer"]
    """<p>The details of the party proposing the agreement terms. This is commonly the seller for <code>PurchaseAgreement</code>.</p>"""
    start_time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the agreement starts.</p>"""
    end_time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the agreement ends. The field is <code>null</code> for pay-as-you-go agreements, which don’t have end dates.</p>"""
    acceptance_time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time the offer was accepted or the agreement was created.</p> <note> <p> <code>AcceptanceTime</code> and <code>StartTime</code> can differ for future dated agreements (FDAs).</p> </note>"""
    agreement_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>The type of agreement. Values are <code>PurchaseAgreement</code> or <code>VendorInsightsAgreement</code>.</p>"""
    estimated_charges: NotRequired[
        "capo_marketplace_agreement.types.estimated_charges.EstimatedCharges"
    ]
    """<p>The estimated cost of the agreement.</p>"""
    proposal_summary: NotRequired[
        "capo_marketplace_agreement.types.proposal_summary.ProposalSummary"
    ]
    """<p>A summary of the proposal received from the proposer.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_status.AgreementStatus"
    ]
    """<p>The current status of the agreement.</p> <p>Statuses include:</p> <ul> <li> <p> <code>ACTIVE</code> – The terms of the agreement are active.</p> </li> <li> <p> <code>CANCELLED</code> – The acceptor ended the agreement before the defined end date.</p> </li> <li> <p> <code>EXPIRED</code> – The agreement ended on the defined end date.</p> </li> <li> <p> <code>RENEWED</code> – The agreement was renewed into a new agreement (for example, an auto-renewal).</p> </li> <li> <p> <code>REPLACED</code> – The agreement was replaced using an agreement replacement offer.</p> </li> <li> <p> <code>TERMINATED</code> – The agreement ended before the defined end date because of an AWS termination (for example, a payment failure).</p> </li> </ul>"""
    initial_agreement_id: NotRequired[
        "capo_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the very first agreement in a chain of related agreements, such as renewals or replacements. It stays the same across all agreements in that chain, which lets you trace an agreement back to the original. When an agreement isn't derived from another agreement, its <code>InitialAgreementId</code> is its own <code>AgreementId</code>.</p>"""
    end_time_behavior: NotRequired[
        "capo_marketplace_agreement.types.end_time_behavior.EndTimeBehavior"
    ]
    """<p>The behavior of the agreement when it reaches its end date. For example, whether the agreement renews, and if it doesn't, the reason why.</p> <p>This field is present for every active agreement that has an end date. It is not present for an agreement that has no end date, because such an agreement never reaches an end time. Pay-as-you-go agreements are the most common example. It is also not present for an agreement that is no longer active.</p>"""
    free_trial_summary: NotRequired[
        "capo_marketplace_agreement.types.free_trial_summary.FreeTrialSummary"
    ]
    """<p>The free trial details of the agreement. This field is present only when the agreement includes a free trial.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAgreementOutput) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "acceptor" in value:
        import capo_marketplace_agreement.types.acceptor

        out["acceptor"] = (
            capo_marketplace_agreement.types.acceptor.serialize_aws_json_1_0(
                value["acceptor"]
            )
        )
    if "proposer" in value:
        import capo_marketplace_agreement.types.proposer

        out["proposer"] = (
            capo_marketplace_agreement.types.proposer.serialize_aws_json_1_0(
                value["proposer"]
            )
        )
    if "start_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["startTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["endTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    if "acceptance_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["acceptanceTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["acceptance_time"]
            )
        )
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "estimated_charges" in value:
        import capo_marketplace_agreement.types.estimated_charges

        out["estimatedCharges"] = (
            capo_marketplace_agreement.types.estimated_charges.serialize_aws_json_1_0(
                value["estimated_charges"]
            )
        )
    if "proposal_summary" in value:
        import capo_marketplace_agreement.types.proposal_summary

        out["proposalSummary"] = (
            capo_marketplace_agreement.types.proposal_summary.serialize_aws_json_1_0(
                value["proposal_summary"]
            )
        )
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "initial_agreement_id" in value:
        out["initialAgreementId"] = value["initial_agreement_id"]
    if "end_time_behavior" in value:
        import capo_marketplace_agreement.types.end_time_behavior

        out["endTimeBehavior"] = (
            capo_marketplace_agreement.types.end_time_behavior.serialize_aws_json_1_0(
                value["end_time_behavior"]
            )
        )
    if "free_trial_summary" in value:
        import capo_marketplace_agreement.types.free_trial_summary

        out["freeTrialSummary"] = (
            capo_marketplace_agreement.types.free_trial_summary.serialize_aws_json_1_0(
                value["free_trial_summary"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAgreementOutput:
    out: DescribeAgreementOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("acceptor") is not None:
        import capo_marketplace_agreement.types.acceptor

        out["acceptor"] = (
            capo_marketplace_agreement.types.acceptor.deserialize_aws_json_1_0(
                data["acceptor"]
            )
        )
    if data.get("proposer") is not None:
        import capo_marketplace_agreement.types.proposer

        out["proposer"] = (
            capo_marketplace_agreement.types.proposer.deserialize_aws_json_1_0(
                data["proposer"]
            )
        )
    if data.get("startTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["start_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["end_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    if data.get("acceptanceTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["acceptance_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["acceptanceTime"]
            )
        )
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("estimatedCharges") is not None:
        import capo_marketplace_agreement.types.estimated_charges

        out["estimated_charges"] = (
            capo_marketplace_agreement.types.estimated_charges.deserialize_aws_json_1_0(
                data["estimatedCharges"]
            )
        )
    if data.get("proposalSummary") is not None:
        import capo_marketplace_agreement.types.proposal_summary

        out["proposal_summary"] = (
            capo_marketplace_agreement.types.proposal_summary.deserialize_aws_json_1_0(
                data["proposalSummary"]
            )
        )
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("initialAgreementId") is not None:
        out["initial_agreement_id"] = data["initialAgreementId"]
    if data.get("endTimeBehavior") is not None:
        import capo_marketplace_agreement.types.end_time_behavior

        out["end_time_behavior"] = (
            capo_marketplace_agreement.types.end_time_behavior.deserialize_aws_json_1_0(
                data["endTimeBehavior"]
            )
        )
    if data.get("freeTrialSummary") is not None:
        import capo_marketplace_agreement.types.free_trial_summary

        out["free_trial_summary"] = (
            capo_marketplace_agreement.types.free_trial_summary.deserialize_aws_json_1_0(
                data["freeTrialSummary"]
            )
        )
    return out
