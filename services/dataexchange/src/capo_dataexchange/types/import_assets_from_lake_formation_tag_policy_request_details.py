"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetsFromLakeFormationTagPolicyRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.aws_account_id
    import capo_dataexchange.types.database_lf_tag_policy_and_permissions
    import capo_dataexchange.types.id
    import capo_dataexchange.types.role_arn
    import capo_dataexchange.types.table_lf_tag_policy_and_permissions


class ImportAssetsFromLakeFormationTagPolicyRequestDetails(TypedDict, closed=True):
    catalog_id: "capo_dataexchange.types.aws_account_id.AwsAccountId"
    """<p>The identifier for the AWS Glue Data Catalog.</p>"""
    database: NotRequired[
        "capo_dataexchange.types.database_lf_tag_policy_and_permissions.DatabaseLFTagPolicyAndPermissions"
    ]
    """<p>A structure for the database object.</p>"""
    table: NotRequired[
        "capo_dataexchange.types.table_lf_tag_policy_and_permissions.TableLFTagPolicyAndPermissions"
    ]
    """<p>A structure for the table object.</p>"""
    role_arn: "capo_dataexchange.types.role_arn.RoleArn"
    """<p>The IAM role's ARN that allows AWS Data Exchange to assume the role and grant and revoke permissions of subscribers to AWS Lake Formation data permissions.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this import job.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetsFromLakeFormationTagPolicyRequestDetails) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    if "database" in value:
        import capo_dataexchange.types.database_lf_tag_policy_and_permissions

        out["Database"] = (
            capo_dataexchange.types.database_lf_tag_policy_and_permissions.serialize_json(
                value["database"]
            )
        )
    if "table" in value:
        import capo_dataexchange.types.table_lf_tag_policy_and_permissions

        out["Table"] = (
            capo_dataexchange.types.table_lf_tag_policy_and_permissions.serialize_json(
                value["table"]
            )
        )
    out["RoleArn"] = value["role_arn"]
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(
    data: dict,
) -> ImportAssetsFromLakeFormationTagPolicyRequestDetails:
    out: ImportAssetsFromLakeFormationTagPolicyRequestDetails = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        out["catalog_id"] = ""
    if data.get("Database") is not None:
        import capo_dataexchange.types.database_lf_tag_policy_and_permissions

        out["database"] = (
            capo_dataexchange.types.database_lf_tag_policy_and_permissions.deserialize_json(
                data["Database"]
            )
        )
    if data.get("Table") is not None:
        import capo_dataexchange.types.table_lf_tag_policy_and_permissions

        out["table"] = (
            capo_dataexchange.types.table_lf_tag_policy_and_permissions.deserialize_json(
                data["Table"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        out["revision_id"] = ""
    return out
