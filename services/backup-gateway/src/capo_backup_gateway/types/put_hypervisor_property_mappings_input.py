"""Generated from Smithy shape ``com.amazonaws.backupgateway#PutHypervisorPropertyMappingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.iam_role_arn
    import capo_backup_gateway.types.server_arn
    import capo_backup_gateway.types.vmware_to_aws_tag_mappings


class PutHypervisorPropertyMappingsInput(TypedDict, closed=True):
    hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn"
    """<p>The Amazon Resource Name (ARN) of the hypervisor.</p>"""
    vmware_to_aws_tag_mappings: (
        "capo_backup_gateway.types.vmware_to_aws_tag_mappings.VmwareToAwsTagMappings"
    )
    """<p>This action requests the mappings of VMware tags to the Amazon Web Services tags.</p>"""
    iam_role_arn: "capo_backup_gateway.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutHypervisorPropertyMappingsInput) -> dict:
    out: dict = {}
    out["HypervisorArn"] = value["hypervisor_arn"]
    import capo_backup_gateway.types.vmware_to_aws_tag_mappings

    out["VmwareToAwsTagMappings"] = (
        capo_backup_gateway.types.vmware_to_aws_tag_mappings.serialize_aws_json_1_0(
            value["vmware_to_aws_tag_mappings"]
        )
    )
    out["IamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutHypervisorPropertyMappingsInput:
    out: PutHypervisorPropertyMappingsInput = {}  # type: ignore[typeddict-item]
    if data.get("HypervisorArn") is not None:
        out["hypervisor_arn"] = data["HypervisorArn"]
    else:
        out["hypervisor_arn"] = ""
    if data.get("VmwareToAwsTagMappings") is not None:
        import capo_backup_gateway.types.vmware_to_aws_tag_mappings

        out["vmware_to_aws_tag_mappings"] = (
            capo_backup_gateway.types.vmware_to_aws_tag_mappings.deserialize_aws_json_1_0(
                data["VmwareToAwsTagMappings"]
            )
        )
    else:
        out["vmware_to_aws_tag_mappings"] = []
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        out["iam_role_arn"] = ""
    return out
