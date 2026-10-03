"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataLakeSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.authorized_session_tag_value_list
    import capo_lakeformation.types.data_lake_principal_list
    import capo_lakeformation.types.nullable_boolean
    import capo_lakeformation.types.parameters_map
    import capo_lakeformation.types.principal_permissions_list
    import capo_lakeformation.types.trusted_resource_owners


class DataLakeSettings(TypedDict, closed=True):
    data_lake_admins: NotRequired[
        "capo_lakeformation.types.data_lake_principal_list.DataLakePrincipalList"
    ]
    """<p>A list of Lake Formation principals. Supported principals are IAM users or IAM roles.</p>"""
    read_only_admins: NotRequired[
        "capo_lakeformation.types.data_lake_principal_list.DataLakePrincipalList"
    ]
    """<p>A list of Lake Formation principals with only view access to the resources, without the ability to make changes. Supported principals are IAM users or IAM roles.</p>"""
    create_database_default_permissions: NotRequired[
        "capo_lakeformation.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>Specifies whether access control on newly created database is managed by Lake Formation permissions or exclusively by IAM permissions.</p> <p>A null value indicates access control by Lake Formation permissions. A value that assigns ALL to IAM_ALLOWED_PRINCIPALS indicates access control by IAM permissions. This is referred to as the setting "Use only IAM access control," and is for backward compatibility with the Glue permission model implemented by IAM permissions.</p> <p>The only permitted values are an empty array or an array that contains a single JSON object that grants ALL to IAM_ALLOWED_PRINCIPALS.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html">Changing the Default Security Settings for Your Data Lake</a>.</p>"""
    create_table_default_permissions: NotRequired[
        "capo_lakeformation.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>Specifies whether access control on newly created table is managed by Lake Formation permissions or exclusively by IAM permissions.</p> <p>A null value indicates access control by Lake Formation permissions. A value that assigns ALL to IAM_ALLOWED_PRINCIPALS indicates access control by IAM permissions. This is referred to as the setting "Use only IAM access control," and is for backward compatibility with the Glue permission model implemented by IAM permissions.</p> <p>The only permitted values are an empty array or an array that contains a single JSON object that grants ALL to IAM_ALLOWED_PRINCIPALS.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html">Changing the Default Security Settings for Your Data Lake</a>.</p>"""
    parameters: NotRequired["capo_lakeformation.types.parameters_map.ParametersMap"]
    """<p>A key-value map that provides an additional configuration on your data lake. The following key-value pairs are supported:</p> <ul> <li> <p> <code>CROSS_ACCOUNT_VERSION</code> - Accepted values are 1, 2, 3, 4, and 5.</p> </li> <li> <p> <code>SET_SOURCE_IDENTITY</code> - Accepted values are <code>TRUE</code> and <code>FALSE</code>. When set to <code>TRUE</code>, Lake Formation includes the IAM role identifier that was used to query in the S3 data event CloudTrail logs for <code>s3:GetObject</code> calls. For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/cloudtrail-logging.html#source-identity-cloudtrail">Tracking query engine IAM roles in S3 data events</a>.</p> </li> </ul>"""
    trusted_resource_owners: NotRequired[
        "capo_lakeformation.types.trusted_resource_owners.TrustedResourceOwners"
    ]
    """<p>A list of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource owner's CloudTrail log.</p> <p>You may want to specify this property when you are in a high-trust boundary, such as the same team or company. </p>"""
    allow_external_data_filtering: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Whether to allow Amazon EMR clusters to access data managed by Lake Formation. </p> <p>If true, you allow Amazon EMR clusters to access data in Amazon S3 locations that are registered with Lake Formation.</p> <p>If false or null, no Amazon EMR clusters will be able to access data in Amazon S3 locations that are registered with Lake Formation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/initial-LF-setup.html#external-data-filter">(Optional) Allow external data filtering</a>.</p>"""
    allow_full_table_external_data_access: NotRequired[
        "capo_lakeformation.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Whether to allow a third-party query engine to get data access credentials without session tags when a caller has full data access permissions.</p>"""
    external_data_filtering_allow_list: NotRequired[
        "capo_lakeformation.types.data_lake_principal_list.DataLakePrincipalList"
    ]
    """<p>A list of the account IDs of Amazon Web Services accounts with Amazon EMR clusters that are to perform data filtering.></p>"""
    authorized_session_tag_value_list: NotRequired[
        "capo_lakeformation.types.authorized_session_tag_value_list.AuthorizedSessionTagValueList"
    ]
    """<p>Lake Formation relies on a privileged process secured by Amazon EMR or the third party integrator to tag the user's role while assuming it. Lake Formation will publish the acceptable key-value pair, for example key = "LakeFormationTrustedCaller" and value = "TRUE" and the third party integrator must properly tag the temporary security credentials that will be used to call Lake Formation's administrative APIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeSettings) -> dict:
    out: dict = {}
    if "data_lake_admins" in value:
        import capo_lakeformation.types.data_lake_principal_list

        out["DataLakeAdmins"] = (
            capo_lakeformation.types.data_lake_principal_list.serialize_json(
                value["data_lake_admins"]
            )
        )
    if "read_only_admins" in value:
        import capo_lakeformation.types.data_lake_principal_list

        out["ReadOnlyAdmins"] = (
            capo_lakeformation.types.data_lake_principal_list.serialize_json(
                value["read_only_admins"]
            )
        )
    if "create_database_default_permissions" in value:
        import capo_lakeformation.types.principal_permissions_list

        out["CreateDatabaseDefaultPermissions"] = (
            capo_lakeformation.types.principal_permissions_list.serialize_json(
                value["create_database_default_permissions"]
            )
        )
    if "create_table_default_permissions" in value:
        import capo_lakeformation.types.principal_permissions_list

        out["CreateTableDefaultPermissions"] = (
            capo_lakeformation.types.principal_permissions_list.serialize_json(
                value["create_table_default_permissions"]
            )
        )
    if "parameters" in value:
        import capo_lakeformation.types.parameters_map

        out["Parameters"] = capo_lakeformation.types.parameters_map.serialize_json(
            value["parameters"]
        )
    if "trusted_resource_owners" in value:
        import capo_lakeformation.types.trusted_resource_owners

        out["TrustedResourceOwners"] = (
            capo_lakeformation.types.trusted_resource_owners.serialize_json(
                value["trusted_resource_owners"]
            )
        )
    if "allow_external_data_filtering" in value:
        out["AllowExternalDataFiltering"] = value["allow_external_data_filtering"]
    if "allow_full_table_external_data_access" in value:
        out["AllowFullTableExternalDataAccess"] = value[
            "allow_full_table_external_data_access"
        ]
    if "external_data_filtering_allow_list" in value:
        import capo_lakeformation.types.data_lake_principal_list

        out["ExternalDataFilteringAllowList"] = (
            capo_lakeformation.types.data_lake_principal_list.serialize_json(
                value["external_data_filtering_allow_list"]
            )
        )
    if "authorized_session_tag_value_list" in value:
        import capo_lakeformation.types.authorized_session_tag_value_list

        out["AuthorizedSessionTagValueList"] = (
            capo_lakeformation.types.authorized_session_tag_value_list.serialize_json(
                value["authorized_session_tag_value_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeSettings:
    out: DataLakeSettings = {}  # type: ignore[typeddict-item]
    if data.get("DataLakeAdmins") is not None:
        import capo_lakeformation.types.data_lake_principal_list

        out["data_lake_admins"] = (
            capo_lakeformation.types.data_lake_principal_list.deserialize_json(
                data["DataLakeAdmins"]
            )
        )
    if data.get("ReadOnlyAdmins") is not None:
        import capo_lakeformation.types.data_lake_principal_list

        out["read_only_admins"] = (
            capo_lakeformation.types.data_lake_principal_list.deserialize_json(
                data["ReadOnlyAdmins"]
            )
        )
    if data.get("CreateDatabaseDefaultPermissions") is not None:
        import capo_lakeformation.types.principal_permissions_list

        out["create_database_default_permissions"] = (
            capo_lakeformation.types.principal_permissions_list.deserialize_json(
                data["CreateDatabaseDefaultPermissions"]
            )
        )
    if data.get("CreateTableDefaultPermissions") is not None:
        import capo_lakeformation.types.principal_permissions_list

        out["create_table_default_permissions"] = (
            capo_lakeformation.types.principal_permissions_list.deserialize_json(
                data["CreateTableDefaultPermissions"]
            )
        )
    if data.get("Parameters") is not None:
        import capo_lakeformation.types.parameters_map

        out["parameters"] = capo_lakeformation.types.parameters_map.deserialize_json(
            data["Parameters"]
        )
    if data.get("TrustedResourceOwners") is not None:
        import capo_lakeformation.types.trusted_resource_owners

        out["trusted_resource_owners"] = (
            capo_lakeformation.types.trusted_resource_owners.deserialize_json(
                data["TrustedResourceOwners"]
            )
        )
    if data.get("AllowExternalDataFiltering") is not None:
        out["allow_external_data_filtering"] = data["AllowExternalDataFiltering"]
    if data.get("AllowFullTableExternalDataAccess") is not None:
        out["allow_full_table_external_data_access"] = data[
            "AllowFullTableExternalDataAccess"
        ]
    if data.get("ExternalDataFilteringAllowList") is not None:
        import capo_lakeformation.types.data_lake_principal_list

        out["external_data_filtering_allow_list"] = (
            capo_lakeformation.types.data_lake_principal_list.deserialize_json(
                data["ExternalDataFilteringAllowList"]
            )
        )
    if data.get("AuthorizedSessionTagValueList") is not None:
        import capo_lakeformation.types.authorized_session_tag_value_list

        out["authorized_session_tag_value_list"] = (
            capo_lakeformation.types.authorized_session_tag_value_list.deserialize_json(
                data["AuthorizedSessionTagValueList"]
            )
        )
    return out
