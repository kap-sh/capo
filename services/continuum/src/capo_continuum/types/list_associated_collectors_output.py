"""Generated from Smithy shape ``com.amazonaws.continuum#ListAssociatedCollectorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.associated_collectors
    import capo_continuum.types.next_token


class ListAssociatedCollectorsOutput(TypedDict, closed=True):
    associated_collectors: (
        "capo_continuum.types.associated_collectors.AssociatedCollectors"
    )
    """The Collectors associated with this Environment, ordered by collectorId ascending. Empty when the Environment has no associations, and also when every association on the page predates Continuum persisting the ARN — the page is still advanced by `nextToken` in that case."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """Pagination token for the next page, if present."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedCollectorsOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.associated_collectors

    out["associatedCollectors"] = (
        capo_continuum.types.associated_collectors.serialize_json(
            value["associated_collectors"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedCollectorsOutput:
    out: ListAssociatedCollectorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("associatedCollectors") is not None:
        import capo_continuum.types.associated_collectors

        out["associated_collectors"] = (
            capo_continuum.types.associated_collectors.deserialize_json(
                data["associatedCollectors"]
            )
        )
    else:
        out["associated_collectors"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
