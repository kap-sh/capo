"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementRequestTermsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_term_list
    import capo_marketplace_agreement.types.next_token


class GetAgreementRequestTermsOutput(TypedDict, closed=True):
    terms: "capo_marketplace_agreement.types.agreement_request_term_list.AgreementRequestTermList"
    """<p>The terms proposed for the agreement request. The terms are fixed when the agreement request is created.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementRequestTermsOutput) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_request_term_list

    out["terms"] = (
        capo_marketplace_agreement.types.agreement_request_term_list.serialize_aws_json_1_0(
            value["terms"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementRequestTermsOutput:
    out: GetAgreementRequestTermsOutput = {}  # type: ignore[typeddict-item]
    if data.get("terms") is not None:
        import capo_marketplace_agreement.types.agreement_request_term_list

        out["terms"] = (
            capo_marketplace_agreement.types.agreement_request_term_list.deserialize_aws_json_1_0(
                data["terms"]
            )
        )
    else:
        out["terms"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAgreementRequestTermsOutput) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_request_term_list

    out["terms"] = (
        capo_marketplace_agreement.types.agreement_request_term_list.serialize_cbor(
            value["terms"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetAgreementRequestTermsOutput:
    out: GetAgreementRequestTermsOutput = {}  # type: ignore[typeddict-item]
    if data.get("terms") is not None:
        import capo_marketplace_agreement.types.agreement_request_term_list

        out["terms"] = (
            capo_marketplace_agreement.types.agreement_request_term_list.deserialize_cbor(
                data["terms"]
            )
        )
    else:
        out["terms"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
