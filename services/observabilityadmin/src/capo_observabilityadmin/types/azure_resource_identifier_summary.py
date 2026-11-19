"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureResourceIdentifierSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_region
    import capo_observabilityadmin.types.azure_resource_id
    import capo_observabilityadmin.types.azure_resource_tags
    import capo_observabilityadmin.types.azure_resource_type
    import capo_observabilityadmin.types.azure_subscription_id


class AzureResourceIdentifierSummary(TypedDict, closed=True):
    resource_id: "capo_observabilityadmin.types.azure_resource_id.AzureResourceId"
    """<p>The Azure Resource Manager ID of the resource.</p>"""
    resource_type: NotRequired[
        "capo_observabilityadmin.types.azure_resource_type.AzureResourceType"
    ]
    """<p>The Azure resource type, for example <code>Microsoft.Compute/virtualMachines</code>.</p>"""
    region: NotRequired["capo_observabilityadmin.types.azure_region.AzureRegion"]
    """<p>The Azure Region of the resource, for example <code>eastus</code>.</p>"""
    subscription_id: NotRequired[
        "capo_observabilityadmin.types.azure_subscription_id.AzureSubscriptionId"
    ]
    """<p>The Azure subscription that contains the resource.</p>"""
    tags: NotRequired[
        "capo_observabilityadmin.types.azure_resource_tags.AzureResourceTags"
    ]
    """<p>The tags on the resource. Absent if the resource has no tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureResourceIdentifierSummary) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "region" in value:
        out["Region"] = value["region"]
    if "subscription_id" in value:
        out["SubscriptionId"] = value["subscription_id"]
    if "tags" in value:
        import capo_observabilityadmin.types.azure_resource_tags

        out["Tags"] = capo_observabilityadmin.types.azure_resource_tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> AzureResourceIdentifierSummary:
    out: AzureResourceIdentifierSummary = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("SubscriptionId") is not None:
        out["subscription_id"] = data["SubscriptionId"]
    if data.get("Tags") is not None:
        import capo_observabilityadmin.types.azure_resource_tags

        out["tags"] = (
            capo_observabilityadmin.types.azure_resource_tags.deserialize_json(
                data["Tags"]
            )
        )
    return out
