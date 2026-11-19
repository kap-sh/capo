"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementTermsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.accepted_term_list
    import capo_marketplace_agreement.types.next_token


class GetAgreementTermsOutput(TypedDict, closed=True):
    accepted_terms: NotRequired[
        "capo_marketplace_agreement.types.accepted_term_list.AcceptedTermList"
    ]
    """<p>A subset of terms proposed by the proposer that have been accepted by the acceptor as part of the agreement creation.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementTermsOutput) -> dict:
    out: dict = {}
    if "accepted_terms" in value:
        import capo_marketplace_agreement.types.accepted_term_list

        out["acceptedTerms"] = (
            capo_marketplace_agreement.types.accepted_term_list.serialize_aws_json_1_0(
                value["accepted_terms"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementTermsOutput:
    out: GetAgreementTermsOutput = {}  # type: ignore[typeddict-item]
    if data.get("acceptedTerms") is not None:
        import capo_marketplace_agreement.types.accepted_term_list

        out["accepted_terms"] = (
            capo_marketplace_agreement.types.accepted_term_list.deserialize_aws_json_1_0(
                data["acceptedTerms"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAgreementTermsOutput) -> dict:
    out: dict = {}
    if "accepted_terms" in value:
        import capo_marketplace_agreement.types.accepted_term_list

        out["acceptedTerms"] = (
            capo_marketplace_agreement.types.accepted_term_list.serialize_cbor(
                value["accepted_terms"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetAgreementTermsOutput:
    out: GetAgreementTermsOutput = {}  # type: ignore[typeddict-item]
    if data.get("acceptedTerms") is not None:
        import capo_marketplace_agreement.types.accepted_term_list

        out["accepted_terms"] = (
            capo_marketplace_agreement.types.accepted_term_list.deserialize_cbor(
                data["acceptedTerms"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
