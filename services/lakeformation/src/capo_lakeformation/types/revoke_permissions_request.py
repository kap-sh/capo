"""Generated from Smithy shape ``com.amazonaws.lakeformation#RevokePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.permission_list
    import capo_lakeformation.types.resource


class RevokePermissionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    principal: "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    """<p>The principal to be revoked permissions on the resource.</p>"""
    resource: "capo_lakeformation.types.resource.Resource"
    """<p>The resource to which permissions are to be revoked.</p>"""
    permissions: "capo_lakeformation.types.permission_list.PermissionList"
    """<p>The permissions revoked to the principal on the resource. For information about permissions, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html">Security and Access Control to Metadata and Data</a>.</p>"""
    condition: NotRequired["capo_lakeformation.types.condition.Condition"]
    permissions_with_grant_option: NotRequired[
        "capo_lakeformation.types.permission_list.PermissionList"
    ]
    """<p>Indicates a list of permissions for which to revoke the grant option allowing the principal to pass permissions to other principals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokePermissionsRequest) -> dict:
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


def deserialize_json(data: dict) -> RevokePermissionsRequest:
    out: RevokePermissionsRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("RevokePermissionsRequest.principal required")
    if data.get("Resource") is not None:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("RevokePermissionsRequest.resource required")
    if data.get("Permissions") is not None:
        import capo_lakeformation.types.permission_list

        out["permissions"] = capo_lakeformation.types.permission_list.deserialize_json(
            data["Permissions"]
        )
    else:
        raise DeserializationError("RevokePermissionsRequest.permissions required")
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
