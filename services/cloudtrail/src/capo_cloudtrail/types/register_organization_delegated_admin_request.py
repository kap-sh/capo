"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RegisterOrganizationDelegatedAdminRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id


class RegisterOrganizationDelegatedAdminRequest(TypedDict, closed=True):
    member_account_id: "capo_cloudtrail.types.account_id.AccountId"
    """<p>An organization member account ID that you want to designate as a delegated administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterOrganizationDelegatedAdminRequest) -> dict:
    out: dict = {}
    out["MemberAccountId"] = value["member_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterOrganizationDelegatedAdminRequest:
    out: RegisterOrganizationDelegatedAdminRequest = {}  # type: ignore[typeddict-item]
    if data.get("MemberAccountId") is not None:
        out["member_account_id"] = data["MemberAccountId"]
    else:
        out["member_account_id"] = ""
    return out
