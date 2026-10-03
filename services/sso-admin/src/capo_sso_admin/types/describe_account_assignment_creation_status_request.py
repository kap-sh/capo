"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeAccountAssignmentCreationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.uu_id


class DescribeAccountAssignmentCreationStatusRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    account_assignment_creation_request_id: "capo_sso_admin.types.uu_id.UUId"
    """<p>The identifier that is used to track the request operation progress.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAccountAssignmentCreationStatusRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["AccountAssignmentCreationRequestId"] = value[
        "account_assignment_creation_request_id"
    ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAccountAssignmentCreationStatusRequest:
    out: DescribeAccountAssignmentCreationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "DescribeAccountAssignmentCreationStatusRequest.instance_arn required"
        )
    if data.get("AccountAssignmentCreationRequestId") is not None:
        out["account_assignment_creation_request_id"] = data[
            "AccountAssignmentCreationRequestId"
        ]
    else:
        raise DeserializationError(
            "DescribeAccountAssignmentCreationStatusRequest.account_assignment_creation_request_id required"
        )
    return out
