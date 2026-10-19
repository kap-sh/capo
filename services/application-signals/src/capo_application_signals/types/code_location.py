"""Generated from Smithy shape ``com.amazonaws.applicationsignals#CodeLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.programming_language


class CodeLocation(TypedDict, closed=True):
    language: "capo_application_signals.types.programming_language.ProgrammingLanguage"
    """<p>The programming language for this instrumentation point, such as Java, Python, or JavaScript.</p>"""
    code_unit: NotRequired["str"]
    """<p>The package, module, or namespace that contains the target code, for example <code>com.amazon.payment</code> or <code>payment_service</code>.</p>"""
    class_name: NotRequired["str"]
    """<p>The class or type name that contains the method. This is required for Java and optional for Python module-level functions.</p>"""
    method_name: NotRequired["str"]
    """<p>The method or function name to instrument, such as <code>validateCreditCard</code> or <code>__init__</code>.</p>"""
    file_path: "str"
    """<p>The source file path relative to the project or source root, such as <code>src/payment/PaymentProcessor.java</code> or <code>src/payment/PaymentProcessor.py</code>.</p>"""
    line_number: NotRequired["int"]
    """<p>The line number to instrument. Provide this to disambiguate overloaded methods and to target a specific line when needed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeLocation) -> dict:
    out: dict = {}
    import capo_application_signals.types.programming_language

    out["Language"] = (
        capo_application_signals.types.programming_language.serialize_json(
            value["language"]
        )
    )
    if "code_unit" in value:
        out["CodeUnit"] = value["code_unit"]
    if "class_name" in value:
        out["ClassName"] = value["class_name"]
    if "method_name" in value:
        out["MethodName"] = value["method_name"]
    out["FilePath"] = value["file_path"]
    if "line_number" in value:
        out["LineNumber"] = value["line_number"]
    return out


def deserialize_json(data: dict) -> CodeLocation:
    out: CodeLocation = {}  # type: ignore[typeddict-item]
    if data.get("Language") is not None:
        import capo_application_signals.types.programming_language

        out["language"] = (
            capo_application_signals.types.programming_language.deserialize_json(
                data["Language"]
            )
        )
    else:
        import typing

        out["language"] = typing.cast(
            "capo_application_signals.types.programming_language.ProgrammingLanguage",
            "",
        )
    if data.get("CodeUnit") is not None:
        out["code_unit"] = data["CodeUnit"]
    if data.get("ClassName") is not None:
        out["class_name"] = data["ClassName"]
    if data.get("MethodName") is not None:
        out["method_name"] = data["MethodName"]
    if data.get("FilePath") is not None:
        out["file_path"] = data["FilePath"]
    else:
        out["file_path"] = ""
    if data.get("LineNumber") is not None:
        out["line_number"] = data["LineNumber"]
    return out
