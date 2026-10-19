"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataProviderSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_database_migration_service.errors import (
    DeserializationError,
    SerializationError,
)
from capo_database_migration_service.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_database_migration_service.types.doc_db_data_provider_settings
    import capo_database_migration_service.types.ibm_db2_luw_data_provider_settings
    import capo_database_migration_service.types.ibm_db2z_os_data_provider_settings
    import capo_database_migration_service.types.maria_db_data_provider_settings
    import capo_database_migration_service.types.microsoft_sql_server_data_provider_settings
    import capo_database_migration_service.types.mongo_db_data_provider_settings
    import capo_database_migration_service.types.my_sql_data_provider_settings
    import capo_database_migration_service.types.oracle_data_provider_settings
    import capo_database_migration_service.types.postgre_sql_data_provider_settings
    import capo_database_migration_service.types.redshift_data_provider_settings
    import capo_database_migration_service.types.sybase_ase_data_provider_settings


class _DataProviderSettings_RedshiftSettings(TypedDict, closed=True):
    RedshiftSettings: "capo_database_migration_service.types.redshift_data_provider_settings.RedshiftDataProviderSettings"


class _DataProviderSettings_PostgreSqlSettings(TypedDict, closed=True):
    PostgreSqlSettings: "capo_database_migration_service.types.postgre_sql_data_provider_settings.PostgreSqlDataProviderSettings"


class _DataProviderSettings_MySqlSettings(TypedDict, closed=True):
    MySqlSettings: "capo_database_migration_service.types.my_sql_data_provider_settings.MySqlDataProviderSettings"


class _DataProviderSettings_OracleSettings(TypedDict, closed=True):
    OracleSettings: "capo_database_migration_service.types.oracle_data_provider_settings.OracleDataProviderSettings"


class _DataProviderSettings_SybaseAseSettings(TypedDict, closed=True):
    SybaseAseSettings: "capo_database_migration_service.types.sybase_ase_data_provider_settings.SybaseAseDataProviderSettings"


class _DataProviderSettings_MicrosoftSqlServerSettings(TypedDict, closed=True):
    MicrosoftSqlServerSettings: "capo_database_migration_service.types.microsoft_sql_server_data_provider_settings.MicrosoftSqlServerDataProviderSettings"


class _DataProviderSettings_DocDbSettings(TypedDict, closed=True):
    DocDbSettings: "capo_database_migration_service.types.doc_db_data_provider_settings.DocDbDataProviderSettings"


class _DataProviderSettings_MariaDbSettings(TypedDict, closed=True):
    MariaDbSettings: "capo_database_migration_service.types.maria_db_data_provider_settings.MariaDbDataProviderSettings"


class _DataProviderSettings_IbmDb2LuwSettings(TypedDict, closed=True):
    IbmDb2LuwSettings: "capo_database_migration_service.types.ibm_db2_luw_data_provider_settings.IbmDb2LuwDataProviderSettings"


class _DataProviderSettings_IbmDb2zOsSettings(TypedDict, closed=True):
    IbmDb2zOsSettings: "capo_database_migration_service.types.ibm_db2z_os_data_provider_settings.IbmDb2zOsDataProviderSettings"


class _DataProviderSettings_MongoDbSettings(TypedDict, closed=True):
    MongoDbSettings: "capo_database_migration_service.types.mongo_db_data_provider_settings.MongoDbDataProviderSettings"


DataProviderSettings: TypeAlias = (
    _DataProviderSettings_RedshiftSettings
    | _DataProviderSettings_PostgreSqlSettings
    | _DataProviderSettings_MySqlSettings
    | _DataProviderSettings_OracleSettings
    | _DataProviderSettings_SybaseAseSettings
    | _DataProviderSettings_MicrosoftSqlServerSettings
    | _DataProviderSettings_DocDbSettings
    | _DataProviderSettings_MariaDbSettings
    | _DataProviderSettings_IbmDb2LuwSettings
    | _DataProviderSettings_IbmDb2zOsSettings
    | _DataProviderSettings_MongoDbSettings
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProviderSettings) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DataProviderSettings: cannot serialize unknown variant {value.name!r}"
        )
    elif "RedshiftSettings" in value:
        import capo_database_migration_service.types.redshift_data_provider_settings

        return {
            "RedshiftSettings": capo_database_migration_service.types.redshift_data_provider_settings.serialize_aws_json_1_1(
                value["RedshiftSettings"]
            )
        }
    elif "PostgreSqlSettings" in value:
        import capo_database_migration_service.types.postgre_sql_data_provider_settings

        return {
            "PostgreSqlSettings": capo_database_migration_service.types.postgre_sql_data_provider_settings.serialize_aws_json_1_1(
                value["PostgreSqlSettings"]
            )
        }
    elif "MySqlSettings" in value:
        import capo_database_migration_service.types.my_sql_data_provider_settings

        return {
            "MySqlSettings": capo_database_migration_service.types.my_sql_data_provider_settings.serialize_aws_json_1_1(
                value["MySqlSettings"]
            )
        }
    elif "OracleSettings" in value:
        import capo_database_migration_service.types.oracle_data_provider_settings

        return {
            "OracleSettings": capo_database_migration_service.types.oracle_data_provider_settings.serialize_aws_json_1_1(
                value["OracleSettings"]
            )
        }
    elif "SybaseAseSettings" in value:
        import capo_database_migration_service.types.sybase_ase_data_provider_settings

        return {
            "SybaseAseSettings": capo_database_migration_service.types.sybase_ase_data_provider_settings.serialize_aws_json_1_1(
                value["SybaseAseSettings"]
            )
        }
    elif "MicrosoftSqlServerSettings" in value:
        import capo_database_migration_service.types.microsoft_sql_server_data_provider_settings

        return {
            "MicrosoftSqlServerSettings": capo_database_migration_service.types.microsoft_sql_server_data_provider_settings.serialize_aws_json_1_1(
                value["MicrosoftSqlServerSettings"]
            )
        }
    elif "DocDbSettings" in value:
        import capo_database_migration_service.types.doc_db_data_provider_settings

        return {
            "DocDbSettings": capo_database_migration_service.types.doc_db_data_provider_settings.serialize_aws_json_1_1(
                value["DocDbSettings"]
            )
        }
    elif "MariaDbSettings" in value:
        import capo_database_migration_service.types.maria_db_data_provider_settings

        return {
            "MariaDbSettings": capo_database_migration_service.types.maria_db_data_provider_settings.serialize_aws_json_1_1(
                value["MariaDbSettings"]
            )
        }
    elif "IbmDb2LuwSettings" in value:
        import capo_database_migration_service.types.ibm_db2_luw_data_provider_settings

        return {
            "IbmDb2LuwSettings": capo_database_migration_service.types.ibm_db2_luw_data_provider_settings.serialize_aws_json_1_1(
                value["IbmDb2LuwSettings"]
            )
        }
    elif "IbmDb2zOsSettings" in value:
        import capo_database_migration_service.types.ibm_db2z_os_data_provider_settings

        return {
            "IbmDb2zOsSettings": capo_database_migration_service.types.ibm_db2z_os_data_provider_settings.serialize_aws_json_1_1(
                value["IbmDb2zOsSettings"]
            )
        }
    elif "MongoDbSettings" in value:
        import capo_database_migration_service.types.mongo_db_data_provider_settings

        return {
            "MongoDbSettings": capo_database_migration_service.types.mongo_db_data_provider_settings.serialize_aws_json_1_1(
                value["MongoDbSettings"]
            )
        }
    else:
        raise SerializationError("DataProviderSettings: no variant present")


