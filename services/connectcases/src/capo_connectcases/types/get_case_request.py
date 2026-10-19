"""Generated from Smithy shape ``com.amazonaws.connectcases#GetCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_id
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_identifier_list
    import capo_connectcases.types.next_token


class GetCaseRequest(TypedDict, closed=True):
    case_id: "capo_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    fields: "capo_connectcases.types.field_identifier_list.FieldIdentifierList"
    """<p>A list of unique field identifiers. </p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCaseRequest) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_identifier_list

    out["fields"] = capo_connectcases.types.field_identifier_list.serialize_json(
        value["fields"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCaseRequest:
    out: GetCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_connectcases.types.field_identifier_list

        out["fields"] = capo_connectcases.types.field_identifier_list.deserialize_json(
            data["fields"]
        )
    else:
        out["fields"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
