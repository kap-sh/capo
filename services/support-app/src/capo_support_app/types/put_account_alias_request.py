"""Generated from Smithy shape ``com.amazonaws.supportapp#PutAccountAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support_app.types.aws_account_alias


class PutAccountAliasRequest(TypedDict, closed=True):
    account_alias: "capo_support_app.types.aws_account_alias.awsAccountAlias"
    """<p>An alias or short name for an Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountAliasRequest) -> dict:
    out: dict = {}
    out["accountAlias"] = value["account_alias"]
    return out


def deserialize_json(data: dict) -> PutAccountAliasRequest:
    out: PutAccountAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountAlias") is not None:
        out["account_alias"] = data["accountAlias"]
    else:
        out["account_alias"] = ""
    return out
