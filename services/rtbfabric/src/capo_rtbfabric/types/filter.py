"""Generated from Smithy shape ``com.amazonaws.rtbfabric#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.filter_criteria


class Filter(TypedDict, closed=True):
    criteria: "capo_rtbfabric.types.filter_criteria.FilterCriteria"
    """<p>Describes the criteria for a filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    import capo_rtbfabric.types.filter_criteria

    out["criteria"] = capo_rtbfabric.types.filter_criteria.serialize_json(
        value["criteria"]
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("criteria") is not None:
        import capo_rtbfabric.types.filter_criteria

        out["criteria"] = capo_rtbfabric.types.filter_criteria.deserialize_json(
            data["criteria"]
        )
    else:
        out["criteria"] = []
    return out
