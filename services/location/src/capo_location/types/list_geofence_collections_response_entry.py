"""Generated from Smithy shape ``com.amazonaws.location#ListGeofenceCollectionsResponseEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class ListGeofenceCollectionsResponseEntry(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the geofence collection.</p>"""
    description: "capo_location.types.resource_description.ResourceDescription"
    """<p>The description for the geofence collection</p>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. Always returns <code>RequestBasedUsage</code>.</p>"""
    pricing_plan_data_source: NotRequired["str"]
    """<p>No longer used. Always returns an empty string.</p>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence collection was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>Specifies a timestamp for when the resource was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGeofenceCollectionsResponseEntry) -> dict:
    out: dict = {}
    out["CollectionName"] = value["collection_name"]
    out["Description"] = value["description"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "pricing_plan_data_source" in value:
        out["PricingPlanDataSource"] = value["pricing_plan_data_source"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> ListGeofenceCollectionsResponseEntry:
    out: ListGeofenceCollectionsResponseEntry = {}  # type: ignore[typeddict-item]
    if data.get("CollectionName") is not None:
        out["collection_name"] = data["CollectionName"]
    else:
        raise DeserializationError(
            "ListGeofenceCollectionsResponseEntry.collection_name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError(
            "ListGeofenceCollectionsResponseEntry.description required"
        )
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("PricingPlanDataSource") is not None:
        out["pricing_plan_data_source"] = data["PricingPlanDataSource"]
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError(
            "ListGeofenceCollectionsResponseEntry.create_time required"
        )
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError(
            "ListGeofenceCollectionsResponseEntry.update_time required"
        )
    return out
