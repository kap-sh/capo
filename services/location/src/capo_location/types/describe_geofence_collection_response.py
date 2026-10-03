"""Generated from Smithy shape ``com.amazonaws.location#DescribeGeofenceCollectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.arn
    import capo_location.types.kms_key_id
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map
    import capo_location.types.timestamp


class DescribeGeofenceCollectionResponse(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the geofence collection.</p>"""
    collection_arn: "capo_location.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all Amazon Web Services. </p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection</code> </p> </li> </ul>"""
    description: "capo_location.types.resource_description.ResourceDescription"
    """<p>The optional description for the geofence collection.</p>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. Always returns <code>RequestBasedUsage</code>.</p>"""
    pricing_plan_data_source: NotRequired["str"]
    """<p>No longer used. Always returns an empty string.</p>"""
    kms_key_id: NotRequired["capo_location.types.kms_key_id.KmsKeyId"]
    """<p>A key identifier for an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html">Amazon Web Services KMS customer managed key</a> assigned to the Amazon Location resource</p>"""
    tags: NotRequired["capo_location.types.tag_map.TagMap"]
    """<p>Displays the key, value pairs of tags associated with this resource.</p>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence collection was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    geofence_count: NotRequired["int"]
    """<p>The number of geofences in the geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGeofenceCollectionResponse) -> dict:
    out: dict = {}
    out["CollectionName"] = value["collection_name"]
    out["CollectionArn"] = value["collection_arn"]
    out["Description"] = value["description"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "pricing_plan_data_source" in value:
        out["PricingPlanDataSource"] = value["pricing_plan_data_source"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
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
    if "geofence_count" in value:
        out["GeofenceCount"] = value["geofence_count"]
    return out


def deserialize_json(data: dict) -> DescribeGeofenceCollectionResponse:
    out: DescribeGeofenceCollectionResponse = {}  # type: ignore[typeddict-item]
    if data.get("CollectionName") is not None:
        out["collection_name"] = data["CollectionName"]
    else:
        raise DeserializationError(
            "DescribeGeofenceCollectionResponse.collection_name required"
        )
    if data.get("CollectionArn") is not None:
        out["collection_arn"] = data["CollectionArn"]
    else:
        raise DeserializationError(
            "DescribeGeofenceCollectionResponse.collection_arn required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError(
            "DescribeGeofenceCollectionResponse.description required"
        )
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("PricingPlanDataSource") is not None:
        out["pricing_plan_data_source"] = data["PricingPlanDataSource"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("Tags") is not None:
        import capo_location.types.tag_map

        out["tags"] = capo_location.types.tag_map.deserialize_json(data["Tags"])
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError(
            "DescribeGeofenceCollectionResponse.create_time required"
        )
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError(
            "DescribeGeofenceCollectionResponse.update_time required"
        )
    if data.get("GeofenceCount") is not None:
        out["geofence_count"] = data["GeofenceCount"]
    return out
