"""Generated from Smithy shape ``com.amazonaws.athena#SystemTableStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.boxed_boolean
    import capo_athena.types.system_table_type


class SystemTableStatus(TypedDict, closed=True):
    table_name: "capo_athena.types.system_table_type.SystemTableType"
    """<p>The name of the system table, such as <code>QUERY_EXECUTIONS</code>.</p>"""
    enabled: "capo_athena.types.boxed_boolean.BoxedBoolean"
    """<p>Indicates whether the system table is enabled for the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTableStatus) -> dict:
    out: dict = {}
    import capo_athena.types.system_table_type

    out["TableName"] = capo_athena.types.system_table_type.serialize_aws_json_1_1(
        value["table_name"]
    )
    out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SystemTableStatus:
    out: SystemTableStatus = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        import capo_athena.types.system_table_type

        out["table_name"] = (
            capo_athena.types.system_table_type.deserialize_aws_json_1_1(
                data["TableName"]
            )
        )
    else:
        import typing

        out["table_name"] = typing.cast(
            "capo_athena.types.system_table_type.SystemTableType", ""
        )
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
