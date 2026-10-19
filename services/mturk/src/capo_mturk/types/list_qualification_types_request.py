"""Generated from Smithy shape ``com.amazonaws.mturk#ListQualificationTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.boolean
    import capo_mturk.types.pagination_token
    import capo_mturk.types.result_size
    import capo_mturk.types.string


class ListQualificationTypesRequest(TypedDict, closed=True):
    query: NotRequired["capo_mturk.types.string.String"]
    """<p> A text query against all of the searchable attributes of Qualification types. </p>"""
    must_be_requestable: "capo_mturk.types.boolean.Boolean"
    """<p>Specifies that only Qualification types that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test, are returned as results of the search. Some Qualification types, such as those assigned automatically by the system, cannot be requested directly by users. If false, all Qualification types, including those managed by the system, are considered. Valid values are True | False. </p>"""
    must_be_owned_by_caller: NotRequired["capo_mturk.types.boolean.Boolean"]
    """<p> Specifies that only Qualification types that the Requester created are returned. If false, the operation returns all Qualification types. </p>"""
    next_token: NotRequired["capo_mturk.types.pagination_token.PaginationToken"]
    max_results: NotRequired["capo_mturk.types.result_size.ResultSize"]
    """<p> The maximum number of results to return in a single call. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQualificationTypesRequest) -> dict:
    out: dict = {}
    if "query" in value:
        out["Query"] = value["query"]
    out["MustBeRequestable"] = value["must_be_requestable"]
    if "must_be_owned_by_caller" in value:
        out["MustBeOwnedByCaller"] = value["must_be_owned_by_caller"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQualificationTypesRequest:
    out: ListQualificationTypesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Query") is not None:
        out["query"] = data["Query"]
    if data.get("MustBeRequestable") is not None:
        out["must_be_requestable"] = data["MustBeRequestable"]
    else:
        out["must_be_requestable"] = False
    if data.get("MustBeOwnedByCaller") is not None:
        out["must_be_owned_by_caller"] = data["MustBeOwnedByCaller"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
