"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeCAEnrollmentPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id


class DescribeCAEnrollmentPolicyRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to retrieve the CA enrollment policy information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCAEnrollmentPolicyRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCAEnrollmentPolicyRequest:
    out: DescribeCAEnrollmentPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    return out
