"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorTypeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.connector_type
    import capo_inspector2.types.connector_type_comparison


class ConnectorTypeFilter(TypedDict, closed=True):
    comparison: (
        "capo_inspector2.types.connector_type_comparison.ConnectorTypeComparison"
    )
    """<p>The comparison operator for the connector type filter.</p>"""
    value: "capo_inspector2.types.connector_type.ConnectorType"
    """<p>The connector type value to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorTypeFilter) -> dict:
    out: dict = {}
    import capo_inspector2.types.connector_type_comparison

    out["comparison"] = capo_inspector2.types.connector_type_comparison.serialize_json(
        value["comparison"]
    )
    import capo_inspector2.types.connector_type

    out["value"] = capo_inspector2.types.connector_type.serialize_json(value["value"])
    return out


def deserialize_json(data: dict) -> ConnectorTypeFilter:
    out: ConnectorTypeFilter = {}  # type: ignore[typeddict-item]
    if data.get("comparison") is not None:
        import capo_inspector2.types.connector_type_comparison

        out["comparison"] = (
            capo_inspector2.types.connector_type_comparison.deserialize_json(
                data["comparison"]
            )
        )
    else:
        import typing

        out["comparison"] = typing.cast(
            "capo_inspector2.types.connector_type_comparison.ConnectorTypeComparison",
            "",
        )
    if data.get("value") is not None:
        import capo_inspector2.types.connector_type

        out["value"] = capo_inspector2.types.connector_type.deserialize_json(
            data["value"]
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_inspector2.types.connector_type.ConnectorType", ""
        )
    return out
