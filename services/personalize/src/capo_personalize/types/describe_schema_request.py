"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeSchemaRequest(TypedDict, closed=True):
    schema_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the schema to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSchemaRequest) -> dict:
    out: dict = {}
    out["schemaArn"] = value["schema_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSchemaRequest:
    out: DescribeSchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("schemaArn") is not None:
        out["schema_arn"] = data["schemaArn"]
    else:
        out["schema_arn"] = ""
    return out
