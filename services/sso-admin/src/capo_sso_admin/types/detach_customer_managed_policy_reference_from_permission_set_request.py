"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DetachCustomerManagedPolicyReferenceFromPermissionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.customer_managed_policy_reference
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.permission_set_arn


class DetachCustomerManagedPolicyReferenceFromPermissionSetRequest(
    TypedDict, closed=True
):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>"""
    permission_set_arn: "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the <code>PermissionSet</code>.</p>"""
    customer_managed_policy_reference: "capo_sso_admin.types.customer_managed_policy_reference.CustomerManagedPolicyReference"
    """<p>Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each Amazon Web Services account where you want to deploy your permission set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DetachCustomerManagedPolicyReferenceFromPermissionSetRequest,
) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    import capo_sso_admin.types.customer_managed_policy_reference

    out["CustomerManagedPolicyReference"] = (
        capo_sso_admin.types.customer_managed_policy_reference.serialize_aws_json_1_1(
            value["customer_managed_policy_reference"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DetachCustomerManagedPolicyReferenceFromPermissionSetRequest:
    out: DetachCustomerManagedPolicyReferenceFromPermissionSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("PermissionSetArn") is not None:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        out["permission_set_arn"] = ""
    if data.get("CustomerManagedPolicyReference") is not None:
        import capo_sso_admin.types.customer_managed_policy_reference

        out["customer_managed_policy_reference"] = (
            capo_sso_admin.types.customer_managed_policy_reference.deserialize_aws_json_1_1(
                data["CustomerManagedPolicyReference"]
            )
        )
    else:
        raise DeserializationError(
            "DetachCustomerManagedPolicyReferenceFromPermissionSetRequest.customer_managed_policy_reference required"
        )
    return out
