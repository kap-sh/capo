"""Generated from Smithy shape ``com.amazonaws.sagemaker#ForEachStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a ForEach step execution. Valid values are:</p> <ul> <li> <p> <code>Succeeded</code> indicates that the ForEach step execution completed successfully.</p> </li> <li> <p> <code>Failed</code> indicates that the ForEach step execution failed.</p> </li> <li> <p> <code>Stopped</code> indicates that the ForEach step execution was stopped.</p> </li> </ul>"""
ForEachStatus: TypeAlias = Literal[
    "Succeeded",
    "Failed",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForEachStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ForEachStatus:
    return cast(ForEachStatus, data)
