"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPrice``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.currency_code
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.route_toll_price_value_range
    import capo_geo_routes.types.sensitive_boolean
    import capo_geo_routes.types.sensitive_double


class RouteTollPrice(TypedDict, closed=True):
    currency: "capo_geo_routes.types.currency_code.CurrencyCode"
    """<p>Currency code corresponding to the price. This is the same as Currency specified in the request.</p>"""
    estimate: "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    """<p>If the price is an estimate or an exact value. </p>"""
    per_duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration for which the price corresponds to.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    range: "capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    """<p>If the price is a range or an exact value. If any of the toll fares making up the route is a range, the overall price is also a range.</p>"""
    range_value: NotRequired[
        "capo_geo_routes.types.route_toll_price_value_range.RouteTollPriceValueRange"
    ]
    """<p>Price range with a minimum and maximum value, if a range.</p>"""
    value: "capo_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Exact price, if not a range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPrice) -> dict:
    out: dict = {}
    out["Currency"] = value["currency"]
    out["Estimate"] = value["estimate"]
    out["PerDuration"] = value.get("per_duration", 0)
    out["Range"] = value["range"]
    if "range_value" in value:
        import capo_geo_routes.types.route_toll_price_value_range

        out["RangeValue"] = (
            capo_geo_routes.types.route_toll_price_value_range.serialize_json(
                value["range_value"]
            )
        )
    out["Value"] = (
        "NaN"
        if value["value"] != value["value"]
        else "Infinity"
        if value["value"] == float("inf")
        else "-Infinity"
        if value["value"] == float("-inf")
        else value["value"]
    )
    return out


def deserialize_json(data: dict) -> RouteTollPrice:
    out: RouteTollPrice = {}  # type: ignore[typeddict-item]
    if data.get("Currency") is not None:
        out["currency"] = data["Currency"]
    else:
        raise DeserializationError("RouteTollPrice.currency required")
    if data.get("Estimate") is not None:
        out["estimate"] = data["Estimate"]
    else:
        raise DeserializationError("RouteTollPrice.estimate required")
    if data.get("PerDuration") is not None:
        out["per_duration"] = data["PerDuration"]
    else:
        out["per_duration"] = 0
    if data.get("Range") is not None:
        out["range"] = data["Range"]
    else:
        raise DeserializationError("RouteTollPrice.range required")
    if data.get("RangeValue") is not None:
        import capo_geo_routes.types.route_toll_price_value_range

        out["range_value"] = (
            capo_geo_routes.types.route_toll_price_value_range.deserialize_json(
                data["RangeValue"]
            )
        )
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    else:
        raise DeserializationError("RouteTollPrice.value required")
    return out


def redact_sensitive(value: RouteTollPrice) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "estimate" in value:
        out["estimate"] = "*** Sensitive Data Redacted ***"
    if "per_duration" in value:
        out["per_duration"] = "*** Sensitive Data Redacted ***"
    if "range" in value:
        out["range"] = "*** Sensitive Data Redacted ***"
    if "range_value" in value:
        import capo_geo_routes.types.route_toll_price_value_range

        out["range_value"] = (
            capo_geo_routes.types.route_toll_price_value_range.redact_sensitive(
                value["range_value"]
            )
        )
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
