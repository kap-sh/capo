"""Generated from Smithy shape ``com.amazonaws.location#DescribeMapResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.geo_arn
    import capo_location.types.map_configuration
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map
    import capo_location.types.timestamp


class DescribeMapResponse(TypedDict, closed=True):
    map_name: "capo_location.types.resource_name.ResourceName"
    """<p>The map style selected from an available provider.</p>"""
    map_arn: "capo_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) for the map resource. Used to specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:map/ExampleMap</code> </p> </li> </ul>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. Always returns <code>RequestBasedUsage</code>.</p>"""
    data_source: "str"
    """<p>Specifies the data provider for the associated map tiles.</p>"""
    configuration: "capo_location.types.map_configuration.MapConfiguration"
    """<p>Specifies the map tile style selected from a partner data provider.</p>"""
    description: "capo_location.types.resource_description.ResourceDescription"
    """<p>The optional description for the map resource.</p>"""
    tags: NotRequired["capo_location.types.tag_map.TagMap"]
    """<p>Tags associated with the map resource.</p>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the map resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the map resource was last update in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeMapResponse) -> dict:
    out: dict = {}
    out["MapName"] = value["map_name"]
    out["MapArn"] = value["map_arn"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    out["DataSource"] = value["data_source"]
    import capo_location.types.map_configuration

    out["Configuration"] = capo_location.types.map_configuration.serialize_json(
        value["configuration"]
    )
    out["Description"] = value["description"]
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
    return out


def deserialize_json(data: dict) -> DescribeMapResponse:
    out: DescribeMapResponse = {}  # type: ignore[typeddict-item]
    if data.get("MapName") is not None:
        out["map_name"] = data["MapName"]
    else:
        raise DeserializationError("DescribeMapResponse.map_name required")
    if data.get("MapArn") is not None:
        out["map_arn"] = data["MapArn"]
    else:
        raise DeserializationError("DescribeMapResponse.map_arn required")
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("DataSource") is not None:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError("DescribeMapResponse.data_source required")
    if data.get("Configuration") is not None:
        import capo_location.types.map_configuration

        out["configuration"] = capo_location.types.map_configuration.deserialize_json(
            data["Configuration"]
        )
    else:
        raise DeserializationError("DescribeMapResponse.configuration required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("DescribeMapResponse.description required")
    if data.get("Tags") is not None:
        import capo_location.types.tag_map

        out["tags"] = capo_location.types.tag_map.deserialize_json(data["Tags"])
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("DescribeMapResponse.create_time required")
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("DescribeMapResponse.update_time required")
    return out
