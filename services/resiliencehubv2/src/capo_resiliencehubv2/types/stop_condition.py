"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StopCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.stop_condition_source


class StopCondition(TypedDict, closed=True):
    source: "capo_resiliencehubv2.types.stop_condition_source.StopConditionSource"
    """<p>The source of the stop condition.</p>"""
    value: "str"
    """<p>The value of the stop condition, such as the ARN of the CloudWatch alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCondition) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.stop_condition_source

    out["source"] = capo_resiliencehubv2.types.stop_condition_source.serialize_json(
        value["source"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> StopCondition:
    out: StopCondition = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_resiliencehubv2.types.stop_condition_source

        out["source"] = (
            capo_resiliencehubv2.types.stop_condition_source.deserialize_json(
                data["source"]
            )
        )
    else:
        import typing

        out["source"] = typing.cast(
            "capo_resiliencehubv2.types.stop_condition_source.StopConditionSource", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
