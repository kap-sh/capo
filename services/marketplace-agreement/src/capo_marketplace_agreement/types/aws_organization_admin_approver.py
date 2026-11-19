"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AwsOrganizationAdminApprover``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.organization_id


class AwsOrganizationAdminApprover(TypedDict, closed=True):
    organization_id: "capo_marketplace_agreement.types.organization_id.OrganizationId"
    """<p>The ID of the AWS organization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOrganizationAdminApprover) -> dict:
    out: dict = {}
    out["organizationId"] = value["organization_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOrganizationAdminApprover:
    out: AwsOrganizationAdminApprover = {}  # type: ignore[typeddict-item]
    if data.get("organizationId") is not None:
        out["organization_id"] = data["organizationId"]
    else:
        out["organization_id"] = ""
    return out
