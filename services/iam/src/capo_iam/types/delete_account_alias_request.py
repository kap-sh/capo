"""Generated from Smithy shape ``com.amazonaws.iam#DeleteAccountAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.account_alias_type


class DeleteAccountAliasRequest(TypedDict, closed=True):
    account_alias: "capo_iam.types.account_alias_type.accountAliasType"
    """<p>The name of the account alias to delete.</p> <p>This parameter allows (through its <a href="http://wikipedia.org/wiki/regex">regex pattern</a>) a string of characters consisting of lowercase letters, digits, and dashes. You cannot start or finish with a dash, nor can you have two dashes in a row.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAccountAliasRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}AccountAlias", str(value["account_alias"])))


def deserialize_query(el: Element) -> DeleteAccountAliasRequest:
    out: DeleteAccountAliasRequest = {}  # type: ignore[typeddict-item]
    child_account_alias = el.find("AccountAlias")
    if child_account_alias is not None:
        out["account_alias"] = str(child_account_alias.text or "")
    else:
        raise DeserializationError("DeleteAccountAliasRequest.account_alias required")
    return out
