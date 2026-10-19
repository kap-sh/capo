"""Generated from Smithy shape ``com.amazonaws.workmail#DeleteAvailabilityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.domain_name
    import capo_workmail.types.organization_id


class DeleteAvailabilityConfigurationRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The WorkMail organization for which the <code>AvailabilityConfiguration</code> will be deleted.</p>"""
    domain_name: "capo_workmail.types.domain_name.DomainName"
    """<p>The domain for which the <code>AvailabilityConfiguration</code> will be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAvailabilityConfigurationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAvailabilityConfigurationRequest:
    out: DeleteAvailabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    return out
