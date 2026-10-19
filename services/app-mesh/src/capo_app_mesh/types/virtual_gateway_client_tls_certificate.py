"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayClientTlsCertificate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_listener_tls_file_certificate
    import capo_app_mesh.types.virtual_gateway_listener_tls_sds_certificate


class _VirtualGatewayClientTlsCertificate_file(TypedDict, closed=True):
    file: "capo_app_mesh.types.virtual_gateway_listener_tls_file_certificate.VirtualGatewayListenerTlsFileCertificate"


class _VirtualGatewayClientTlsCertificate_sds(TypedDict, closed=True):
    sds: "capo_app_mesh.types.virtual_gateway_listener_tls_sds_certificate.VirtualGatewayListenerTlsSdsCertificate"


VirtualGatewayClientTlsCertificate: TypeAlias = (
    _VirtualGatewayClientTlsCertificate_file
    | _VirtualGatewayClientTlsCertificate_sds
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayClientTlsCertificate) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"VirtualGatewayClientTlsCertificate: cannot serialize unknown variant {value.name!r}"
        )
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
            "VirtualGatewayClientTlsCertificate: no variant present"
        )


def deserialize_json(data: dict) -> VirtualGatewayClientTlsCertificate:
    if data.get("file") is not None:
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
            return UnknownUnionMember(name)
        raise DeserializationError(
            "VirtualGatewayClientTlsCertificate: no recognized variant key"
        )
