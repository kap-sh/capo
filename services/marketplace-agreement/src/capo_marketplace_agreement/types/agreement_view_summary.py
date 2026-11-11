"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementViewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.acceptor
    import capo_marketplace_agreement.types.agreement_status
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.end_time_behavior_reason_code
    import capo_marketplace_agreement.types.end_time_behavior_type
    import capo_marketplace_agreement.types.entitlement_list
    import capo_marketplace_agreement.types.proposal_summary
    import capo_marketplace_agreement.types.proposer
    import capo_marketplace_agreement.types.resource_id
    import capo_marketplace_agreement.types.timestamp


class AgreementViewSummary(TypedDict, closed=True):
    agreement_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the agreement.</p>"""
    acceptance_time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time that the agreement was accepted.</p>"""
    start_time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the agreement starts.</p>"""
    end_time: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the agreement ends. The field is <code>null</code> for pay-as-you-go agreements, which don’t have end dates.</p>"""
    last_update_time: NotRequired[
        "capo_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the agreement was last updated. An agreement is updated when any of its attributes or accepted terms change. Amendments, renewals, and a party changing whether the agreement renews are all examples.</p> <p>Use the <code>BeforeLastUpdateTime</code> and <code>AfterLastUpdateTime</code> filters to search on this value, and <code>LastUpdateTime</code> as the <code>SortBy</code> value to sort by it. Sorting by <code>LastUpdateTime</code> is supported only when <code>PartyType</code> is <code>Proposer</code>.</p>"""
    agreement_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>The type of agreement.</p>"""
    acceptor: NotRequired["capo_marketplace_agreement.types.acceptor.Acceptor"]
    """<p>Details of the party accepting the agreement terms. This is commonly the buyer for <code>PurchaseAgreement.</code> </p>"""
    proposer: NotRequired["capo_marketplace_agreement.types.proposer.Proposer"]
    """<p>Details of the party proposing the agreement terms, most commonly the seller for <code>PurchaseAgreement</code>.</p>"""
    proposal_summary: NotRequired[
        "capo_marketplace_agreement.types.proposal_summary.ProposalSummary"
    ]
    """<p>A summary of the proposal</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_status.AgreementStatus"
    ]
    """<p>The current status of the agreement. </p>"""
    entitlements: NotRequired[
        "capo_marketplace_agreement.types.entitlement_list.EntitlementList"
    ]
    """<p>A list of entitlements associated with the agreement.</p>"""
    initial_agreement_id: NotRequired[
        "capo_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the very first agreement in a chain of related agreements, such as renewals or replacements. It stays the same across all agreements in that chain, which lets you trace an agreement back to the original. You can also use it as the <code>InitialAgreementId</code> filter value to return every agreement in the same chain.</p>"""
    end_time_behavior_type: NotRequired[
        "capo_marketplace_agreement.types.end_time_behavior_type.EndTimeBehaviorType"
    ]
    """<p>The behavior of the agreement when it reaches its end date. The field is <code>null</code> for agreements that have no end date, because those agreements never reach an end time.</p> <p>Types include:</p> <ul> <li> <p> <code>RENEW</code> – A new agreement is created from the accepted terms of this agreement.</p> </li> <li> <p> <code>REPLACE</code> – A new agreement is created from a different offer than the one this agreement was created from. This happens, for example, when a private offer reaches its end date and the acceptor transitions to the public offer for the product.</p> </li> <li> <p> <code>EXPIRE</code> – The agreement ends and isn't renewed or replaced.</p> </li> </ul>"""
    end_time_behavior_reason_code: NotRequired[
        "capo_marketplace_agreement.types.end_time_behavior_reason_code.EndTimeBehaviorReasonCode"
    ]
    """<p>The reason why the agreement doesn't renew at its end date. The field is <code>null</code> when the agreement renews.</p> <p>More than one reason can apply to the same agreement. When that happens, the operation returns only one reason code, and <code>PROPOSER_RENEW_OPTED_OUT</code> takes precedence over all others.</p> <p>The <code>EnableAutoRenew</code> field reflects only the acceptor's preference, and doesn't reflect the other reasons an agreement might not renew.</p> <p>Reason codes include:</p> <ul> <li> <p> <code>PROPOSER_RENEW_OPTED_OUT</code> – The proposer opted out of renewing the agreement.</p> </li> <li> <p> <code>ACCEPTOR_RENEW_OPTED_OUT</code> – The acceptor opted out of renewing the agreement.</p> </li> <li> <p> <code>NO_RENEWAL_TERM</code> – The accepted terms of the agreement don't include a renewal term, which is required for an agreement to renew.</p> </li> <li> <p> <code>RENEWAL_LIMIT_EXHAUSTED</code> – The agreement reached the maximum number of renewals allowed by its renewal term.</p> </li> </ul>"""
    free_trial_end_time: NotRequired[
        "capo_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the free trial of the agreement ends. This field is present only when the agreement includes a free trial.</p> <p>For an agreement that includes both a free trial and usage-based pricing, the agreement converts to paid usage at this time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementViewSummary) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "acceptance_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["acceptanceTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["acceptance_time"]
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
    if "last_update_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["lastUpdateTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["last_update_time"]
            )
        )
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
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
    if "entitlements" in value:
        import capo_marketplace_agreement.types.entitlement_list

        out["entitlements"] = (
            capo_marketplace_agreement.types.entitlement_list.serialize_aws_json_1_0(
                value["entitlements"]
            )
        )
    if "initial_agreement_id" in value:
        out["initialAgreementId"] = value["initial_agreement_id"]
    if "end_time_behavior_type" in value:
        import capo_marketplace_agreement.types.end_time_behavior_type

        out["endTimeBehaviorType"] = (
            capo_marketplace_agreement.types.end_time_behavior_type.serialize_aws_json_1_0(
                value["end_time_behavior_type"]
            )
        )
    if "end_time_behavior_reason_code" in value:
        import capo_marketplace_agreement.types.end_time_behavior_reason_code

        out["endTimeBehaviorReasonCode"] = (
            capo_marketplace_agreement.types.end_time_behavior_reason_code.serialize_aws_json_1_0(
                value["end_time_behavior_reason_code"]
            )
        )
    if "free_trial_end_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["freeTrialEndTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["free_trial_end_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementViewSummary:
    out: AgreementViewSummary = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("acceptanceTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["acceptance_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["acceptanceTime"]
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
    if data.get("lastUpdateTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["last_update_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["lastUpdateTime"]
            )
        )
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
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
    if data.get("entitlements") is not None:
        import capo_marketplace_agreement.types.entitlement_list

        out["entitlements"] = (
            capo_marketplace_agreement.types.entitlement_list.deserialize_aws_json_1_0(
                data["entitlements"]
            )
        )
    if data.get("initialAgreementId") is not None:
        out["initial_agreement_id"] = data["initialAgreementId"]
    if data.get("endTimeBehaviorType") is not None:
        import capo_marketplace_agreement.types.end_time_behavior_type

        out["end_time_behavior_type"] = (
            capo_marketplace_agreement.types.end_time_behavior_type.deserialize_aws_json_1_0(
                data["endTimeBehaviorType"]
            )
        )
    if data.get("endTimeBehaviorReasonCode") is not None:
        import capo_marketplace_agreement.types.end_time_behavior_reason_code

        out["end_time_behavior_reason_code"] = (
            capo_marketplace_agreement.types.end_time_behavior_reason_code.deserialize_aws_json_1_0(
                data["endTimeBehaviorReasonCode"]
            )
        )
    if data.get("freeTrialEndTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["free_trial_end_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["freeTrialEndTime"]
            )
        )
    return out
