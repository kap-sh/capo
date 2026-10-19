"""Generated from Smithy shape ``com.amazonaws.databrew#AllowedStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.statistic_list


class AllowedStatistics(TypedDict, closed=True):
    statistics: "capo_databrew.types.statistic_list.StatisticList"
    """<p>One or more column statistics to allow for columns that contain detected entities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AllowedStatistics) -> dict:
    out: dict = {}
    import capo_databrew.types.statistic_list

    out["Statistics"] = capo_databrew.types.statistic_list.serialize_json(
        value["statistics"]
    )
    return out


def deserialize_json(data: dict) -> AllowedStatistics:
    out: AllowedStatistics = {}  # type: ignore[typeddict-item]
    if data.get("Statistics") is not None:
        import capo_databrew.types.statistic_list

        out["statistics"] = capo_databrew.types.statistic_list.deserialize_json(
            data["Statistics"]
        )
    else:
        out["statistics"] = []
    return out
