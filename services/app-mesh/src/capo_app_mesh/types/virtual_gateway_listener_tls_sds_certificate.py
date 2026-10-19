"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListenerTlsSdsCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_sds_secret_name


class VirtualGatewayListenerTlsSdsCertificate(TypedDict, closed=True):
    secret_name: "capo_app_mesh.types.virtual_gateway_sds_secret_name.VirtualGatewaySdsSecretName"
    """<p>A reference to an object that represents the name of the secret secret requested from the Secret Discovery Service provider representing Transport Layer Security (TLS) materials like a certificate or certificate chain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListenerTlsSdsCertificate) -> dict:
    out: dict = {}
    out["secretName"] = value["secret_name"]
    return out


def deserialize_json(data: dict) -> VirtualGatewayListenerTlsSdsCertificate:
    out: VirtualGatewayListenerTlsSdsCertificate = {}  # type: ignore[typeddict-item]
    if data.get("secretName") is not None:
        out["secret_name"] = data["secretName"]
    else:
        out["secret_name"] = ""
    return out
