"""Generated from Smithy shape ``com.amazonaws.directconnect#ConfirmCustomerAgreementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.agreement_name


class ConfirmCustomerAgreementRequest(TypedDict, closed=True):
    agreement_name: NotRequired[
        "capo_direct_connect.types.agreement_name.AgreementName"
    ]
    """<p> The name of the customer agreement. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmCustomerAgreementRequest) -> dict:
    out: dict = {}
    if "agreement_name" in value:
        out["agreementName"] = value["agreement_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmCustomerAgreementRequest:
    out: ConfirmCustomerAgreementRequest = {}  # type: ignore[typeddict-item]
    if data.get("agreementName") is not None:
        out["agreement_name"] = data["agreementName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfirmCustomerAgreementRequest) -> dict:
    out: dict = {}
    if "agreement_name" in value:
        out["agreementName"] = value["agreement_name"]
    return out


def deserialize_cbor(data: dict) -> ConfirmCustomerAgreementRequest:
    out: ConfirmCustomerAgreementRequest = {}  # type: ignore[typeddict-item]
    if data.get("agreementName") is not None:
        out["agreement_name"] = data["agreementName"]
    return out
