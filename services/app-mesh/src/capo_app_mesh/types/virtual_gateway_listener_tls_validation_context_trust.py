"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayListenerTlsValidationContextTrust``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust
    import capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust


class VirtualGatewayListenerTlsValidationContextTrustFileMember(TypedDict, closed=True):
    file: "capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust.VirtualGatewayTlsValidationContextFileTrust"


class VirtualGatewayListenerTlsValidationContextTrustSdsMember(TypedDict, closed=True):
    sds: "capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust.VirtualGatewayTlsValidationContextSdsTrust"


VirtualGatewayListenerTlsValidationContextTrust: TypeAlias = (
    VirtualGatewayListenerTlsValidationContextTrustFileMember
    | VirtualGatewayListenerTlsValidationContextTrustSdsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayListenerTlsValidationContextTrust) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"VirtualGatewayListenerTlsValidationContextTrust: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "file" in value:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust

        return {
            "file": capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust.serialize_json(
                value["file"]
            )
        }
    elif "sds" in value:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust

        return {
            "sds": capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust.serialize_json(
                value["sds"]
            )
        }
    else:
        raise SerializationError(
            "VirtualGatewayListenerTlsValidationContextTrust: no variant present"
        )


def deserialize_json(data: dict) -> VirtualGatewayListenerTlsValidationContextTrust:
    if data.get("file") is not None:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust

        return {
            "file": capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust.deserialize_json(
                data["file"]
            )
        }
    elif data.get("sds") is not None:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust

        return {
            "sds": capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust.deserialize_json(
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
            "VirtualGatewayListenerTlsValidationContextTrust: no recognized variant key"
        )
