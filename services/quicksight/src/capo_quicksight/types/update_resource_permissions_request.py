"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateResourcePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.role_arn
    import capo_quicksight.types.service_role_type


class UpdateResourcePermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account whose service role configuration you want to update.</p>"""
    role_type: "capo_quicksight.types.service_role_type.ServiceRoleType"
    """<p>The type of service role that you want Amazon Quick Sight to use. The only supported value for this operation is <code>CUSTOMER_MANAGED</code>. Requests that specify <code>QUICKSIGHT_MANAGED</code> are rejected.</p>"""
    customer_managed_role_arn: "capo_quicksight.types.role_arn.RoleArn"
    """<p>The ARN of the customer-managed role that you want Amazon Quick Sight to use. To use this operation, you must have the <code>iam:PassRole</code> permission for the role.</p> <p>Configure the role as follows:</p> <ul> <li> <p>The role must belong to the Amazon Web Services account specified by <code>AwsAccountId</code>.</p> </li> <li> <p>Configure the role trust policy to allow the Amazon Quick Sight service principal to call <code>sts:AssumeRole</code>.</p> </li> <li> <p>Attach a permissions policy that allows access to the resources that you want Amazon Quick Sight to use.</p> </li> <li> <p>To use features that rely on session tags, configure the role trust policy to allow the Amazon Quick Sight service principal to call <code>sts:TagSession</code>.</p> </li> </ul> <p>If the role doesn't exist or its trust policy doesn't allow <code>sts:AssumeRole</code>, the request returns an <code>AccessDeniedException</code>.</p> <p>When you call this operation, Amazon Quick Sight attempts to assume the role with session tags and records whether the attempt succeeds. If you later add or remove <code>sts:TagSession</code> from the trust policy, call this operation again with the same role ARN to refresh the stored capability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourcePermissionsRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.service_role_type

    out["RoleType"] = capo_quicksight.types.service_role_type.serialize_json(
        value["role_type"]
    )
    out["CustomerManagedRoleArn"] = value["customer_managed_role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateResourcePermissionsRequest:
    out: UpdateResourcePermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("RoleType") is not None:
        import capo_quicksight.types.service_role_type

        out["role_type"] = capo_quicksight.types.service_role_type.deserialize_json(
            data["RoleType"]
        )
    else:
        import typing

        out["role_type"] = typing.cast(
            "capo_quicksight.types.service_role_type.ServiceRoleType", ""
        )
    if data.get("CustomerManagedRoleArn") is not None:
        out["customer_managed_role_arn"] = data["CustomerManagedRoleArn"]
    else:
        out["customer_managed_role_arn"] = ""
    return out
