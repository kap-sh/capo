"""Generated from Smithy shape ``com.amazonaws.elementalinference#BedrockApi``."""

from typing import Literal, TypeAlias, cast

BedrockApi: TypeAlias = Literal["INVOKE_MODEL",]


# --- restJson1 ser/de ---
def serialize_json(value: BedrockApi) -> str:
    return value


def deserialize_json(data: str) -> BedrockApi:
    return cast(BedrockApi, data)
