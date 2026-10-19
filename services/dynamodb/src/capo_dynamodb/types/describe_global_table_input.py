"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeGlobalTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.table_name


class DescribeGlobalTableInput(TypedDict, closed=True):
    global_table_name: "capo_dynamodb.types.table_name.TableName"
    """<p>The name of the global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeGlobalTableInput) -> dict:
    out: dict = {}
    out["GlobalTableName"] = value["global_table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeGlobalTableInput:
    out: DescribeGlobalTableInput = {}  # type: ignore[typeddict-item]
    if data.get("GlobalTableName") is not None:
        out["global_table_name"] = data["GlobalTableName"]
    else:
        out["global_table_name"] = ""
    return out
