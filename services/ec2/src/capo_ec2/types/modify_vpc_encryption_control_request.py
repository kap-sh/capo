"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEncryptionControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.vpc_encryption_control_exclusion_state_input
    import capo_ec2.types.vpc_encryption_control_id
    import capo_ec2.types.vpc_encryption_control_mode


class ModifyVpcEncryptionControlRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_encryption_control_id: NotRequired[
        "capo_ec2.types.vpc_encryption_control_id.VpcEncryptionControlId"
    ]
    """<p>The ID of the VPC Encryption Control resource to modify.</p>"""
    mode: NotRequired[
        "capo_ec2.types.vpc_encryption_control_mode.VpcEncryptionControlMode"
    ]
    """<p>The encryption mode for the VPC Encryption Control configuration.</p>"""
    internet_gateway_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude internet gateway traffic from encryption enforcement.</p>"""
    egress_only_internet_gateway_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude egress-only internet gateway traffic from encryption enforcement.</p>"""
    nat_gateway_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude NAT gateway traffic from encryption enforcement.</p>"""
    virtual_private_gateway_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude virtual private gateway traffic from encryption enforcement.</p>"""
    vpc_peering_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude VPC peering connection traffic from encryption enforcement.</p>"""
    lambda_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude Lambda function traffic from encryption enforcement.</p>"""
    vpc_lattice_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude VPC Lattice traffic from encryption enforcement.</p>"""
    elastic_file_system_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude Elastic File System traffic from encryption enforcement.</p>"""
    global_accelerator_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude Amazon Web Services Global Accelerator traffic from encryption enforcement.</p>"""
    api_gateway_v2_exclusion: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusion_state_input.VpcEncryptionControlExclusionStateInput"
    ]
    """<p>Specifies whether to exclude Amazon API Gateway V2 traffic from encryption enforcement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcEncryptionControlRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "vpc_encryption_control_id" in value:
        pairs.append(
            (
                f"{key_prefix}VpcEncryptionControlId",
                str(value["vpc_encryption_control_id"]),
            )
        )
    if "mode" in value:
        import capo_ec2.types.vpc_encryption_control_mode

        capo_ec2.types.vpc_encryption_control_mode.serialize_ec2_query(
            value["mode"], pairs, f"{key_prefix}Mode"
        )
    if "internet_gateway_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["internet_gateway_exclusion"],
            pairs,
            f"{key_prefix}InternetGatewayExclusion",
        )
    if "egress_only_internet_gateway_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["egress_only_internet_gateway_exclusion"],
            pairs,
            f"{key_prefix}EgressOnlyInternetGatewayExclusion",
        )
    if "nat_gateway_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["nat_gateway_exclusion"], pairs, f"{key_prefix}NatGatewayExclusion"
        )
    if "virtual_private_gateway_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["virtual_private_gateway_exclusion"],
            pairs,
            f"{key_prefix}VirtualPrivateGatewayExclusion",
        )
    if "vpc_peering_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["vpc_peering_exclusion"], pairs, f"{key_prefix}VpcPeeringExclusion"
        )
    if "lambda_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["lambda_exclusion"], pairs, f"{key_prefix}LambdaExclusion"
        )
    if "vpc_lattice_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["vpc_lattice_exclusion"], pairs, f"{key_prefix}VpcLatticeExclusion"
        )
    if "elastic_file_system_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["elastic_file_system_exclusion"],
            pairs,
            f"{key_prefix}ElasticFileSystemExclusion",
        )
    if "global_accelerator_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["global_accelerator_exclusion"],
            pairs,
            f"{key_prefix}GlobalAcceleratorExclusion",
        )
    if "api_gateway_v2_exclusion" in value:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        capo_ec2.types.vpc_encryption_control_exclusion_state_input.serialize_ec2_query(
            value["api_gateway_v2_exclusion"],
            pairs,
            f"{key_prefix}ApiGatewayV2Exclusion",
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcEncryptionControlRequest:
    out: ModifyVpcEncryptionControlRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_vpc_encryption_control_id = el.find("VpcEncryptionControlId")
    if child_vpc_encryption_control_id is not None:
        out["vpc_encryption_control_id"] = str(
            child_vpc_encryption_control_id.text or ""
        )
    child_mode = el.find("Mode")
    if child_mode is not None:
        import capo_ec2.types.vpc_encryption_control_mode

        out["mode"] = capo_ec2.types.vpc_encryption_control_mode.deserialize_ec2_query(
            child_mode
        )
    child_internet_gateway_exclusion = el.find("InternetGatewayExclusion")
    if child_internet_gateway_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["internet_gateway_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_internet_gateway_exclusion
            )
        )
    child_egress_only_internet_gateway_exclusion = el.find(
        "EgressOnlyInternetGatewayExclusion"
    )
    if child_egress_only_internet_gateway_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["egress_only_internet_gateway_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_egress_only_internet_gateway_exclusion
            )
        )
    child_nat_gateway_exclusion = el.find("NatGatewayExclusion")
    if child_nat_gateway_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["nat_gateway_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_nat_gateway_exclusion
            )
        )
    child_virtual_private_gateway_exclusion = el.find("VirtualPrivateGatewayExclusion")
    if child_virtual_private_gateway_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["virtual_private_gateway_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_virtual_private_gateway_exclusion
            )
        )
    child_vpc_peering_exclusion = el.find("VpcPeeringExclusion")
    if child_vpc_peering_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["vpc_peering_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_vpc_peering_exclusion
            )
        )
    child_lambda_exclusion = el.find("LambdaExclusion")
    if child_lambda_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["lambda_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_lambda_exclusion
            )
        )
    child_vpc_lattice_exclusion = el.find("VpcLatticeExclusion")
    if child_vpc_lattice_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["vpc_lattice_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_vpc_lattice_exclusion
            )
        )
    child_elastic_file_system_exclusion = el.find("ElasticFileSystemExclusion")
    if child_elastic_file_system_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["elastic_file_system_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_elastic_file_system_exclusion
            )
        )
    child_global_accelerator_exclusion = el.find("GlobalAcceleratorExclusion")
    if child_global_accelerator_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["global_accelerator_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_global_accelerator_exclusion
            )
        )
    child_api_gateway_v2_exclusion = el.find("ApiGatewayV2Exclusion")
    if child_api_gateway_v2_exclusion is not None:
        import capo_ec2.types.vpc_encryption_control_exclusion_state_input

        out["api_gateway_v2_exclusion"] = (
            capo_ec2.types.vpc_encryption_control_exclusion_state_input.deserialize_ec2_query(
                child_api_gateway_v2_exclusion
            )
        )
    return out
