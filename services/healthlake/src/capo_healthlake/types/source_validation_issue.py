"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#SourceValidationIssue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.validation_severity


class SourceValidationIssue(TypedDict, closed=True):
    severity: "capo_healthlake.types.validation_severity.ValidationSeverity"
    """<p>The severity of the validation issue (ERROR or WARNING). Errors indicate problems that prevent successful conversion; warnings indicate potential issues that do not block conversion.</p>"""
    message: "str"
    """<p>A description of the validation issue.</p>"""
    field: NotRequired["str"]
    """<p>The field in the source file that caused the validation issue.</p>"""
    code: NotRequired["str"]
    """<p>The validation rule code that identified this issue.</p>"""
    line: NotRequired["int"]
    """<p>The line number in the source file where the issue was detected.</p>"""
    column: NotRequired["int"]
    """<p>The column number in the source file where the issue was detected.</p>"""
    xpath: NotRequired["str"]
    """<p>The XPath expression that identifies the location of the issue within a C-CDA document. The service populates this field only for C-CDA source files.</p>"""
    remediation: NotRequired["str"]
    """<p>A suggested fix for the validation issue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceValidationIssue) -> dict:
    out: dict = {}
    import capo_healthlake.types.validation_severity

    out["Severity"] = capo_healthlake.types.validation_severity.serialize_aws_json_1_0(
        value["severity"]
    )
    out["Message"] = value["message"]
    if "field" in value:
        out["Field"] = value["field"]
    if "code" in value:
        out["Code"] = value["code"]
    if "line" in value:
        out["Line"] = value["line"]
    if "column" in value:
        out["Column"] = value["column"]
    if "xpath" in value:
        out["Xpath"] = value["xpath"]
    if "remediation" in value:
        out["Remediation"] = value["remediation"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SourceValidationIssue:
    out: SourceValidationIssue = {}  # type: ignore[typeddict-item]
    if data.get("Severity") is not None:
        import capo_healthlake.types.validation_severity

        out["severity"] = (
            capo_healthlake.types.validation_severity.deserialize_aws_json_1_0(
                data["Severity"]
            )
        )
    else:
        import typing

        out["severity"] = typing.cast(
            "capo_healthlake.types.validation_severity.ValidationSeverity", ""
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("Field") is not None:
        out["field"] = data["Field"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Line") is not None:
        out["line"] = data["Line"]
    if data.get("Column") is not None:
        out["column"] = data["Column"]
    if data.get("Xpath") is not None:
        out["xpath"] = data["Xpath"]
    if data.get("Remediation") is not None:
        out["remediation"] = data["Remediation"]
    return out
