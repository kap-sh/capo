"""Generated from Smithy shape ``com.amazonaws.glue#AnalysisType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of upgrade analysis. For auto-upgrade jobs, this value is <code>AUTO_UPGRADE</code>.</p>"""
AnalysisType: TypeAlias = Literal["AUTO_UPGRADE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnalysisType:
    return cast(AnalysisType, data)
