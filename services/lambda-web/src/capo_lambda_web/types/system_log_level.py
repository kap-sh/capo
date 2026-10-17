"""Generated from Smithy shape ``com.amazonaws.lambdaweb#SystemLogLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>The log level for system logs from the Lambda runtime. Lambda sends logs at the selected level and at all more severe levels. Possible values, from least to most severe:</p> <ul> <li> <p> <code>DEBUG</code> – Detailed information about the runtime, for debugging.</p> </li> <li> <p> <code>INFO</code> – General information about the runtime, such as the start and end of execution.</p> </li> <li> <p> <code>WARN</code> – Potential issues detected by the runtime.</p> </li> </ul>"""
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
