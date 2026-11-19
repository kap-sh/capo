"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementEntitlementList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_entitlement

AgreementEntitlementList: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_entitlement.AgreementEntitlement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementEntitlementList) -> list:
    import capo_marketplace_agreement.types.agreement_entitlement

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_entitlement.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementEntitlementList:
    import capo_marketplace_agreement.types.agreement_entitlement

    out: AgreementEntitlementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_entitlement.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementEntitlementList) -> list:
    import capo_marketplace_agreement.types.agreement_entitlement

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_entitlement.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AgreementEntitlementList:
    import capo_marketplace_agreement.types.agreement_entitlement

    out: AgreementEntitlementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_entitlement.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: AgreementEntitlementList) -> list[Any]:
    import capo_marketplace_agreement.types.agreement_entitlement

    return [
        capo_marketplace_agreement.types.agreement_entitlement.redact_sensitive(item)
        for item in value
    ]
