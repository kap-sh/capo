"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementApprovalsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_summaries
    import capo_marketplace_agreement.types.next_token


class ListAgreementApprovalsOutput(TypedDict, closed=True):
    items: "capo_marketplace_agreement.types.agreement_approval_summaries.AgreementApprovalSummaries"
    """<p>An array of <code>AgreementApprovalSummary</code> objects containing summary information about each agreement approval.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementApprovalsOutput) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_approval_summaries

    out["items"] = (
        capo_marketplace_agreement.types.agreement_approval_summaries.serialize_aws_json_1_0(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementApprovalsOutput:
    out: ListAgreementApprovalsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_marketplace_agreement.types.agreement_approval_summaries

        out["items"] = (
            capo_marketplace_agreement.types.agreement_approval_summaries.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAgreementApprovalsOutput) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_approval_summaries

    out["items"] = (
        capo_marketplace_agreement.types.agreement_approval_summaries.serialize_cbor(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAgreementApprovalsOutput:
    out: ListAgreementApprovalsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_marketplace_agreement.types.agreement_approval_summaries

        out["items"] = (
            capo_marketplace_agreement.types.agreement_approval_summaries.deserialize_cbor(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
