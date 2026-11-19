"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlExclusions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc_encryption_control_exclusion

VpcEncryptionControlExclusions = TypedDict(
    "VpcEncryptionControlExclusions",
    {
        "internet_gateway": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "egress_only_internet_gateway": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "nat_gateway": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "virtual_private_gateway": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "vpc_peering": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "lambda": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "vpc_lattice": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "elastic_file_system": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "global_accelerator": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "api_gateway_v2": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionControlExclusions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "internet_gateway" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["internet_gateway"], pairs, f"{key_prefix}InternetGateway"
        )
    if "egress_only_internet_gateway" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["egress_only_internet_gateway"],
            pairs,
            f"{key_prefix}EgressOnlyInternetGateway",
        )
    if "nat_gateway" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["nat_gateway"], pairs, f"{key_prefix}NatGateway"
        )
    if "virtual_private_gateway" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["virtual_private_gateway"],
            pairs,
            f"{key_prefix}VirtualPrivateGateway",
        )
    if "vpc_peering" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["vpc_peering"], pairs, f"{key_prefix}VpcPeering"
        )
    if "lambda" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["lambda"], pairs, f"{key_prefix}Lambda"
        )
    if "vpc_lattice" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["vpc_lattice"], pairs, f"{key_prefix}VpcLattice"
        )
    if "elastic_file_system" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["elastic_file_system"], pairs, f"{key_prefix}ElasticFileSystem"
        )
    if "global_accelerator" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["global_accelerator"], pairs, f"{key_prefix}GlobalAccelerator"
        )
    if "api_gateway_v2" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion

        capo_ec2.types.vpc_encryption_control_exclusion.serialize_ec2_query(
            value["api_gateway_v2"], pairs, f"{key_prefix}ApiGatewayV2"
        )


def deserialize_ec2_query(el: Element) -> VpcEncryptionControlExclusions:
    out: VpcEncryptionControlExclusions = {}  # type: ignore[typeddict-item]
    child_internet_gateway = el.find("internetGateway")
    if child_internet_gateway is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["internet_gateway"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_internet_gateway
            )
        )
    child_egress_only_internet_gateway = el.find("egressOnlyInternetGateway")
    if child_egress_only_internet_gateway is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["egress_only_internet_gateway"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_egress_only_internet_gateway
            )
        )
    child_nat_gateway = el.find("natGateway")
    if child_nat_gateway is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["nat_gateway"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_nat_gateway
            )
        )
    child_virtual_private_gateway = el.find("virtualPrivateGateway")
    if child_virtual_private_gateway is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["virtual_private_gateway"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_virtual_private_gateway
            )
        )
    child_vpc_peering = el.find("vpcPeering")
    if child_vpc_peering is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["vpc_peering"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_vpc_peering
            )
        )
    child_lambda = el.find("lambda")
    if child_lambda is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["lambda"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_lambda
            )
        )
    child_vpc_lattice = el.find("vpcLattice")
    if child_vpc_lattice is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["vpc_lattice"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_vpc_lattice
            )
        )
    child_elastic_file_system = el.find("elasticFileSystem")
    if child_elastic_file_system is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["elastic_file_system"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_elastic_file_system
            )
        )
    child_global_accelerator = el.find("globalAccelerator")
    if child_global_accelerator is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["global_accelerator"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_global_accelerator
            )
        )
    child_api_gateway_v2 = el.find("apiGatewayV2")
    if child_api_gateway_v2 is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion

        out["api_gateway_v2"] = (
            capo_ec2.types.vpc_encryption_control_exclusion.deserialize_ec2_query(
                child_api_gateway_v2
            )
        )
    return out
