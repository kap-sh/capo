"""Generated from Smithy shape ``com.amazonaws.directconnect#ConfirmCustomerAgreementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.status


class ConfirmCustomerAgreementResponse(TypedDict, closed=True):
    status: NotRequired["capo_direct_connect.types.status.Status"]
    """<p> The status of the customer agreement when the connection was created. This will be either <code>signed</code> or <code>unsigned</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmCustomerAgreementResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmCustomerAgreementResponse:
    out: ConfirmCustomerAgreementResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfirmCustomerAgreementResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_cbor(data: dict) -> ConfirmCustomerAgreementResponse:
    out: ConfirmCustomerAgreementResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    return out
