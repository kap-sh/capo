"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedConnectorEgressConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError, SerializationError
from capo_transfer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_transfer.types.described_connector_vpc_lattice_egress_config


class DescribedConnectorEgressConfigVpcLatticeMember(TypedDict, closed=True):
    VpcLattice: "capo_transfer.types.described_connector_vpc_lattice_egress_config.DescribedConnectorVpcLatticeEgressConfig"


DescribedConnectorEgressConfig: TypeAlias = (
    DescribedConnectorEgressConfigVpcLatticeMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedConnectorEgressConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DescribedConnectorEgressConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "VpcLattice" in value:
        import capo_transfer.types.described_connector_vpc_lattice_egress_config

        return {
            "VpcLattice": capo_transfer.types.described_connector_vpc_lattice_egress_config.serialize_aws_json_1_1(
                value["VpcLattice"]
            )
        }
    else:
        raise SerializationError("DescribedConnectorEgressConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> DescribedConnectorEgressConfig:
    if data.get("VpcLattice") is not None:
        import capo_transfer.types.described_connector_vpc_lattice_egress_config

        return {
            "VpcLattice": capo_transfer.types.described_connector_vpc_lattice_egress_config.deserialize_aws_json_1_1(
                data["VpcLattice"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DescribedConnectorEgressConfig: no recognized variant key"
        )
