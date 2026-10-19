"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#DeleteAliasInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.alias_name


class DeleteAliasInput(TypedDict, closed=True):
    alias_name: "capo_payment_cryptography.types.alias_name.AliasName"
    """<p>A friendly name that you can use to refer Amazon Web Services Payment Cryptography key. This value must begin with <code>alias/</code> followed by a name, such as <code>alias/ExampleAlias</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAliasInput) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAliasInput:
    out: DeleteAliasInput = {}  # type: ignore[typeddict-item]
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    else:
        out["alias_name"] = ""
    return out
