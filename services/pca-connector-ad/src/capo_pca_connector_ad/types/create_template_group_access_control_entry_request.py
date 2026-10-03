"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CreateTemplateGroupAccessControlEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.access_rights
    import capo_pca_connector_ad.types.client_token
    import capo_pca_connector_ad.types.display_name
    import capo_pca_connector_ad.types.group_security_identifier
    import capo_pca_connector_ad.types.template_arn


class CreateTemplateGroupAccessControlEntryRequest(TypedDict, closed=True):
    template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>"""
    group_security_identifier: (
        "capo_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier"
    )
    """<p>Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".</p>"""
    group_display_name: "capo_pca_connector_ad.types.display_name.DisplayName"
    """<p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>"""
    access_rights: "capo_pca_connector_ad.types.access_rights.AccessRights"
    """<p> Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.</p>"""
    client_token: NotRequired["capo_pca_connector_ad.types.client_token.ClientToken"]
    """<p>Idempotency token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateGroupAccessControlEntryRequest) -> dict:
    out: dict = {}
    out["GroupSecurityIdentifier"] = value["group_security_identifier"]
    out["GroupDisplayName"] = value["group_display_name"]
    import capo_pca_connector_ad.types.access_rights

    out["AccessRights"] = capo_pca_connector_ad.types.access_rights.serialize_json(
        value["access_rights"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateTemplateGroupAccessControlEntryRequest:
    out: CreateTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupSecurityIdentifier") is not None:
        out["group_security_identifier"] = data["GroupSecurityIdentifier"]
    else:
        raise DeserializationError(
            "CreateTemplateGroupAccessControlEntryRequest.group_security_identifier required"
        )
    if data.get("GroupDisplayName") is not None:
        out["group_display_name"] = data["GroupDisplayName"]
    else:
        raise DeserializationError(
            "CreateTemplateGroupAccessControlEntryRequest.group_display_name required"
        )
    if data.get("AccessRights") is not None:
        import capo_pca_connector_ad.types.access_rights

        out["access_rights"] = (
            capo_pca_connector_ad.types.access_rights.deserialize_json(
                data["AccessRights"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTemplateGroupAccessControlEntryRequest.access_rights required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
