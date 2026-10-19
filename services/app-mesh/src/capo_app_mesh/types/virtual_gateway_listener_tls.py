"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListenerTls``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_listener_tls_certificate
    import capo_app_mesh.types.virtual_gateway_listener_tls_mode
    import capo_app_mesh.types.virtual_gateway_listener_tls_validation_context


class VirtualGatewayListenerTls(TypedDict, closed=True):
    mode: "capo_app_mesh.types.virtual_gateway_listener_tls_mode.VirtualGatewayListenerTlsMode"
    """<p>Specify one of the following modes.</p> <ul> <li> <p> <b/>STRICT – Listener only accepts connections with TLS enabled. </p> </li> <li> <p> <b/>PERMISSIVE – Listener accepts connections with or without TLS enabled.</p> </li> <li> <p> <b/>DISABLED – Listener only accepts connections without TLS. </p> </li> </ul>"""
    validation: NotRequired[
        "capo_app_mesh.types.virtual_gateway_listener_tls_validation_context.VirtualGatewayListenerTlsValidationContext"
    ]
    """<p>A reference to an object that represents a virtual gateway's listener's Transport Layer Security (TLS) validation context.</p>"""
    certificate: "capo_app_mesh.types.virtual_gateway_listener_tls_certificate.VirtualGatewayListenerTlsCertificate"
    """<p>An object that represents a Transport Layer Security (TLS) certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListenerTls) -> dict:
    out: dict = {}
    out["mode"] = value["mode"]
    if "validation" in value:
        import capo_app_mesh.types.virtual_gateway_listener_tls_validation_context

        out["validation"] = (
            capo_app_mesh.types.virtual_gateway_listener_tls_validation_context.serialize_json(
                value["validation"]
            )
        )
    import capo_app_mesh.types.virtual_gateway_listener_tls_certificate

    out["certificate"] = (
        capo_app_mesh.types.virtual_gateway_listener_tls_certificate.serialize_json(
            value["certificate"]
        )
    )
    return out


def deserialize_json(data: dict) -> VirtualGatewayListenerTls:
    out: VirtualGatewayListenerTls = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        out["mode"] = data["mode"]
    else:
        out["mode"] = ""
    if data.get("validation") is not None:
        import capo_app_mesh.types.virtual_gateway_listener_tls_validation_context

        out["validation"] = (
            capo_app_mesh.types.virtual_gateway_listener_tls_validation_context.deserialize_json(
                data["validation"]
            )
        )
    if data.get("certificate") is not None:
        import capo_app_mesh.types.virtual_gateway_listener_tls_certificate

        out["certificate"] = (
            capo_app_mesh.types.virtual_gateway_listener_tls_certificate.deserialize_json(
                data["certificate"]
            )
        )
    else:
        import capo_app_mesh.types._unknown

        out["certificate"] = capo_app_mesh.types._unknown.UnknownUnionMember("")
    return out
