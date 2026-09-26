"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#MatchedStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iam_toolbox.types.statement_effect


class MatchedStatement(TypedDict, closed=True):
    sid: NotRequired["str"]
    """<p>The statement ID (Sid). If the statement has no Sid, one is generated for reference.</p>"""
    evaluated_effect: NotRequired[
        "capo_iam_toolbox.types.statement_effect.StatementEffect"
    ]
    """<p>The evaluated effect of this statement. Valid values:</p> <ul> <li> <p> <code>ALLOW</code> - The statement allows the action.</p> </li> <li> <p> <code>DENY</code> - The statement denies the action.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchedStatement) -> dict:
    out: dict = {}
    if "sid" in value:
        out["sid"] = value["sid"]
    if "evaluated_effect" in value:
        import capo_iam_toolbox.types.statement_effect

        out["evaluatedEffect"] = capo_iam_toolbox.types.statement_effect.serialize_json(
            value["evaluated_effect"]
        )
    return out


def deserialize_json(data: dict) -> MatchedStatement:
    out: MatchedStatement = {}  # type: ignore[typeddict-item]
    if data.get("sid") is not None:
        out["sid"] = data["sid"]
    if data.get("evaluatedEffect") is not None:
        import capo_iam_toolbox.types.statement_effect

        out["evaluated_effect"] = (
            capo_iam_toolbox.types.statement_effect.deserialize_json(
                data["evaluatedEffect"]
            )
        )
    return out
