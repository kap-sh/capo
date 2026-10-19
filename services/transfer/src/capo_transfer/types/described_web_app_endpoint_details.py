"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedWebAppEndpointDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError
from capo_transfer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_transfer.types.described_web_app_vpc_config


class _DescribedWebAppEndpointDetails_Vpc(TypedDict, closed=True):
    Vpc: "capo_transfer.types.described_web_app_vpc_config.DescribedWebAppVpcConfig"


DescribedWebAppEndpointDetails: TypeAlias = (
    _DescribedWebAppEndpointDetails_Vpc | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedWebAppEndpointDetails) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DescribedWebAppEndpointDetails: cannot serialize unknown variant {value.name!r}"
        )
    elif "Vpc" in value:
        import capo_transfer.types.described_web_app_vpc_config

        return {
            "Vpc": capo_transfer.types.described_web_app_vpc_config.serialize_aws_json_1_1(
                value["Vpc"]
            )
        }
    else:
        raise SerializationError("DescribedWebAppEndpointDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> DescribedWebAppEndpointDetails:
    if data.get("Vpc") is not None:
        import capo_transfer.types.described_web_app_vpc_config

        return {
            "Vpc": capo_transfer.types.described_web_app_vpc_config.deserialize_aws_json_1_1(
                data["Vpc"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "DescribedWebAppEndpointDetails: no recognized variant key"
        )
