"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateFileSystemAssociationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.audit_destination_arn
    import capo_storage_gateway.types.cache_attributes
    import capo_storage_gateway.types.domain_user_name
    import capo_storage_gateway.types.domain_user_password
    import capo_storage_gateway.types.file_system_association_arn


class UpdateFileSystemAssociationInput(TypedDict, closed=True):
    file_system_association_arn: "capo_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN"
    """<p>The Amazon Resource Name (ARN) of the file system association that you want to update.</p>"""
    user_name: NotRequired["capo_storage_gateway.types.domain_user_name.DomainUserName"]
    """<p>The user name of the user credential that has permission to access the root share D$ of the Amazon FSx file system. The user account must belong to the Amazon FSx delegated admin user group.</p>"""
    password: NotRequired[
        "capo_storage_gateway.types.domain_user_password.DomainUserPassword"
    ]
    """<p>The password of the user credential.</p>"""
    audit_destination_arn: NotRequired[
        "capo_storage_gateway.types.audit_destination_arn.AuditDestinationARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the storage used for the audit logs.</p>"""
    cache_attributes: NotRequired[
        "capo_storage_gateway.types.cache_attributes.CacheAttributes"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemAssociationInput) -> dict:
    out: dict = {}
    out["FileSystemAssociationARN"] = value["file_system_association_arn"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "password" in value:
        out["Password"] = value["password"]
    if "audit_destination_arn" in value:
        out["AuditDestinationARN"] = value["audit_destination_arn"]
    if "cache_attributes" in value:
        import capo_storage_gateway.types.cache_attributes

        out["CacheAttributes"] = (
            capo_storage_gateway.types.cache_attributes.serialize_aws_json_1_1(
                value["cache_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemAssociationInput:
    out: UpdateFileSystemAssociationInput = {}  # type: ignore[typeddict-item]
    if data.get("FileSystemAssociationARN") is not None:
        out["file_system_association_arn"] = data["FileSystemAssociationARN"]
    else:
        raise DeserializationError(
            "UpdateFileSystemAssociationInput.file_system_association_arn required"
        )
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("AuditDestinationARN") is not None:
        out["audit_destination_arn"] = data["AuditDestinationARN"]
    if data.get("CacheAttributes") is not None:
        import capo_storage_gateway.types.cache_attributes

        out["cache_attributes"] = (
            capo_storage_gateway.types.cache_attributes.deserialize_aws_json_1_1(
                data["CacheAttributes"]
            )
        )
    return out


def redact_sensitive(value: UpdateFileSystemAssociationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
