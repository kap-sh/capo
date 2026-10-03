"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#UpdateTemplateGroupAccessControlEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.access_rights
    import capo_pca_connector_ad.types.display_name
    import capo_pca_connector_ad.types.group_security_identifier
    import capo_pca_connector_ad.types.template_arn


class UpdateTemplateGroupAccessControlEntryRequest(TypedDict, closed=True):
    template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>"""
    group_security_identifier: (
        "capo_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier"
    )
    """<p>Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".</p>"""
    group_display_name: NotRequired[
        "capo_pca_connector_ad.types.display_name.DisplayName"
    ]
    """<p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>"""
    access_rights: NotRequired["capo_pca_connector_ad.types.access_rights.AccessRights"]
    """<p>Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateGroupAccessControlEntryRequest) -> dict:
    out: dict = {}
    if "group_display_name" in value:
        out["GroupDisplayName"] = value["group_display_name"]
    if "access_rights" in value:
        import capo_pca_connector_ad.types.access_rights

        out["AccessRights"] = capo_pca_connector_ad.types.access_rights.serialize_json(
            value["access_rights"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTemplateGroupAccessControlEntryRequest:
    out: UpdateTemplateGroupAccessControlEntryRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupDisplayName") is not None:
        out["group_display_name"] = data["GroupDisplayName"]
    if data.get("AccessRights") is not None:
        import capo_pca_connector_ad.types.access_rights

        out["access_rights"] = (
            capo_pca_connector_ad.types.access_rights.deserialize_json(
                data["AccessRights"]
            )
        )
    return out
