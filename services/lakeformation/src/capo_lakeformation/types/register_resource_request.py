"""Generated from Smithy shape ``com.amazonaws.lakeformation#RegisterResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.account_id_string
    import capo_lakeformation.types.boolean
    import capo_lakeformation.types.iam_role_arn
    import capo_lakeformation.types.nullable_boolean
    import capo_lakeformation.types.resource_arn_string


class RegisterResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to register.</p>"""
    use_service_linked_role: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Designates an Identity and Access Management (IAM) service-linked role by registering this role with the Data Catalog. A service-linked role is a unique type of IAM role that is linked directly to Lake Formation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/service-linked-roles.html">Using Service-Linked Roles for Lake Formation</a>.</p>"""
    role_arn: NotRequired["capo_lakeformation.types.iam_role_arn.IAMRoleArn"]
    """<p>The identifier for the role that registers the resource.</p>"""
    with_federation: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Whether or not the resource is a federated resource.</p>"""
    hybrid_access_enabled: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p> Specifies whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies. </p>"""
    with_privileged_access: "capo_lakeformation.types.boolean.Boolean"
    """<p>Grants the calling principal the permissions to perform all supported Lake Formation operations on the registered data location. </p>"""
    expected_resource_owner_account: NotRequired[
        "capo_lakeformation.types.account_id_string.AccountIdString"
    ]
    """<p>The Amazon Web Services account that owns the Glue tables associated with specific Amazon S3 locations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "use_service_linked_role" in value:
        out["UseServiceLinkedRole"] = value["use_service_linked_role"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "with_federation" in value:
        out["WithFederation"] = value["with_federation"]
    if "hybrid_access_enabled" in value:
        out["HybridAccessEnabled"] = value["hybrid_access_enabled"]
    out["WithPrivilegedAccess"] = value.get("with_privileged_access", False)
    if "expected_resource_owner_account" in value:
        out["ExpectedResourceOwnerAccount"] = value["expected_resource_owner_account"]
    return out


def deserialize_json(data: dict) -> RegisterResourceRequest:
    out: RegisterResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("RegisterResourceRequest.resource_arn required")
    if data.get("UseServiceLinkedRole") is not None:
        out["use_service_linked_role"] = data["UseServiceLinkedRole"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("WithFederation") is not None:
        out["with_federation"] = data["WithFederation"]
    if data.get("HybridAccessEnabled") is not None:
        out["hybrid_access_enabled"] = data["HybridAccessEnabled"]
    if data.get("WithPrivilegedAccess") is not None:
        out["with_privileged_access"] = data["WithPrivilegedAccess"]
    else:
        out["with_privileged_access"] = False
    if data.get("ExpectedResourceOwnerAccount") is not None:
        out["expected_resource_owner_account"] = data["ExpectedResourceOwnerAccount"]
    return out
