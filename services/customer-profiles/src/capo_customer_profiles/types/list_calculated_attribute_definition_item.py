"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListCalculatedAttributeDefinitionItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.display_name
    import capo_customer_profiles.types.optional_boolean
    import capo_customer_profiles.types.readiness_status
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.type_name


class ListCalculatedAttributeDefinitionItem(TypedDict, closed=True):
    calculated_attribute_name: NotRequired[
        "capo_customer_profiles.types.type_name.typeName"
    ]
    """<p>The unique name of the calculated attribute.</p>"""
    display_name: NotRequired["capo_customer_profiles.types.display_name.displayName"]
    """<p>The display name of the calculated attribute.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The threshold for the calculated attribute.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The threshold for the calculated attribute.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the calculated attribute definition was most recently edited.</p>"""
    use_historical_data: NotRequired[
        "capo_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Whether historical data ingested before the Calculated Attribute was created should be included in calculations.</p>"""
    status: NotRequired["capo_customer_profiles.types.readiness_status.ReadinessStatus"]
    """<p>Status of the Calculated Attribute creation (whether all historical data has been indexed.)</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCalculatedAttributeDefinitionItem) -> dict:
    out: dict = {}
    if "calculated_attribute_name" in value:
        out["CalculatedAttributeName"] = value["calculated_attribute_name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
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
    if "use_historical_data" in value:
        out["UseHistoricalData"] = value["use_historical_data"]
    if "status" in value:
        import capo_customer_profiles.types.readiness_status

        out["Status"] = capo_customer_profiles.types.readiness_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListCalculatedAttributeDefinitionItem:
    out: ListCalculatedAttributeDefinitionItem = {}  # type: ignore[typeddict-item]
    if data.get("CalculatedAttributeName") is not None:
        out["calculated_attribute_name"] = data["CalculatedAttributeName"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
    if data.get("UseHistoricalData") is not None:
        out["use_historical_data"] = data["UseHistoricalData"]
    if data.get("Status") is not None:
        import capo_customer_profiles.types.readiness_status

        out["status"] = capo_customer_profiles.types.readiness_status.deserialize_json(
            data["Status"]
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: ListCalculatedAttributeDefinitionItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
