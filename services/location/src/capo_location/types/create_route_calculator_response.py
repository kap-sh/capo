"""Generated from Smithy shape ``com.amazonaws.location#CreateRouteCalculatorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.geo_arn
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class CreateRouteCalculatorResponse(TypedDict, closed=True):
    calculator_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the route calculator resource. </p> <ul> <li> <p>For example, <code>ExampleRouteCalculator</code>.</p> </li> </ul>"""
    calculator_arn: "capo_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) for the route calculator resource. Use the ARN when you specify a resource across all Amazon Web Services.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:route-calculator/ExampleCalculator</code> </p> </li> </ul>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp when the route calculator resource was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p> <ul> <li> <p>For example, <code>2020–07-2T12:15:20.000Z+01:00</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRouteCalculatorResponse) -> dict:
    out: dict = {}
    out["CalculatorName"] = value["calculator_name"]
    out["CalculatorArn"] = value["calculator_arn"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateRouteCalculatorResponse:
    out: CreateRouteCalculatorResponse = {}  # type: ignore[typeddict-item]
    if data.get("CalculatorName") is not None:
        out["calculator_name"] = data["CalculatorName"]
    else:
        raise DeserializationError(
            "CreateRouteCalculatorResponse.calculator_name required"
        )
    if data.get("CalculatorArn") is not None:
        out["calculator_arn"] = data["CalculatorArn"]
    else:
        raise DeserializationError(
            "CreateRouteCalculatorResponse.calculator_arn required"
        )
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("CreateRouteCalculatorResponse.create_time required")
    return out
