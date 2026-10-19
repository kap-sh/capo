"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AccountSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.unicode_string


class AccountSummary(TypedDict, closed=True):
    name: "capo_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The name associated with the AWS account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountSummary) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountSummary:
    out: AccountSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
