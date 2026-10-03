"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectSyntaxResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.list_of_syntax_tokens


class DetectSyntaxResponse(TypedDict, closed=True):
    syntax_tokens: NotRequired[
        "capo_comprehend.types.list_of_syntax_tokens.ListOfSyntaxTokens"
    ]
    """<p>A collection of syntax tokens describing the text. For each token, the response provides the text, the token type, where the text begins and ends, and the level of confidence that Amazon Comprehend has that the token is correct. For a list of token types, see <a href="https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html">Syntax</a> in the Comprehend Developer Guide. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectSyntaxResponse) -> dict:
    out: dict = {}
    if "syntax_tokens" in value:
        import capo_comprehend.types.list_of_syntax_tokens

        out["SyntaxTokens"] = (
            capo_comprehend.types.list_of_syntax_tokens.serialize_aws_json_1_1(
                value["syntax_tokens"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectSyntaxResponse:
    out: DetectSyntaxResponse = {}  # type: ignore[typeddict-item]
    if data.get("SyntaxTokens") is not None:
        import capo_comprehend.types.list_of_syntax_tokens

        out["syntax_tokens"] = (
            capo_comprehend.types.list_of_syntax_tokens.deserialize_aws_json_1_1(
                data["SyntaxTokens"]
            )
        )
    return out
