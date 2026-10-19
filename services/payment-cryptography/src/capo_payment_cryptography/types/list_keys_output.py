"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ListKeysOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.key_summary_list
    import capo_payment_cryptography.types.next_token


class ListKeysOutput(TypedDict, closed=True):
    keys: "capo_payment_cryptography.types.key_summary_list.KeySummaryList"
    """<p>The list of keys created within the caller's Amazon Web Services account and Amazon Web Services Region.</p>"""
    next_token: NotRequired["capo_payment_cryptography.types.next_token.NextToken"]
    """<p>The token for the next set of results, or an empty or null value if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListKeysOutput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.key_summary_list

    out["Keys"] = (
        capo_payment_cryptography.types.key_summary_list.serialize_aws_json_1_0(
            value["keys"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListKeysOutput:
    out: ListKeysOutput = {}  # type: ignore[typeddict-item]
    if data.get("Keys") is not None:
        import capo_payment_cryptography.types.key_summary_list

        out["keys"] = (
            capo_payment_cryptography.types.key_summary_list.deserialize_aws_json_1_0(
                data["Keys"]
            )
        )
    else:
        out["keys"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
