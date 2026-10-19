"""Generated from Smithy shape ``com.amazonaws.xray#SamplingBoost``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.double
    import capo_xray.types.timestamp


class SamplingBoost(TypedDict, closed=True):
    boost_rate: "capo_xray.types.double.Double"
    """<p>The calculated sampling boost rate for this service </p>"""
    boost_rate_ttl: "capo_xray.types.timestamp.Timestamp"
    """<p>When the sampling boost expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingBoost) -> dict:
    out: dict = {}
    out["BoostRate"] = (
        "NaN"
        if value.get("boost_rate", 0) != value.get("boost_rate", 0)
        else "Infinity"
        if value.get("boost_rate", 0) == float("inf")
        else "-Infinity"
        if value.get("boost_rate", 0) == float("-inf")
        else value.get("boost_rate", 0)
    )
    import capo_xray.types.timestamp

    out["BoostRateTTL"] = capo_xray.types.timestamp.serialize_json(
        value["boost_rate_ttl"]
    )
    return out


def deserialize_json(data: dict) -> SamplingBoost:
    out: SamplingBoost = {}  # type: ignore[typeddict-item]
    if data.get("BoostRate") is not None:
        out["boost_rate"] = float(data["BoostRate"])
    else:
        out["boost_rate"] = 0
    if data.get("BoostRateTTL") is not None:
        import capo_xray.types.timestamp

        out["boost_rate_ttl"] = capo_xray.types.timestamp.deserialize_json(
            data["BoostRateTTL"]
        )
    else:
        import datetime

        out["boost_rate_ttl"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
