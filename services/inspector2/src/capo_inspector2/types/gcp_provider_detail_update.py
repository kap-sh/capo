"""Generated from Smithy shape ``com.amazonaws.inspector2#GcpProviderDetailUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.gcp_region_list
    import capo_inspector2.types.gcp_scope_configuration_input


class GcpProviderDetailUpdate(TypedDict, closed=True):
    gcp_regions: NotRequired["capo_inspector2.types.gcp_region_list.GcpRegionList"]
    """<p>The updated GCP locations to scan, such as regions, zones, multi-regions, or dual-regions. Specify <code>ALL</code> to scan all locations.</p>"""
    scope_configuration: NotRequired[
        "capo_inspector2.types.gcp_scope_configuration_input.GcpScopeConfigurationInput"
    ]
    """<p>The updated scope configuration that defines which GCP resources to scan.</p>"""
    auto_install_vm_scanner: NotRequired["bool"]
    """<p>Specifies whether to automatically install the VM scanner on connected GCP resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GcpProviderDetailUpdate) -> dict:
    out: dict = {}
    if "gcp_regions" in value:
        import capo_inspector2.types.gcp_region_list

        out["gcpRegions"] = capo_inspector2.types.gcp_region_list.serialize_json(
            value["gcp_regions"]
        )
    if "scope_configuration" in value:
        import capo_inspector2.types.gcp_scope_configuration_input

        out["scopeConfiguration"] = (
            capo_inspector2.types.gcp_scope_configuration_input.serialize_json(
                value["scope_configuration"]
            )
        )
    if "auto_install_vm_scanner" in value:
        out["autoInstallVMScanner"] = value["auto_install_vm_scanner"]
    return out


def deserialize_json(data: dict) -> GcpProviderDetailUpdate:
    out: GcpProviderDetailUpdate = {}  # type: ignore[typeddict-item]
    if data.get("gcpRegions") is not None:
        import capo_inspector2.types.gcp_region_list

        out["gcp_regions"] = capo_inspector2.types.gcp_region_list.deserialize_json(
            data["gcpRegions"]
        )
    if data.get("scopeConfiguration") is not None:
        import capo_inspector2.types.gcp_scope_configuration_input

        out["scope_configuration"] = (
            capo_inspector2.types.gcp_scope_configuration_input.deserialize_json(
                data["scopeConfiguration"]
            )
        )
    if data.get("autoInstallVMScanner") is not None:
        out["auto_install_vm_scanner"] = data["autoInstallVMScanner"]
    return out
