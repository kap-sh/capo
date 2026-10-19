"""Generated from Smithy shape ``com.amazonaws.transfer#ConnectorEgressConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError
from capo_transfer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_transfer.types.connector_vpc_lattice_egress_config


class _ConnectorEgressConfig_VpcLattice(TypedDict, closed=True):
    VpcLattice: "capo_transfer.types.connector_vpc_lattice_egress_config.ConnectorVpcLatticeEgressConfig"


ConnectorEgressConfig: TypeAlias = (
    _ConnectorEgressConfig_VpcLattice | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorEgressConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ConnectorEgressConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "VpcLattice" in value:
        import capo_transfer.types.connector_vpc_lattice_egress_config

        return {
            "VpcLattice": capo_transfer.types.connector_vpc_lattice_egress_config.serialize_aws_json_1_1(
                value["VpcLattice"]
            )
        }
    else:
        raise SerializationError("ConnectorEgressConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ConnectorEgressConfig:
    if data.get("VpcLattice") is not None:
        import capo_transfer.types.connector_vpc_lattice_egress_config

        return {
            "VpcLattice": capo_transfer.types.connector_vpc_lattice_egress_config.deserialize_aws_json_1_1(
                data["VpcLattice"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ConnectorEgressConfig: no recognized variant key")
