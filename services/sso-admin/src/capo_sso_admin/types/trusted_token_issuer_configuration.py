"""Generated from Smithy shape ``com.amazonaws.ssoadmin#TrustedTokenIssuerConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError, SerializationError
from capo_sso_admin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sso_admin.types.oidc_jwt_configuration


class _TrustedTokenIssuerConfiguration_OidcJwtConfiguration(TypedDict, closed=True):
    OidcJwtConfiguration: (
        "capo_sso_admin.types.oidc_jwt_configuration.OidcJwtConfiguration"
    )


TrustedTokenIssuerConfiguration: TypeAlias = (
    _TrustedTokenIssuerConfiguration_OidcJwtConfiguration | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedTokenIssuerConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TrustedTokenIssuerConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "OidcJwtConfiguration" in value:
        import capo_sso_admin.types.oidc_jwt_configuration

        return {
            "OidcJwtConfiguration": capo_sso_admin.types.oidc_jwt_configuration.serialize_aws_json_1_1(
                value["OidcJwtConfiguration"]
            )
        }
    else:
        raise SerializationError("TrustedTokenIssuerConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> TrustedTokenIssuerConfiguration:
    if data.get("OidcJwtConfiguration") is not None:
        import capo_sso_admin.types.oidc_jwt_configuration

        return {
            "OidcJwtConfiguration": capo_sso_admin.types.oidc_jwt_configuration.deserialize_aws_json_1_1(
                data["OidcJwtConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "TrustedTokenIssuerConfiguration: no recognized variant key"
        )
