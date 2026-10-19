"""Generated from Smithy shape ``com.amazonaws.appsync#DynamodbDataSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.boolean
    import capo_appsync.types.delta_sync_config
    import capo_appsync.types.string


class DynamodbDataSourceConfig(TypedDict, closed=True):
    table_name: "capo_appsync.types.string.String"
    """<p>The table name.</p>"""
    aws_region: "capo_appsync.types.string.String"
    """<p>The Amazon Web Services Region.</p>"""
    use_caller_credentials: "capo_appsync.types.boolean.Boolean"
    """<p>Set to TRUE to use Amazon Cognito credentials with this data source.</p>"""
    delta_sync_config: NotRequired[
        "capo_appsync.types.delta_sync_config.DeltaSyncConfig"
    ]
    """<p>The <code>DeltaSyncConfig</code> for a versioned data source.</p>"""
    versioned: "capo_appsync.types.boolean.Boolean"
    """<p>Set to TRUE to use Conflict Detection and Resolution with this data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynamodbDataSourceConfig) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    out["awsRegion"] = value["aws_region"]
    out["useCallerCredentials"] = value.get("use_caller_credentials", False)
    if "delta_sync_config" in value:
        import capo_appsync.types.delta_sync_config

        out["deltaSyncConfig"] = capo_appsync.types.delta_sync_config.serialize_json(
            value["delta_sync_config"]
        )
    out["versioned"] = value.get("versioned", False)
    return out


def deserialize_json(data: dict) -> DynamodbDataSourceConfig:
    out: DynamodbDataSourceConfig = {}  # type: ignore[typeddict-item]
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("awsRegion") is not None:
        out["aws_region"] = data["awsRegion"]
    else:
        out["aws_region"] = ""
    if data.get("useCallerCredentials") is not None:
        out["use_caller_credentials"] = data["useCallerCredentials"]
    else:
        out["use_caller_credentials"] = False
    if data.get("deltaSyncConfig") is not None:
        import capo_appsync.types.delta_sync_config

        out["delta_sync_config"] = (
            capo_appsync.types.delta_sync_config.deserialize_json(
                data["deltaSyncConfig"]
            )
        )
    if data.get("versioned") is not None:
        out["versioned"] = data["versioned"]
    else:
        out["versioned"] = False
    return out
