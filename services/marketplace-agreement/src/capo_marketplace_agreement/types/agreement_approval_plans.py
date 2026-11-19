"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalPlans``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_plan

AgreementApprovalPlans: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_approval_plan.AgreementApprovalPlan"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalPlans) -> list:
    import capo_marketplace_agreement.types.agreement_approval_plan

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_approval_plan.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementApprovalPlans:
    import capo_marketplace_agreement.types.agreement_approval_plan

    out: AgreementApprovalPlans = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_approval_plan.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalPlans) -> list:
    import capo_marketplace_agreement.types.agreement_approval_plan

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_approval_plan.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AgreementApprovalPlans:
    import capo_marketplace_agreement.types.agreement_approval_plan

    out: AgreementApprovalPlans = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_approval_plan.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: AgreementApprovalPlans) -> list[Any]:
    import capo_marketplace_agreement.types.agreement_approval_plan

    return [
        capo_marketplace_agreement.types.agreement_approval_plan.redact_sensitive(item)
        for item in value
    ]
