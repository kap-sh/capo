"""Generated from Smithy shape ``com.amazonaws.securitylake#RegisterDataLakeDelegatedAdministratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.safe_string


class RegisterDataLakeDelegatedAdministratorRequest(TypedDict, closed=True):
    account_id: "capo_securitylake.types.safe_string.SafeString"
    """<p>The Amazon Web Services account ID of the Security Lake delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterDataLakeDelegatedAdministratorRequest) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> RegisterDataLakeDelegatedAdministratorRequest:
    out: RegisterDataLakeDelegatedAdministratorRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    return out
