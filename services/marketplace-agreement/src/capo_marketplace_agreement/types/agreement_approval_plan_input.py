"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalPlanInput``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError, SerializationError
from capo_marketplace_agreement.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input


class AgreementApprovalPlanInputBuyerAgreementApprovalPlanInputMember(
    TypedDict, closed=True
):
    buyerAgreementApprovalPlanInput: "capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.BuyerAgreementApprovalPlanInput"


AgreementApprovalPlanInput: TypeAlias = (
    AgreementApprovalPlanInputBuyerAgreementApprovalPlanInputMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalPlanInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AgreementApprovalPlanInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "buyerAgreementApprovalPlanInput" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input

        return {
            "buyerAgreementApprovalPlanInput": capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.serialize_aws_json_1_0(
                value["buyerAgreementApprovalPlanInput"]
            )
        }
    else:
        raise SerializationError("AgreementApprovalPlanInput: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AgreementApprovalPlanInput:
    if data.get("buyerAgreementApprovalPlanInput") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input

        return {
            "buyerAgreementApprovalPlanInput": capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.deserialize_aws_json_1_0(
                data["buyerAgreementApprovalPlanInput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AgreementApprovalPlanInput: no recognized variant key"
        )


def redact_sensitive(value: AgreementApprovalPlanInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "buyerAgreementApprovalPlanInput" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input

        out["buyerAgreementApprovalPlanInput"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.redact_sensitive(
                value["buyerAgreementApprovalPlanInput"]
            )
        )
    return out
