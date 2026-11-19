"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementRequestApprovalPlansOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_plans
    import capo_marketplace_agreement.types.next_token


class GetAgreementRequestApprovalPlansOutput(TypedDict, closed=True):
    items: "capo_marketplace_agreement.types.agreement_approval_plans.AgreementApprovalPlans"
    """<p>An array of <code>AgreementApprovalPlan</code> objects, one for each approval plan that applies to the agreement request.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementRequestApprovalPlansOutput) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_approval_plans

    out["items"] = (
        capo_marketplace_agreement.types.agreement_approval_plans.serialize_aws_json_1_0(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementRequestApprovalPlansOutput:
    out: GetAgreementRequestApprovalPlansOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_marketplace_agreement.types.agreement_approval_plans

        out["items"] = (
            capo_marketplace_agreement.types.agreement_approval_plans.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: GetAgreementRequestApprovalPlansOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_marketplace_agreement.types.agreement_approval_plans

        out["items"] = (
            capo_marketplace_agreement.types.agreement_approval_plans.redact_sensitive(
                value["items"]
            )
        )
    return out
