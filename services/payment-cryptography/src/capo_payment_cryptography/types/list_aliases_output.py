"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ListAliasesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.aliases
    import capo_payment_cryptography.types.next_token


class ListAliasesOutput(TypedDict, closed=True):
    aliases: "capo_payment_cryptography.types.aliases.Aliases"
    """<p>The list of aliases. Each alias describes the <code>KeyArn</code> contained within.</p>"""
    next_token: NotRequired["capo_payment_cryptography.types.next_token.NextToken"]
    """<p>The token for the next set of results, or an empty or null value if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAliasesOutput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.aliases

    out["Aliases"] = capo_payment_cryptography.types.aliases.serialize_aws_json_1_0(
        value["aliases"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAliasesOutput:
    out: ListAliasesOutput = {}  # type: ignore[typeddict-item]
    if data.get("Aliases") is not None:
        import capo_payment_cryptography.types.aliases

        out["aliases"] = (
            capo_payment_cryptography.types.aliases.deserialize_aws_json_1_0(
                data["Aliases"]
            )
        )
    else:
        out["aliases"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
