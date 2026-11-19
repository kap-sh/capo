"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#StartAgreementApprovalsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_summaries


class StartAgreementApprovalsOutput(TypedDict, closed=True):
    approval_summaries: "capo_marketplace_agreement.types.agreement_approval_summaries.AgreementApprovalSummaries"
    """<p>An array of <code>AgreementApprovalSummary</code> objects, one for each agreement approval that was started.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartAgreementApprovalsOutput) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_approval_summaries

    out["approvalSummaries"] = (
        capo_marketplace_agreement.types.agreement_approval_summaries.serialize_aws_json_1_0(
            value["approval_summaries"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartAgreementApprovalsOutput:
    out: StartAgreementApprovalsOutput = {}  # type: ignore[typeddict-item]
    if data.get("approvalSummaries") is not None:
        import capo_marketplace_agreement.types.agreement_approval_summaries

        out["approval_summaries"] = (
            capo_marketplace_agreement.types.agreement_approval_summaries.deserialize_aws_json_1_0(
                data["approvalSummaries"]
            )
        )
    else:
        out["approval_summaries"] = []
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartAgreementApprovalsOutput) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_approval_summaries

    out["approvalSummaries"] = (
        capo_marketplace_agreement.types.agreement_approval_summaries.serialize_cbor(
            value["approval_summaries"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> StartAgreementApprovalsOutput:
    out: StartAgreementApprovalsOutput = {}  # type: ignore[typeddict-item]
    if data.get("approvalSummaries") is not None:
        import capo_marketplace_agreement.types.agreement_approval_summaries

        out["approval_summaries"] = (
            capo_marketplace_agreement.types.agreement_approval_summaries.deserialize_cbor(
                data["approvalSummaries"]
            )
        )
    else:
        out["approval_summaries"] = []
    return out
