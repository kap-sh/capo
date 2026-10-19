"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateDataProviderMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.data_provider_settings
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.tag_list


class CreateDataProviderMessage(TypedDict, closed=True):
    data_provider_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A user-friendly name for the data provider.</p>"""
    description: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A user-friendly description of the data provider.</p>"""
    engine: "capo_database_migration_service.types.string.String"
    """<p>The type of database engine for the data provider.</p> <p>Valid values: <code>aurora</code>, <code>aurora-postgresql</code>, <code>db2</code>, <code>db2-zos</code>, <code>docdb</code>, <code>mariadb</code>, <code>mongodb</code>, <code>mysql</code>, <code>oracle</code>, <code>postgres</code>, <code>redshift</code>, <code>sqlserver</code>, and <code>sybase</code>. A value of <code>aurora</code> represents Amazon Aurora MySQL-Compatible Edition.</p>"""
    virtual: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the data provider is virtual.</p>"""
    settings: "capo_database_migration_service.types.data_provider_settings.DataProviderSettings"
    """<p>The settings in JSON format for a data provider.</p>"""
    tags: NotRequired["capo_database_migration_service.types.tag_list.TagList"]
    """<p>One or more tags to be assigned to the data provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataProviderMessage) -> dict:
    out: dict = {}
    if "data_provider_name" in value:
        out["DataProviderName"] = value["data_provider_name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Engine"] = value["engine"]
    if "virtual" in value:
        out["Virtual"] = value["virtual"]
    import capo_database_migration_service.types.data_provider_settings

    out["Settings"] = (
        capo_database_migration_service.types.data_provider_settings.serialize_aws_json_1_1(
            value["settings"]
        )
    )
    if "tags" in value:
        import capo_database_migration_service.types.tag_list

        out["Tags"] = (
            capo_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataProviderMessage:
    out: CreateDataProviderMessage = {}  # type: ignore[typeddict-item]
    if data.get("DataProviderName") is not None:
        out["data_provider_name"] = data["DataProviderName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    else:
        out["engine"] = ""
    if data.get("Virtual") is not None:
        out["virtual"] = data["Virtual"]
    if data.get("Settings") is not None:
        import capo_database_migration_service.types.data_provider_settings

        out["settings"] = (
            capo_database_migration_service.types.data_provider_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    else:
        import capo_database_migration_service.types._unknown

        out["settings"] = (
            capo_database_migration_service.types._unknown.UnknownUnionMember("")
        )
    if data.get("Tags") is not None:
        import capo_database_migration_service.types.tag_list

        out["tags"] = (
            capo_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    return out
