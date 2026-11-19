"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptAgreementRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.resource_id


class AcceptAgreementRequestOutput(TypedDict, closed=True):
    agreement_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the agreement created or modified by accepting the agreement request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAgreementRequestOutput) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptAgreementRequestOutput:
    out: AcceptAgreementRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AcceptAgreementRequestOutput) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    return out


def deserialize_cbor(data: dict) -> AcceptAgreementRequestOutput:
    out: AcceptAgreementRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    return out
