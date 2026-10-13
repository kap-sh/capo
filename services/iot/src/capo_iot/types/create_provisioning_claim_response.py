"""Generated from Smithy shape ``com.amazonaws.iot#CreateProvisioningClaimResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_id
    import capo_iot.types.certificate_pem
    import capo_iot.types.date_type
    import capo_iot.types.key_pair


class CreateProvisioningClaimResponse(TypedDict, closed=True):
    certificate_id: NotRequired["capo_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the certificate.</p>"""
    certificate_pem: NotRequired["capo_iot.types.certificate_pem.CertificatePem"]
    """<p>The provisioning claim certificate.</p>"""
    key_pair: NotRequired["capo_iot.types.key_pair.KeyPair"]
    """<p>The provisioning claim key pair.</p>"""
    expiration: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The provisioning claim expiration time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningClaimResponse) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    if "certificate_pem" in value:
        out["certificatePem"] = value["certificate_pem"]
    if "key_pair" in value:
        import capo_iot.types.key_pair

        out["keyPair"] = capo_iot.types.key_pair.serialize_json(value["key_pair"])
    if "expiration" in value:
        import capo_iot.types.date_type

        out["expiration"] = capo_iot.types.date_type.serialize_json(value["expiration"])
    return out


def deserialize_json(data: dict) -> CreateProvisioningClaimResponse:
    out: CreateProvisioningClaimResponse = {}  # type: ignore[typeddict-item]
    if data.get("certificateId") is not None:
        out["certificate_id"] = data["certificateId"]
    if data.get("certificatePem") is not None:
        out["certificate_pem"] = data["certificatePem"]
    if data.get("keyPair") is not None:
        import capo_iot.types.key_pair

        out["key_pair"] = capo_iot.types.key_pair.deserialize_json(data["keyPair"])
    if data.get("expiration") is not None:
        import capo_iot.types.date_type

        out["expiration"] = capo_iot.types.date_type.deserialize_json(
            data["expiration"]
        )
    return out


def redact_sensitive(value: CreateProvisioningClaimResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key_pair" in value:
        import capo_iot.types.key_pair

        out["key_pair"] = capo_iot.types.key_pair.redact_sensitive(value["key_pair"])
    return out
