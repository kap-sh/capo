"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileObjectTypeItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.min_size0
    import capo_customer_profiles.types.min_size1
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.text
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.type_name


class ListProfileObjectTypeItem(TypedDict, closed=True):
    object_type_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The name of the profile object type.</p>"""
    description: "capo_customer_profiles.types.text.text"
    """<p>Description of the profile object type.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the domain was created.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the profile object type was most recently edited.</p>"""
    max_profile_object_count: NotRequired[
        "capo_customer_profiles.types.min_size1.minSize1"
    ]
    """<p>The amount of profile object max count assigned to the object type.</p>"""
    max_available_profile_object_count: NotRequired[
        "capo_customer_profiles.types.min_size0.minSize0"
    ]
    """<p>The amount of provisioned profile object max count available.</p>"""
    source_priority: NotRequired["capo_customer_profiles.types.min_size1.minSize1"]
    """<p>An integer that determines the priority of this object type when data from multiple sources is ingested. Lower values take priority. Object types without a specified source priority default to the lowest priority.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileObjectTypeItem) -> dict:
    out: dict = {}
    out["ObjectTypeName"] = value["object_type_name"]
    out["Description"] = value["description"]
    if "created_at" in value:
        import capo_customer_profiles.types.timestamp

        out["CreatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_customer_profiles.types.timestamp

        out["LastUpdatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "max_profile_object_count" in value:
        out["MaxProfileObjectCount"] = value["max_profile_object_count"]
    if "max_available_profile_object_count" in value:
        out["MaxAvailableProfileObjectCount"] = value[
            "max_available_profile_object_count"
        ]
    if "source_priority" in value:
        out["SourcePriority"] = value["source_priority"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListProfileObjectTypeItem:
    out: ListProfileObjectTypeItem = {}  # type: ignore[typeddict-item]
    if data.get("ObjectTypeName") is not None:
        out["object_type_name"] = data["ObjectTypeName"]
    else:
        out["object_type_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("CreatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["created_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["last_updated_at"] = (
            capo_customer_profiles.types.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if data.get("MaxProfileObjectCount") is not None:
        out["max_profile_object_count"] = data["MaxProfileObjectCount"]
    if data.get("MaxAvailableProfileObjectCount") is not None:
        out["max_available_profile_object_count"] = data[
            "MaxAvailableProfileObjectCount"
        ]
    if data.get("SourcePriority") is not None:
        out["source_priority"] = data["SourcePriority"]
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
