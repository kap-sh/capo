"""Generated from Smithy shape ``com.amazonaws.directoryservice#SharedDirectory``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.created_date_time
    import capo_directory_service.types.customer_id
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.last_updated_date_time
    import capo_directory_service.types.notes
    import capo_directory_service.types.share_method
    import capo_directory_service.types.share_status


class SharedDirectory(TypedDict, closed=True):
    owner_account_id: NotRequired["capo_directory_service.types.customer_id.CustomerId"]
    """<p>Identifier of the directory owner account, which contains the directory that has been shared to the consumer account.</p>"""
    owner_directory_id: NotRequired[
        "capo_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>Identifier of the directory in the directory owner account. </p>"""
    share_method: NotRequired["capo_directory_service.types.share_method.ShareMethod"]
    """<p>The method used when sharing a directory to determine whether the directory should be shared within your Amazon Web Services organization (<code>ORGANIZATIONS</code>) or with any Amazon Web Services account by sending a shared directory request (<code>HANDSHAKE</code>).</p>"""
    shared_account_id: NotRequired[
        "capo_directory_service.types.customer_id.CustomerId"
    ]
    """<p>Identifier of the directory consumer account that has access to the shared directory (<code>OwnerDirectoryId</code>) in the directory owner account.</p>"""
    shared_directory_id: NotRequired[
        "capo_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.</p>"""
    share_status: NotRequired["capo_directory_service.types.share_status.ShareStatus"]
    """<p>Current directory status of the shared Managed Microsoft AD directory.</p>"""
    share_notes: NotRequired["capo_directory_service.types.notes.Notes"]
    """<p>A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.</p>"""
    created_date_time: NotRequired[
        "capo_directory_service.types.created_date_time.CreatedDateTime"
    ]
    """<p>The date and time that the shared directory was created.</p>"""
    last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time that the shared directory was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharedDirectory) -> dict:
    out: dict = {}
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "owner_directory_id" in value:
        out["OwnerDirectoryId"] = value["owner_directory_id"]
    if "share_method" in value:
        import capo_directory_service.types.share_method

        out["ShareMethod"] = (
            capo_directory_service.types.share_method.serialize_aws_json_1_1(
                value["share_method"]
            )
        )
    if "shared_account_id" in value:
        out["SharedAccountId"] = value["shared_account_id"]
    if "shared_directory_id" in value:
        out["SharedDirectoryId"] = value["shared_directory_id"]
    if "share_status" in value:
        import capo_directory_service.types.share_status

        out["ShareStatus"] = (
            capo_directory_service.types.share_status.serialize_aws_json_1_1(
                value["share_status"]
            )
        )
    if "share_notes" in value:
        out["ShareNotes"] = value["share_notes"]
    if "created_date_time" in value:
        import capo_directory_service.types.created_date_time

        out["CreatedDateTime"] = (
            capo_directory_service.types.created_date_time.serialize_aws_json_1_1(
                value["created_date_time"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SharedDirectory:
    out: SharedDirectory = {}  # type: ignore[typeddict-item]
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("OwnerDirectoryId") is not None:
        out["owner_directory_id"] = data["OwnerDirectoryId"]
    if data.get("ShareMethod") is not None:
        import capo_directory_service.types.share_method

        out["share_method"] = (
            capo_directory_service.types.share_method.deserialize_aws_json_1_1(
                data["ShareMethod"]
            )
        )
    if data.get("SharedAccountId") is not None:
        out["shared_account_id"] = data["SharedAccountId"]
    if data.get("SharedDirectoryId") is not None:
        out["shared_directory_id"] = data["SharedDirectoryId"]
    if data.get("ShareStatus") is not None:
        import capo_directory_service.types.share_status

        out["share_status"] = (
            capo_directory_service.types.share_status.deserialize_aws_json_1_1(
                data["ShareStatus"]
            )
        )
    if data.get("ShareNotes") is not None:
        out["share_notes"] = data["ShareNotes"]
    if data.get("CreatedDateTime") is not None:
        import capo_directory_service.types.created_date_time

        out["created_date_time"] = (
            capo_directory_service.types.created_date_time.deserialize_aws_json_1_1(
                data["CreatedDateTime"]
            )
        )
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    return out


def redact_sensitive(value: SharedDirectory) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "share_notes" in value:
        out["share_notes"] = "*** Sensitive Data Redacted ***"
    return out
