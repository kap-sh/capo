"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommentReactionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.next_token
    import capo_codecommit.types.reactions_for_comment_list


class GetCommentReactionsOutput(TypedDict, closed=True):
    reactions_for_comment: (
        "capo_codecommit.types.reactions_for_comment_list.ReactionsForCommentList"
    )
    """<p>An array of reactions to the specified comment.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommentReactionsOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.reactions_for_comment_list

    out["reactionsForComment"] = (
        capo_codecommit.types.reactions_for_comment_list.serialize_aws_json_1_1(
            value["reactions_for_comment"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommentReactionsOutput:
    out: GetCommentReactionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("reactionsForComment") is not None:
        import capo_codecommit.types.reactions_for_comment_list

        out["reactions_for_comment"] = (
            capo_codecommit.types.reactions_for_comment_list.deserialize_aws_json_1_1(
                data["reactionsForComment"]
            )
        )
    else:
        out["reactions_for_comment"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
