"""Generated from Smithy shape ``com.amazonaws.organizations#CloseAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.account_id


class CloseAccountRequest(TypedDict, closed=True):
    account_id: "capo_organizations.types.account_id.AccountId"
    """<p>Retrieves the Amazon Web Services account Id for the current <code>CloseAccount</code> API request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloseAccountRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloseAccountRequest:
    out: CloseAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    return out
