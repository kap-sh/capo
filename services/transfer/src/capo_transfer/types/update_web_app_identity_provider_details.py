"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppIdentityProviderDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError
from capo_transfer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_transfer.types.update_web_app_identity_center_config


class _UpdateWebAppIdentityProviderDetails_IdentityCenterConfig(TypedDict, closed=True):
    IdentityCenterConfig: "capo_transfer.types.update_web_app_identity_center_config.UpdateWebAppIdentityCenterConfig"


UpdateWebAppIdentityProviderDetails: TypeAlias = (
    _UpdateWebAppIdentityProviderDetails_IdentityCenterConfig | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebAppIdentityProviderDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UpdateWebAppIdentityProviderDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "IdentityCenterConfig" in value:
        import capo_transfer.types.update_web_app_identity_center_config

        return {
            "IdentityCenterConfig": capo_transfer.types.update_web_app_identity_center_config.serialize_aws_json_1_1(
                value["IdentityCenterConfig"]
            )
        }
    else:
        raise SerializationError(
            "UpdateWebAppIdentityProviderDetails: no variant present"
        )


def deserialize_aws_json_1_1(data: dict) -> UpdateWebAppIdentityProviderDetails:
    if data.get("IdentityCenterConfig") is not None:
        import capo_transfer.types.update_web_app_identity_center_config

        return {
            "IdentityCenterConfig": capo_transfer.types.update_web_app_identity_center_config.deserialize_aws_json_1_1(
                data["IdentityCenterConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "UpdateWebAppIdentityProviderDetails: no recognized variant key"
        )
