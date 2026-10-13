"""Generated from Smithy shape ``com.amazonaws.cloudfront#TestFunctionResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.test_result


class TestFunctionResult(TypedDict, closed=True):
    test_result: NotRequired["capo_cloudfront.types.test_result.TestResult"]
    """<p>An object that represents the result of running the function with the provided event object.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TestFunctionResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "test_result" in value:
        import capo_cloudfront.types.test_result

        capo_cloudfront.types.test_result.serialize_xml(
            value["test_result"], el, "TestResult"
        )


def deserialize_xml(el: Element) -> TestFunctionResult:
    out: TestFunctionResult = {}  # type: ignore[typeddict-item]
    child_test_result = el.find("TestResult")
    if child_test_result is not None:
        import capo_cloudfront.types.test_result

        out["test_result"] = capo_cloudfront.types.test_result.deserialize_xml(
            child_test_result
        )
    return out


def redact_sensitive(value: TestFunctionResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "test_result" in value:
        import capo_cloudfront.types.test_result

        out["test_result"] = capo_cloudfront.types.test_result.redact_sensitive(
            value["test_result"]
        )
    return out
