"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyAccountVpcEncryptionControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_vpc_encryption_control_mode
    import capo_ec2.types.boolean
    import capo_ec2.types.vpc_encryption_control_exclusion_state_input

ModifyAccountVpcEncryptionControlRequest = TypedDict(
    "ModifyAccountVpcEncryptionControlRequest",
    {
        "dry_run": NotRequired["capo_ec2.types.boolean.Boolean"],
        "mode": NotRequired[
            "capo_ec2.types.account_vpc_encryption_control_mode.AccountVpcEncryptionControlMode"
        ],
        "internet_gateway": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
        "egress_only_internet_gateway": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
        "nat_gateway": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
        "virtual_private_gateway": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
        "vpc_peering": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
        "lambda": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
        "vpc_lattice": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
        "elastic_file_system": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
        "global_accelerator": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
        "api_gateway_v2": NotRequired[
            "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
        ],
    },
    closed=True,
)


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyAccountVpcEncryptionControlRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "mode" in value:
        import capo_ec2.types.account_vpc_encryption_control_mode

        capo_ec2.types.account_vpc_encryption_control_mode.serialize_ec2_query(
            value["mode"], pairs, f"{key_prefix}Mode"
        )
    if "internet_gateway" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["internet_gateway"], pairs, f"{key_prefix}InternetGateway"
        )
    if "egress_only_internet_gateway" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["egress_only_internet_gateway"],
            pairs,
            f"{key_prefix}EgressOnlyInternetGateway",
        )
    if "nat_gateway" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["nat_gateway"], pairs, f"{key_prefix}NatGateway"
        )
    if "virtual_private_gateway" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["virtual_private_gateway"],
            pairs,
            f"{key_prefix}VirtualPrivateGateway",
        )
    if "vpc_peering" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["vpc_peering"], pairs, f"{key_prefix}VpcPeering"
        )
    if "lambda" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["lambda"], pairs, f"{key_prefix}Lambda"
        )
    if "vpc_lattice" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["vpc_lattice"], pairs, f"{key_prefix}VpcLattice"
        )
    if "elastic_file_system" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["elastic_file_system"], pairs, f"{key_prefix}ElasticFileSystem"
        )
    if "global_accelerator" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["global_accelerator"], pairs, f"{key_prefix}GlobalAccelerator"
        )
    if "api_gateway_v2" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["api_gateway_v2"], pairs, f"{key_prefix}ApiGatewayV2"
        )


def deserialize_ec2_query(el: Element) -> ModifyAccountVpcEncryptionControlRequest:
    out: ModifyAccountVpcEncryptionControlRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_mode = el.find("Mode")
    if child_mode is not None:
        import capo_ec2.types.account_vpc_encryption_control_mode

        out["mode"] = (
            capo_ec2.types.account_vpc_encryption_control_mode.deserialize_ec2_query(
                child_mode
            )
        )
    child_internet_gateway = el.find("InternetGateway")
    if child_internet_gateway is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["internet_gateway"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_internet_gateway
            )
        )
    child_egress_only_internet_gateway = el.find("EgressOnlyInternetGateway")
    if child_egress_only_internet_gateway is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["egress_only_internet_gateway"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_egress_only_internet_gateway
            )
        )
    child_nat_gateway = el.find("NatGateway")
    if child_nat_gateway is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["nat_gateway"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_nat_gateway
            )
        )
    child_virtual_private_gateway = el.find("VirtualPrivateGateway")
    if child_virtual_private_gateway is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["virtual_private_gateway"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_virtual_private_gateway
            )
        )
    child_vpc_peering = el.find("VpcPeering")
    if child_vpc_peering is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["vpc_peering"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_vpc_peering
            )
        )
    child_lambda = el.find("Lambda")
    if child_lambda is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["lambda"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_lambda
            )
        )
    child_vpc_lattice = el.find("VpcLattice")
    if child_vpc_lattice is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["vpc_lattice"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_vpc_lattice
            )
        )
    child_elastic_file_system = el.find("ElasticFileSystem")
    if child_elastic_file_system is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["elastic_file_system"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_elastic_file_system
            )
        )
    child_global_accelerator = el.find("GlobalAccelerator")
    if child_global_accelerator is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["global_accelerator"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_global_accelerator
            )
        )
    child_api_gateway_v2 = el.find("ApiGatewayV2")
    if child_api_gateway_v2 is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["api_gateway_v2"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_api_gateway_v2
            )
        )
    return out
