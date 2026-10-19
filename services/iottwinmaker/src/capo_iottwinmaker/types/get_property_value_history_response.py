"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetPropertyValueHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.next_token
    import capo_iottwinmaker.types.property_value_list


class GetPropertyValueHistoryResponse(TypedDict, closed=True):
    property_values: "capo_iottwinmaker.types.property_value_list.PropertyValueList"
    """<p>An object that maps strings to the property definitions in the component type. Each string in the mapping must be unique to this object.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertyValueHistoryResponse) -> dict:
    out: dict = {}
    import capo_iottwinmaker.types.property_value_list

    out["propertyValues"] = capo_iottwinmaker.types.property_value_list.serialize_json(
        value["property_values"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetPropertyValueHistoryResponse:
    out: GetPropertyValueHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("propertyValues") is not None:
        import capo_iottwinmaker.types.property_value_list

        out["property_values"] = (
            capo_iottwinmaker.types.property_value_list.deserialize_json(
                data["propertyValues"]
            )
        )
    else:
        out["property_values"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
