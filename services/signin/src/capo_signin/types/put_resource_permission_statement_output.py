"""Generated from Smithy shape ``com.amazonaws.signin#PutResourcePermissionStatementOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signin.types.statement_id


class PutResourcePermissionStatementOutput(TypedDict, closed=True):
    statement_id: "capo_signin.types.statement_id.StatementId"
    """Unique identifier for the created permission statement"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePermissionStatementOutput) -> dict:
    out: dict = {}
    out["statementId"] = value["statement_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePermissionStatementOutput:
    out: PutResourcePermissionStatementOutput = {}  # type: ignore[typeddict-item]
    if data.get("statementId") is not None:
        out["statement_id"] = data["statementId"]
    else:
        out["statement_id"] = ""
    return out
