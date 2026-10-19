"""Generated from Smithy shape ``com.amazonaws.chime#CreateAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.account_name


class CreateAccountRequest(TypedDict, closed=True):
    name: "capo_chime.types.account_name.AccountName"
    """<p>The name of the Amazon Chime account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateAccountRequest:
    out: CreateAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
