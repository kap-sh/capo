"""Generated from Smithy shape ``com.amazonaws.signin#PermissionStatementSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.condition_block
    import capo_signin.types.statement_id


class PermissionStatementSummary(TypedDict, closed=True):
    sid: "capo_signin.types.statement_id.StatementId"
    """Unique identifier for the permission statement"""
    condition: NotRequired["capo_signin.types.condition_block.ConditionBlock"]
    """Condition block for the permission statement"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionStatementSummary) -> dict:
    out: dict = {}
    out["sid"] = value["sid"]
    if "condition" in value:
        import capo_signin.types.condition_block

        out["condition"] = capo_signin.types.condition_block.serialize_json(
            value["condition"]
        )
    return out


def deserialize_json(data: dict) -> PermissionStatementSummary:
    out: PermissionStatementSummary = {}  # type: ignore[typeddict-item]
    if data.get("sid") is not None:
        out["sid"] = data["sid"]
    else:
        out["sid"] = ""
    if data.get("condition") is not None:
        import capo_signin.types.condition_block

        out["condition"] = capo_signin.types.condition_block.deserialize_json(
            data["condition"]
        )
    return out
