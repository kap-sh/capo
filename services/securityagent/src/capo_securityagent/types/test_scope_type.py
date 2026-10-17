"""Generated from Smithy shape ``com.amazonaws.securityagent#TestScopeType``."""

from typing import Literal, TypeAlias, cast

"""<p>The category of application a pentest targets.</p>"""
TestScopeType: TypeAlias = Literal[
    "WEB_APP",
    "GENERATIVE_AI_APP",
]


# --- restJson1 ser/de ---
def serialize_json(value: TestScopeType) -> str:
    return value


def deserialize_json(data: str) -> TestScopeType:
    return cast(TestScopeType, data)
