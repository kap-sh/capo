"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListenerTlsValidationContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.subject_alternative_names
    import capo_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust


class VirtualGatewayListenerTlsValidationContext(TypedDict, closed=True):
    trust: "capo_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust.VirtualGatewayListenerTlsValidationContextTrust"
    """<p>A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.</p>"""
    subject_alternative_names: NotRequired[
        "capo_app_mesh.types.subject_alternative_names.SubjectAlternativeNames"
    ]
    """<p>A reference to an object that represents the SANs for a virtual gateway listener's Transport Layer Security (TLS) validation context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListenerTlsValidationContext) -> dict:
    out: dict = {}
    import capo_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust

    out["trust"] = (
        capo_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust.serialize_json(
            value["trust"]
        )
    )
    if "subject_alternative_names" in value:
        import capo_app_mesh.types.subject_alternative_names

        out["subjectAlternativeNames"] = (
            capo_app_mesh.types.subject_alternative_names.serialize_json(
                value["subject_alternative_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> VirtualGatewayListenerTlsValidationContext:
    out: VirtualGatewayListenerTlsValidationContext = {}  # type: ignore[typeddict-item]
    if data.get("trust") is not None:
        import capo_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust

        out["trust"] = (
            capo_app_mesh.types.virtual_gateway_listener_tls_validation_context_trust.deserialize_json(
                data["trust"]
            )
        )
    else:
        import capo_app_mesh.types._unknown

        out["trust"] = capo_app_mesh.types._unknown.UnknownUnionMember("")
    if data.get("subjectAlternativeNames") is not None:
        import capo_app_mesh.types.subject_alternative_names

        out["subject_alternative_names"] = (
            capo_app_mesh.types.subject_alternative_names.deserialize_json(
                data["subjectAlternativeNames"]
            )
        )
    return out
