"""Generated from Smithy shape ``com.amazonaws.location#DescribeTrackerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.arn
    import capo_location.types.kms_key_id
    import capo_location.types.position_filtering
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map
    import capo_location.types.timestamp


class DescribeTrackerResponse(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the tracker resource.</p>"""
    tracker_arn: "capo_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the tracker resource. Used when you need to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:tracker/ExampleTracker</code> </p> </li> </ul>"""
    description: "capo_location.types.resource_description.ResourceDescription"
    """<p>The optional description for the tracker resource.</p>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>Always returns <code>RequestBasedUsage</code>.</p>"""
    pricing_plan_data_source: NotRequired["str"]
    """<p>No longer used. Always returns an empty string.</p>"""
    tags: NotRequired["capo_location.types.tag_map.TagMap"]
    """<p>The tags associated with the tracker resource.</p>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the tracker resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the tracker resource was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""
    kms_key_id: NotRequired["capo_location.types.kms_key_id.KmsKeyId"]
    """<p>A key identifier for an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a> assigned to the Amazon Location resource.</p>"""
    position_filtering: NotRequired[
        "capo_location.types.position_filtering.PositionFiltering"
    ]
    """<p>The position filtering method of the tracker resource.</p>"""
    event_bridge_enabled: NotRequired["bool"]
    """<p>Whether <code>UPDATE</code> events from this tracker in EventBridge are enabled. If set to <code>true</code> these events will be sent to EventBridge.</p>"""
    kms_key_enable_geospatial_queries: NotRequired["bool"]
    """<p>Enables <code>GeospatialQueries</code> for a tracker that uses a <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a>.</p> <p>This parameter is only used if you are using a KMS customer managed key.</p> <note> <p>If you wish to encrypt your data using your own KMS customer managed key, then the Bounding Polygon Queries feature will be disabled by default. This is because by using this feature, a representation of your device positions will not be encrypted using the your KMS managed key. The exact device position, however; is still encrypted using your managed key.</p> <p>You can choose to opt-in to the Bounding Polygon Quseries feature. This is done by setting the <code>KmsKeyEnableGeospatialQueries</code> parameter to true when creating or updating a Tracker.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTrackerResponse) -> dict:
    out: dict = {}
    out["TrackerName"] = value["tracker_name"]
    out["TrackerArn"] = value["tracker_arn"]
    out["Description"] = value["description"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "pricing_plan_data_source" in value:
        out["PricingPlanDataSource"] = value["pricing_plan_data_source"]
    if "tags" in value:
        import capo_location.types.tag_map

        out["Tags"] = capo_location.types.tag_map.serialize_json(value["tags"])
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "position_filtering" in value:
        out["PositionFiltering"] = value["position_filtering"]
    if "event_bridge_enabled" in value:
        out["EventBridgeEnabled"] = value["event_bridge_enabled"]
    if "kms_key_enable_geospatial_queries" in value:
        out["KmsKeyEnableGeospatialQueries"] = value[
            "kms_key_enable_geospatial_queries"
        ]
    return out


def deserialize_json(data: dict) -> DescribeTrackerResponse:
    out: DescribeTrackerResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrackerName") is not None:
        out["tracker_name"] = data["TrackerName"]
    else:
        raise DeserializationError("DescribeTrackerResponse.tracker_name required")
    if data.get("TrackerArn") is not None:
        out["tracker_arn"] = data["TrackerArn"]
    else:
        raise DeserializationError("DescribeTrackerResponse.tracker_arn required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("DescribeTrackerResponse.description required")
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("PricingPlanDataSource") is not None:
        out["pricing_plan_data_source"] = data["PricingPlanDataSource"]
    if data.get("Tags") is not None:
        import capo_location.types.tag_map

        out["tags"] = capo_location.types.tag_map.deserialize_json(data["Tags"])
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("DescribeTrackerResponse.create_time required")
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("DescribeTrackerResponse.update_time required")
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("PositionFiltering") is not None:
        out["position_filtering"] = data["PositionFiltering"]
    if data.get("EventBridgeEnabled") is not None:
        out["event_bridge_enabled"] = data["EventBridgeEnabled"]
    if data.get("KmsKeyEnableGeospatialQueries") is not None:
        out["kms_key_enable_geospatial_queries"] = data["KmsKeyEnableGeospatialQueries"]
    return out
