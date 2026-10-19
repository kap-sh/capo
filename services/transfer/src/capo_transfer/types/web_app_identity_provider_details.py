"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppIdentityProviderDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError
from capo_transfer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_transfer.types.identity_center_config


class _WebAppIdentityProviderDetails_IdentityCenterConfig(TypedDict, closed=True):
    IdentityCenterConfig: (
        "capo_transfer.types.identity_center_config.IdentityCenterConfig"
    )


WebAppIdentityProviderDetails: TypeAlias = (
    _WebAppIdentityProviderDetails_IdentityCenterConfig | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppIdentityProviderDetails) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"WebAppIdentityProviderDetails: cannot serialize unknown variant {value.name!r}"
        )
    elif "IdentityCenterConfig" in value:
        import capo_transfer.types.identity_center_config

        return {
            "IdentityCenterConfig": capo_transfer.types.identity_center_config.serialize_aws_json_1_1(
                value["IdentityCenterConfig"]
            )
        }
    else:
        raise SerializationError("WebAppIdentityProviderDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> WebAppIdentityProviderDetails:
    if data.get("IdentityCenterConfig") is not None:
        import capo_transfer.types.identity_center_config

        return {
            "IdentityCenterConfig": capo_transfer.types.identity_center_config.deserialize_aws_json_1_1(
                data["IdentityCenterConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "WebAppIdentityProviderDetails: no recognized variant key"
        )
