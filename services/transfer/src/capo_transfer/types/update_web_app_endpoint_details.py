"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppEndpointDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError
from capo_transfer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_transfer.types.update_web_app_vpc_config


class UpdateWebAppEndpointDetailsVpcMember(TypedDict, closed=True):
    Vpc: "capo_transfer.types.update_web_app_vpc_config.UpdateWebAppVpcConfig"


UpdateWebAppEndpointDetails: TypeAlias = (
    UpdateWebAppEndpointDetailsVpcMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebAppEndpointDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UpdateWebAppEndpointDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Vpc" in value:
        import capo_transfer.types.update_web_app_vpc_config

        return {
            "Vpc": capo_transfer.types.update_web_app_vpc_config.serialize_aws_json_1_1(
                value["Vpc"]
            )
        }
    else:
        raise SerializationError("UpdateWebAppEndpointDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> UpdateWebAppEndpointDetails:
    if data.get("Vpc") is not None:
        import capo_transfer.types.update_web_app_vpc_config

        return {
            "Vpc": capo_transfer.types.update_web_app_vpc_config.deserialize_aws_json_1_1(
                data["Vpc"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "UpdateWebAppEndpointDetails: no recognized variant key"
        )
