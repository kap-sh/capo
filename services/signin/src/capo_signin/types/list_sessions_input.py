"""Generated from Smithy shape ``com.amazonaws.signin#ListSessionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.next_token
    import capo_signin.types.principal_arn_filter
    import capo_signin.types.session_status
    import capo_signin.types.sessions_max_results


class ListSessionsInput(TypedDict, closed=True):
    principal_arn: NotRequired[
        "capo_signin.types.principal_arn_filter.PrincipalArnFilter"
    ]
    """The identity whose sessions to list. Omit to list the caller's own sessions. Specify arn:aws:iam::{account-id}:* to list all sessions in the account."""
    max_results: NotRequired[
        "capo_signin.types.sessions_max_results.SessionsMaxResults"
    ]
    """Maximum number of results to return"""
    next_token: NotRequired["capo_signin.types.next_token.NextToken"]
    """Token for pagination"""
    status: NotRequired["capo_signin.types.session_status.SessionStatus"]
    """Returns only sessions with this status"""
    client_id: NotRequired["str"]
    """Returns only sessions created by this OAuth client"""
    issued_after: NotRequired["int"]
    """Returns only sessions created at or after this time, in Unix epoch seconds"""
    issued_before: NotRequired["int"]
    """Returns only sessions created before this time, in Unix epoch seconds"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsInput) -> dict:
    out: dict = {}
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "status" in value:
        import capo_signin.types.session_status

        out["status"] = capo_signin.types.session_status.serialize_json(value["status"])
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "issued_after" in value:
        out["issuedAfter"] = value["issued_after"]
    if "issued_before" in value:
        out["issuedBefore"] = value["issued_before"]
    return out


def deserialize_json(data: dict) -> ListSessionsInput:
    out: ListSessionsInput = {}  # type: ignore[typeddict-item]
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("status") is not None:
        import capo_signin.types.session_status

        out["status"] = capo_signin.types.session_status.deserialize_json(
            data["status"]
        )
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    if data.get("issuedAfter") is not None:
        out["issued_after"] = data["issuedAfter"]
    if data.get("issuedBefore") is not None:
        out["issued_before"] = data["issuedBefore"]
    return out
