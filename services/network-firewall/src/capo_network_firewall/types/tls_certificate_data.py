"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TlsCertificateData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.collection_member_string
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.status_reason


class TlsCertificateData(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    certificate_serial: NotRequired[
        "capo_network_firewall.types.collection_member_string.CollectionMember_String"
    ]
    """<p>The serial number of the certificate.</p>"""
    status: NotRequired[
        "capo_network_firewall.types.collection_member_string.CollectionMember_String"
    ]
    """<p>The status of the certificate.</p>"""
    status_message: NotRequired[
        "capo_network_firewall.types.status_reason.StatusReason"
    ]
    """<p>Contains details about the certificate status, including information about certificate errors.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TlsCertificateData) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "certificate_serial" in value:
        out["CertificateSerial"] = value["certificate_serial"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TlsCertificateData:
    out: TlsCertificateData = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("CertificateSerial") is not None:
        out["certificate_serial"] = data["CertificateSerial"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TlsCertificateData) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "certificate_serial" in value:
        out["CertificateSerial"] = value["certificate_serial"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_cbor(data: dict) -> TlsCertificateData:
    out: TlsCertificateData = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    if data.get("CertificateSerial") is not None:
        out["certificate_serial"] = data["CertificateSerial"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
