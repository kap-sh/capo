"""Generated from Smithy shape ``com.amazonaws.databrew#StatisticOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.parameter_map
    import capo_databrew.types.statistic


class StatisticOverride(TypedDict, closed=True):
    statistic: "capo_databrew.types.statistic.Statistic"
    """<p>The name of an evaluation</p>"""
    parameters: "capo_databrew.types.parameter_map.ParameterMap"
    """<p>A map that includes overrides of an evaluation’s parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatisticOverride) -> dict:
    out: dict = {}
    out["Statistic"] = value["statistic"]
    import capo_databrew.types.parameter_map

    out["Parameters"] = capo_databrew.types.parameter_map.serialize_json(
        value["parameters"]
    )
    return out


def deserialize_json(data: dict) -> StatisticOverride:
    out: StatisticOverride = {}  # type: ignore[typeddict-item]
    if data.get("Statistic") is not None:
        out["statistic"] = data["Statistic"]
    else:
        out["statistic"] = ""
    if data.get("Parameters") is not None:
        import capo_databrew.types.parameter_map

        out["parameters"] = capo_databrew.types.parameter_map.deserialize_json(
            data["Parameters"]
        )
    else:
        out["parameters"] = {}
    return out
