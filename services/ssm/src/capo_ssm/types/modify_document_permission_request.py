"""Generated from Smithy shape ``com.amazonaws.ssm#ModifyDocumentPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.account_id_list
    import capo_ssm.types.document_name
    import capo_ssm.types.document_permission_type
    import capo_ssm.types.shared_document_version


class ModifyDocumentPermissionRequest(TypedDict, closed=True):
    name: "capo_ssm.types.document_name.DocumentName"
    """<p>The name of the document that you want to share.</p>"""
    permission_type: "capo_ssm.types.document_permission_type.DocumentPermissionType"
    """<p>The permission type for the document. The permission type can be <i>Share</i>.</p>"""
    account_ids_to_add: NotRequired["capo_ssm.types.account_id_list.AccountIdList"]
    """<p>The Amazon Web Services users that should have access to the document. The account IDs can either be a group of account IDs or <i>All</i>. You must specify a value for this parameter or the <code>AccountIdsToRemove</code> parameter.</p>"""
    account_ids_to_remove: NotRequired["capo_ssm.types.account_id_list.AccountIdList"]
    """<p>The Amazon Web Services users that should no longer have access to the document. The Amazon Web Services user can either be a group of account IDs or <i>All</i>. This action has a higher priority than <code>AccountIdsToAdd</code>. If you specify an ID to add and the same ID to remove, the system removes access to the document. You must specify a value for this parameter or the <code>AccountIdsToAdd</code> parameter.</p>"""
    shared_document_version: NotRequired[
        "capo_ssm.types.shared_document_version.SharedDocumentVersion"
    ]
    """<p>(Optional) The version of the document to share. If it isn't specified, the system choose the <code>Default</code> version to share.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyDocumentPermissionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_ssm.types.document_permission_type

    out["PermissionType"] = (
        capo_ssm.types.document_permission_type.serialize_aws_json_1_1(
            value["permission_type"]
        )
    )
    if "account_ids_to_add" in value:
        import capo_ssm.types.account_id_list

        out["AccountIdsToAdd"] = capo_ssm.types.account_id_list.serialize_aws_json_1_1(
            value["account_ids_to_add"]
        )
    if "account_ids_to_remove" in value:
        import capo_ssm.types.account_id_list

        out["AccountIdsToRemove"] = (
            capo_ssm.types.account_id_list.serialize_aws_json_1_1(
                value["account_ids_to_remove"]
            )
        )
    if "shared_document_version" in value:
        out["SharedDocumentVersion"] = value["shared_document_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyDocumentPermissionRequest:
    out: ModifyDocumentPermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("PermissionType") is not None:
        import capo_ssm.types.document_permission_type

        out["permission_type"] = (
            capo_ssm.types.document_permission_type.deserialize_aws_json_1_1(
                data["PermissionType"]
            )
        )
    else:
        import typing

        out["permission_type"] = typing.cast(
            "capo_ssm.types.document_permission_type.DocumentPermissionType", ""
        )
    if data.get("AccountIdsToAdd") is not None:
        import capo_ssm.types.account_id_list

        out["account_ids_to_add"] = (
            capo_ssm.types.account_id_list.deserialize_aws_json_1_1(
                data["AccountIdsToAdd"]
            )
        )
    if data.get("AccountIdsToRemove") is not None:
        import capo_ssm.types.account_id_list

        out["account_ids_to_remove"] = (
            capo_ssm.types.account_id_list.deserialize_aws_json_1_1(
                data["AccountIdsToRemove"]
            )
        )
    if data.get("SharedDocumentVersion") is not None:
        out["shared_document_version"] = data["SharedDocumentVersion"]
    return out
