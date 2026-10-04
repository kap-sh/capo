"""Generated from Smithy shape ``com.amazonaws.appstream#AgentSoftwareVersion``."""

from typing import Literal, TypeAlias, cast

"""<p>The image type is the type of AppStream image resource.</p>"""
AgentSoftwareVersion: TypeAlias = Literal[
    "CURRENT_LATEST",
    "ALWAYS_LATEST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentSoftwareVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentSoftwareVersion:
    return cast(AgentSoftwareVersion, data)
