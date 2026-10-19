"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#LinuxSubscriptionsDiscoverySettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.organization_integration
    import capo_license_manager_linux_subscriptions.types.string_list


class LinuxSubscriptionsDiscoverySettings(TypedDict, closed=True):
    source_regions: (
        "capo_license_manager_linux_subscriptions.types.string_list.StringList"
    )
    """<p>The Regions in which to discover data for Linux subscriptions.</p>"""
    organization_integration: "capo_license_manager_linux_subscriptions.types.organization_integration.OrganizationIntegration"
    """<p>Details if you have enabled resource discovery across your accounts in Organizations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinuxSubscriptionsDiscoverySettings) -> dict:
    out: dict = {}
    import capo_license_manager_linux_subscriptions.types.string_list

    out["SourceRegions"] = (
        capo_license_manager_linux_subscriptions.types.string_list.serialize_json(
            value["source_regions"]
        )
    )
    out["OrganizationIntegration"] = value["organization_integration"]
    return out


def deserialize_json(data: dict) -> LinuxSubscriptionsDiscoverySettings:
    out: LinuxSubscriptionsDiscoverySettings = {}  # type: ignore[typeddict-item]
    if data.get("SourceRegions") is not None:
        import capo_license_manager_linux_subscriptions.types.string_list

        out["source_regions"] = (
            capo_license_manager_linux_subscriptions.types.string_list.deserialize_json(
                data["SourceRegions"]
            )
        )
    else:
        out["source_regions"] = []
    if data.get("OrganizationIntegration") is not None:
        out["organization_integration"] = data["OrganizationIntegration"]
    else:
        out["organization_integration"] = ""
    return out
