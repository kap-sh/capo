"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkGetDeviceProfile``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.application_server_public_key
    import capo_iot_wireless.types.dak_certificate_metadata_list
    import capo_iot_wireless.types.qualification_status


class SidewalkGetDeviceProfile(TypedDict, closed=True):
    application_server_public_key: NotRequired[
        "capo_iot_wireless.types.application_server_public_key.ApplicationServerPublicKey"
    ]
    """<p>The Sidewalk application server public key.</p>"""
    qualification_status: NotRequired[
        "capo_iot_wireless.types.qualification_status.QualificationStatus"
    ]
    """<p>Gets information about the certification status of a Sidewalk device profile.</p>"""
    dak_certificate_metadata: NotRequired[
        "capo_iot_wireless.types.dak_certificate_metadata_list.DakCertificateMetadataList"
    ]
    """<p>The DAK certificate information of the Sidewalk device profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkGetDeviceProfile) -> dict:
    out: dict = {}
    if "application_server_public_key" in value:
        out["ApplicationServerPublicKey"] = value["application_server_public_key"]
    if "qualification_status" in value:
        out["QualificationStatus"] = value["qualification_status"]
    if "dak_certificate_metadata" in value:
        import capo_iot_wireless.types.dak_certificate_metadata_list

        out["DakCertificateMetadata"] = (
            capo_iot_wireless.types.dak_certificate_metadata_list.serialize_json(
                value["dak_certificate_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SidewalkGetDeviceProfile:
    out: SidewalkGetDeviceProfile = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationServerPublicKey") is not None:
        out["application_server_public_key"] = data["ApplicationServerPublicKey"]
    if data.get("QualificationStatus") is not None:
        out["qualification_status"] = data["QualificationStatus"]
    if data.get("DakCertificateMetadata") is not None:
        import capo_iot_wireless.types.dak_certificate_metadata_list

        out["dak_certificate_metadata"] = (
            capo_iot_wireless.types.dak_certificate_metadata_list.deserialize_json(
                data["DakCertificateMetadata"]
            )
        )
    return out


def redact_sensitive(value: SidewalkGetDeviceProfile) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "application_server_public_key" in value:
        out["application_server_public_key"] = "*** Sensitive Data Redacted ***"
    return out
