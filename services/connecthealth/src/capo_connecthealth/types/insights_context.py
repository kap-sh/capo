"""Generated from Smithy shape ``com.amazonaws.connecthealth#InsightsContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.insights_type


class InsightsContext(TypedDict, closed=True):
    insights_type: "capo_connecthealth.types.insights_type.InsightsType"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightsContext) -> dict:
    out: dict = {}
    import capo_connecthealth.types.insights_type

    out["insightsType"] = capo_connecthealth.types.insights_type.serialize_json(
        value["insights_type"]
    )
    return out


def deserialize_json(data: dict) -> InsightsContext:
    out: InsightsContext = {}  # type: ignore[typeddict-item]
    if data.get("insightsType") is not None:
        import capo_connecthealth.types.insights_type

        out["insights_type"] = capo_connecthealth.types.insights_type.deserialize_json(
            data["insightsType"]
        )
    else:
        import typing

        out["insights_type"] = typing.cast(
            "capo_connecthealth.types.insights_type.InsightsType", ""
        )
    return out
