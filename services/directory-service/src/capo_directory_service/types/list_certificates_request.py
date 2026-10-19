"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListCertificatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.next_token
    import capo_directory_service.types.page_limit


class ListCertificatesRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>A token for requesting another page of certificates if the <code>NextToken</code> response element indicates that more certificates are available. Use the value of the returned <code>NextToken</code> element in your request until the token comes back as <code>null</code>. Pass <code>null</code> if this is the first call.</p>"""
    limit: NotRequired["capo_directory_service.types.page_limit.PageLimit"]
    """<p>The number of items that should show up on one page</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificatesRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificatesRequest:
    out: ListCertificatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
