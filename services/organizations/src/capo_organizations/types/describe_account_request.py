"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.account_id


class DescribeAccountRequest(TypedDict, closed=True):
    account_id: "capo_organizations.types.account_id.AccountId"
    """<p>The unique identifier (ID) of the Amazon Web Services account that you want information about. You can get the ID from the <a>ListAccounts</a> or <a>ListAccountsForParent</a> operations.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for an account ID string requires exactly 12 digits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountRequest:
    out: DescribeAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("DescribeAccountRequest.account_id required")
    return out
