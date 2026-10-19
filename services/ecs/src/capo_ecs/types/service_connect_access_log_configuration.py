"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectAccessLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.service_connect_access_logging_format
    import capo_ecs.types.service_connect_include_query_parameters


class ServiceConnectAccessLogConfiguration(TypedDict, closed=True):
    format: "capo_ecs.types.service_connect_access_logging_format.ServiceConnectAccessLoggingFormat"
    """<p>The format for Service Connect access log output. Choose TEXT for human-readable logs or JSON for structured data that integrates well with log analysis tools.</p>"""
    include_query_parameters: NotRequired[
        "capo_ecs.types.service_connect_include_query_parameters.ServiceConnectIncludeQueryParameters"
    ]
    """<p>Specifies whether to include query parameters in Service Connect access logs.</p> <p>When enabled, query parameters from HTTP requests are included in the access logs. Consider security and privacy implications when enabling this feature, as query parameters may contain sensitive information such as request IDs and tokens. By default, this parameter is <code>DISABLED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectAccessLogConfiguration) -> dict:
    out: dict = {}
    import capo_ecs.types.service_connect_access_logging_format

    out["format"] = (
        capo_ecs.types.service_connect_access_logging_format.serialize_aws_json_1_1(
            value["format"]
        )
    )
    if "include_query_parameters" in value:
        import capo_ecs.types.service_connect_include_query_parameters

        out["includeQueryParameters"] = (
            capo_ecs.types.service_connect_include_query_parameters.serialize_aws_json_1_1(
                value["include_query_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectAccessLogConfiguration:
    out: ServiceConnectAccessLogConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_ecs.types.service_connect_access_logging_format

        out["format"] = (
            capo_ecs.types.service_connect_access_logging_format.deserialize_aws_json_1_1(
                data["format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_ecs.types.service_connect_access_logging_format.ServiceConnectAccessLoggingFormat",
            "",
        )
    if data.get("includeQueryParameters") is not None:
        import capo_ecs.types.service_connect_include_query_parameters

        out["include_query_parameters"] = (
            capo_ecs.types.service_connect_include_query_parameters.deserialize_aws_json_1_1(
                data["includeQueryParameters"]
            )
        )
    return out
