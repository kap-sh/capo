"""Generated from Smithy shape ``com.amazonaws.pipes#FilterCriteria``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.filter_list


class FilterCriteria(TypedDict, closed=True):
    filters: NotRequired["capo_pipes.types.filter_list.FilterList"]
    """<p>The event patterns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteria) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_pipes.types.filter_list

        out["Filters"] = capo_pipes.types.filter_list.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> FilterCriteria:
    out: FilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_pipes.types.filter_list

        out["filters"] = capo_pipes.types.filter_list.deserialize_json(data["Filters"])
    return out


def redact_sensitive(value: FilterCriteria) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        import capo_pipes.types.filter_list

        out["filters"] = capo_pipes.types.filter_list.redact_sensitive(value["filters"])
    return out
