"""Generated from Smithy shape ``com.amazonaws.organizations#RegisterDelegatedAdministratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.account_id
    import capo_organizations.types.service_principal


class RegisterDelegatedAdministratorRequest(TypedDict, closed=True):
    account_id: "capo_organizations.types.account_id.AccountId"
    """<p>The account ID number of the member account in the organization to register as a delegated administrator.</p>"""
    service_principal: "capo_organizations.types.service_principal.ServicePrincipal"
    """<p>The service principal of the Amazon Web Services service for which you want to make the member account a delegated administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterDelegatedAdministratorRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["ServicePrincipal"] = value["service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterDelegatedAdministratorRequest:
    out: RegisterDelegatedAdministratorRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("ServicePrincipal") is not None:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        out["service_principal"] = ""
    return out
