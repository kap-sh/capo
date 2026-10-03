"""Generated from Smithy shape ``com.amazonaws.location#DescribeRouteCalculatorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.geo_arn
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.tag_map
    import capo_location.types.timestamp


class DescribeRouteCalculatorResponse(TypedDict, closed=True):
    calculator_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the route calculator resource being described.</p>"""
    calculator_arn: "capo_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) for the Route calculator resource. Use the ARN when you specify a resource across Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:route-calculator/ExampleCalculator</code> </p> </li> </ul>"""
    pricing_plan: NotRequired["capo_location.types.pricing_plan.PricingPlan"]
    """<p>Always returns <code>RequestBasedUsage</code>.</p>"""
    description: "capo_location.types.resource_description.ResourceDescription"
    """<p>The optional description of the route calculator resource.</p>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp when the route calculator resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p> <ul> <li> <p>For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp when the route calculator resource was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p> <ul> <li> <p>For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>"""
    data_source: "str"
    """<p>The data provider of traffic and road network data. Indicates one of the available providers:</p> <ul> <li> <p> <code>Esri</code> </p> </li> <li> <p> <code>Grab</code> </p> </li> <li> <p> <code>Here</code> </p> </li> </ul> <p>For more information about data providers, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html">Amazon Location Service data providers</a>.</p>"""
    tags: NotRequired["capo_location.types.tag_map.TagMap"]
    """<p>Tags associated with route calculator resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRouteCalculatorResponse) -> dict:
    out: dict = {}
    out["CalculatorName"] = value["calculator_name"]
    out["CalculatorArn"] = value["calculator_arn"]
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    out["Description"] = value["description"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    out["DataSource"] = value["data_source"]
    if "tags" in value:
        import capo_location.types.tag_map

        out["Tags"] = capo_location.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeRouteCalculatorResponse:
    out: DescribeRouteCalculatorResponse = {}  # type: ignore[typeddict-item]
    if data.get("CalculatorName") is not None:
        out["calculator_name"] = data["CalculatorName"]
    else:
        raise DeserializationError(
            "DescribeRouteCalculatorResponse.calculator_name required"
        )
    if data.get("CalculatorArn") is not None:
        out["calculator_arn"] = data["CalculatorArn"]
    else:
        raise DeserializationError(
            "DescribeRouteCalculatorResponse.calculator_arn required"
        )
    if data.get("PricingPlan") is not None:
        out["pricing_plan"] = data["PricingPlan"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError(
            "DescribeRouteCalculatorResponse.description required"
        )
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError(
            "DescribeRouteCalculatorResponse.create_time required"
        )
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError(
            "DescribeRouteCalculatorResponse.update_time required"
        )
    if data.get("DataSource") is not None:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError(
            "DescribeRouteCalculatorResponse.data_source required"
        )
    if data.get("Tags") is not None:
        import capo_location.types.tag_map

        out["tags"] = capo_location.types.tag_map.deserialize_json(data["Tags"])
    return out
