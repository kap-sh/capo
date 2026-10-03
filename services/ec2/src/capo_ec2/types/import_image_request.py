"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boot_mode_values
    import capo_ec2.types.client_data
    import capo_ec2.types.image_disk_container_list
    import capo_ec2.types.import_image_license_specification_list_request
    import capo_ec2.types.kms_key_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class ImportImageRequest(TypedDict, closed=True):
    architecture: NotRequired["capo_ec2.types.string.String"]
    """<p>The architecture of the virtual machine.</p> <p>Valid values: <code>i386</code> | <code>x86_64</code> </p>"""
    client_data: NotRequired["capo_ec2.types.client_data.ClientData"]
    """<p>The client-specific data.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to enable idempotency for VM import requests.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description string for the import image task.</p>"""
    disk_containers: NotRequired[
        "capo_ec2.types.image_disk_container_list.ImageDiskContainerList"
    ]
    """<p>Information about the disk containers.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether the destination AMI of the imported image should be encrypted. The default KMS key for EBS is used unless you specify a non-default KMS key using <code>KmsKeyId</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html">Amazon EBS Encryption</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>"""
    hypervisor: NotRequired["capo_ec2.types.string.String"]
    """<p>The target hypervisor platform.</p> <p>Valid values: <code>xen</code> </p>"""
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>An identifier for the symmetric KMS key to use when creating the encrypted AMI. This parameter is only required if you want to use a non-default KMS key; if this parameter is not specified, the default KMS key for EBS is used. If a <code>KmsKeyId</code> is specified, the <code>Encrypted</code> flag must also be set. </p> <p>The KMS key identifier may be provided in any of the following formats: </p> <ul> <li> <p>Key ID</p> </li> <li> <p>Key alias</p> </li> <li> <p>ARN using key ID. The ID ARN contains the <code>arn:aws:kms</code> namespace, followed by the Region of the key, the Amazon Web Services account ID of the key owner, the <code>key</code> namespace, and then the key ID. For example, arn:aws:kms:<i>us-east-1</i>:<i>012345678910</i>:key/<i>abcd1234-a123-456a-a12b-a123b4cd56ef</i>.</p> </li> <li> <p>ARN using key alias. The alias ARN contains the <code>arn:aws:kms</code> namespace, followed by the Region of the key, the Amazon Web Services account ID of the key owner, the <code>alias</code> namespace, and then the key alias. For example, arn:aws:kms:<i>us-east-1</i>:<i>012345678910</i>:alias/<i>ExampleAlias</i>. </p> </li> </ul> <p>Amazon Web Services parses <code>KmsKeyId</code> asynchronously, meaning that the action you call may appear to complete even though you provided an invalid identifier. This action will eventually report failure. </p> <p>The specified KMS key must exist in the Region that the AMI is being copied to.</p> <p>Amazon EBS does not support asymmetric KMS keys.</p>"""
    license_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The license type to be used for the Amazon Machine Image (AMI) after importing.</p> <p>Specify <code>AWS</code> to replace the source-system license with an Amazon Web Services license or <code>BYOL</code> to retain the source-system license. Leaving this parameter undefined is the same as choosing <code>AWS</code> when importing a Windows Server operating system, and the same as choosing <code>BYOL</code> when importing a Windows client operating system (such as Windows 10) or a Linux operating system.</p> <p>To use <code>BYOL</code>, you must have existing licenses with rights to use these licenses in a third party cloud, such as Amazon Web Services. For more information, see <a href="https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-image-import.html#prerequisites-image">Prerequisites</a> in the VM Import/Export User Guide.</p>"""
    platform: NotRequired["capo_ec2.types.string.String"]
    """<p>The operating system of the virtual machine. If you import a VM that is compatible with Unified Extensible Firmware Interface (UEFI) using an EBS snapshot, you must specify a value for the platform.</p> <p>Valid values: <code>Windows</code> | <code>Linux</code> </p>"""
    role_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the role to use when not using the default role, 'vmimport'.</p>"""
    license_specifications: NotRequired[
        "capo_ec2.types.import_image_license_specification_list_request.ImportImageLicenseSpecificationListRequest"
    ]
    """<p>The ARNs of the license configurations.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the import image task during creation.</p>"""
    usage_operation: NotRequired["capo_ec2.types.string.String"]
    """<p>The usage operation value. For more information, see <a href="https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#prerequisites">Licensing options</a> in the <i>VM Import/Export User Guide</i>.</p>"""
    boot_mode: NotRequired["capo_ec2.types.boot_mode_values.BootModeValues"]
    """<p>The boot mode of the virtual machine.</p> <note> <p>The <code>uefi-preferred</code> boot mode isn't supported for importing images. For more information, see <a href="https://docs.aws.amazon.com/vm-import/latest/userguide/prerequisites.html#vmimport-boot-modes">Boot modes</a> in the <i>VM Import/Export User Guide</i>.</p> </note>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportImageRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "architecture" in value:
        pairs.append((f"{key_prefix}Architecture", str(value["architecture"])))
    if "client_data" in value:
        import capo_ec2.types.client_data

        capo_ec2.types.client_data.serialize_ec2_query(
            value["client_data"], pairs, f"{key_prefix}ClientData"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "disk_containers" in value:
        import capo_ec2.types.image_disk_container_list

        capo_ec2.types.image_disk_container_list.serialize_ec2_query(
            value["disk_containers"], pairs, f"{key_prefix}DiskContainer"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "hypervisor" in value:
        pairs.append((f"{key_prefix}Hypervisor", str(value["hypervisor"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "license_type" in value:
        pairs.append((f"{key_prefix}LicenseType", str(value["license_type"])))
    if "platform" in value:
        pairs.append((f"{key_prefix}Platform", str(value["platform"])))
    if "role_name" in value:
        pairs.append((f"{key_prefix}RoleName", str(value["role_name"])))
    if "license_specifications" in value:
        import capo_ec2.types.import_image_license_specification_list_request

        capo_ec2.types.import_image_license_specification_list_request.serialize_ec2_query(
            value["license_specifications"], pairs, f"{key_prefix}LicenseSpecifications"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "usage_operation" in value:
        pairs.append((f"{key_prefix}UsageOperation", str(value["usage_operation"])))
    if "boot_mode" in value:
        import capo_ec2.types.boot_mode_values

        capo_ec2.types.boot_mode_values.serialize_ec2_query(
            value["boot_mode"], pairs, f"{key_prefix}BootMode"
        )


def deserialize_ec2_query(el: Element) -> ImportImageRequest:
    out: ImportImageRequest = {}  # type: ignore[typeddict-item]
    child_architecture = el.find("Architecture")
    if child_architecture is not None:
        out["architecture"] = str(child_architecture.text or "")
    child_client_data = el.find("ClientData")
    if child_client_data is not None:
        import capo_ec2.types.client_data

        out["client_data"] = capo_ec2.types.client_data.deserialize_ec2_query(
            child_client_data
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_disk_containers = el.find("DiskContainer")
    if child_disk_containers is not None:
        import capo_ec2.types.image_disk_container_list

        out["disk_containers"] = (
            capo_ec2.types.image_disk_container_list.deserialize_ec2_query(
                child_disk_containers
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_hypervisor = el.find("Hypervisor")
    if child_hypervisor is not None:
        out["hypervisor"] = str(child_hypervisor.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_license_type = el.find("LicenseType")
    if child_license_type is not None:
        out["license_type"] = str(child_license_type.text or "")
    child_platform = el.find("Platform")
    if child_platform is not None:
        out["platform"] = str(child_platform.text or "")
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    child_license_specifications = el.find("LicenseSpecifications")
    if child_license_specifications is not None:
        import capo_ec2.types.import_image_license_specification_list_request

        out["license_specifications"] = (
            capo_ec2.types.import_image_license_specification_list_request.deserialize_ec2_query(
                child_license_specifications
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_usage_operation = el.find("UsageOperation")
    if child_usage_operation is not None:
        out["usage_operation"] = str(child_usage_operation.text or "")
    child_boot_mode = el.find("BootMode")
    if child_boot_mode is not None:
        import capo_ec2.types.boot_mode_values

        out["boot_mode"] = capo_ec2.types.boot_mode_values.deserialize_ec2_query(
            child_boot_mode
        )
    return out
