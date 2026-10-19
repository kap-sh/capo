"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTls``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.listener_tls_certificate
    import capo_app_mesh.types.listener_tls_mode
    import capo_app_mesh.types.listener_tls_validation_context


class ListenerTls(TypedDict, closed=True):
    mode: "capo_app_mesh.types.listener_tls_mode.ListenerTlsMode"
    """<p>Specify one of the following modes.</p> <ul> <li> <p> <b/>STRICT – Listener only accepts connections with TLS enabled. </p> </li> <li> <p> <b/>PERMISSIVE – Listener accepts connections with or without TLS enabled.</p> </li> <li> <p> <b/>DISABLED – Listener only accepts connections without TLS. </p> </li> </ul>"""
    certificate: "capo_app_mesh.types.listener_tls_certificate.ListenerTlsCertificate"
    """<p>A reference to an object that represents a listener's Transport Layer Security (TLS) certificate.</p>"""
    validation: NotRequired[
        "capo_app_mesh.types.listener_tls_validation_context.ListenerTlsValidationContext"
    ]
    """<p>A reference to an object that represents a listener's Transport Layer Security (TLS) validation context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTls) -> dict:
    out: dict = {}
    out["mode"] = value["mode"]
    import capo_app_mesh.types.listener_tls_certificate

    out["certificate"] = capo_app_mesh.types.listener_tls_certificate.serialize_json(
        value["certificate"]
    )
    if "validation" in value:
        import capo_app_mesh.types.listener_tls_validation_context

        out["validation"] = (
            capo_app_mesh.types.listener_tls_validation_context.serialize_json(
                value["validation"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListenerTls:
    out: ListenerTls = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        out["mode"] = data["mode"]
    else:
        out["mode"] = ""
    if data.get("certificate") is not None:
        import capo_app_mesh.types.listener_tls_certificate

        out["certificate"] = (
            capo_app_mesh.types.listener_tls_certificate.deserialize_json(
                data["certificate"]
            )
        )
    else:
        import capo_app_mesh.types._unknown

        out["certificate"] = capo_app_mesh.types._unknown.UnknownUnionMember("")
    if data.get("validation") is not None:
        import capo_app_mesh.types.listener_tls_validation_context

        out["validation"] = (
            capo_app_mesh.types.listener_tls_validation_context.deserialize_json(
                data["validation"]
            )
        )
    return out
