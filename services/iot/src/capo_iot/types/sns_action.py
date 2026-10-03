"""Generated from Smithy shape ``com.amazonaws.iot#SnsAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.message_format


class SnsAction(TypedDict, closed=True):
    target_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the SNS topic.</p>"""
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access.</p>"""
    message_format: NotRequired["capo_iot.types.message_format.MessageFormat"]
    """<p>(Optional) The message format of the message to publish. Accepted values are "JSON" and "RAW". The default value of the attribute is "RAW". SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see <a href="https://docs.aws.amazon.com/sns/latest/dg/json-formats.html">https://docs.aws.amazon.com/sns/latest/dg/json-formats.html</a> refer to their official documentation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnsAction) -> dict:
    out: dict = {}
    out["targetArn"] = value["target_arn"]
    out["roleArn"] = value["role_arn"]
    if "message_format" in value:
        import capo_iot.types.message_format

        out["messageFormat"] = capo_iot.types.message_format.serialize_json(
            value["message_format"]
        )
    return out


def deserialize_json(data: dict) -> SnsAction:
    out: SnsAction = {}  # type: ignore[typeddict-item]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("SnsAction.target_arn required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("SnsAction.role_arn required")
    if data.get("messageFormat") is not None:
        import capo_iot.types.message_format

        out["message_format"] = capo_iot.types.message_format.deserialize_json(
            data["messageFormat"]
        )
    return out
