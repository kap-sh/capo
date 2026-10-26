"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListenerTlsCertificate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_listener_tls_acm_certificate
    import capo_app_mesh.types.virtual_gateway_listener_tls_file_certificate
    import capo_app_mesh.types.virtual_gateway_listener_tls_sds_certificate


class _VirtualGatewayListenerTlsCertificate_acm(TypedDict, closed=True):
    acm: "capo_app_mesh.types.virtual_gateway_listener_tls_acm_certificate.VirtualGatewayListenerTlsAcmCertificate"


class _VirtualGatewayListenerTlsCertificate_file(TypedDict, closed=True):
    file: "capo_app_mesh.types.virtual_gateway_listener_tls_file_certificate.VirtualGatewayListenerTlsFileCertificate"


class _VirtualGatewayListenerTlsCertificate_sds(TypedDict, closed=True):
    sds: "capo_app_mesh.types.virtual_gateway_listener_tls_sds_certificate.VirtualGatewayListenerTlsSdsCertificate"


VirtualGatewayListenerTlsCertificate: TypeAlias = (
    _VirtualGatewayListenerTlsCertificate_acm
    | _VirtualGatewayListenerTlsCertificate_file
    | _VirtualGatewayListenerTlsCertificate_sds
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListenerTlsCertificate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"VirtualGatewayListenerTlsCertificate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "acm" in value:
        import capo_app_mesh.types.virtual_gateway_listener_tls_acm_certificate

        return {
            "acm": capo_app_mesh.types.virtual_gateway_listener_tls_acm_certificate.serialize_json(
                value["acm"]
            )
        }
    elif "file" in value:
        import capo_app_mesh.types.virtual_gateway_listener_tls_file_certificate

        return {
            "file": capo_app_mesh.types.virtual_gateway_listener_tls_file_certificate.serialize_json(
                value["file"]
            )
        }
    elif "sds" in value:
        import capo_app_mesh.types.virtual_gateway_listener_tls_sds_certificate

        return {
            "sds": capo_app_mesh.types.virtual_gateway_listener_tls_sds_certificate.serialize_json(
                value["sds"]
            )
        }
    else:
        raise SerializationError(
            "VirtualGatewayListenerTlsCertificate: no variant present"
        )


def deserialize_json(data: dict) -> VirtualGatewayListenerTlsCertificate:
    if data.get("acm") is not None:
        import capo_app_mesh.types.virtual_gateway_listener_tls_acm_certificate

        return {
            "acm": capo_app_mesh.types.virtual_gateway_listener_tls_acm_certificate.deserialize_json(
                data["acm"]
            )
        }
    elif data.get("file") is not None:
        import capo_app_mesh.types.virtual_gateway_listener_tls_file_certificate

        return {
            "file": capo_app_mesh.types.virtual_gateway_listener_tls_file_certificate.deserialize_json(
                data["file"]
            )
        }
    elif data.get("sds") is not None:
        import capo_app_mesh.types.virtual_gateway_listener_tls_sds_certificate

        return {
            "sds": capo_app_mesh.types.virtual_gateway_listener_tls_sds_certificate.deserialize_json(
                data["sds"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "VirtualGatewayListenerTlsCertificate: no recognized variant key"
        )