def deserialize_aws_json_1_1(data: dict) -> DataProviderSettings:
    if data.get("RedshiftSettings") is not None:
        import capo_database_migration_service.types.redshift_data_provider_settings

        return {
            "RedshiftSettings": capo_database_migration_service.types.redshift_data_provider_settings.deserialize_aws_json_1_1(
                data["RedshiftSettings"]
            )
        }
    elif data.get("PostgreSqlSettings") is not None:
        import capo_database_migration_service.types.postgre_sql_data_provider_settings

        return {
            "PostgreSqlSettings": capo_database_migration_service.types.postgre_sql_data_provider_settings.deserialize_aws_json_1_1(
                data["PostgreSqlSettings"]
            )
        }
    elif data.get("MySqlSettings") is not None:
        import capo_database_migration_service.types.my_sql_data_provider_settings

        return {
            "MySqlSettings": capo_database_migration_service.types.my_sql_data_provider_settings.deserialize_aws_json_1_1(
                data["MySqlSettings"]
            )
        }
    elif data.get("OracleSettings") is not None:
        import capo_database_migration_service.types.oracle_data_provider_settings

        return {
            "OracleSettings": capo_database_migration_service.types.oracle_data_provider_settings.deserialize_aws_json_1_1(
                data["OracleSettings"]
            )
        }
    elif data.get("SybaseAseSettings") is not None:
        import capo_database_migration_service.types.sybase_ase_data_provider_settings

        return {
            "SybaseAseSettings": capo_database_migration_service.types.sybase_ase_data_provider_settings.deserialize_aws_json_1_1(
                data["SybaseAseSettings"]
            )
        }
    elif data.get("MicrosoftSqlServerSettings") is not None:
        import capo_database_migration_service.types.microsoft_sql_server_data_provider_settings

        return {
            "MicrosoftSqlServerSettings": capo_database_migration_service.types.microsoft_sql_server_data_provider_settings.deserialize_aws_json_1_1(
                data["MicrosoftSqlServerSettings"]
            )
        }
    elif data.get("DocDbSettings") is not None:
        import capo_database_migration_service.types.doc_db_data_provider_settings

        return {
            "DocDbSettings": capo_database_migration_service.types.doc_db_data_provider_settings.deserialize_aws_json_1_1(
                data["DocDbSettings"]
            )
        }
    elif data.get("MariaDbSettings") is not None:
        import capo_database_migration_service.types.maria_db_data_provider_settings

        return {
            "MariaDbSettings": capo_database_migration_service.types.maria_db_data_provider_settings.deserialize_aws_json_1_1(
                data["MariaDbSettings"]
            )
        }
    elif data.get("IbmDb2LuwSettings") is not None:
        import capo_database_migration_service.types.ibm_db2_luw_data_provider_settings

        return {
            "IbmDb2LuwSettings": capo_database_migration_service.types.ibm_db2_luw_data_provider_settings.deserialize_aws_json_1_1(
                data["IbmDb2LuwSettings"]
            )
        }
    elif data.get("IbmDb2zOsSettings") is not None:
        import capo_database_migration_service.types.ibm_db2z_os_data_provider_settings

        return {
            "IbmDb2zOsSettings": capo_database_migration_service.types.ibm_db2z_os_data_provider_settings.deserialize_aws_json_1_1(
                data["IbmDb2zOsSettings"]
            )
        }
    elif data.get("MongoDbSettings") is not None:
        import capo_database_migration_service.types.mongo_db_data_provider_settings

        return {
            "MongoDbSettings": capo_database_migration_service.types.mongo_db_data_provider_settings.deserialize_aws_json_1_1(
                data["MongoDbSettings"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("DataProviderSettings: no recognized variant key")
