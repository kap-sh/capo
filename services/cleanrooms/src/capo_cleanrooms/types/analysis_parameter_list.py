"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisParameterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_parameter

AnalysisParameterList: TypeAlias = list[
    "capo_cleanrooms.types.analysis_parameter.AnalysisParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisParameterList) -> list:
    import capo_cleanrooms.types.analysis_parameter

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.analysis_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisParameterList:
    import capo_cleanrooms.types.analysis_parameter

    out: AnalysisParameterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cleanrooms.types.analysis_parameter.deserialize_json(item))
    return out


def redact_sensitive(value: AnalysisParameterList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
