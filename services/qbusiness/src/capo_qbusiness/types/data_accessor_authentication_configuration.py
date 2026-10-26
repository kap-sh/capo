"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessorAuthenticationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration


class _DataAccessorAuthenticationConfiguration_idcTrustedTokenIssuerConfiguration(
    TypedDict, closed=True
):
    idcTrustedTokenIssuerConfiguration: "capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration.DataAccessorIdcTrustedTokenIssuerConfiguration"


DataAccessorAuthenticationConfiguration: TypeAlias = (
    _DataAccessorAuthenticationConfiguration_idcTrustedTokenIssuerConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataAccessorAuthenticationConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DataAccessorAuthenticationConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "idcTrustedTokenIssuerConfiguration" in value:
        import capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration

        return {
            "idcTrustedTokenIssuerConfiguration": capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration.serialize_json(
                value["idcTrustedTokenIssuerConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "DataAccessorAuthenticationConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> DataAccessorAuthenticationConfiguration:
    if data.get("idcTrustedTokenIssuerConfiguration") is not None:
        import capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration

        return {
            "idcTrustedTokenIssuerConfiguration": capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration.deserialize_json(
                data["idcTrustedTokenIssuerConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DataAccessorAuthenticationConfiguration: no recognized variant key"
        )
