"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateCalculatedAttributeDefinitionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_details
    import capo_customer_profiles.types.conditions
    import capo_customer_profiles.types.display_name
    import capo_customer_profiles.types.filter
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.optional_boolean
    import capo_customer_profiles.types.sensitive_text
    import capo_customer_profiles.types.statistic
    import capo_customer_profiles.types.tag_map
    import capo_customer_profiles.types.type_name


class CreateCalculatedAttributeDefinitionRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    calculated_attribute_name: "capo_customer_profiles.types.type_name.typeName"
    """<p>The unique name of the calculated attribute.</p>"""
    display_name: NotRequired["capo_customer_profiles.types.display_name.displayName"]
    """<p>The display name of the calculated attribute.</p>"""
    description: NotRequired[
        "capo_customer_profiles.types.sensitive_text.sensitiveText"
    ]
    """<p>The description of the calculated attribute.</p>"""
    attribute_details: "capo_customer_profiles.types.attribute_details.AttributeDetails"
    """<p>Mathematical expression and a list of attribute items specified in that expression.</p>"""
    conditions: NotRequired["capo_customer_profiles.types.conditions.Conditions"]
    """<p>The conditions including range, object count, and threshold for the calculated attribute.</p>"""
    filter: NotRequired["capo_customer_profiles.types.filter.Filter"]
    """<p>Defines how to filter incoming objects to include part of the Calculated Attribute.</p>"""
    statistic: "capo_customer_profiles.types.statistic.Statistic"
    """<p>The aggregation operation to perform for the calculated attribute.</p>"""
    use_historical_data: NotRequired[
        "capo_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Whether historical data ingested before the Calculated Attribute was created should be included in calculations.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCalculatedAttributeDefinitionRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_customer_profiles.types.attribute_details

    out["AttributeDetails"] = (
        capo_customer_profiles.types.attribute_details.serialize_json(
            value["attribute_details"]
        )
    )
    if "conditions" in value:
        import capo_customer_profiles.types.conditions

        out["Conditions"] = capo_customer_profiles.types.conditions.serialize_json(
            value["conditions"]
        )
    if "filter" in value:
        import capo_customer_profiles.types.filter

        out["Filter"] = capo_customer_profiles.types.filter.serialize_json(
            value["filter"]
        )
    import capo_customer_profiles.types.statistic

    out["Statistic"] = capo_customer_profiles.types.statistic.serialize_json(
        value["statistic"]
    )
    if "use_historical_data" in value:
        out["UseHistoricalData"] = value["use_historical_data"]
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCalculatedAttributeDefinitionRequest:
    out: CreateCalculatedAttributeDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AttributeDetails") is not None:
        import capo_customer_profiles.types.attribute_details

        out["attribute_details"] = (
            capo_customer_profiles.types.attribute_details.deserialize_json(
                data["AttributeDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCalculatedAttributeDefinitionRequest.attribute_details required"
        )
    if data.get("Conditions") is not None:
        import capo_customer_profiles.types.conditions

        out["conditions"] = capo_customer_profiles.types.conditions.deserialize_json(
            data["Conditions"]
        )
    if data.get("Filter") is not None:
        import capo_customer_profiles.types.filter

        out["filter"] = capo_customer_profiles.types.filter.deserialize_json(
            data["Filter"]
        )
    if data.get("Statistic") is not None:
        import capo_customer_profiles.types.statistic

        out["statistic"] = capo_customer_profiles.types.statistic.deserialize_json(
            data["Statistic"]
        )
    else:
        import typing

        out["statistic"] = typing.cast(
            "capo_customer_profiles.types.statistic.Statistic", ""
        )
    if data.get("UseHistoricalData") is not None:
        out["use_historical_data"] = data["UseHistoricalData"]
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(
    value: CreateCalculatedAttributeDefinitionRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "attribute_details" in value:
        out["attribute_details"] = "*** Sensitive Data Redacted ***"
    if "conditions" in value:
        out["conditions"] = "*** Sensitive Data Redacted ***"
    if "statistic" in value:
        out["statistic"] = "*** Sensitive Data Redacted ***"
    return out
