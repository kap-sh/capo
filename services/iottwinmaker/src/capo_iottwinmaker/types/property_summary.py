"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.data_value
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.property_definition_response


class PropertySummary(TypedDict, closed=True):
    definition: NotRequired[
        "capo_iottwinmaker.types.property_definition_response.PropertyDefinitionResponse"
    ]
    """<p>This is the schema for the property.</p>"""
    property_name: "capo_iottwinmaker.types.name.Name"
    """<p>This is the name of the property.</p>"""
    value: NotRequired["capo_iottwinmaker.types.data_value.DataValue"]
    """<p>This is the value for the property.</p>"""
    are_all_property_values_returned: NotRequired[
        "capo_iottwinmaker.types.boolean.Boolean"
    ]
    """<p>This flag notes whether all values of a list or map type property are returned in the API response. The maximum number of values per property returned is 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertySummary) -> dict:
    out: dict = {}
    if "definition" in value:
        import capo_iottwinmaker.types.property_definition_response

        out["definition"] = (
            capo_iottwinmaker.types.property_definition_response.serialize_json(
                value["definition"]
            )
        )
    out["propertyName"] = value["property_name"]
    if "value" in value:
        import capo_iottwinmaker.types.data_value

        out["value"] = capo_iottwinmaker.types.data_value.serialize_json(value["value"])
    if "are_all_property_values_returned" in value:
        out["areAllPropertyValuesReturned"] = value["are_all_property_values_returned"]
    return out


def deserialize_json(data: dict) -> PropertySummary:
    out: PropertySummary = {}  # type: ignore[typeddict-item]
    if data.get("definition") is not None:
        import capo_iottwinmaker.types.property_definition_response

        out["definition"] = (
            capo_iottwinmaker.types.property_definition_response.deserialize_json(
                data["definition"]
            )
        )
    if data.get("propertyName") is not None:
        out["property_name"] = data["propertyName"]
    else:
        out["property_name"] = ""
    if data.get("value") is not None:
        import capo_iottwinmaker.types.data_value

        out["value"] = capo_iottwinmaker.types.data_value.deserialize_json(
            data["value"]
        )
    if data.get("areAllPropertyValuesReturned") is not None:
        out["are_all_property_values_returned"] = data["areAllPropertyValuesReturned"]
    return out
