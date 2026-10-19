"""Generated from Smithy shape ``com.amazonaws.signin#DeleteResourcePermissionStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.client_token
    import capo_signin.types.statement_id


class DeleteResourcePermissionStatementInput(TypedDict, closed=True):
    statement_id: "capo_signin.types.statement_id.StatementId"
    """Unique identifier of the permission statement to delete"""
    client_token: NotRequired["capo_signin.types.client_token.ClientToken"]
    """Idempotency token for the request"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePermissionStatementInput) -> dict:
    out: dict = {}
    out["statementId"] = value["statement_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteResourcePermissionStatementInput:
    out: DeleteResourcePermissionStatementInput = {}  # type: ignore[typeddict-item]
    if data.get("statementId") is not None:
        out["statement_id"] = data["statementId"]
    else:
        out["statement_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
