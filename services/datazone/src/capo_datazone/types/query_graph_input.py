"""Generated from Smithy shape ``com.amazonaws.datazone#QueryGraphInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.additional_attributes
    import capo_datazone.types.domain_id
    import capo_datazone.types.match_clauses
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token


class QueryGraphInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    match: "capo_datazone.types.match_clauses.MatchClauses"
    """<p>List of query match clauses.</p>"""
    max_results: NotRequired["capo_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of entities to return in a single call to <code>QueryGraph</code>. When the number of entities to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>QueryGraph</code> to list the next set of entities.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of entities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of entities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>QueryGraph</code> to list the next set of entities.</p>"""
    additional_attributes: NotRequired[
        "capo_datazone.types.additional_attributes.AdditionalAttributes"
    ]
    """<p>Additional details on the queried entity that can be requested in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryGraphInput) -> dict:
    out: dict = {}
    import capo_datazone.types.match_clauses

    out["match"] = capo_datazone.types.match_clauses.serialize_json(value["match"])
    if "additional_attributes" in value:
        import capo_datazone.types.additional_attributes

        out["additionalAttributes"] = (
            capo_datazone.types.additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> QueryGraphInput:
    out: QueryGraphInput = {}  # type: ignore[typeddict-item]
    if data.get("match") is not None:
        import capo_datazone.types.match_clauses

        out["match"] = capo_datazone.types.match_clauses.deserialize_json(data["match"])
    else:
        out["match"] = []
    if data.get("additionalAttributes") is not None:
        import capo_datazone.types.additional_attributes

        out["additional_attributes"] = (
            capo_datazone.types.additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    return out
