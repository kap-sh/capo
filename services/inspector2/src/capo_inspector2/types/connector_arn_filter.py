"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorArnFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_arn
    import capo_inspector2.types.connector_arn_comparison


class ConnectorArnFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.connector_arn_comparison.ConnectorArnComparison"
    """<p>The comparison operator for the connector ARN filter.</p>"""
    value: "capo_inspector2.types.connector_arn.ConnectorArn"
    """<p>The connector ARN value to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorArnFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.connector_arn_comparison

    out["comparison"] = capo_inspector2.types.connector_arn_comparison.serialize_json(
        value["comparison"]
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ConnectorArnFilter:
    out: ConnectorArnFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.connector_arn_comparison

        out["comparison"] = (
            capo_inspector2.types.connector_arn_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_inspector2.types.connector_arn_comparison.ConnectorArnComparison", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
