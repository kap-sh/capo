"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#MatchedPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam_toolbox.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam_toolbox.types.matched_statement_list


class MatchedPolicy(TypedDict, closed=True):
    uri: "str"
    """<p>The URI of the policy. This cross-references an entry in the top-level policies list. The value depends on the policy type:</p> <ul> <li> <p>For managed policies, this is the policy ARN.</p> </li> <li> <p>For inline policies, this is an opaque identifier.</p> </li> </ul>"""
    matched_statements: NotRequired[
        "capo_iam_toolbox.types.matched_statement_list.MatchedStatementList"
    ]
    """<p>The statements within the policy that matched during the evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchedPolicy) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    if "matched_statements" in value:
        import capo_iam_toolbox.types.matched_statement_list

        out["matchedStatements"] = (
            capo_iam_toolbox.types.matched_statement_list.serialize_json(
                value["matched_statements"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatchedPolicy:
    out: MatchedPolicy = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("MatchedPolicy.uri required")
    if data.get("matchedStatements") is not None:
        import capo_iam_toolbox.types.matched_statement_list

        out["matched_statements"] = (
            capo_iam_toolbox.types.matched_statement_list.deserialize_json(
                data["matchedStatements"]
            )
        )
    return out
