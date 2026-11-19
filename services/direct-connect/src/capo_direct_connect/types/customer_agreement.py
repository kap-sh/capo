"""Generated from Smithy shape ``com.amazonaws.directconnect#CustomerAgreement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.agreement_name
    import capo_direct_connect.types.status


class CustomerAgreement(TypedDict, closed=True):
    agreement_name: NotRequired[
        "capo_direct_connect.types.agreement_name.AgreementName"
    ]
    """<p>The name of the agreement.</p>"""
    status: NotRequired["capo_direct_connect.types.status.Status"]
    """<p>The status of the customer agreement. This will be either <code>signed</code> or <code>unsigned</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerAgreement) -> dict:
    out: dict = {}
    if "agreement_name" in value:
        out["agreementName"] = value["agreement_name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerAgreement:
    out: CustomerAgreement = {}  # type: ignore[typeddict-item]
    if data.get("agreementName") is not None:
        out["agreement_name"] = data["agreementName"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomerAgreement) -> dict:
    out: dict = {}
    if "agreement_name" in value:
        out["agreementName"] = value["agreement_name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_cbor(data: dict) -> CustomerAgreement:
    out: CustomerAgreement = {}  # type: ignore[typeddict-item]
    if data.get("agreementName") is not None:
        out["agreement_name"] = data["agreementName"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
