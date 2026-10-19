"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#StartQualificationsDisassociationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.client_token
    import capo_partnercentral_account.types.partner_identifier
    import capo_partnercentral_account.types.qualifications_association_partner


class StartQualificationsDisassociationTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog in which to perform the qualifications disassociation. Valid values: <code>AWS</code>, <code>Sandbox</code>.</p>"""
    identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    """<p>Your partner identifier. You can provide either a partner ID (for example, <code>partner-abc123</code>) or a partner ARN. You must own this identifier.</p>"""
    client_token: NotRequired[
        "capo_partnercentral_account.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    associated_partner: "capo_partnercentral_account.types.qualifications_association_partner.QualificationsAssociationPartner"
    """<p>The primary partner's profile and account identifier that you are currently associated with and will disassociate from. You must provide at least one of <code>ProfileId</code> or <code>AccountId</code>. The specified partner must match your current primary association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartQualificationsDisassociationTaskRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import capo_partnercentral_account.types.qualifications_association_partner

    out["AssociatedPartner"] = (
        capo_partnercentral_account.types.qualifications_association_partner.serialize_aws_json_1_0(
            value["associated_partner"]
        )
    )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> StartQualificationsDisassociationTaskRequest:
    out: StartQualificationsDisassociationTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("AssociatedPartner") is not None:
        import capo_partnercentral_account.types.qualifications_association_partner

        out["associated_partner"] = (
            capo_partnercentral_account.types.qualifications_association_partner.deserialize_aws_json_1_0(
                data["AssociatedPartner"]
            )
        )
    else:
        raise DeserializationError(
            "StartQualificationsDisassociationTaskRequest.associated_partner required"
        )
    return out
