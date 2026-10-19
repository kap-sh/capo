"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.alias_name


class GetAliasInput(TypedDict, closed=True):
    alias_name: "capo_payment_cryptography.types.alias_name.AliasName"
    """<p>The alias of the Amazon Web Services Payment Cryptography key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAliasInput) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAliasInput:
    out: GetAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    else:
        out["alias_name"] = ""
    return out
