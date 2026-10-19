"""Generated from Smithy shape ``com.amazonaws.location#UpdateRouteCalculatorResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.geo_arn
    import capo_location.types.resource_name
    import capo_location.types.timestamp


class UpdateRouteCalculatorResponse(TypedDict, closed=True):
    calculator_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the updated route calculator resource.</p>"""
    calculator_arn: "capo_location.types.geo_arn.GeoArn"
    """<p>The Amazon Resource Name (ARN) of the updated route calculator resource. Used to specify a resource across AWS.</p> <ul> <li> <p>Format example: <code>arn:aws:geo:region:account-id:route- calculator/ExampleCalculator</code> </p> </li> </ul>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the route calculator was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html"> ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouteCalculatorResponse) -> dict:
    out: dict = {}
    out["CalculatorName"] = value["calculator_name"]
    out["CalculatorArn"] = value["calculator_arn"]
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRouteCalculatorResponse:
    out: UpdateRouteCalculatorResponse = {}  # type: ignore[typeddict-item]
    if data.get("CalculatorName") is not None:
        out["calculator_name"] = data["CalculatorName"]
    else:
        out["calculator_name"] = ""
    if data.get("CalculatorArn") is not None:
        out["calculator_arn"] = data["CalculatorArn"]
    else:
        out["calculator_arn"] = ""
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out


def redact_sensitive(value: UpdateRouteCalculatorResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "update_time" in value:
        out["update_time"] = "*** Sensitive Data Redacted ***"
    return out
