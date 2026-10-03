"""Generated from Smithy shape ``com.amazonaws.organizations#RemoveAccountFromOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.account_id


class RemoveAccountFromOrganizationRequest(TypedDict, closed=True):
    account_id: "capo_organizations.types.account_id.AccountId"
    """<p>ID for the member account that you want to remove from the organization.</p> <p>The <a href="http://wikipedia.org/wiki/regex">regex pattern</a> for an account ID string requires exactly 12 digits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveAccountFromOrganizationRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveAccountFromOrganizationRequest:
    out: RemoveAccountFromOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "RemoveAccountFromOrganizationRequest.account_id required"
        )
    return out
