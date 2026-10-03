"""Generated from Smithy shape ``com.amazonaws.emr#SupportedInstanceType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.boolean
    import capo_emr.types.float
    import capo_emr.types.integer
    import capo_emr.types.string


class SupportedInstanceType(TypedDict, closed=True):
    type: NotRequired["capo_emr.types.string.String"]
    """<p>The <a href="http://aws.amazon.com/ec2/instance-types/">Amazon EC2 instance type</a>, for example <code>m5.xlarge</code>, of the <code>SupportedInstanceType</code>.</p>"""
    memory_gb: NotRequired["capo_emr.types.float.Float"]
    """<p>The amount of memory that is available to Amazon EMR from the <code>SupportedInstanceType</code>. The kernel and hypervisor software consume some memory, so this value might be lower than the overall memory for the instance type.</p>"""
    storage_gb: NotRequired["capo_emr.types.integer.Integer"]
    """<p> <code>StorageGB</code> represents the storage capacity of the <code>SupportedInstanceType</code>. This value is <code>0</code> for Amazon EBS-only instance types.</p>"""
    vcpu: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The number of vCPUs available for the <code>SupportedInstanceType</code>.</p>"""
    is64_bits_only: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Indicates whether the <code>SupportedInstanceType</code> only supports 64-bit architecture.</p>"""
    instance_family_id: NotRequired["capo_emr.types.string.String"]
    """<p>The Amazon EC2 family and generation for the <code>SupportedInstanceType</code>.</p>"""
    ebs_optimized_available: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Indicates whether the <code>SupportedInstanceType</code> supports Amazon EBS optimization.</p>"""
    ebs_optimized_by_default: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Indicates whether the <code>SupportedInstanceType</code> uses Amazon EBS optimization by default.</p>"""
    number_of_disks: NotRequired["capo_emr.types.integer.Integer"]
    """<p>Number of disks for the <code>SupportedInstanceType</code>. This value is <code>0</code> for Amazon EBS-only instance types.</p>"""
    ebs_storage_only: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Indicates whether the <code>SupportedInstanceType</code> only supports Amazon EBS.</p>"""
    architecture: NotRequired["capo_emr.types.string.String"]
    """<p>The CPU architecture, for example <code>X86_64</code> or <code>AARCH64</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedInstanceType) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "memory_gb" in value:
        out["MemoryGB"] = (
            "NaN"
            if value["memory_gb"] != value["memory_gb"]
            else "Infinity"
            if value["memory_gb"] == float("inf")
            else "-Infinity"
            if value["memory_gb"] == float("-inf")
            else value["memory_gb"]
        )
    if "storage_gb" in value:
        out["StorageGB"] = value["storage_gb"]
    if "vcpu" in value:
        out["VCPU"] = value["vcpu"]
    if "is64_bits_only" in value:
        out["Is64BitsOnly"] = value["is64_bits_only"]
    if "instance_family_id" in value:
        out["InstanceFamilyId"] = value["instance_family_id"]
    if "ebs_optimized_available" in value:
        out["EbsOptimizedAvailable"] = value["ebs_optimized_available"]
    if "ebs_optimized_by_default" in value:
        out["EbsOptimizedByDefault"] = value["ebs_optimized_by_default"]
    if "number_of_disks" in value:
        out["NumberOfDisks"] = value["number_of_disks"]
    if "ebs_storage_only" in value:
        out["EbsStorageOnly"] = value["ebs_storage_only"]
    if "architecture" in value:
        out["Architecture"] = value["architecture"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SupportedInstanceType:
    out: SupportedInstanceType = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("MemoryGB") is not None:
        out["memory_gb"] = float(data["MemoryGB"])
    if data.get("StorageGB") is not None:
        out["storage_gb"] = data["StorageGB"]
    if data.get("VCPU") is not None:
        out["vcpu"] = data["VCPU"]
    if data.get("Is64BitsOnly") is not None:
        out["is64_bits_only"] = data["Is64BitsOnly"]
    if data.get("InstanceFamilyId") is not None:
        out["instance_family_id"] = data["InstanceFamilyId"]
    if data.get("EbsOptimizedAvailable") is not None:
        out["ebs_optimized_available"] = data["EbsOptimizedAvailable"]
    if data.get("EbsOptimizedByDefault") is not None:
        out["ebs_optimized_by_default"] = data["EbsOptimizedByDefault"]
    if data.get("NumberOfDisks") is not None:
        out["number_of_disks"] = data["NumberOfDisks"]
    if data.get("EbsStorageOnly") is not None:
        out["ebs_storage_only"] = data["EbsStorageOnly"]
    if data.get("Architecture") is not None:
        out["architecture"] = data["Architecture"]
    return out
