"""Generated from Smithy shape ``com.amazonaws.athena#GetSystemTableConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.system_table_name


class GetSystemTableConfigurationInput(TypedDict, closed=True):
    table_name: "capo_athena.types.system_table_name.SystemTableName"
    """<p>The system table configuration to retrieve. The only accepted value is <code>ALL</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemTableConfigurationInput) -> dict:
    out: dict = {}
    import capo_athena.types.system_table_name

    out["TableName"] = capo_athena.types.system_table_name.serialize_aws_json_1_1(
        value["table_name"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemTableConfigurationInput:
    out: GetSystemTableConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        import capo_athena.types.system_table_name

        out["table_name"] = (
            capo_athena.types.system_table_name.deserialize_aws_json_1_1(
                data["TableName"]
            )
        )
    else:
        import typing

        out["table_name"] = typing.cast(
            "capo_athena.types.system_table_name.SystemTableName", ""
        )
    return out
