"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetQualificationsDisassociationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.partner_identifier


class GetQualificationsDisassociationTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog in which to look up the qualifications disassociation task. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>"""
    identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    """<p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQualificationsDisassociationTaskRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQualificationsDisassociationTaskRequest:
    out: GetQualificationsDisassociationTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
