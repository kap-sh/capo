"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalPlanLevel``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_level_name
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups


class BuyerAgreementApprovalPlanLevel(TypedDict, closed=True):
    name: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_level_name.AgreementApprovalLevelName"
    ]
    """<p>The name of the level.</p>"""
    groups: "capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups.BuyerAgreementApprovalPlanGroups"
    """<p>The group of approvers at this level.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalPlanLevel) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups

    out["groups"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups.serialize_aws_json_1_0(
            value["groups"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BuyerAgreementApprovalPlanLevel:
    out: BuyerAgreementApprovalPlanLevel = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("groups") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups

        out["groups"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups.deserialize_aws_json_1_0(
                data["groups"]
            )
        )
    else:
        out["groups"] = []
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuyerAgreementApprovalPlanLevel) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups

    out["groups"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups.serialize_cbor(
            value["groups"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> BuyerAgreementApprovalPlanLevel:
    out: BuyerAgreementApprovalPlanLevel = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("groups") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups

        out["groups"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups.deserialize_cbor(
                data["groups"]
            )
        )
    else:
        out["groups"] = []
    return out


def redact_sensitive(value: BuyerAgreementApprovalPlanLevel) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "groups" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups

        out["groups"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_groups.redact_sensitive(
                value["groups"]
            )
        )
    return out
