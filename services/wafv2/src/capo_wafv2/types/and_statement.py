"""Generated from Smithy shape ``com.amazonaws.wafv2#AndStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.statements


class AndStatement(TypedDict, closed=True):
    statements: "capo_wafv2.types.statements.Statements"
    """<p>The statements to combine with AND logic. You can use any statements that can be nested. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AndStatement) -> dict:
    out: dict = {}
    import capo_wafv2.types.statements

    out["Statements"] = capo_wafv2.types.statements.serialize_aws_json_1_1(
        value["statements"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AndStatement:
    out: AndStatement = {}  # type: ignore[typeddict-item]
    if data.get("Statements") is not None:
        import capo_wafv2.types.statements

        out["statements"] = capo_wafv2.types.statements.deserialize_aws_json_1_1(
            data["Statements"]
        )
    else:
        out["statements"] = []
    return out
