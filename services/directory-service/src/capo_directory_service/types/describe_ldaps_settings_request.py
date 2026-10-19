"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeLDAPSSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.ldaps_type
    import capo_directory_service.types.next_token
    import capo_directory_service.types.page_limit


class DescribeLDAPSSettingsRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    type: NotRequired["capo_directory_service.types.ldaps_type.LDAPSType"]
    """<p>The type of LDAP security to enable. Currently only the value <code>Client</code> is supported.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The type of next token used for pagination.</p>"""
    limit: NotRequired["capo_directory_service.types.page_limit.PageLimit"]
    """<p>Specifies the number of items that should be displayed on one page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLDAPSSettingsRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "type" in value:
        import capo_directory_service.types.ldaps_type

        out["Type"] = capo_directory_service.types.ldaps_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLDAPSSettingsRequest:
    out: DescribeLDAPSSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("Type") is not None:
        import capo_directory_service.types.ldaps_type

        out["type"] = capo_directory_service.types.ldaps_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
