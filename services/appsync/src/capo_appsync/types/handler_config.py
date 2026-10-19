"""Generated from Smithy shape ``com.amazonaws.appsync#HandlerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.handler_behavior
    import capo_appsync.types.integration


class HandlerConfig(TypedDict, closed=True):
    behavior: "capo_appsync.types.handler_behavior.HandlerBehavior"
    """<p>The behavior for the handler.</p>"""
    integration: "capo_appsync.types.integration.Integration"
    """<p>The integration data source configuration for the handler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HandlerConfig) -> dict:
    out: dict = {}
    import capo_appsync.types.handler_behavior

    out["behavior"] = capo_appsync.types.handler_behavior.serialize_json(
        value["behavior"]
    )
    import capo_appsync.types.integration

    out["integration"] = capo_appsync.types.integration.serialize_json(
        value["integration"]
    )
    return out


def deserialize_json(data: dict) -> HandlerConfig:
    out: HandlerConfig = {}  # type: ignore[typeddict-item]
    if data.get("behavior") is not None:
        import capo_appsync.types.handler_behavior

        out["behavior"] = capo_appsync.types.handler_behavior.deserialize_json(
            data["behavior"]
        )
    else:
        import typing

        out["behavior"] = typing.cast(
            "capo_appsync.types.handler_behavior.HandlerBehavior", ""
        )
    if data.get("integration") is not None:
        import capo_appsync.types.integration

        out["integration"] = capo_appsync.types.integration.deserialize_json(
            data["integration"]
        )
    else:
        raise DeserializationError("HandlerConfig.integration required")
    return out
