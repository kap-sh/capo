"""Generated from Smithy shape ``com.amazonaws.location#CreateTrackerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.kms_key_id
    import capo_location.types.position_filtering
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map


class CreateTrackerRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name for the tracker resource.</p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A-Z, a-z, 0-9) , hyphens (-), periods (.), and underscores (_).</p> </li> <li> <p>Must be a unique tracker resource name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExampleTracker</code>.</p> </li> </ul>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>"""
    kms_key_id: NotRequired["capo_location.types.kms_key_id.KmsKeyId"]
    """<p>A key identifier for an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a>. Enter a key ID, key ARN, alias name, or alias ARN.</p>"""
    pricing_plan_data_source: NotRequired["str"]
    """<p>This parameter is no longer used.</p>"""
    description: NotRequired[
        "capo_location.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description for the tracker resource.</p>"""
    tags: NotRequired["capo_location.types.tag_map.TagMap"]
    """<p>Applies one or more tags to the tracker resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>"""
    position_filtering: NotRequired[
        "capo_location.types.position_filtering.PositionFiltering"
    ]
    """<p>Specifies the position filtering for the tracker resource.</p> <p>Valid values:</p> <ul> <li> <p> <code>TimeBased</code> - Location updates are evaluated against linked geofence collections, but not every location update is stored. If your update frequency is more often than 30 seconds, only one update per 30 seconds is stored for each unique device ID. </p> </li> <li> <p> <code>DistanceBased</code> - If the device has moved less than 30 m (98.4 ft), location updates are ignored. Location updates within this area are neither evaluated against linked geofence collections, nor stored. This helps control costs by reducing the number of geofence evaluations and historical device positions to paginate through. Distance-based filtering can also reduce the effects of GPS noise when displaying device trajectories on a map. </p> </li> <li> <p> <code>AccuracyBased</code> - If the device has moved less than the measured accuracy, location updates are ignored. For example, if two consecutive updates from a device have a horizontal accuracy of 5 m and 10 m, the second update is ignored if the device has moved less than 15 m. Ignored location updates are neither evaluated against linked geofence collections, nor stored. This can reduce the effects of GPS noise when displaying device trajectories on a map, and can help control your costs by reducing the number of geofence evaluations. </p> </li> </ul> <p>This field is optional. If not specified, the default value is <code>TimeBased</code>.</p>"""
    event_bridge_enabled: NotRequired["bool"]
    """<p>Whether to enable position <code>UPDATE</code> events from this tracker to be sent to EventBridge.</p> <note> <p>You do not need enable this feature to get <code>ENTER</code> and <code>EXIT</code> events for geofences with this tracker. Those events are always sent to EventBridge.</p> </note>"""
    kms_key_enable_geospatial_queries: NotRequired["bool"]
    """<p>Enables <code>GeospatialQueries</code> for a tracker that uses a <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a>.</p> <p>This parameter is only used if you are using a KMS customer managed key.</p> <note> <p>If you wish to encrypt your data using your own KMS customer managed key, then the Bounding Polygon Queries feature will be disabled by default. This is because by using this feature, a representation of your device positions will not be encrypted using the your KMS managed key. The exact device position, however; is still encrypted using your managed key.</p> <p>You can choose to opt-in to the Bounding Polygon Quseries feature. This is done by setting the <code>KmsKeyEnableGeospatialQueries</code> parameter to true when creating or updating a Tracker.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrackerRequest) -> dict:
    out: dict = {}
    out["TrackerName"] = value["tracker_name"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "pricing_plan_data_source" in value:
        out["PricingPlanDataSource"] = value["pricing_plan_data_source"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_location.types.tag_map

        out["Tags"] = capo_location.types.tag_map.serialize_json(value["tags"])
    if "position_filtering" in value:
        out["PositionFiltering"] = value["position_filtering"]
    if "event_bridge_enabled" in value:
        out["EventBridgeEnabled"] = value["event_bridge_enabled"]
    if "kms_key_enable_geospatial_queries" in value:
        out["KmsKeyEnableGeospatialQueries"] = value[
            "kms_key_enable_geospatial_queries"
        ]
    return out


def deserialize_json(data: dict) -> CreateTrackerRequest:
    out: CreateTrackerRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrackerName") is not None:
        out["tracker_name"] = data["TrackerName"]
    else:
        raise DeserializationError("CreateTrackerRequest.tracker_name required")
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("PricingPlanDataSource") is not None:
        out["pricing_plan_data_source"] = data["PricingPlanDataSource"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_location.types.tag_map

        out["tags"] = capo_location.types.tag_map.deserialize_json(data["Tags"])
    if data.get("PositionFiltering") is not None:
        out["position_filtering"] = data["PositionFiltering"]
    if data.get("EventBridgeEnabled") is not None:
        out["event_bridge_enabled"] = data["EventBridgeEnabled"]
    if data.get("KmsKeyEnableGeospatialQueries") is not None:
        out["kms_key_enable_geospatial_queries"] = data["KmsKeyEnableGeospatialQueries"]
    return out
