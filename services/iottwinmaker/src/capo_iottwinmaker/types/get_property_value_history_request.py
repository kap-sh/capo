"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetPropertyValueHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_path
    import capo_iottwinmaker.types.component_type_id
    import capo_iottwinmaker.types.entity_id
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.interpolation_parameters
    import capo_iottwinmaker.types.max_results
    import capo_iottwinmaker.types.name
    import capo_iottwinmaker.types.next_token
    import capo_iottwinmaker.types.order_by_time
    import capo_iottwinmaker.types.property_filters
    import capo_iottwinmaker.types.selected_property_list
    import capo_iottwinmaker.types.time
    import capo_iottwinmaker.types.timestamp


class GetPropertyValueHistoryRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    entity_id: NotRequired["capo_iottwinmaker.types.entity_id.EntityId"]
    """<p>The ID of the entity.</p>"""
    component_name: NotRequired["capo_iottwinmaker.types.name.Name"]
    """<p>The name of the component.</p>"""
    component_path: NotRequired["capo_iottwinmaker.types.component_path.ComponentPath"]
    """<p>This string specifies the path to the composite component, starting from the top-level component.</p>"""
    component_type_id: NotRequired[
        "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
    ]
    """<p>The ID of the component type.</p>"""
    selected_properties: (
        "capo_iottwinmaker.types.selected_property_list.SelectedPropertyList"
    )
    """<p>A list of properties whose value histories the request retrieves.</p>"""
    property_filters: NotRequired[
        "capo_iottwinmaker.types.property_filters.PropertyFilters"
    ]
    """<p>A list of objects that filter the property value history request.</p>"""
    start_date_time: NotRequired["capo_iottwinmaker.types.timestamp.Timestamp"]
    """<p>The date and time of the earliest property value to return.</p>"""
    end_date_time: NotRequired["capo_iottwinmaker.types.timestamp.Timestamp"]
    """<p>The date and time of the latest property value to return.</p>"""
    interpolation: NotRequired[
        "capo_iottwinmaker.types.interpolation_parameters.InterpolationParameters"
    ]
    """<p>An object that specifies the interpolation type and the interval over which to interpolate data.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""
    max_results: NotRequired["capo_iottwinmaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p> <p>Valid Range: Minimum value of 1. Maximum value of 250.</p>"""
    order_by_time: NotRequired["capo_iottwinmaker.types.order_by_time.OrderByTime"]
    """<p>The time direction to use in the result order.</p>"""
    start_time: NotRequired["capo_iottwinmaker.types.time.Time"]
    """<p>The ISO8601 DateTime of the earliest property value to return.</p> <p>For more information about the ISO8601 DateTime format, see the data type <a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValue.html">PropertyValue</a>.</p>"""
    end_time: NotRequired["capo_iottwinmaker.types.time.Time"]
    """<p>The ISO8601 DateTime of the latest property value to return.</p> <p>For more information about the ISO8601 DateTime format, see the data type <a href="https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_PropertyValue.html">PropertyValue</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertyValueHistoryRequest) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "component_name" in value:
        out["componentName"] = value["component_name"]
    if "component_path" in value:
        out["componentPath"] = value["component_path"]
    if "component_type_id" in value:
        out["componentTypeId"] = value["component_type_id"]
    import capo_iottwinmaker.types.selected_property_list

    out["selectedProperties"] = (
        capo_iottwinmaker.types.selected_property_list.serialize_json(
            value["selected_properties"]
        )
    )
    if "property_filters" in value:
        import capo_iottwinmaker.types.property_filters

        out["propertyFilters"] = (
            capo_iottwinmaker.types.property_filters.serialize_json(
                value["property_filters"]
            )
        )
    if "start_date_time" in value:
        import capo_iottwinmaker.types.timestamp

        out["startDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
            value["start_date_time"]
        )
    if "end_date_time" in value:
        import capo_iottwinmaker.types.timestamp

        out["endDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
            value["end_date_time"]
        )
    if "interpolation" in value:
        import capo_iottwinmaker.types.interpolation_parameters

        out["interpolation"] = (
            capo_iottwinmaker.types.interpolation_parameters.serialize_json(
                value["interpolation"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "order_by_time" in value:
        out["orderByTime"] = value["order_by_time"]
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "end_time" in value:
        out["endTime"] = value["end_time"]
    return out


def deserialize_json(data: dict) -> GetPropertyValueHistoryRequest:
    out: GetPropertyValueHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    if data.get("componentName") is not None:
        out["component_name"] = data["componentName"]
    if data.get("componentPath") is not None:
        out["component_path"] = data["componentPath"]
    if data.get("componentTypeId") is not None:
        out["component_type_id"] = data["componentTypeId"]
    if data.get("selectedProperties") is not None:
        import capo_iottwinmaker.types.selected_property_list

        out["selected_properties"] = (
            capo_iottwinmaker.types.selected_property_list.deserialize_json(
                data["selectedProperties"]
            )
        )
    else:
        raise DeserializationError(
            "GetPropertyValueHistoryRequest.selected_properties required"
        )
    if data.get("propertyFilters") is not None:
        import capo_iottwinmaker.types.property_filters

        out["property_filters"] = (
            capo_iottwinmaker.types.property_filters.deserialize_json(
                data["propertyFilters"]
            )
        )
    if data.get("startDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["start_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["startDateTime"]
        )
    if data.get("endDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["end_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["endDateTime"]
        )
    if data.get("interpolation") is not None:
        import capo_iottwinmaker.types.interpolation_parameters

        out["interpolation"] = (
            capo_iottwinmaker.types.interpolation_parameters.deserialize_json(
                data["interpolation"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("orderByTime") is not None:
        out["order_by_time"] = data["orderByTime"]
    if data.get("startTime") is not None:
        out["start_time"] = data["startTime"]
    if data.get("endTime") is not None:
        out["end_time"] = data["endTime"]
    return out
