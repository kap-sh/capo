"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyDataProviderMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.data_provider_settings
    import capo_database_migration_service.types.string


class ModifyDataProviderMessage(TypedDict, closed=True):
    data_provider_identifier: "capo_database_migration_service.types.string.String"
    """<p>The identifier of the data provider. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.</p>"""
    data_provider_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The name of the data provider.</p>"""
    description: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A user-friendly description of the data provider.</p>"""
    engine: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The type of database engine for the data provider.</p> <p>Valid values: <code>aurora</code>, <code>aurora-postgresql</code>, <code>db2</code>, <code>db2-zos</code>, <code>docdb</code>, <code>mariadb</code>, <code>mongodb</code>, <code>mysql</code>, <code>oracle</code>, <code>postgres</code>, <code>redshift</code>, <code>sqlserver</code>, and <code>sybase</code>. A value of <code>aurora</code> represents Amazon Aurora MySQL-Compatible Edition.</p>"""
    virtual: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the data provider is virtual.</p>"""
    exact_settings: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If this attribute is Y, the current call to <code>ModifyDataProvider</code> replaces all existing data provider settings with the exact settings that you specify in this call. If this attribute is N, the current call to <code>ModifyDataProvider</code> does two things: </p> <ul> <li> <p>It replaces any data provider settings that already exist with new values, for settings with the same names.</p> </li> <li> <p>It creates new data provider settings that you specify in the call, for settings with different names. </p> </li> </ul>"""
    settings: NotRequired[
        "capo_database_migration_service.types.data_provider_settings.DataProviderSettings"
    ]
    """<p>The settings in JSON format for a data provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyDataProviderMessage) -> dict:
    out: dict = {}
    out["DataProviderIdentifier"] = value["data_provider_identifier"]
    if "data_provider_name" in value:
        out["DataProviderName"] = value["data_provider_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "virtual" in value:
        out["Virtual"] = value["virtual"]
    if "exact_settings" in value:
        out["ExactSettings"] = value["exact_settings"]
    if "settings" in value:
        import capo_database_migration_service.types.data_provider_settings

        out["Settings"] = (
            capo_database_migration_service.types.data_provider_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyDataProviderMessage:
    out: ModifyDataProviderMessage = {}  # type: ignore[typeddict-item]
    if data.get("DataProviderIdentifier") is not None:
        out["data_provider_identifier"] = data["DataProviderIdentifier"]
    else:
        out["data_provider_identifier"] = ""
    if data.get("DataProviderName") is not None:
        out["data_provider_name"] = data["DataProviderName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Engine") is not None:
        out["engine"] = data["Engine"]
    if data.get("Virtual") is not None:
        out["virtual"] = data["Virtual"]
    if data.get("ExactSettings") is not None:
        out["exact_settings"] = data["ExactSettings"]
    if data.get("Settings") is not None:
        import capo_database_migration_service.types.data_provider_settings

        out["settings"] = (
            capo_database_migration_service.types.data_provider_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out
