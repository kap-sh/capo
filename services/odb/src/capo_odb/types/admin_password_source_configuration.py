"""Generated from Smithy shape ``com.amazonaws.odb#AdminPasswordSourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_odb.errors import DeserializationError, SerializationError
from capo_odb.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_odb.types.customer_managed_aws_secret_configuration


class AdminPasswordSourceConfigurationCustomerManagedAwsSecretMember(
    TypedDict, closed=True
):
    customerManagedAwsSecret: "capo_odb.types.customer_managed_aws_secret_configuration.CustomerManagedAwsSecretConfiguration"


AdminPasswordSourceConfiguration: TypeAlias = (
    AdminPasswordSourceConfigurationCustomerManagedAwsSecretMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AdminPasswordSourceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AdminPasswordSourceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customerManagedAwsSecret" in value:
        import capo_odb.types.customer_managed_aws_secret_configuration

        return {
            "customerManagedAwsSecret": capo_odb.types.customer_managed_aws_secret_configuration.serialize_aws_json_1_0(
                value["customerManagedAwsSecret"]
            )
        }
    else:
        raise SerializationError("AdminPasswordSourceConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AdminPasswordSourceConfiguration:
    if data.get("customerManagedAwsSecret") is not None:
        import capo_odb.types.customer_managed_aws_secret_configuration

        return {
            "customerManagedAwsSecret": capo_odb.types.customer_managed_aws_secret_configuration.deserialize_aws_json_1_0(
                data["customerManagedAwsSecret"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AdminPasswordSourceConfiguration: no recognized variant key"
        )
