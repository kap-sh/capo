"""Generated from Smithy shape ``com.amazonaws.dsql#KinesisTargetDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.kinesis_stream_arn
    import capo_dsql.types.role_arn


class KinesisTargetDefinition(TypedDict, closed=True):
    stream_arn: "capo_dsql.types.kinesis_stream_arn.KinesisStreamArn"
    """<p>The ARN of the Kinesis stream.</p>"""
    role_arn: "capo_dsql.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants permission to write to the Kinesis stream. This can be a standard role (<code>arn:aws:iam::account-id:role/role-name</code>) or a role with a path prefix (<code>arn:aws:iam::account-id:role/service-role/role-name</code>), such as roles auto-created by the console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisTargetDefinition) -> dict:
    out: dict = {}
    out["streamArn"] = value["stream_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> KinesisTargetDefinition:
    out: KinesisTargetDefinition = {}  # type: ignore[typeddict-item]
    if data.get("streamArn") is not None:
        out["stream_arn"] = data["streamArn"]
    else:
        out["stream_arn"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
