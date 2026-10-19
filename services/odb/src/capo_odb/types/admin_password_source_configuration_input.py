"""Generated from Smithy shape ``com.amazonaws.odb#AdminPasswordSourceConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError, SerializationError
from capo_odb.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_odb.types.customer_managed_aws_secret_configuration_input


class _AdminPasswordSourceConfigurationInput_customerManagedAwsSecret(
    TypedDict, closed=True
):
    customerManagedAwsSecret: "capo_odb.types.customer_managed_aws_secret_configuration_input.CustomerManagedAwsSecretConfigurationInput"


AdminPasswordSourceConfigurationInput: TypeAlias = (
    _AdminPasswordSourceConfigurationInput_customerManagedAwsSecret | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AdminPasswordSourceConfigurationInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AdminPasswordSourceConfigurationInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "customerManagedAwsSecret" in value:
        import capo_odb.types.customer_managed_aws_secret_configuration_input

        return {
            "customerManagedAwsSecret": capo_odb.types.customer_managed_aws_secret_configuration_input.serialize_aws_json_1_0(
                value["customerManagedAwsSecret"]
            )
        }
    else:
        raise SerializationError(
            "AdminPasswordSourceConfigurationInput: no variant present"
        )


def deserialize_aws_json_1_0(data: dict) -> AdminPasswordSourceConfigurationInput:
    if data.get("customerManagedAwsSecret") is not None:
        import capo_odb.types.customer_managed_aws_secret_configuration_input

        return {
            "customerManagedAwsSecret": capo_odb.types.customer_managed_aws_secret_configuration_input.deserialize_aws_json_1_0(
                data["customerManagedAwsSecret"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "AdminPasswordSourceConfigurationInput: no recognized variant key"
        )
