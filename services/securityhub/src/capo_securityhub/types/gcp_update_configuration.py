"""Generated from Smithy shape ``com.amazonaws.securityhub#GcpUpdateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.gcp_region_list
    import capo_securityhub.types.gcp_scope_configuration


class GcpUpdateConfiguration(TypedDict, closed=True):
    scope_configuration: NotRequired[
        "capo_securityhub.types.gcp_scope_configuration.GcpScopeConfiguration"
    ]
    """<p>The updated scope configuration.</p>"""
    gcp_regions: NotRequired["capo_securityhub.types.gcp_region_list.GcpRegionList"]
    """<p>The updated list of GCP regions to monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GcpUpdateConfiguration) -> dict:
    out: dict = {}
    if "scope_configuration" in value:
        import capo_securityhub.types.gcp_scope_configuration

        out["ScopeConfiguration"] = (
            capo_securityhub.types.gcp_scope_configuration.serialize_json(
                value["scope_configuration"]
            )
        )
    if "gcp_regions" in value:
        import capo_securityhub.types.gcp_region_list

        out["GCPRegions"] = capo_securityhub.types.gcp_region_list.serialize_json(
            value["gcp_regions"]
        )
    return out


def deserialize_json(data: dict) -> GcpUpdateConfiguration:
    out: GcpUpdateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ScopeConfiguration") is not None:
        import capo_securityhub.types.gcp_scope_configuration

        out["scope_configuration"] = (
            capo_securityhub.types.gcp_scope_configuration.deserialize_json(
                data["ScopeConfiguration"]
            )
        )
    if data.get("GCPRegions") is not None:
        import capo_securityhub.types.gcp_region_list

        out["gcp_regions"] = capo_securityhub.types.gcp_region_list.deserialize_json(
            data["GCPRegions"]
        )
    return out
