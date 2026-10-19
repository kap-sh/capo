"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteConditionalForwarderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.remote_domain_name


class DeleteConditionalForwarderRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The directory ID for which you are deleting the conditional forwarder.</p>"""
    remote_domain_name: (
        "capo_directory_service.types.remote_domain_name.RemoteDomainName"
    )
    """<p>The fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteConditionalForwarderRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["RemoteDomainName"] = value["remote_domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteConditionalForwarderRequest:
    out: DeleteConditionalForwarderRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("RemoteDomainName") is not None:
        out["remote_domain_name"] = data["RemoteDomainName"]
    else:
        out["remote_domain_name"] = ""
    return out
