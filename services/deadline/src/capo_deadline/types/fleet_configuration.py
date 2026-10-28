"""Generated from Smithy shape ``com.amazonaws.deadline#FleetConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.customer_managed_fleet_configuration
    import capo_deadline.types.service_managed_ec2_fleet_configuration


class FleetConfigurationCustomerManagedMember(TypedDict, closed=True):
    customerManaged: "capo_deadline.types.customer_managed_fleet_configuration.CustomerManagedFleetConfiguration"


class FleetConfigurationServiceManagedEc2Member(TypedDict, closed=True):
    serviceManagedEc2: "capo_deadline.types.service_managed_ec2_fleet_configuration.ServiceManagedEc2FleetConfiguration"


FleetConfiguration: TypeAlias = (
    FleetConfigurationCustomerManagedMember
    | FleetConfigurationServiceManagedEc2Member
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FleetConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FleetConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customerManaged" in value:
        import capo_deadline.types.customer_managed_fleet_configuration

        return {
            "customerManaged": capo_deadline.types.customer_managed_fleet_configuration.serialize_json(
                value["customerManaged"]
            )
        }
    elif "serviceManagedEc2" in value:
        import capo_deadline.types.service_managed_ec2_fleet_configuration

        return {
            "serviceManagedEc2": capo_deadline.types.service_managed_ec2_fleet_configuration.serialize_json(
                value["serviceManagedEc2"]
            )
        }
    else:
        raise SerializationError("FleetConfiguration: no variant present")


def deserialize_json(data: dict) -> FleetConfiguration:
    if data.get("customerManaged") is not None:
        import capo_deadline.types.customer_managed_fleet_configuration

        return {
            "customerManaged": capo_deadline.types.customer_managed_fleet_configuration.deserialize_json(
                data["customerManaged"]
            )
        }
    elif data.get("serviceManagedEc2") is not None:
        import capo_deadline.types.service_managed_ec2_fleet_configuration

        return {
            "serviceManagedEc2": capo_deadline.types.service_managed_ec2_fleet_configuration.deserialize_json(
                data["serviceManagedEc2"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FleetConfiguration: no recognized variant key")
