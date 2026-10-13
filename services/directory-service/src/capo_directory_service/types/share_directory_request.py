"""Generated from Smithy shape ``com.amazonaws.directoryservice#ShareDirectoryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.notes
    import capo_directory_service.types.share_method
    import capo_directory_service.types.share_target


class ShareDirectoryRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the Managed Microsoft AD directory that you want to share with other Amazon Web Services accounts.</p>"""
    share_notes: NotRequired["capo_directory_service.types.notes.Notes"]
    """<p>A directory share request that is sent by the directory owner to the directory consumer. The request includes a typed message to help the directory consumer administrator determine whether to approve or reject the share invitation.</p>"""
    share_target: "capo_directory_service.types.share_target.ShareTarget"
    """<p>Identifier for the directory consumer account with whom the directory is to be shared.</p>"""
    share_method: "capo_directory_service.types.share_method.ShareMethod"
    """<p>The method used when sharing a directory to determine whether the directory should be shared within your Amazon Web Services organization (<code>ORGANIZATIONS</code>) or with any Amazon Web Services account by sending a directory sharing request (<code>HANDSHAKE</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareDirectoryRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "share_notes" in value:
        out["ShareNotes"] = value["share_notes"]
    import capo_directory_service.types.share_target

    out["ShareTarget"] = (
        capo_directory_service.types.share_target.serialize_aws_json_1_1(
            value["share_target"]
        )
    )
    import capo_directory_service.types.share_method

    out["ShareMethod"] = (
        capo_directory_service.types.share_method.serialize_aws_json_1_1(
            value["share_method"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ShareDirectoryRequest:
    out: ShareDirectoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("ShareDirectoryRequest.directory_id required")
    if data.get("ShareNotes") is not None:
        out["share_notes"] = data["ShareNotes"]
    if data.get("ShareTarget") is not None:
        import capo_directory_service.types.share_target

        out["share_target"] = (
            capo_directory_service.types.share_target.deserialize_aws_json_1_1(
                data["ShareTarget"]
            )
        )
    else:
        raise DeserializationError("ShareDirectoryRequest.share_target required")
    if data.get("ShareMethod") is not None:
        import capo_directory_service.types.share_method

        out["share_method"] = (
            capo_directory_service.types.share_method.deserialize_aws_json_1_1(
                data["ShareMethod"]
            )
        )
    else:
        raise DeserializationError("ShareDirectoryRequest.share_method required")
    return out


def redact_sensitive(value: ShareDirectoryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "share_notes" in value:
        out["share_notes"] = "*** Sensitive Data Redacted ***"
    return out
