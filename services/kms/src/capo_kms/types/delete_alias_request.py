"""Generated from Smithy shape ``com.amazonaws.kms#DeleteAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kms.types.alias_name_type


class DeleteAliasRequest(TypedDict, closed=True):
    alias_name: "capo_kms.types.alias_name_type.AliasNameType"
    """<p>The alias to be deleted. The alias name must begin with <code>alias/</code> followed by the alias name, such as <code>alias/ExampleAlias</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAliasRequest) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAliasRequest:
    out: DeleteAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    else:
        out["alias_name"] = ""
    return out
