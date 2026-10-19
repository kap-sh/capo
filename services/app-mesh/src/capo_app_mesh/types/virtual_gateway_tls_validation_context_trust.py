"""Generated from Smithy shape ``com.amazonaws.appmesh#VirtualGatewayTlsValidationContextTrust``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust
    import capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust
    import capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust


class _VirtualGatewayTlsValidationContextTrust_acm(TypedDict, closed=True):
    acm: "capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust.VirtualGatewayTlsValidationContextAcmTrust"


class _VirtualGatewayTlsValidationContextTrust_file(TypedDict, closed=True):
    file: "capo_app_mesh.types.virtual_gateway_tls_validation_context_file_trust.VirtualGatewayTlsValidationContextFileTrust"


class _VirtualGatewayTlsValidationContextTrust_sds(TypedDict, closed=True):
    sds: "capo_app_mesh.types.virtual_gateway_tls_validation_context_sds_trust.VirtualGatewayTlsValidationContextSdsTrust"


VirtualGatewayTlsValidationContextTrust: TypeAlias = (
    _VirtualGatewayTlsValidationContextTrust_acm
    | _VirtualGatewayTlsValidationContextTrust_file
    | _VirtualGatewayTlsValidationContextTrust_sds
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VirtualGatewayTlsValidationContextTrust) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"VirtualGatewayTlsValidationContextTrust: cannot serialize unknown variant {value.name!r}"
        )
    elif "acm" in value:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust

        return {
            "acm": capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust.serialize_json(
                value["acm"]
            )
        }
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
            "VirtualGatewayTlsValidationContextTrust: no variant present"
        )


def deserialize_json(data: dict) -> VirtualGatewayTlsValidationContextTrust:
    if data.get("acm") is not None:
        import capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust

        return {
            "acm": capo_app_mesh.types.virtual_gateway_tls_validation_context_acm_trust.deserialize_json(
                data["acm"]
            )
        }
    elif data.get("file") is not None:
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
            return UnknownUnionMember(name)
        raise DeserializationError(
            "VirtualGatewayTlsValidationContextTrust: no recognized variant key"
        )
