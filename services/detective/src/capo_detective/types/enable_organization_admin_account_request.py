"""Generated from Smithy shape ``com.amazonaws.detective#EnableOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.account_id


class EnableOrganizationAdminAccountRequest(TypedDict, closed=True):
    account_id: "capo_detective.types.account_id.AccountId"
    """<p>The Amazon Web Services account identifier of the account to designate as the Detective administrator account for the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> EnableOrganizationAdminAccountRequest:
    out: EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    return out
