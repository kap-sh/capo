"""Generated from Smithy shape ``com.amazonaws.workmail#GetMailDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.organization_id
    import capo_workmail.types.work_mail_domain_name


class GetMailDomainRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which the domain is retrieved.</p>"""
    domain_name: "capo_workmail.types.work_mail_domain_name.WorkMailDomainName"
    """<p>The domain from which you want to retrieve details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMailDomainRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMailDomainRequest:
    out: GetMailDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    return out
