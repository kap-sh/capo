"""Generated from Smithy shape ``com.amazonaws.ssoadmin#TrustedTokenIssuerUpdateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError, SerializationError
from capo_sso_admin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sso_admin.types.oidc_jwt_update_configuration


class _TrustedTokenIssuerUpdateConfiguration_OidcJwtConfiguration(
    TypedDict, closed=True
):
    OidcJwtConfiguration: (
        "capo_sso_admin.types.oidc_jwt_update_configuration.OidcJwtUpdateConfiguration"
    )


TrustedTokenIssuerUpdateConfiguration: TypeAlias = (
    _TrustedTokenIssuerUpdateConfiguration_OidcJwtConfiguration | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedTokenIssuerUpdateConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"TrustedTokenIssuerUpdateConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "OidcJwtConfiguration" in value:
        import capo_sso_admin.types.oidc_jwt_update_configuration

        return {
            "OidcJwtConfiguration": capo_sso_admin.types.oidc_jwt_update_configuration.serialize_aws_json_1_1(
                value["OidcJwtConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "TrustedTokenIssuerUpdateConfiguration: no variant present"
        )


def deserialize_aws_json_1_1(data: dict) -> TrustedTokenIssuerUpdateConfiguration:
    if data.get("OidcJwtConfiguration") is not None:
        import capo_sso_admin.types.oidc_jwt_update_configuration

        return {
            "OidcJwtConfiguration": capo_sso_admin.types.oidc_jwt_update_configuration.deserialize_aws_json_1_1(
                data["OidcJwtConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "TrustedTokenIssuerUpdateConfiguration: no recognized variant key"
        )
