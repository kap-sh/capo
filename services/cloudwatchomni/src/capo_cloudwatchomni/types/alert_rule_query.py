"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertRuleQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.query_language


class AlertRuleQuery(TypedDict, closed=True):
    language: "capo_cloudwatchomni.types.query_language.QueryLanguage"
    """The query language of the expression."""
    expression: "str"
    """The query expression to evaluate."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertRuleQuery) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.query_language

    out["language"] = capo_cloudwatchomni.types.query_language.serialize_cbor(
        value["language"]
    )
    out["expression"] = value["expression"]
    return out


def deserialize_cbor(data: dict) -> AlertRuleQuery:
    out: AlertRuleQuery = {}  # type: ignore[typeddict-item]
    if data.get("language") is not None:
        import capo_cloudwatchomni.types.query_language

        out["language"] = capo_cloudwatchomni.types.query_language.deserialize_cbor(
            data["language"]
        )
    else:
        import typing

        out["language"] = typing.cast(
            "capo_cloudwatchomni.types.query_language.QueryLanguage", ""
        )
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    return out
