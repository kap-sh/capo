"""Generated from Smithy shape ``com.amazonaws.signin#ListResourcePermissionStatementsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.next_token
    import capo_signin.types.permission_statement_summaries


class ListResourcePermissionStatementsOutput(TypedDict, closed=True):
    permission_statements: (
        "capo_signin.types.permission_statement_summaries.PermissionStatementSummaries"
    )
    """List of permission statement summaries"""
    next_token: NotRequired["capo_signin.types.next_token.NextToken"]
    """Token for next page of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcePermissionStatementsOutput) -> dict:
    out: dict = {}
    import capo_signin.types.permission_statement_summaries

    out["permissionStatements"] = (
        capo_signin.types.permission_statement_summaries.serialize_json(
            value["permission_statements"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourcePermissionStatementsOutput:
    out: ListResourcePermissionStatementsOutput = {}  # type: ignore[typeddict-item]
    if data.get("permissionStatements") is not None:
        import capo_signin.types.permission_statement_summaries

        out["permission_statements"] = (
            capo_signin.types.permission_statement_summaries.deserialize_json(
                data["permissionStatements"]
            )
        )
    else:
        out["permission_statements"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
