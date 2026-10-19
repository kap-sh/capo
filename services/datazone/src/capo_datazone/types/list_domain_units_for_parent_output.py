"""Generated from Smithy shape ``com.amazonaws.datazone#ListDomainUnitsForParentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_summaries
    import capo_datazone.types.pagination_token


class ListDomainUnitsForParentOutput(TypedDict, closed=True):
    items: "capo_datazone.types.domain_unit_summaries.DomainUnitSummaries"
    """<p>The results returned by this action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of domain units is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of domain units, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainUnitsForParentOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.domain_unit_summaries

    out["items"] = capo_datazone.types.domain_unit_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainUnitsForParentOutput:
    out: ListDomainUnitsForParentOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.domain_unit_summaries

        out["items"] = capo_datazone.types.domain_unit_summaries.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
