"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateResourcePermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.service_role_type
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class UpdateResourcePermissionsResponse(TypedDict, closed=True):
    role_type: NotRequired["capo_quicksight.types.service_role_type.ServiceRoleType"]
    """<p>The type of service role that Amazon Quick Sight uses for your account after the update. This value is <code>CUSTOMER_MANAGED</code>.</p>"""
    customer_managed_role_arn: NotRequired["capo_quicksight.types.string.String"]
    """<p>The ARN of the customer-managed role that Amazon Quick Sight uses for your account after the update.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourcePermissionsResponse) -> dict:
    out: dict = {}
    if "role_type" in value:
        import capo_quicksight.types.service_role_type

        out["RoleType"] = capo_quicksight.types.service_role_type.serialize_json(
            value["role_type"]
        )
    if "customer_managed_role_arn" in value:
        out["CustomerManagedRoleArn"] = value["customer_managed_role_arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateResourcePermissionsResponse:
    out: UpdateResourcePermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("RoleType") is not None:
        import capo_quicksight.types.service_role_type

        out["role_type"] = capo_quicksight.types.service_role_type.deserialize_json(
            data["RoleType"]
        )
    if data.get("CustomerManagedRoleArn") is not None:
        out["customer_managed_role_arn"] = data["CustomerManagedRoleArn"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
