"""Generated from Smithy shape ``com.amazonaws.inspector2#MachineImageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.architecture
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.platform
    import capo_inspector2.types.provider_account_id


class MachineImageDetails(TypedDict, closed=True):
    machine_image_id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """The machine image ID (e.g., ami-0abcdef1234567890)"""
    name: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """Human-readable image name"""
    owner_account_id: NotRequired[
        "capo_inspector2.types.provider_account_id.ProviderAccountId"
    ]
    """Account ID that owns the image"""
    platform: NotRequired["capo_inspector2.types.platform.Platform"]
    """OS platform (Linux/Windows)"""
    architecture: NotRequired["capo_inspector2.types.architecture.Architecture"]
    """CPU architecture (x86_64/arm64)"""
    creation_date: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """When the image was created"""
    state: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """Image state (available/pending/deregistered)"""
    is_public: NotRequired["bool"]
    """Whether the image is publicly shared"""
    root_device_type: NotRequired[
        "capo_inspector2.types.non_empty_string.NonEmptyString"
    ]
    """Root device type (ebs/instance-store) — AWS-specific"""
    virtualization_type: NotRequired[
        "capo_inspector2.types.non_empty_string.NonEmptyString"
    ]
    """Virtualization type (hvm/paravirtual) — AWS-specific"""
    source_resource_id: NotRequired[
        "capo_inspector2.types.non_empty_string.NonEmptyString"
    ]
    """Source resource the image was created from (nullable)"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineImageDetails) -> dict:
    out: dict = {}
    out["machineImageId"] = value["machine_image_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "owner_account_id" in value:
        out["ownerAccountId"] = value["owner_account_id"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "creation_date" in value:
        import capo_inspector2.types.date_time_timestamp

        out["creationDate"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["creation_date"]
        )
    if "state" in value:
        out["state"] = value["state"]
    if "is_public" in value:
        out["isPublic"] = value["is_public"]
    if "root_device_type" in value:
        out["rootDeviceType"] = value["root_device_type"]
    if "virtualization_type" in value:
        out["virtualizationType"] = value["virtualization_type"]
    if "source_resource_id" in value:
        out["sourceResourceId"] = value["source_resource_id"]
    return out


def deserialize_json(data: dict) -> MachineImageDetails:
    out: MachineImageDetails = {}  # type: ignore[typeddict-item]
    if data.get("machineImageId") is not None:
        out["machine_image_id"] = data["machineImageId"]
    else:
        out["machine_image_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    if data.get("creationDate") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["creation_date"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["creationDate"]
            )
        )
    if data.get("state") is not None:
        out["state"] = data["state"]
    if data.get("isPublic") is not None:
        out["is_public"] = data["isPublic"]
    if data.get("rootDeviceType") is not None:
        out["root_device_type"] = data["rootDeviceType"]
    if data.get("virtualizationType") is not None:
        out["virtualization_type"] = data["virtualizationType"]
    if data.get("sourceResourceId") is not None:
        out["source_resource_id"] = data["sourceResourceId"]
    return out
