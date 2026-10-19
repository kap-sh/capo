"""Generated from Smithy shape ``com.amazonaws.lakeformation#GrantPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.permission_list
    import capo_lakeformation.types.resource


class GrantPermissionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    principal: "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    """<p>The principal to be granted the permissions on the resource. Supported principals are IAM users or IAM roles, and they are defined by their principal type and their ARN.</p> <p>Note that if you define a resource with a particular ARN, then later delete, and recreate a resource with that same ARN, the resource maintains the permissions already granted. </p>"""
    resource: "capo_lakeformation.types.resource.Resource"
    """<p>The resource to which permissions are to be granted. Resources in Lake Formation are the Data Catalog, databases, and tables.</p>"""
    permissions: "capo_lakeformation.types.permission_list.PermissionList"
    """<p>The permissions granted to the principal on the resource. Lake Formation defines privileges to grant and revoke access to metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3. Lake Formation requires that each principal be authorized to perform a specific task on Lake Formation resources. </p>"""
    condition: NotRequired["capo_lakeformation.types.condition.Condition"]
    permissions_with_grant_option: NotRequired[
        "capo_lakeformation.types.permission_list.PermissionList"
    ]
    """<p>Indicates a list of the granted permissions that the principal may pass to other users. These permissions may only be a subset of the permissions granted in the <code>Privileges</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrantPermissionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.data_lake_principal

    out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
        value["principal"]
    )
    import capo_lakeformation.types.resource

    out["Resource"] = capo_lakeformation.types.resource.serialize_json(
        value["resource"]
    )
    import capo_lakeformation.types.permission_list

    out["Permissions"] = capo_lakeformation.types.permission_list.serialize_json(
        value["permissions"]
    )
    if "condition" in value:
        import capo_lakeformation.types.condition

        out["Condition"] = capo_lakeformation.types.condition.serialize_json(
            value["condition"]
        )
    if "permissions_with_grant_option" in value:
        import capo_lakeformation.types.permission_list

        out["PermissionsWithGrantOption"] = (
            capo_lakeformation.types.permission_list.serialize_json(
                value["permissions_with_grant_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> GrantPermissionsRequest:
    out: GrantPermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Principal") is not None:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    else:
        raise DeserializationError("GrantPermissionsRequest.principal required")
    if data.get("Resource") is not None:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("GrantPermissionsRequest.resource required")
    if data.get("Permissions") is not None:
        import capo_lakeformation.types.permission_list

        out["permissions"] = capo_lakeformation.types.permission_list.deserialize_json(
            data["Permissions"]
        )
    else:
        out["permissions"] = []
    if data.get("Condition") is not None:
        import capo_lakeformation.types.condition

        out["condition"] = capo_lakeformation.types.condition.deserialize_json(
            data["Condition"]
        )
    if data.get("PermissionsWithGrantOption") is not None:
        import capo_lakeformation.types.permission_list

        out["permissions_with_grant_option"] = (
            capo_lakeformation.types.permission_list.deserialize_json(
                data["PermissionsWithGrantOption"]
            )
        )
    return out
