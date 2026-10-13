"""Generated from Smithy shape ``com.amazonaws.ssmsap#Database``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_sap.types.application_credential_list
    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.component_arn_list
    import capo_ssm_sap.types.component_id
    import capo_ssm_sap.types.database_id
    import capo_ssm_sap.types.database_status
    import capo_ssm_sap.types.database_type
    import capo_ssm_sap.types.ssm_sap_arn


class Database(TypedDict, closed=True):
    application_id: NotRequired["capo_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    component_id: NotRequired["capo_ssm_sap.types.component_id.ComponentId"]
    """<p>The ID of the component.</p>"""
    credentials: NotRequired[
        "capo_ssm_sap.types.application_credential_list.ApplicationCredentialList"
    ]
    """<p>The credentials of the database.</p>"""
    database_id: NotRequired["capo_ssm_sap.types.database_id.DatabaseId"]
    """<p>The ID of the SAP HANA database.</p>"""
    database_name: NotRequired["str"]
    """<p>The name of the database.</p>"""
    database_type: NotRequired["capo_ssm_sap.types.database_type.DatabaseType"]
    """<p>The type of the database.</p>"""
    arn: NotRequired["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the database.</p>"""
    status: NotRequired["capo_ssm_sap.types.database_status.DatabaseStatus"]
    """<p>The status of the database.</p>"""
    primary_host: NotRequired["str"]
    """<p>The primary host of the database.</p>"""
    sql_port: NotRequired["int"]
    """<p>The SQL port of the database.</p>"""
    last_updated: NotRequired["datetime.datetime"]
    """<p>The time at which the database was last updated.</p>"""
    connected_component_arns: NotRequired[
        "capo_ssm_sap.types.component_arn_list.ComponentArnList"
    ]
    """<p>The Amazon Resource Names of the connected AWS Systems Manager for SAP components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Database) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "component_id" in value:
        out["ComponentId"] = value["component_id"]
    if "credentials" in value:
        import capo_ssm_sap.types.application_credential_list

        out["Credentials"] = (
            capo_ssm_sap.types.application_credential_list.serialize_json(
                value["credentials"]
            )
        )
    if "database_id" in value:
        out["DatabaseId"] = value["database_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "database_type" in value:
        import capo_ssm_sap.types.database_type

        out["DatabaseType"] = capo_ssm_sap.types.database_type.serialize_json(
            value["database_type"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "status" in value:
        import capo_ssm_sap.types.database_status

        out["Status"] = capo_ssm_sap.types.database_status.serialize_json(
            value["status"]
        )
    if "primary_host" in value:
        out["PrimaryHost"] = value["primary_host"]
    if "sql_port" in value:
        out["SQLPort"] = value["sql_port"]
    if "last_updated" in value:
        import capo_ssm_sap.types._prelude.timestamp

        out["LastUpdated"] = capo_ssm_sap.types._prelude.timestamp.serialize_json(
            value["last_updated"]
        )
    if "connected_component_arns" in value:
        import capo_ssm_sap.types.component_arn_list

        out["ConnectedComponentArns"] = (
            capo_ssm_sap.types.component_arn_list.serialize_json(
                value["connected_component_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> Database:
    out: Database = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("ComponentId") is not None:
        out["component_id"] = data["ComponentId"]
    if data.get("Credentials") is not None:
        import capo_ssm_sap.types.application_credential_list

        out["credentials"] = (
            capo_ssm_sap.types.application_credential_list.deserialize_json(
                data["Credentials"]
            )
        )
    if data.get("DatabaseId") is not None:
        out["database_id"] = data["DatabaseId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("DatabaseType") is not None:
        import capo_ssm_sap.types.database_type

        out["database_type"] = capo_ssm_sap.types.database_type.deserialize_json(
            data["DatabaseType"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Status") is not None:
        import capo_ssm_sap.types.database_status

        out["status"] = capo_ssm_sap.types.database_status.deserialize_json(
            data["Status"]
        )
    if data.get("PrimaryHost") is not None:
        out["primary_host"] = data["PrimaryHost"]
    if data.get("SQLPort") is not None:
        out["sql_port"] = data["SQLPort"]
    if data.get("LastUpdated") is not None:
        import capo_ssm_sap.types._prelude.timestamp

        out["last_updated"] = capo_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["LastUpdated"]
        )
    if data.get("ConnectedComponentArns") is not None:
        import capo_ssm_sap.types.component_arn_list

        out["connected_component_arns"] = (
            capo_ssm_sap.types.component_arn_list.deserialize_json(
                data["ConnectedComponentArns"]
            )
        )
    return out


def redact_sensitive(value: Database) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        import capo_ssm_sap.types.application_credential_list

        out["credentials"] = (
            capo_ssm_sap.types.application_credential_list.redact_sensitive(
                value["credentials"]
            )
        )
    return out
