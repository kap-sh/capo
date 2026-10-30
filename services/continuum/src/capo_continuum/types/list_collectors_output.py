"""Generated from Smithy shape ``com.amazonaws.continuum#ListCollectorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.collector_summaries


class ListCollectorsOutput(TypedDict, closed=True):
    items: "capo_continuum.types.collector_summaries.CollectorSummaries"
    """The Collectors owned by the authenticated caller's account. At most one result is currently returned, so no result ordering applies."""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollectorsOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.collector_summaries

    out["items"] = capo_continuum.types.collector_summaries.serialize_json(
        value["items"]
    )
    return out


def deserialize_json(data: dict) -> ListCollectorsOutput:
    out: ListCollectorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_continuum.types.collector_summaries

        out["items"] = capo_continuum.types.collector_summaries.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    return out
