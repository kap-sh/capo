"""Generated from Smithy shape ``com.amazonaws.lambdaweb#SystemLogLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>The log level for system logs from the Lambda runtime. Possible values: <code>DEBUG</code>, <code>INFO</code>, <code>WARN</code>.</p>"""
SystemLogLevel: TypeAlias = Literal[
    "DEBUG",
    "INFO",
    "WARN",
]


# --- restJson1 ser/de ---
def serialize_json(value: SystemLogLevel) -> str:
    return value


def deserialize_json(data: str) -> SystemLogLevel:
    return cast(SystemLogLevel, data)
