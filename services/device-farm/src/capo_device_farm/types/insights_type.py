"""Generated from Smithy shape ``com.amazonaws.devicefarm#InsightsType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of insights to generate. Possible values are:</p> <ul> <li> <p>TEST_REPORT: Specifies that you receive a test summary for each job in the run, and an aggregated summary for the run. This is the default value. Use <code>TEST_REPORT</code> when you want job-level and run-level test summaries.</p> </li> <li> <p>NONE: Specifies that you do not receive insights for the run. Use <code>NONE</code> when you do not want insights generated. You cannot combine <code>NONE</code> with any other value.</p> </li> </ul>"""
InsightsType: TypeAlias = Literal[
    "TEST_REPORT",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InsightsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InsightsType:
    return cast(InsightsType, data)
