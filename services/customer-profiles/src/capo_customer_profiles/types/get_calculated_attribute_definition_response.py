"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetCalculatedAttributeDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_details
    import capo_customer_profiles.types.conditions
    import capo_customer_profiles.types.display_name
    import capo_customer_profiles.types.filter
    import capo_customer_profiles.types.optional_boolean
    import capo_customer_profiles.types.readiness
    import capo_customer_profiles.types.readiness_status
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.statistic
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.timestamp
    import capo_customer_profiles.types.type_name


class GetCalculatedAttributeDefinitionResponse(TypedDict, closed=True):
    calculated_attribute_name: NotRequired[
        "capo_customer_profiles.types.type_name.typeName"
    ]
    """<p>The unique name of the calculated attribute.</p>"""
    display_name: NotRequired["capo_customer_profiles.types.display_name.displayName"]
    """<p>The display name of the calculated attribute.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the calculated attribute.</p>"""
    created_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the calculated attribute definition was created.</p>"""
    last_updated_at: NotRequired["capo_customer_profiles.types.timestamp.timestamp"]
    """<p>The timestamp of when the calculated attribute definition was most recently edited.</p>"""
    statistic: NotRequired["capo_customer_profiles.types.statistic.Statistic"]
    """<p>The aggregation operation to perform for the calculated attribute.</p>"""
    filter: NotRequired["capo_customer_profiles.types.filter.Filter"]
    """<p>The filter assigned to this calculated attribute definition.</p>"""
    conditions: NotRequired["capo_customer_profiles.types.conditions.Conditions"]
    """<p>The conditions including range, object count, and threshold for the calculated attribute.</p>"""
    attribute_details: NotRequired[
        "capo_customer_profiles.types.attribute_details.AttributeDetails"
    ]
    """<p>Mathematical expression and a list of attribute items specified in that expression.</p>"""
    use_historical_data: NotRequired[
        "capo_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Whether historical data ingested before the Calculated Attribute was created should be included in calculations.</p>"""
    status: NotRequired["capo_customer_profiles.types.readiness_status.ReadinessStatus"]
    """<p>Status of the Calculated Attribute creation (whether all historical data has been indexed).</p>"""
    readiness: NotRequired["capo_customer_profiles.types.readiness.Readiness"]
    """<p>Information indicating if the Calculated Attribute is ready for use by confirming all historical data has been processed and reflected.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCalculatedAttributeDefinitionResponse) -> dict:
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
    if "statistic" in value:
        import capo_customer_profiles.types.statistic

        out["Statistic"] = capo_customer_profiles.types.statistic.serialize_json(
            value["statistic"]
        )
    if "filter" in value:
        import capo_customer_profiles.types.filter

        out["Filter"] = capo_customer_profiles.types.filter.serialize_json(
            value["filter"]
        )
    if "conditions" in value:
        import capo_customer_profiles.types.conditions

        out["Conditions"] = capo_customer_profiles.types.conditions.serialize_json(
            value["conditions"]
        )
    if "attribute_details" in value:
        import capo_customer_profiles.types.attribute_details

        out["AttributeDetails"] = (
            capo_customer_profiles.types.attribute_details.serialize_json(
                value["attribute_details"]
            )
        )
    if "use_historical_data" in value:
        out["UseHistoricalData"] = value["use_historical_data"]
    if "status" in value:
        import capo_customer_profiles.types.readiness_status

        out["Status"] = capo_customer_profiles.types.readiness_status.serialize_json(
            value["status"]
        )
    if "readiness" in value:
        import capo_customer_profiles.types.readiness

        out["Readiness"] = capo_customer_profiles.types.readiness.serialize_json(
            value["readiness"]
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCalculatedAttributeDefinitionResponse:
    out: GetCalculatedAttributeDefinitionResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("Statistic") is not None:
        import capo_customer_profiles.types.statistic

        out["statistic"] = capo_customer_profiles.types.statistic.deserialize_json(
            data["Statistic"]
        )
    if data.get("Filter") is not None:
        import capo_customer_profiles.types.filter

        out["filter"] = capo_customer_profiles.types.filter.deserialize_json(
            data["Filter"]
        )
    if data.get("Conditions") is not None:
        import capo_customer_profiles.types.conditions

        out["conditions"] = capo_customer_profiles.types.conditions.deserialize_json(
            data["Conditions"]
        )
    if data.get("AttributeDetails") is not None:
        import capo_customer_profiles.types.attribute_details

        out["attribute_details"] = (
            capo_customer_profiles.types.attribute_details.deserialize_json(
                data["AttributeDetails"]
            )
        )
    if data.get("UseHistoricalData") is not None:
        out["use_historical_data"] = data["UseHistoricalData"]
    if data.get("Status") is not None:
        import capo_customer_profiles.types.readiness_status

        out["status"] = capo_customer_profiles.types.readiness_status.deserialize_json(
            data["Status"]
        )
    if data.get("Readiness") is not None:
        import capo_customer_profiles.types.readiness

        out["readiness"] = capo_customer_profiles.types.readiness.deserialize_json(
            data["Readiness"]
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetCalculatedAttributeDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "statistic" in value:
        out["statistic"] = "*** Sensitive Data Redacted ***"
    if "conditions" in value:
        out["conditions"] = "*** Sensitive Data Redacted ***"
    if "attribute_details" in value:
        out["attribute_details"] = "*** Sensitive Data Redacted ***"
    return out
