"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalPlan``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_marketplace_agreement.errors import DeserializationError, SerializationError
from capo_marketplace_agreement.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan


class AgreementApprovalPlanBuyerAgreementApprovalPlanMember(TypedDict, closed=True):
    buyerAgreementApprovalPlan: "capo_marketplace_agreement.types.buyer_agreement_approval_plan.BuyerAgreementApprovalPlan"


AgreementApprovalPlan: TypeAlias = (
    AgreementApprovalPlanBuyerAgreementApprovalPlanMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalPlan) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AgreementApprovalPlan: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "buyerAgreementApprovalPlan" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan

        return {
            "buyerAgreementApprovalPlan": capo_marketplace_agreement.types.buyer_agreement_approval_plan.serialize_aws_json_1_0(
                value["buyerAgreementApprovalPlan"]
            )
        }
    else:
        raise SerializationError("AgreementApprovalPlan: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AgreementApprovalPlan:
    if data.get("buyerAgreementApprovalPlan") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan

        return {
            "buyerAgreementApprovalPlan": capo_marketplace_agreement.types.buyer_agreement_approval_plan.deserialize_aws_json_1_0(
                data["buyerAgreementApprovalPlan"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AgreementApprovalPlan: no recognized variant key")


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalPlan) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AgreementApprovalPlan: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "buyerAgreementApprovalPlan" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan

        return {
            "buyerAgreementApprovalPlan": capo_marketplace_agreement.types.buyer_agreement_approval_plan.serialize_cbor(
                value["buyerAgreementApprovalPlan"]
            )
        }
    else:
        raise SerializationError("AgreementApprovalPlan: no variant present")


def deserialize_cbor(data: dict) -> AgreementApprovalPlan:
    if data.get("buyerAgreementApprovalPlan") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan

        return {
            "buyerAgreementApprovalPlan": capo_marketplace_agreement.types.buyer_agreement_approval_plan.deserialize_cbor(
                data["buyerAgreementApprovalPlan"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AgreementApprovalPlan: no recognized variant key")


def redact_sensitive(value: AgreementApprovalPlan) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "buyerAgreementApprovalPlan" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan

        out["buyerAgreementApprovalPlan"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan.redact_sensitive(
                value["buyerAgreementApprovalPlan"]
            )
        )
    return out
