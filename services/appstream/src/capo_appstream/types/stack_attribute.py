"""Generated from Smithy shape ``com.amazonaws.appstream#StackAttribute``."""

from typing import Literal, TypeAlias, cast

"""<p>The stack attributes to delete.</p> <ul> <li> <p>STORAGE_CONNECTORS</p> </li> <li> <p>STORAGE_CONNECTOR_HOMEFOLDERS</p> </li> <li> <p>STORAGE_CONNECTOR_GOOGLE_DRIVE</p> </li> <li> <p>STORAGE_CONNECTOR_ONE_DRIVE</p> </li> <li> <p>REDIRECT_URL</p> </li> <li> <p>FEEDBACK_URL</p> </li> <li> <p>THEME_NAME</p> </li> <li> <p>USER_SETTINGS</p> </li> <li> <p>EMBED_HOST_DOMAINS</p> </li> <li> <p>IAM_ROLE_ARN</p> </li> <li> <p>ACCESS_ENDPOINTS</p> </li> <li> <p>STREAMING_EXPERIENCE_SETTINGS</p> </li> <li> <p>AGENT_ACCESS_CONFIG</p> </li> </ul>"""
StackAttribute: TypeAlias = Literal[
    "STORAGE_CONNECTORS",
    "STORAGE_CONNECTOR_HOMEFOLDERS",
    "STORAGE_CONNECTOR_GOOGLE_DRIVE",
    "STORAGE_CONNECTOR_ONE_DRIVE",
    "REDIRECT_URL",
    "FEEDBACK_URL",
    "THEME_NAME",
    "USER_SETTINGS",
    "EMBED_HOST_DOMAINS",
    "IAM_ROLE_ARN",
    "ACCESS_ENDPOINTS",
    "STREAMING_EXPERIENCE_SETTINGS",
    "CONTENT_REDIRECTION",
    "AGENT_ACCESS_CONFIG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StackAttribute:
    return cast(StackAttribute, data)
