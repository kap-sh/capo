"""Generated from Smithy shape ``com.amazonaws.mediatailor#FunctionType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of a function, which determines what the function can do at runtime. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types.html">Function types and composition</a> in the <i>MediaTailor User Guide</i>.</p>"""
FunctionType: TypeAlias = Literal[
    "HTTP_REQUEST",
    "AWS_SERVICE_REQUEST",
    "CUSTOM_OUTPUT",
    "CONCURRENT_EXECUTOR",
    "SEQUENTIAL_EXECUTOR",
    "VAST_REQUEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionType) -> str:
    return value


def deserialize_json(data: str) -> FunctionType:
    return cast(FunctionType, data)
