"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ApplicationLogLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>The log level for application logs. Possible values: <code>TRACE</code>, <code>DEBUG</code>, <code>INFO</code>, <code>WARN</code>, <code>ERROR</code>, <code>FATAL</code>.</p>"""
ApplicationLogLevel: TypeAlias = Literal[
    "TRACE",
    "DEBUG",
    "INFO",
    "WARN",
    "ERROR",
    "FATAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationLogLevel) -> str:
    return value


def deserialize_json(data: str) -> ApplicationLogLevel:
    return cast(ApplicationLogLevel, data)
