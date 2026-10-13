"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeRoleConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.snowflake_role


class SnowflakeRoleConfiguration(TypedDict, closed=True):
    enabled: NotRequired["capo_firehose.types.boolean_object.BooleanObject"]
    """<p>Enable Snowflake role</p>"""
    snowflake_role: NotRequired["capo_firehose.types.snowflake_role.SnowflakeRole"]
    """<p>The Snowflake role you wish to configure</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeRoleConfiguration) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "snowflake_role" in value:
        out["SnowflakeRole"] = value["snowflake_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeRoleConfiguration:
    out: SnowflakeRoleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("SnowflakeRole") is not None:
        out["snowflake_role"] = data["SnowflakeRole"]
    return out


def redact_sensitive(value: SnowflakeRoleConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "snowflake_role" in value:
        out["snowflake_role"] = "*** Sensitive Data Redacted ***"
    return out
