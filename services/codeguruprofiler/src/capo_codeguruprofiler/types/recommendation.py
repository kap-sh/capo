"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Recommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.matches
    import capo_codeguruprofiler.types.pattern
    import capo_codeguruprofiler.types.timestamp


class Recommendation(TypedDict, closed=True):
    all_matches_count: "int"
    """<p>How many different places in the profile graph triggered a match.</p>"""
    all_matches_sum: "float"
    """<p>How much of the total sample count is potentially affected.</p>"""
    pattern: "capo_codeguruprofiler.types.pattern.Pattern"
    """<p>The pattern that analysis recognized in the profile to make this recommendation.</p>"""
    top_matches: "capo_codeguruprofiler.types.matches.Matches"
    """<p>List of the matches with most impact. </p>"""
    start_time: "capo_codeguruprofiler.types.timestamp.Timestamp"
    """<p>The start time of the profile that was used by this analysis. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p>"""
    end_time: "capo_codeguruprofiler.types.timestamp.Timestamp"
    """<p>End time of the profile that was used by this analysis. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    out["allMatchesCount"] = value["all_matches_count"]
    out["allMatchesSum"] = (
        "NaN"
        if value["all_matches_sum"] != value["all_matches_sum"]
        else "Infinity"
        if value["all_matches_sum"] == float("inf")
        else "-Infinity"
        if value["all_matches_sum"] == float("-inf")
        else value["all_matches_sum"]
    )
    import capo_codeguruprofiler.types.pattern

    out["pattern"] = capo_codeguruprofiler.types.pattern.serialize_json(
        value["pattern"]
    )
    import capo_codeguruprofiler.types.matches

    out["topMatches"] = capo_codeguruprofiler.types.matches.serialize_json(
        value["top_matches"]
    )
    import capo_codeguruprofiler.types.timestamp

    out["startTime"] = capo_codeguruprofiler.types.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_codeguruprofiler.types.timestamp

    out["endTime"] = capo_codeguruprofiler.types.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if data.get("allMatchesCount") is not None:
        out["all_matches_count"] = data["allMatchesCount"]
    else:
        out["all_matches_count"] = 0
    if data.get("allMatchesSum") is not None:
        out["all_matches_sum"] = float(data["allMatchesSum"])
    else:
        out["all_matches_sum"] = 0.0
    if data.get("pattern") is not None:
        import capo_codeguruprofiler.types.pattern

        out["pattern"] = capo_codeguruprofiler.types.pattern.deserialize_json(
            data["pattern"]
        )
    else:
        raise DeserializationError("Recommendation.pattern required")
    if data.get("topMatches") is not None:
        import capo_codeguruprofiler.types.matches

        out["top_matches"] = capo_codeguruprofiler.types.matches.deserialize_json(
            data["topMatches"]
        )
    else:
        out["top_matches"] = []
    if data.get("startTime") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["start_time"] = capo_codeguruprofiler.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endTime") is not None:
        import capo_codeguruprofiler.types.timestamp

        out["end_time"] = capo_codeguruprofiler.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
