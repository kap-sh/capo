"""Generated from Smithy shape ``com.amazonaws.securityhub#DateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.date_range
    import capo_securityhub.types.non_empty_string


class DateFilter(TypedDict, closed=True):
    start: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A timestamp that provides the start date for the date filter.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    end: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A timestamp that provides the end date for the date filter.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    date_range: NotRequired["capo_securityhub.types.date_range.DateRange"]
    """<p>A date range for the date filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateFilter) -> dict:
    out: dict = {}
    if "start" in value:
        out["Start"] = value["start"]
    if "end" in value:
        out["End"] = value["end"]
    if "date_range" in value:
        import capo_securityhub.types.date_range

        out["DateRange"] = capo_securityhub.types.date_range.serialize_json(
            value["date_range"]
        )
    return out


def deserialize_json(data: dict) -> DateFilter:
    out: DateFilter = {}  # type: ignore[typeddict-item]
    if data.get("Start") is not None:
        out["start"] = data["Start"]
    if data.get("End") is not None:
        out["end"] = data["End"]
    if data.get("DateRange") is not None:
        import capo_securityhub.types.date_range

        out["date_range"] = capo_securityhub.types.date_range.deserialize_json(
            data["DateRange"]
        )
    return out
