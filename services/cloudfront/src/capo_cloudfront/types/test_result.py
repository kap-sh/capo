"""Generated from Smithy shape ``com.amazonaws.cloudfront#TestResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.function_execution_log_list
    import capo_cloudfront.types.function_summary
    import capo_cloudfront.types.sensitive_string_type
    import capo_cloudfront.types.string


class TestResult(TypedDict, closed=True):
    function_summary: NotRequired[
        "capo_cloudfront.types.function_summary.FunctionSummary"
    ]
    """<p>Contains configuration information and metadata about the CloudFront function that was tested.</p>"""
    compute_utilization: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The amount of time that the function took to run as a percentage of the maximum allowed time. For example, a compute utilization of 35 means that the function completed in 35% of the maximum allowed time.</p>"""
    function_execution_logs: NotRequired[
        "capo_cloudfront.types.function_execution_log_list.FunctionExecutionLogList"
    ]
    """<p>Contains the log lines that the function wrote (if any) when running the test.</p>"""
    function_error_message: NotRequired[
        "capo_cloudfront.types.sensitive_string_type.sensitiveStringType"
    ]
    """<p>If the result of testing the function was an error, this field contains the error message.</p>"""
    function_output: NotRequired[
        "capo_cloudfront.types.sensitive_string_type.sensitiveStringType"
    ]
    """<p>The event object returned by the function. For more information about the structure of the event object, see <a href="https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/functions-event-structure.html">Event object structure</a> in the <i>Amazon CloudFront Developer Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TestResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "function_summary" in value:
        import capo_cloudfront.types.function_summary

        capo_cloudfront.types.function_summary.serialize_xml(
            value["function_summary"], el, "FunctionSummary"
        )
    if "compute_utilization" in value:
        SubElement(el, "ComputeUtilization").text = str(value["compute_utilization"])
    if "function_execution_logs" in value:
        import capo_cloudfront.types.function_execution_log_list

        capo_cloudfront.types.function_execution_log_list.serialize_xml(
            value["function_execution_logs"], el, "FunctionExecutionLogs"
        )
    if "function_error_message" in value:
        SubElement(el, "FunctionErrorMessage").text = str(
            value["function_error_message"]
        )
    if "function_output" in value:
        SubElement(el, "FunctionOutput").text = str(value["function_output"])


def deserialize_xml(el: Element) -> TestResult:
    out: TestResult = {}  # type: ignore[typeddict-item]
    child_function_summary = el.find("FunctionSummary")
    if child_function_summary is not None:
        import capo_cloudfront.types.function_summary

        out["function_summary"] = (
            capo_cloudfront.types.function_summary.deserialize_xml(
                child_function_summary
            )
        )
    child_compute_utilization = el.find("ComputeUtilization")
    if child_compute_utilization is not None:
        out["compute_utilization"] = str(child_compute_utilization.text or "")
    child_function_execution_logs = el.find("FunctionExecutionLogs")
    if child_function_execution_logs is not None:
        import capo_cloudfront.types.function_execution_log_list

        out["function_execution_logs"] = (
            capo_cloudfront.types.function_execution_log_list.deserialize_xml(
                child_function_execution_logs
            )
        )
    child_function_error_message = el.find("FunctionErrorMessage")
    if child_function_error_message is not None:
        out["function_error_message"] = str(child_function_error_message.text or "")
    child_function_output = el.find("FunctionOutput")
    if child_function_output is not None:
        out["function_output"] = str(child_function_output.text or "")
    return out
