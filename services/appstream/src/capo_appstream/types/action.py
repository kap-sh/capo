"""Generated from Smithy shape ``com.amazonaws.appstream#Action``."""

from typing import Literal, TypeAlias, cast

Action: TypeAlias = Literal[
    "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
    "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
    "FILE_UPLOAD",
    "FILE_DOWNLOAD",
    "PRINTING_TO_LOCAL_DEVICE",
    "DOMAIN_PASSWORD_SIGNIN",
    "DOMAIN_SMART_CARD_SIGNIN",
    "AUTO_TIME_ZONE_REDIRECTION",
    "SMART_CARD_REDIRECTION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Action) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Action:
    return cast(Action, data)
