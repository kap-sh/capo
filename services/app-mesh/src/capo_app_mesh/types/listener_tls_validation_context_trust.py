"""Generated from Smithy shape ``com.amazonaws.appmesh#ListenerTlsValidationContextTrust``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError, SerializationError
from capo_app_mesh.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_app_mesh.types.tls_validation_context_file_trust
    import capo_app_mesh.types.tls_validation_context_sds_trust


class ListenerTlsValidationContextTrustFileMember(TypedDict, closed=True):
    file: "capo_app_mesh.types.tls_validation_context_file_trust.TlsValidationContextFileTrust"


class ListenerTlsValidationContextTrustSdsMember(TypedDict, closed=True):
    sds: "capo_app_mesh.types.tls_validation_context_sds_trust.TlsValidationContextSdsTrust"


ListenerTlsValidationContextTrust: TypeAlias = (
    ListenerTlsValidationContextTrustFileMember
    | ListenerTlsValidationContextTrustSdsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ListenerTlsValidationContextTrust) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ListenerTlsValidationContextTrust: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "file" in value:
        import capo_app_mesh.types.tls_validation_context_file_trust

        return {
            "file": capo_app_mesh.types.tls_validation_context_file_trust.serialize_json(
                value["file"]
            )
        }
    elif "sds" in value:
        import capo_app_mesh.types.tls_validation_context_sds_trust

        return {
            "sds": capo_app_mesh.types.tls_validation_context_sds_trust.serialize_json(
                value["sds"]
            )
        }
    else:
        raise SerializationError(
            "ListenerTlsValidationContextTrust: no variant present"
        )


def deserialize_json(data: dict) -> ListenerTlsValidationContextTrust:
    if data.get("file") is not None:
        import capo_app_mesh.types.tls_validation_context_file_trust

        return {
            "file": capo_app_mesh.types.tls_validation_context_file_trust.deserialize_json(
                data["file"]
            )
        }
    elif data.get("sds") is not None:
        import capo_app_mesh.types.tls_validation_context_sds_trust

        return {
            "sds": capo_app_mesh.types.tls_validation_context_sds_trust.deserialize_json(
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
            "ListenerTlsValidationContextTrust: no recognized variant key"
        )
