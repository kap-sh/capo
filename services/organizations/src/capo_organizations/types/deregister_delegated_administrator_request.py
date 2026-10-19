"""Generated from Smithy shape ``com.amazonaws.organizations#DeregisterDelegatedAdministratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.account_id
    import capo_organizations.types.service_principal


class DeregisterDelegatedAdministratorRequest(TypedDict, closed=True):
    account_id: "capo_organizations.types.account_id.AccountId"
    """<p>The account ID number of the member account in the organization that you want to deregister as a delegated administrator.</p>"""
    service_principal: "capo_organizations.types.service_principal.ServicePrincipal"
    """<p>The service principal name of an Amazon Web Services service for which the account is a delegated administrator.</p> <p>Delegated administrator privileges are revoked for only the specified Amazon Web Services service from the member account. If the specified service is the only service for which the member account is a delegated administrator, the operation also revokes Organizations read action permissions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterDelegatedAdministratorRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["ServicePrincipal"] = value["service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterDelegatedAdministratorRequest:
    out: DeregisterDelegatedAdministratorRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("ServicePrincipal") is not None:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        out["service_principal"] = ""
    return out
