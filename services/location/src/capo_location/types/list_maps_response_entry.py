"""Generated from Smithy shape ``com.amazonaws.location#ListMapsResponseEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class ListMapsResponseEntry(TypedDict, closed=True):
    map_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the associated map resource.</p>"""
    description: "capo_location.types.resource_description.ResourceDescription"
    """<p>The description for the map resource.</p>"""
    data_source: "str"
    """<p>Specifies the data provider for the associated map tiles.</p>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. Always returns <code>RequestBasedUsage</code>.</p>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the map resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the map resource was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMapsResponseEntry) -> dict:
    out: dict = {}
    out["MapName"] = value["map_name"]
    out["Description"] = value["description"]
    out["DataSource"] = value["data_source"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> ListMapsResponseEntry:
    out: ListMapsResponseEntry = {}  # type: ignore[typeddict-item]
    if data.get("MapName") is not None:
        out["map_name"] = data["MapName"]
    else:
        raise DeserializationError("ListMapsResponseEntry.map_name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("ListMapsResponseEntry.description required")
    if data.get("DataSource") is not None:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError("ListMapsResponseEntry.data_source required")
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("ListMapsResponseEntry.create_time required")
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("ListMapsResponseEntry.update_time required")
    return out
