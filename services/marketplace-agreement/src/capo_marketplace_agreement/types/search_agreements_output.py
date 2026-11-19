"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SearchAgreementsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_view_summary_list
    import capo_marketplace_agreement.types.next_token


class SearchAgreementsOutput(TypedDict, closed=True):
    agreement_view_summaries: NotRequired[
        "capo_marketplace_agreement.types.agreement_view_summary_list.AgreementViewSummaryList"
    ]
    """<p>A summary of the agreement, including top-level attributes (for example, the agreement ID, proposer, and acceptor).</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchAgreementsOutput) -> dict:
    out: dict = {}
    if "agreement_view_summaries" in value:
        import capo_marketplace_agreement.types.agreement_view_summary_list

        out["agreementViewSummaries"] = (
            capo_marketplace_agreement.types.agreement_view_summary_list.serialize_aws_json_1_0(
                value["agreement_view_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchAgreementsOutput:
    out: SearchAgreementsOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementViewSummaries") is not None:
        import capo_marketplace_agreement.types.agreement_view_summary_list

        out["agreement_view_summaries"] = (
            capo_marketplace_agreement.types.agreement_view_summary_list.deserialize_aws_json_1_0(
                data["agreementViewSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchAgreementsOutput) -> dict:
    out: dict = {}
    if "agreement_view_summaries" in value:
        import capo_marketplace_agreement.types.agreement_view_summary_list

        out["agreementViewSummaries"] = (
            capo_marketplace_agreement.types.agreement_view_summary_list.serialize_cbor(
                value["agreement_view_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> SearchAgreementsOutput:
    out: SearchAgreementsOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementViewSummaries") is not None:
        import capo_marketplace_agreement.types.agreement_view_summary_list

        out["agreement_view_summaries"] = (
            capo_marketplace_agreement.types.agreement_view_summary_list.deserialize_cbor(
                data["agreementViewSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
