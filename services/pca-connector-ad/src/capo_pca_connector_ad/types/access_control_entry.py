"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#AccessControlEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pca_connector_ad.types.access_rights
    import capo_pca_connector_ad.types.display_name
    import capo_pca_connector_ad.types.group_security_identifier
    import capo_pca_connector_ad.types.template_arn


class AccessControlEntry(TypedDict, closed=True):
    group_display_name: NotRequired[
        "capo_pca_connector_ad.types.display_name.DisplayName"
    ]
    """<p>Name of the Active Directory group. This name does not need to match the group name in Active Directory.</p>"""
    group_security_identifier: NotRequired[
        "capo_pca_connector_ad.types.group_security_identifier.GroupSecurityIdentifier"
    ]
    """<p>Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".</p>"""
    access_rights: NotRequired["capo_pca_connector_ad.types.access_rights.AccessRights"]
    """<p>Permissions to allow or deny an Active Directory group to enroll or autoenroll certificates issued against a template.</p>"""
    template_arn: NotRequired["capo_pca_connector_ad.types.template_arn.TemplateArn"]
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the Access Control Entry was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the Access Control Entry was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessControlEntry) -> dict:
    out: dict = {}
    if "group_display_name" in value:
        out["GroupDisplayName"] = value["group_display_name"]
    if "group_security_identifier" in value:
        out["GroupSecurityIdentifier"] = value["group_security_identifier"]
    if "access_rights" in value:
        import capo_pca_connector_ad.types.access_rights

        out["AccessRights"] = capo_pca_connector_ad.types.access_rights.serialize_json(
            value["access_rights"]
        )
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "created_at" in value:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["CreatedAt"] = (
            capo_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["UpdatedAt"] = (
            capo_pca_connector_ad.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccessControlEntry:
    out: AccessControlEntry = {}  # type: ignore[typeddict-item]
    if data.get("GroupDisplayName") is not None:
        out["group_display_name"] = data["GroupDisplayName"]
    if data.get("GroupSecurityIdentifier") is not None:
        out["group_security_identifier"] = data["GroupSecurityIdentifier"]
    if data.get("AccessRights") is not None:
        import capo_pca_connector_ad.types.access_rights

        out["access_rights"] = (
            capo_pca_connector_ad.types.access_rights.deserialize_json(
                data["AccessRights"]
            )
        )
    if data.get("TemplateArn") is not None:
        out["template_arn"] = data["TemplateArn"]
    if data.get("CreatedAt") is not None:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["created_at"] = (
            capo_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_pca_connector_ad.types._prelude.timestamp

        out["updated_at"] = (
            capo_pca_connector_ad.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    return out
