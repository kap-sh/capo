"""Generated from Smithy shape ``com.amazonaws.ssm#CloudConnectorConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError, SerializationError
from capo_ssm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm.types.azure_configuration


class CloudConnectorConfigurationAzureConfigurationMember(TypedDict, closed=True):
    AzureConfiguration: "capo_ssm.types.azure_configuration.AzureConfiguration"


CloudConnectorConfiguration: TypeAlias = (
    CloudConnectorConfigurationAzureConfigurationMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudConnectorConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CloudConnectorConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AzureConfiguration" in value:
        import capo_ssm.types.azure_configuration

        return {
            "AzureConfiguration": capo_ssm.types.azure_configuration.serialize_aws_json_1_1(
                value["AzureConfiguration"]
            )
        }
    else:
        raise SerializationError("CloudConnectorConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CloudConnectorConfiguration:
    if data.get("AzureConfiguration") is not None:
        import capo_ssm.types.azure_configuration

        return {
            "AzureConfiguration": capo_ssm.types.azure_configuration.deserialize_aws_json_1_1(
                data["AzureConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CloudConnectorConfiguration: no recognized variant key"
        )
