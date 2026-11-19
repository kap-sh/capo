"""Generated from Smithy shape ``com.amazonaws.backupgateway#GetHypervisorPropertyMappingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.iam_role_arn
    import capo_backup_gateway.types.server_arn
    import capo_backup_gateway.types.vmware_to_aws_tag_mappings


class GetHypervisorPropertyMappingsOutput(TypedDict, closed=True):
    hypervisor_arn: NotRequired["capo_backup_gateway.types.server_arn.ServerArn"]
    """<p>The Amazon Resource Name (ARN) of the hypervisor.</p>"""
    vmware_to_aws_tag_mappings: NotRequired[
        "capo_backup_gateway.types.vmware_to_aws_tag_mappings.VmwareToAwsTagMappings"
    ]
    """<p>This is a display of the mappings of VMware tags to the Amazon Web Services tags.</p>"""
    iam_role_arn: NotRequired["capo_backup_gateway.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetHypervisorPropertyMappingsOutput) -> dict:
    out: dict = {}
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    if "vmware_to_aws_tag_mappings" in value:
        import capo_backup_gateway.types.vmware_to_aws_tag_mappings

        out["VmwareToAwsTagMappings"] = (
            capo_backup_gateway.types.vmware_to_aws_tag_mappings.serialize_aws_json_1_0(
                value["vmware_to_aws_tag_mappings"]
            )
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetHypervisorPropertyMappingsOutput:
    out: GetHypervisorPropertyMappingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    if data.get("VmwareToAwsTagMappings") is not None:
        import capo_backup_gateway.types.vmware_to_aws_tag_mappings

        out["vmware_to_aws_tag_mappings"] = (
            capo_backup_gateway.types.vmware_to_aws_tag_mappings.deserialize_aws_json_1_0(
                data["VmwareToAwsTagMappings"]
            )
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetHypervisorPropertyMappingsOutput) -> dict:
    out: dict = {}
    if "hypervisor_arn" in value:
        out["HypervisorArn"] = value["hypervisor_arn"]
    if "vmware_to_aws_tag_mappings" in value:
        import capo_backup_gateway.types.vmware_to_aws_tag_mappings

        out["VmwareToAwsTagMappings"] = (
            capo_backup_gateway.types.vmware_to_aws_tag_mappings.serialize_cbor(
                value["vmware_to_aws_tag_mappings"]
            )
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_cbor(data: dict) -> GetHypervisorPropertyMappingsOutput:
    out: GetHypervisorPropertyMappingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    if data.get("VmwareToAwsTagMappings") is not None:
        import capo_backup_gateway.types.vmware_to_aws_tag_mappings

        out["vmware_to_aws_tag_mappings"] = (
            capo_backup_gateway.types.vmware_to_aws_tag_mappings.deserialize_cbor(
                data["VmwareToAwsTagMappings"]
            )
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    return out
