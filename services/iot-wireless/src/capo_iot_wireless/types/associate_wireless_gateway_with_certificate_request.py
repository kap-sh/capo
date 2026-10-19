"""Generated from Smithy shape ``com.amazonaws.iotwireless#AssociateWirelessGatewayWithCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.iot_certificate_id
    import capo_iot_wireless.types.wireless_gateway_id


class AssociateWirelessGatewayWithCertificateRequest(TypedDict, closed=True):
    id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId"
    """<p>The ID of the resource to update.</p>"""
    iot_certificate_id: "capo_iot_wireless.types.iot_certificate_id.IotCertificateId"
    """<p>The ID of the certificate to associate with the wireless gateway.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWirelessGatewayWithCertificateRequest) -> dict:
    out: dict = {}
    out["IotCertificateId"] = value["iot_certificate_id"]
    return out


def deserialize_json(data: dict) -> AssociateWirelessGatewayWithCertificateRequest:
    out: AssociateWirelessGatewayWithCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("IotCertificateId") is not None:
        out["iot_certificate_id"] = data["IotCertificateId"]
    else:
        out["iot_certificate_id"] = ""
    return out
