"""Generated from Smithy shape ``com.amazonaws.securityagent#TestScope``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.test_scope_type


class TestScope(TypedDict, closed=True):
    type: "capo_securityagent.types.test_scope_type.TestScopeType"
    """<p>The category of application under test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestScope) -> dict:
    out: dict = {}
    import capo_securityagent.types.test_scope_type

    out["type"] = capo_securityagent.types.test_scope_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> TestScope:
    out: TestScope = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_securityagent.types.test_scope_type

        out["type"] = capo_securityagent.types.test_scope_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_securityagent.types.test_scope_type.TestScopeType", ""
        )
    return out
