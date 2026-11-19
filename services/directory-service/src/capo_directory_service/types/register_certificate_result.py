"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegisterCertificateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.certificate_id


class RegisterCertificateResult(TypedDict, closed=True):
    certificate_id: NotRequired[
        "capo_directory_service.types.certificate_id.CertificateId"
    ]
    """<p>The identifier of the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterCertificateResult) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterCertificateResult:
    out: RegisterCertificateResult = {}  # type: ignore[typeddict-item]
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegisterCertificateResult) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    return out


def deserialize_cbor(data: dict) -> RegisterCertificateResult:
    out: RegisterCertificateResult = {}  # type: ignore[typeddict-item]
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    return out
