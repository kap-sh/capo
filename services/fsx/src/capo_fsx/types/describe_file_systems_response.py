"""Generated from Smithy shape ``com.amazonaws.fsx#DescribeFileSystemsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.file_systems
    import capo_fsx.types.next_token


class DescribeFileSystemsResponse(TypedDict, closed=True):
    file_systems: NotRequired["capo_fsx.types.file_systems.FileSystems"]
    """<p>An array of file system descriptions.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]
    """<p>Present if there are more file systems than returned in the response (String). You can use the <code>NextToken</code> value in the later request to fetch the descriptions. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFileSystemsResponse) -> dict:
    out: dict = {}
    if "file_systems" in value:
        import capo_fsx.types.file_systems

        out["FileSystems"] = capo_fsx.types.file_systems.serialize_aws_json_1_1(
            value["file_systems"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFileSystemsResponse:
    out: DescribeFileSystemsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FileSystems") is not None:
        import capo_fsx.types.file_systems

        out["file_systems"] = capo_fsx.types.file_systems.deserialize_aws_json_1_1(
            data["FileSystems"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeFileSystemsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_systems" in value:
        import capo_fsx.types.file_systems

        out["file_systems"] = capo_fsx.types.file_systems.redact_sensitive(
            value["file_systems"]
        )
    return out
