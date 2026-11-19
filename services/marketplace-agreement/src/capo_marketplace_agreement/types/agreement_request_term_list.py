"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementRequestTermList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_term

AgreementRequestTermList: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_request_term.AgreementRequestTerm"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementRequestTermList) -> list:
    import capo_marketplace_agreement.types.agreement_request_term

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_request_term.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementRequestTermList:
    import capo_marketplace_agreement.types.agreement_request_term

    out: AgreementRequestTermList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_request_term.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementRequestTermList) -> list:
    import capo_marketplace_agreement.types.agreement_request_term

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_request_term.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AgreementRequestTermList:
    import capo_marketplace_agreement.types.agreement_request_term

    out: AgreementRequestTermList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_request_term.deserialize_cbor(
                item
            )
        )
    return out
