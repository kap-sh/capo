"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CancelAgreementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.resource_id


class CancelAgreementInput(TypedDict, closed=True):
    agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId"
    """<p>The unique identifier of the agreement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelAgreementInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelAgreementInput:
    out: CancelAgreementInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    return out
