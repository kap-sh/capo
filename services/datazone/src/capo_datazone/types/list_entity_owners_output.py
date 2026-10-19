"""Generated from Smithy shape ``com.amazonaws.datazone#ListEntityOwnersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.entity_owners
    import capo_datazone.types.pagination_token


class ListEntityOwnersOutput(TypedDict, closed=True):
    owners: "capo_datazone.types.entity_owners.EntityOwners"
    """<p>The owners of the entity.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of entities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of entities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEntityOwners</code> to list the next set of entities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntityOwnersOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.entity_owners

    out["owners"] = capo_datazone.types.entity_owners.serialize_json(value["owners"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntityOwnersOutput:
    out: ListEntityOwnersOutput = {}  # type: ignore[typeddict-item]
    if data.get("owners") is not None:
        import capo_datazone.types.entity_owners

        out["owners"] = capo_datazone.types.entity_owners.deserialize_json(
            data["owners"]
        )
    else:
        out["owners"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
