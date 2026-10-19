"""Generated from Smithy shape ``com.amazonaws.mailmanager#Analysis``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.analyzer_arn
    import capo_mailmanager.types.result_field


class Analysis(TypedDict, closed=True):
    analyzer: "capo_mailmanager.types.analyzer_arn.AnalyzerArn"
    """<p>The Amazon Resource Name (ARN) of an Add On.</p>"""
    result_field: "capo_mailmanager.types.result_field.ResultField"
    """<p>The returned value from an Add On.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Analysis) -> dict:
    out: dict = {}
    out["Analyzer"] = value["analyzer"]
    out["ResultField"] = value["result_field"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Analysis:
    out: Analysis = {}  # type: ignore[typeddict-item]
    if data.get("Analyzer") is not None:
        out["analyzer"] = data["Analyzer"]
    else:
        out["analyzer"] = ""
    if data.get("ResultField") is not None:
        out["result_field"] = data["ResultField"]
    else:
        out["result_field"] = ""
    return out
