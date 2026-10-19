"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeConditionalForwardersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.remote_domain_names


class DescribeConditionalForwardersRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The directory ID for which to get the list of associated conditional forwarders.</p>"""
    remote_domain_names: NotRequired[
        "capo_directory_service.types.remote_domain_names.RemoteDomainNames"
    ]
    """<p>The fully qualified domain names (FQDN) of the remote domains for which to get the list of associated conditional forwarders. If this member is null, all conditional forwarders are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConditionalForwardersRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "remote_domain_names" in value:
        import capo_directory_service.types.remote_domain_names

        out["RemoteDomainNames"] = (
            capo_directory_service.types.remote_domain_names.serialize_aws_json_1_1(
                value["remote_domain_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConditionalForwardersRequest:
    out: DescribeConditionalForwardersRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("RemoteDomainNames") is not None:
        import capo_directory_service.types.remote_domain_names

        out["remote_domain_names"] = (
            capo_directory_service.types.remote_domain_names.deserialize_aws_json_1_1(
                data["RemoteDomainNames"]
            )
        )
    return out
