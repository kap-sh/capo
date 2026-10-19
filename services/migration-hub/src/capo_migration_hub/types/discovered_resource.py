"""Generated from Smithy shape ``com.amazonaws.migrationhub#DiscoveredResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.configuration_id
    import capo_migration_hub.types.discovered_resource_description


class DiscoveredResource(TypedDict, closed=True):
    configuration_id: "capo_migration_hub.types.configuration_id.ConfigurationId"
    """<p>The configurationId in Application Discovery Service that uniquely identifies the on-premise resource.</p>"""
    description: NotRequired[
        "capo_migration_hub.types.discovered_resource_description.DiscoveredResourceDescription"
    ]
    """<p>A description that can be free-form text to record additional detail about the discovered resource for clarity or later reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoveredResource) -> dict:
    out: dict = {}
    out["ConfigurationId"] = value["configuration_id"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoveredResource:
    out: DiscoveredResource = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationId") is not None:
        out["configuration_id"] = data["ConfigurationId"]
    else:
        out["configuration_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
