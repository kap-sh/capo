"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ApplicationLogLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>The log level for application logs. Lambda sends logs at the selected level and at all more severe levels. Possible values, from least to most severe:</p> <ul> <li> <p> <code>TRACE</code> – The most detailed information, for tracing code paths.</p> </li> <li> <p> <code>DEBUG</code> – Detailed information for debugging.</p> </li> <li> <p> <code>INFO</code> – General information about application progress.</p> </li> <li> <p> <code>WARN</code> – Potential issues that don't prevent the application from running.</p> </li> <li> <p> <code>ERROR</code> – Errors that prevent an operation from completing.</p> </li> <li> <p> <code>FATAL</code> – Severe errors that cause the application to stop.</p> </li> </ul>"""
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
