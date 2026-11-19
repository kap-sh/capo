"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CpuOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.amd_sev_snp_enum
    import capo_workspaces_instances.types.nested_virtualization_enum
    import capo_workspaces_instances.types.non_negative_integer


class CpuOptionsRequest(TypedDict, closed=True):
    amd_sev_snp: NotRequired[
        "capo_workspaces_instances.types.amd_sev_snp_enum.AmdSevSnpEnum"
    ]
    """<p>AMD Secure Encrypted Virtualization configuration.</p>"""
    core_count: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Number of CPU cores to allocate.</p>"""
    threads_per_core: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Number of threads per CPU core.</p>"""
    nested_virtualization: NotRequired[
        "capo_workspaces_instances.types.nested_virtualization_enum.NestedVirtualizationEnum"
    ]
    """<p>Specifies whether to enable or disable nested virtualization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CpuOptionsRequest) -> dict:
    out: dict = {}
    if "amd_sev_snp" in value:
        import capo_workspaces_instances.types.amd_sev_snp_enum

        out["AmdSevSnp"] = (
            capo_workspaces_instances.types.amd_sev_snp_enum.serialize_aws_json_1_0(
                value["amd_sev_snp"]
            )
        )
    if "core_count" in value:
        out["CoreCount"] = value["core_count"]
    if "threads_per_core" in value:
        out["ThreadsPerCore"] = value["threads_per_core"]
    if "nested_virtualization" in value:
        import capo_workspaces_instances.types.nested_virtualization_enum

        out["NestedVirtualization"] = (
            capo_workspaces_instances.types.nested_virtualization_enum.serialize_aws_json_1_0(
                value["nested_virtualization"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CpuOptionsRequest:
    out: CpuOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AmdSevSnp") is not None:
        import capo_workspaces_instances.types.amd_sev_snp_enum

        out["amd_sev_snp"] = (
            capo_workspaces_instances.types.amd_sev_snp_enum.deserialize_aws_json_1_0(
                data["AmdSevSnp"]
            )
        )
    if data.get("CoreCount") is not None:
        out["core_count"] = data["CoreCount"]
    if data.get("ThreadsPerCore") is not None:
        out["threads_per_core"] = data["ThreadsPerCore"]
    if data.get("NestedVirtualization") is not None:
        import capo_workspaces_instances.types.nested_virtualization_enum

        out["nested_virtualization"] = (
            capo_workspaces_instances.types.nested_virtualization_enum.deserialize_aws_json_1_0(
                data["NestedVirtualization"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CpuOptionsRequest) -> dict:
    out: dict = {}
    if "amd_sev_snp" in value:
        import capo_workspaces_instances.types.amd_sev_snp_enum

        out["AmdSevSnp"] = (
            capo_workspaces_instances.types.amd_sev_snp_enum.serialize_cbor(
                value["amd_sev_snp"]
            )
        )
    if "core_count" in value:
        out["CoreCount"] = value["core_count"]
    if "threads_per_core" in value:
        out["ThreadsPerCore"] = value["threads_per_core"]
    if "nested_virtualization" in value:
        import capo_workspaces_instances.types.nested_virtualization_enum

        out["NestedVirtualization"] = (
            capo_workspaces_instances.types.nested_virtualization_enum.serialize_cbor(
                value["nested_virtualization"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CpuOptionsRequest:
    out: CpuOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AmdSevSnp") is not None:
        import capo_workspaces_instances.types.amd_sev_snp_enum

        out["amd_sev_snp"] = (
            capo_workspaces_instances.types.amd_sev_snp_enum.deserialize_cbor(
                data["AmdSevSnp"]
            )
        )
    if data.get("CoreCount") is not None:
        out["core_count"] = data["CoreCount"]
    if data.get("ThreadsPerCore") is not None:
        out["threads_per_core"] = data["ThreadsPerCore"]
    if data.get("NestedVirtualization") is not None:
        import capo_workspaces_instances.types.nested_virtualization_enum

        out["nested_virtualization"] = (
            capo_workspaces_instances.types.nested_virtualization_enum.deserialize_cbor(
                data["NestedVirtualization"]
            )
        )
    return out
