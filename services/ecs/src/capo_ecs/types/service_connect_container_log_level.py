"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectContainerLogLevel``."""

from typing import Literal, TypeAlias, cast

"""<p>The log level of the Service Connect proxy container.</p> <p>Valid values:</p> <ul> <li> <p> <code>debug</code> - Collects more detailed proxy logs for troubleshooting connectivity issues between services.</p> </li> <li> <p> <code>info</code> - The default log level.</p> </li> </ul>"""
ServiceConnectContainerLogLevel: TypeAlias = Literal[
    "debug",
    "info",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectContainerLogLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceConnectContainerLogLevel:
    return cast(ServiceConnectContainerLogLevel, data)
