"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeDocumentPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.document_name
    import capo_ssm.types.document_permission_max_results
    import capo_ssm.types.document_permission_type
    import capo_ssm.types.next_token


class DescribeDocumentPermissionRequest(TypedDict, closed=True):
    name: "capo_ssm.types.document_name.DocumentName"
    """<p>The name of the document for which you are the owner. </p>"""
    permission_type: "capo_ssm.types.document_permission_type.DocumentPermissionType"
    """<p>The permission type for the document. The permission type can be <i>Share</i>.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.document_permission_max_results.DocumentPermissionMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDocumentPermissionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_ssm.types.document_permission_type

    out["PermissionType"] = (
        capo_ssm.types.document_permission_type.serialize_aws_json_1_1(
            value["permission_type"]
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDocumentPermissionRequest:
    out: DescribeDocumentPermissionRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
