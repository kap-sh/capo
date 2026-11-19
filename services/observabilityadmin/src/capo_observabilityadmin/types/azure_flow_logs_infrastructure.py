"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureFlowLogsInfrastructure``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError, SerializationError
from capo_observabilityadmin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_aws_managed_flow_logs
    import capo_observabilityadmin.types.azure_customer_managed_flow_logs


class AzureFlowLogsInfrastructureCustomerManagedMember(TypedDict, closed=True):
    CustomerManaged: "capo_observabilityadmin.types.azure_customer_managed_flow_logs.AzureCustomerManagedFlowLogs"


class AzureFlowLogsInfrastructureAwsManagedMember(TypedDict, closed=True):
    AwsManaged: "capo_observabilityadmin.types.azure_aws_managed_flow_logs.AzureAwsManagedFlowLogs"


AzureFlowLogsInfrastructure: TypeAlias = (
    AzureFlowLogsInfrastructureCustomerManagedMember
    | AzureFlowLogsInfrastructureAwsManagedMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AzureFlowLogsInfrastructure) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AzureFlowLogsInfrastructure: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "CustomerManaged" in value:
        import capo_observabilityadmin.types.azure_customer_managed_flow_logs

        return {
            "CustomerManaged": capo_observabilityadmin.types.azure_customer_managed_flow_logs.serialize_json(
                value["CustomerManaged"]
            )
        }
    elif "AwsManaged" in value:
        import capo_observabilityadmin.types.azure_aws_managed_flow_logs

        return {
            "AwsManaged": capo_observabilityadmin.types.azure_aws_managed_flow_logs.serialize_json(
                value["AwsManaged"]
            )
        }
    else:
        raise SerializationError("AzureFlowLogsInfrastructure: no variant present")


def deserialize_json(data: dict) -> AzureFlowLogsInfrastructure:
    if data.get("CustomerManaged") is not None:
        import capo_observabilityadmin.types.azure_customer_managed_flow_logs

        return {
            "CustomerManaged": capo_observabilityadmin.types.azure_customer_managed_flow_logs.deserialize_json(
                data["CustomerManaged"]
            )
        }
    elif data.get("AwsManaged") is not None:
        import capo_observabilityadmin.types.azure_aws_managed_flow_logs

        return {
            "AwsManaged": capo_observabilityadmin.types.azure_aws_managed_flow_logs.deserialize_json(
                data["AwsManaged"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AzureFlowLogsInfrastructure: no recognized variant key"
        )
