"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_resource

AgreementApprovalResources: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_approval_resource.AgreementApprovalResource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalResources) -> list:
    import capo_marketplace_agreement.types.agreement_approval_resource

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_approval_resource.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementApprovalResources:
    import capo_marketplace_agreement.types.agreement_approval_resource

    out: AgreementApprovalResources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_approval_resource.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalResources) -> list:
    import capo_marketplace_agreement.types.agreement_approval_resource

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_approval_resource.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AgreementApprovalResources:
    import capo_marketplace_agreement.types.agreement_approval_resource

    out: AgreementApprovalResources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_approval_resource.deserialize_cbor(
                item
            )
        )
    return out
