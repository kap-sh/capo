"""Generated from Smithy shape ``com.amazonaws.iotwireless#DakCertificateMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.ap_id
    import capo_iot_wireless.types.dak_certificate_id
    import capo_iot_wireless.types.device_type_id
    import capo_iot_wireless.types.factory_support
    import capo_iot_wireless.types.max_allowed_signature


class DakCertificateMetadata(TypedDict, closed=True):
    certificate_id: "capo_iot_wireless.types.dak_certificate_id.DakCertificateId"
    """<p>The certificate ID for the DAK.</p>"""
    max_allowed_signature: NotRequired[
        "capo_iot_wireless.types.max_allowed_signature.MaxAllowedSignature"
    ]
    """<p>The maximum number of signatures that the DAK can sign. A value of <code>-1</code> indicates that there's no device limit.</p>"""
    factory_support: NotRequired[
        "capo_iot_wireless.types.factory_support.FactorySupport"
    ]
    """<p>Whether factory support has been enabled.</p>"""
    ap_id: NotRequired["capo_iot_wireless.types.ap_id.ApId"]
    """<p>The advertised product ID (APID) that's used for pre-production and production applications.</p>"""
    device_type_id: NotRequired["capo_iot_wireless.types.device_type_id.DeviceTypeId"]
    """<p>The device type ID that's used for prototyping applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DakCertificateMetadata) -> dict:
    out: dict = {}
    out["CertificateId"] = value["certificate_id"]
    if "max_allowed_signature" in value:
        out["MaxAllowedSignature"] = value["max_allowed_signature"]
    if "factory_support" in value:
        out["FactorySupport"] = value["factory_support"]
    if "ap_id" in value:
        out["ApId"] = value["ap_id"]
    if "device_type_id" in value:
        out["DeviceTypeId"] = value["device_type_id"]
    return out


def deserialize_json(data: dict) -> DakCertificateMetadata:
    out: DakCertificateMetadata = {}  # type: ignore[typeddict-item]
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    else:
        out["certificate_id"] = ""
    if data.get("MaxAllowedSignature") is not None:
        out["max_allowed_signature"] = data["MaxAllowedSignature"]
    if data.get("FactorySupport") is not None:
        out["factory_support"] = data["FactorySupport"]
    if data.get("ApId") is not None:
        out["ap_id"] = data["ApId"]
    if data.get("DeviceTypeId") is not None:
        out["device_type_id"] = data["DeviceTypeId"]
    return out
