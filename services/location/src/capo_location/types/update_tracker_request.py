"""Generated from Smithy shape ``com.amazonaws.location#UpdateTrackerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.position_filtering
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name


class UpdateTrackerRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource to update.</p>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>"""
    pricing_plan_data_source: NotRequired["str"]
    """<p>This parameter is no longer used.</p>"""
    description: NotRequired[
        "capo_location.types.resource_description.ResourceDescription"
    ]
    """<p>Updates the description for the tracker resource.</p>"""
    position_filtering: NotRequired[
        "capo_location.types.position_filtering.PositionFiltering"
    ]
    """<p>Updates the position filtering for the tracker resource.</p> <p>Valid values:</p> <ul> <li> <p> <code>TimeBased</code> - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID. </p> </li> <li> <p> <code>DistanceBased</code> - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this distance are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map. </p> </li> <li> <p> <code>AccuracyBased</code> - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This helps educe the effects of GPS noise when displaying device trajectories on a map, and can help control costs by reducing the number of geofence evaluations. </p> </li> </ul>"""
    event_bridge_enabled: NotRequired["bool"]
    """<p>Whether to enable position <code>UPDATE</code> events from this tracker to be sent to EventBridge.</p> <note> <p>You do not need enable this feature to get <code>ENTER</code> and <code>EXIT</code> events for geofences with this tracker. Those events are always sent to EventBridge.</p> </note>"""
    kms_key_enable_geospatial_queries: NotRequired["bool"]
    """<p>Enables <code>GeospatialQueries</code> for a tracker that uses a <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a>.</p> <p>This parameter is only used if you are using a KMS customer managed key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTrackerRequest) -> dict:
    out: dict = {}
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "pricing_plan_data_source" in value:
        out["PricingPlanDataSource"] = value["pricing_plan_data_source"]
    if "description" in value:
        out["Description"] = value["description"]
    if "position_filtering" in value:
        out["PositionFiltering"] = value["position_filtering"]
    if "event_bridge_enabled" in value:
        out["EventBridgeEnabled"] = value["event_bridge_enabled"]
    if "kms_key_enable_geospatial_queries" in value:
        out["KmsKeyEnableGeospatialQueries"] = value[
            "kms_key_enable_geospatial_queries"
        ]
    return out


def deserialize_json(data: dict) -> UpdateTrackerRequest:
    out: UpdateTrackerRequest = {}  # type: ignore[typeddict-item]
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("PricingPlanDataSource") is not None:
        out["pricing_plan_data_source"] = data["PricingPlanDataSource"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("PositionFiltering") is not None:
        out["position_filtering"] = data["PositionFiltering"]
    if data.get("EventBridgeEnabled") is not None:
        out["event_bridge_enabled"] = data["EventBridgeEnabled"]
    if data.get("KmsKeyEnableGeospatialQueries") is not None:
        out["kms_key_enable_geospatial_queries"] = data["KmsKeyEnableGeospatialQueries"]
    return out
