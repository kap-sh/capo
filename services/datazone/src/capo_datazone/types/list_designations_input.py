"""Generated from Smithy shape ``com.amazonaws.datazone#ListDesignationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.list_designations_max_results
    import capo_datazone.types.pagination_token


class ListDesignationsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain that contains the designations to list.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>If the results exceed the value of <code>MaxResults</code>, the previous call returns a pagination token. Specify this token in a subsequent call to <code>ListDesignations</code> to retrieve the next set of results. If not specified, the operation returns the first page of results.</p>"""
    max_results: NotRequired[
        "capo_datazone.types.list_designations_max_results.ListDesignationsMaxResults"
    ]
    """<p>The maximum number of designations to return in a single call to <code>ListDesignations</code>. If the number of designations exceeds <code>MaxResults</code>, the response includes a <code>NextToken</code> value. Use that token in a subsequent call to <code>ListDesignations</code> to retrieve the next set of designations. The default value is 20.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDesignationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDesignationsInput:
    out: ListDesignationsInput = {}  # type: ignore[typeddict-item]
    return out
