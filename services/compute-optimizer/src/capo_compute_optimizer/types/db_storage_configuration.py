"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#DBStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.allocated_storage
    import capo_compute_optimizer.types.nullable_iops
    import capo_compute_optimizer.types.nullable_max_allocated_storage
    import capo_compute_optimizer.types.nullable_storage_throughput
    import capo_compute_optimizer.types.storage_type


class DBStorageConfiguration(TypedDict, closed=True):
    storage_type: NotRequired["capo_compute_optimizer.types.storage_type.StorageType"]
    """<p> The type of DB storage. </p>"""
    allocated_storage: "capo_compute_optimizer.types.allocated_storage.AllocatedStorage"
    """<p> The size of the DB storage in gigabytes (GB). </p>"""
    iops: NotRequired["capo_compute_optimizer.types.nullable_iops.NullableIOPS"]
    """<p> The provisioned IOPs of the DB storage. </p>"""
    max_allocated_storage: NotRequired[
        "capo_compute_optimizer.types.nullable_max_allocated_storage.NullableMaxAllocatedStorage"
    ]
    """<p> The maximum limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance. </p>"""
    storage_throughput: NotRequired[
        "capo_compute_optimizer.types.nullable_storage_throughput.NullableStorageThroughput"
    ]
    """<p> The storage throughput of the DB storage. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DBStorageConfiguration) -> dict:
    out: dict = {}
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    out["allocatedStorage"] = value.get("allocated_storage", 0)
    if "iops" in value:
        out["iops"] = value["iops"]
    if "max_allocated_storage" in value:
        out["maxAllocatedStorage"] = value["max_allocated_storage"]
    if "storage_throughput" in value:
        out["storageThroughput"] = value["storage_throughput"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DBStorageConfiguration:
    out: DBStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    if data.get("allocatedStorage") is not None:
        out["allocated_storage"] = data["allocatedStorage"]
    else:
        out["allocated_storage"] = 0
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("maxAllocatedStorage") is not None:
        out["max_allocated_storage"] = data["maxAllocatedStorage"]
    if data.get("storageThroughput") is not None:
        out["storage_throughput"] = data["storageThroughput"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DBStorageConfiguration) -> dict:
    out: dict = {}
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    out["allocatedStorage"] = value.get("allocated_storage", 0)
    if "iops" in value:
        out["iops"] = value["iops"]
    if "max_allocated_storage" in value:
        out["maxAllocatedStorage"] = value["max_allocated_storage"]
    if "storage_throughput" in value:
        out["storageThroughput"] = value["storage_throughput"]
    return out


def deserialize_cbor(data: dict) -> DBStorageConfiguration:
    out: DBStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    if data.get("allocatedStorage") is not None:
        out["allocated_storage"] = data["allocatedStorage"]
    else:
        out["allocated_storage"] = 0
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("maxAllocatedStorage") is not None:
        out["max_allocated_storage"] = data["maxAllocatedStorage"]
    if data.get("storageThroughput") is not None:
        out["storage_throughput"] = data["storageThroughput"]
    return out
