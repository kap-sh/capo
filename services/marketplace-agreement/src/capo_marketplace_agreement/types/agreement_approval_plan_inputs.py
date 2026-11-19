"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalPlanInputs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_plan_input

AgreementApprovalPlanInputs: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_approval_plan_input.AgreementApprovalPlanInput"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalPlanInputs) -> list:
    import capo_marketplace_agreement.types.agreement_approval_plan_input

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_approval_plan_input.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementApprovalPlanInputs:
    import capo_marketplace_agreement.types.agreement_approval_plan_input

    out: AgreementApprovalPlanInputs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_approval_plan_input.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalPlanInputs) -> list:
    import capo_marketplace_agreement.types.agreement_approval_plan_input

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_approval_plan_input.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AgreementApprovalPlanInputs:
    import capo_marketplace_agreement.types.agreement_approval_plan_input

    out: AgreementApprovalPlanInputs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_approval_plan_input.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: AgreementApprovalPlanInputs) -> list[Any]:
    import capo_marketplace_agreement.types.agreement_approval_plan_input

    return [
        capo_marketplace_agreement.types.agreement_approval_plan_input.redact_sensitive(
            item
        )
        for item in value
    ]
