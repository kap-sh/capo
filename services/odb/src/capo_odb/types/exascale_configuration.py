"""Generated from Smithy shape ``com.amazonaws.odb#ExascaleConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class ExascaleConfiguration(TypedDict, closed=True):
    total_storage_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of Exascale storage, in gigabytes (GB), configured on the Exadata infrastructure.</p>"""
    available_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of Exascale storage, in gigabytes (GB), that's available on the Exadata infrastructure.</p>"""
    total_vm_storage_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of Exascale VM storage, in gigabytes (GB), on the Exadata infrastructure. VM clusters use Exascale VM storage for their VM file systems and VM backups.</p>"""
    available_vm_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of Exascale VM storage, in gigabytes (GB), that's available on the Exadata infrastructure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExascaleConfiguration) -> dict:
    out: dict = {}
    if "total_storage_size_in_g_bs" in value:
        out["totalStorageSizeInGBs"] = value["total_storage_size_in_g_bs"]
    if "available_storage_size_in_g_bs" in value:
        out["availableStorageSizeInGBs"] = value["available_storage_size_in_g_bs"]
    if "total_vm_storage_size_in_g_bs" in value:
        out["totalVmStorageSizeInGBs"] = value["total_vm_storage_size_in_g_bs"]
    if "available_vm_storage_size_in_g_bs" in value:
        out["availableVmStorageSizeInGBs"] = value["available_vm_storage_size_in_g_bs"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExascaleConfiguration:
    out: ExascaleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("totalStorageSizeInGBs") is not None:
        out["total_storage_size_in_g_bs"] = data["totalStorageSizeInGBs"]
    if data.get("availableStorageSizeInGBs") is not None:
        out["available_storage_size_in_g_bs"] = data["availableStorageSizeInGBs"]
    if data.get("totalVmStorageSizeInGBs") is not None:
        out["total_vm_storage_size_in_g_bs"] = data["totalVmStorageSizeInGBs"]
    if data.get("availableVmStorageSizeInGBs") is not None:
        out["available_vm_storage_size_in_g_bs"] = data["availableVmStorageSizeInGBs"]
    return out
