"""Generated from Smithy shape ``com.amazonaws.cloudfront#ConnectionFunctionTestResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.connection_function_summary
    import capo_cloudfront.types.function_execution_log_list
    import capo_cloudfront.types.sensitive_string_type
    import capo_cloudfront.types.string


class ConnectionFunctionTestResult(TypedDict, closed=True):
    connection_function_summary: NotRequired[
        "capo_cloudfront.types.connection_function_summary.ConnectionFunctionSummary"
    ]
    """<p>The connection function summary.</p>"""
    compute_utilization: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The connection function compute utilization.</p>"""
    connection_function_execution_logs: NotRequired[
        "capo_cloudfront.types.function_execution_log_list.FunctionExecutionLogList"
    ]
    """<p>The connection function execution logs.</p>"""
    connection_function_error_message: NotRequired[
        "capo_cloudfront.types.sensitive_string_type.sensitiveStringType"
    ]
    """<p>The connection function error message.</p>"""
    connection_function_output: NotRequired[
        "capo_cloudfront.types.sensitive_string_type.sensitiveStringType"
    ]
    """<p>The connection function output.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ConnectionFunctionTestResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "connection_function_summary" in value:
        import capo_cloudfront.types.connection_function_summary

        capo_cloudfront.types.connection_function_summary.serialize_xml(
            value["connection_function_summary"], el, "ConnectionFunctionSummary"
        )
    if "compute_utilization" in value:
        SubElement(el, "ComputeUtilization").text = str(value["compute_utilization"])
    if "connection_function_execution_logs" in value:
        import capo_cloudfront.types.function_execution_log_list

        capo_cloudfront.types.function_execution_log_list.serialize_xml(
            value["connection_function_execution_logs"],
            el,
            "ConnectionFunctionExecutionLogs",
        )
    if "connection_function_error_message" in value:
        SubElement(el, "ConnectionFunctionErrorMessage").text = str(
            value["connection_function_error_message"]
        )
    if "connection_function_output" in value:
        SubElement(el, "ConnectionFunctionOutput").text = str(
            value["connection_function_output"]
        )


def deserialize_xml(el: Element) -> ConnectionFunctionTestResult:
    out: ConnectionFunctionTestResult = {}  # type: ignore[typeddict-item]
    child_connection_function_summary = el.find("ConnectionFunctionSummary")
    if child_connection_function_summary is not None:
        import capo_cloudfront.types.connection_function_summary

        out["connection_function_summary"] = (
            capo_cloudfront.types.connection_function_summary.deserialize_xml(
                child_connection_function_summary
            )
        )
    child_compute_utilization = el.find("ComputeUtilization")
    if child_compute_utilization is not None:
        out["compute_utilization"] = str(child_compute_utilization.text or "")
    child_connection_function_execution_logs = el.find(
        "ConnectionFunctionExecutionLogs"
    )
    if child_connection_function_execution_logs is not None:
        import capo_cloudfront.types.function_execution_log_list

        out["connection_function_execution_logs"] = (
            capo_cloudfront.types.function_execution_log_list.deserialize_xml(
                child_connection_function_execution_logs
            )
        )
    child_connection_function_error_message = el.find("ConnectionFunctionErrorMessage")
    if child_connection_function_error_message is not None:
        out["connection_function_error_message"] = str(
            child_connection_function_error_message.text or ""
        )
    child_connection_function_output = el.find("ConnectionFunctionOutput")
    if child_connection_function_output is not None:
        out["connection_function_output"] = str(
            child_connection_function_output.text or ""
        )
    return out


def redact_sensitive(value: ConnectionFunctionTestResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_function_execution_logs" in value:
        out["connection_function_execution_logs"] = "*** Sensitive Data Redacted ***"
    if "connection_function_error_message" in value:
        out["connection_function_error_message"] = "*** Sensitive Data Redacted ***"
    if "connection_function_output" in value:
        out["connection_function_output"] = "*** Sensitive Data Redacted ***"
    return out
