"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeHybridADUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.hybrid_update_type
    import capo_directory_service.types.next_token


class DescribeHybridADUpdateRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the hybrid directory for which to retrieve update information.</p>"""
    update_type: NotRequired[
        "capo_directory_service.types.hybrid_update_type.HybridUpdateType"
    ]
    """<p>The type of update activities to retrieve. Valid values include <code>SelfManagedInstances</code> and <code>HybridAdministratorAccount</code>.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The pagination token from a previous request to <a>DescribeHybridADUpdate</a>. Pass null if this is the first request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHybridADUpdateRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "update_type" in value:
        import capo_directory_service.types.hybrid_update_type

        out["UpdateType"] = (
            capo_directory_service.types.hybrid_update_type.serialize_aws_json_1_1(
                value["update_type"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHybridADUpdateRequest:
    out: DescribeHybridADUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("UpdateType") is not None:
        import capo_directory_service.types.hybrid_update_type

        out["update_type"] = (
            capo_directory_service.types.hybrid_update_type.deserialize_aws_json_1_1(
                data["UpdateType"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
