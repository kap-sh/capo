"""Generated from Smithy shape ``com.amazonaws.location#UpdateMapRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.map_configuration_update
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name


class UpdateMapRequest(TypedDict, closed=True):
    map_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the map resource to update.</p>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>"""
    description: NotRequired[
        "capo_location.types.resource_description.ResourceDescription"
    ]
    """<p>Updates the description for the map resource.</p>"""
    configuration_update: NotRequired[
        "capo_location.types.map_configuration_update.MapConfigurationUpdate"
    ]
    """<p>Updates the parts of the map configuration that can be updated, including the political view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMapRequest) -> dict:
    out: dict = {}
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "description" in value:
        out["Description"] = value["description"]
    if "configuration_update" in value:
        import capo_location.types.map_configuration_update

        out["ConfigurationUpdate"] = (
            capo_location.types.map_configuration_update.serialize_json(
                value["configuration_update"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMapRequest:
    out: UpdateMapRequest = {}  # type: ignore[typeddict-item]
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ConfigurationUpdate") is not None:
        import capo_location.types.map_configuration_update

        out["configuration_update"] = (
            capo_location.types.map_configuration_update.deserialize_json(
                data["ConfigurationUpdate"]
            )
        )
    return out


def redact_sensitive(value: UpdateMapRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration_update" in value:
        import capo_location.types.map_configuration_update

        out["configuration_update"] = (
            capo_location.types.map_configuration_update.redact_sensitive(
                value["configuration_update"]
            )
        )
    return out
