"""Generated from Smithy shape ``com.amazonaws.iot#CreateKeysAndCertificateResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_arn
    import capo_iot.types.certificate_id
    import capo_iot.types.certificate_pem
    import capo_iot.types.key_pair


class CreateKeysAndCertificateResponse(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_iot.types.certificate_arn.CertificateArn"]
    """<p>The ARN of the certificate.</p>"""
    certificate_id: NotRequired["capo_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the certificate. IoT issues a default subject name for the certificate (for example, IoT Certificate).</p>"""
    certificate_pem: NotRequired["capo_iot.types.certificate_pem.CertificatePem"]
    """<p>The certificate data, in PEM format.</p>"""
    key_pair: NotRequired["capo_iot.types.key_pair.KeyPair"]
    """<p>The generated key pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKeysAndCertificateResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    if "certificate_pem" in value:
        out["certificatePem"] = value["certificate_pem"]
    if "key_pair" in value:
        import capo_iot.types.key_pair

        out["keyPair"] = capo_iot.types.key_pair.serialize_json(value["key_pair"])
    return out


def deserialize_json(data: dict) -> CreateKeysAndCertificateResponse:
    out: CreateKeysAndCertificateResponse = {}  # type: ignore[typeddict-item]
    if data.get("certificateArn") is not None:
        out["certificate_arn"] = data["certificateArn"]
    if data.get("certificateId") is not None:
        out["certificate_id"] = data["certificateId"]
    if data.get("certificatePem") is not None:
        out["certificate_pem"] = data["certificatePem"]
    if data.get("keyPair") is not None:
        import capo_iot.types.key_pair

        out["key_pair"] = capo_iot.types.key_pair.deserialize_json(data["keyPair"])
    return out


def redact_sensitive(value: CreateKeysAndCertificateResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key_pair" in value:
        import capo_iot.types.key_pair

        out["key_pair"] = capo_iot.types.key_pair.redact_sensitive(value["key_pair"])
    return out
