"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#MatchedStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iam_toolbox.types.matched_statement

MatchedStatementList: TypeAlias = list[
    "capo_iam_toolbox.types.matched_statement.MatchedStatement"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchedStatementList) -> list:
    import capo_iam_toolbox.types.matched_statement

    out: list = []
    for item in value:
        out.append(capo_iam_toolbox.types.matched_statement.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchedStatementList:
    import capo_iam_toolbox.types.matched_statement

    out: MatchedStatementList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iam_toolbox.types.matched_statement.deserialize_json(item))
    return out
