"""Generated from Smithy shape ``com.amazonaws.cloudfront#TestConnectionFunctionResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.connection_function_test_result


class TestConnectionFunctionResult(TypedDict, closed=True):
    connection_function_test_result: NotRequired[
        "capo_cloudfront.types.connection_function_test_result.ConnectionFunctionTestResult"
    ]
    """<p>The connection function test result.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: TestConnectionFunctionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "connection_function_test_result" in value:
        import capo_cloudfront.types.connection_function_test_result

        capo_cloudfront.types.connection_function_test_result.serialize_xml(
            value["connection_function_test_result"], el, "ConnectionFunctionTestResult"
        )


def deserialize_xml(el: Element) -> TestConnectionFunctionResult:
    out: TestConnectionFunctionResult = {}  # type: ignore[typeddict-item]
    child_connection_function_test_result = el.find("ConnectionFunctionTestResult")
    if child_connection_function_test_result is not None:
        import capo_cloudfront.types.connection_function_test_result

        out["connection_function_test_result"] = (
            capo_cloudfront.types.connection_function_test_result.deserialize_xml(
                child_connection_function_test_result
            )
        )
    return out


def redact_sensitive(value: TestConnectionFunctionResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connection_function_test_result" in value:
        import capo_cloudfront.types.connection_function_test_result

        out["connection_function_test_result"] = (
            capo_cloudfront.types.connection_function_test_result.redact_sensitive(
                value["connection_function_test_result"]
            )
        )
    return out
