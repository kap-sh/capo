"""Generated from Smithy shape ``com.amazonaws.location#CreateMapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.map_configuration
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map


class CreateMapRequest(TypedDict, closed=True):
    map_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name for the map resource.</p> <p>Requirements:</p> <ul> <li> <p>Must contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_). </p> </li> <li> <p>Must be a unique map resource name. </p> </li> <li> <p>No spaces allowed. For example, <code>ExampleMap</code>.</p> </li> </ul>"""
    configuration: "capo_location.types.map_configuration.MapConfiguration"
    """<p>Specifies the <code>MapConfiguration</code>, including the map style, for the map resource that you create. The map style defines the look of maps and the data provider for your map resource.</p>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>"""
    description: NotRequired[
        "capo_location.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description for the map resource.</p>"""
    tags: NotRequired["capo_location.types.tag_map.TagMap"]
    """<p>Applies one or more tags to the map resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource</p> </li> <li> <p>Each resource tag must be unique with a maximum of one value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @. </p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMapRequest) -> dict:
    out: dict = {}
    out["MapName"] = value["map_name"]
    import capo_location.types.map_configuration

    out["Configuration"] = capo_location.types.map_configuration.serialize_json(
        value["configuration"]
    )
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_location.types.tag_map

        out["Tags"] = capo_location.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMapRequest:
    out: CreateMapRequest = {}  # type: ignore[typeddict-item]
    if data.get("MapName") is not None:
        out["map_name"] = data["MapName"]
    else:
        raise DeserializationError("CreateMapRequest.map_name required")
    if data.get("Configuration") is not None:
        import capo_location.types.map_configuration

        out["configuration"] = capo_location.types.map_configuration.deserialize_json(
            data["Configuration"]
        )
    else:
        raise DeserializationError("CreateMapRequest.configuration required")
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_location.types.tag_map

        out["tags"] = capo_location.types.tag_map.deserialize_json(data["Tags"])
    return out
