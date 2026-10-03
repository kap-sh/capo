"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ConversationLogsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.iam_role_arn
    import capo_lex_model_building_service.types.log_settings_request_list


class ConversationLogsRequest(TypedDict, closed=True):
    log_settings: "capo_lex_model_building_service.types.log_settings_request_list.LogSettingsRequestList"
    """<p>The settings for your conversation logs. You can log the conversation text, conversation audio, or both.</p>"""
    iam_role_arn: "capo_lex_model_building_service.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to write to your CloudWatch Logs for text logs and your S3 bucket for audio logs. If audio encryption is enabled, this role also provides access permission for the AWS KMS key used for encrypting audio logs. For more information, see <a href="https://docs.aws.amazon.com/lex/latest/dg/conversation-logs-role-and-policy.html">Creating an IAM Role and Policy for Conversation Logs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversationLogsRequest) -> dict:
    out: dict = {}
    import capo_lex_model_building_service.types.log_settings_request_list

    out["logSettings"] = (
        capo_lex_model_building_service.types.log_settings_request_list.serialize_json(
            value["log_settings"]
        )
    )
    out["iamRoleArn"] = value["iam_role_arn"]
    return out


def deserialize_json(data: dict) -> ConversationLogsRequest:
    out: ConversationLogsRequest = {}  # type: ignore[typeddict-item]
    if data.get("logSettings") is not None:
        import capo_lex_model_building_service.types.log_settings_request_list

        out["log_settings"] = (
            capo_lex_model_building_service.types.log_settings_request_list.deserialize_json(
                data["logSettings"]
            )
        )
    else:
        raise DeserializationError("ConversationLogsRequest.log_settings required")
    if data.get("iamRoleArn") is not None:
        out["iam_role_arn"] = data["iamRoleArn"]
    else:
        raise DeserializationError("ConversationLogsRequest.iam_role_arn required")
    return out
