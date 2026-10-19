"""Generated from Smithy shape ``com.amazonaws.workmail#RegisterMailDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.idempotency_client_token
    import capo_workmail.types.organization_id
    import capo_workmail.types.work_mail_domain_name


class RegisterMailDomainRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_workmail.types.idempotency_client_token.IdempotencyClientToken"
    ]
    """<p>Idempotency token used when retrying requests.</p>"""
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization under which you're creating the domain.</p>"""
    domain_name: "capo_workmail.types.work_mail_domain_name.WorkMailDomainName"
    """<p>The name of the mail domain to create in WorkMail and SES.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterMailDomainRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterMailDomainRequest:
    out: RegisterMailDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    return out
