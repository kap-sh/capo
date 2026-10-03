"""Generated from Smithy shape ``com.amazonaws.ec2#CpuOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.amd_sev_snp_specification
    import capo_ec2.types.integer
    import capo_ec2.types.nested_virtualization_specification


class CpuOptions(TypedDict, closed=True):
    core_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of CPU cores for the instance.</p>"""
    threads_per_core: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of threads per CPU core.</p>"""
    amd_sev_snp: NotRequired[
        "capo_ec2.types.amd_sev_snp_specification.AmdSevSnpSpecification"
    ]
    """<p>Indicates whether the instance is enabled for AMD SEV-SNP. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html">AMD SEV-SNP</a>.</p>"""
    nested_virtualization: NotRequired[
        "capo_ec2.types.nested_virtualization_specification.NestedVirtualizationSpecification"
    ]
    """<p>Indicates whether the instance is enabled for nested virtualization.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CpuOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "core_count" in value:
        pairs.append((f"{key_prefix}CoreCount", str(value["core_count"])))
    if "threads_per_core" in value:
        pairs.append((f"{key_prefix}ThreadsPerCore", str(value["threads_per_core"])))
    if "amd_sev_snp" in value:
        import capo_ec2.types.amd_sev_snp_specification

        capo_ec2.types.amd_sev_snp_specification.serialize_ec2_query(
            value["amd_sev_snp"], pairs, f"{key_prefix}AmdSevSnp"
        )
    if "nested_virtualization" in value:
        import capo_ec2.types.nested_virtualization_specification

        capo_ec2.types.nested_virtualization_specification.serialize_ec2_query(
            value["nested_virtualization"], pairs, f"{key_prefix}NestedVirtualization"
        )


def deserialize_ec2_query(el: Element) -> CpuOptions:
    out: CpuOptions = {}  # type: ignore[typeddict-item]
    child_core_count = el.find("coreCount")
    if child_core_count is not None:
        out["core_count"] = int(child_core_count.text or "")
    child_threads_per_core = el.find("threadsPerCore")
    if child_threads_per_core is not None:
        out["threads_per_core"] = int(child_threads_per_core.text or "")
    child_amd_sev_snp = el.find("amdSevSnp")
    if child_amd_sev_snp is not None:
        import capo_ec2.types.amd_sev_snp_specification

        out["amd_sev_snp"] = (
            capo_ec2.types.amd_sev_snp_specification.deserialize_ec2_query(
                child_amd_sev_snp
            )
        )
    child_nested_virtualization = el.find("nestedVirtualization")
    if child_nested_virtualization is not None:
        import capo_ec2.types.nested_virtualization_specification

        out["nested_virtualization"] = (
            capo_ec2.types.nested_virtualization_specification.deserialize_ec2_query(
                child_nested_virtualization
            )
        )
    return out
