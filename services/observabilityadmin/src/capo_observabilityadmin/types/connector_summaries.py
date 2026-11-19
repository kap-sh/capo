"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ConnectorSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_summary

ConnectorSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.connector_summary.ConnectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSummaries) -> list:
    import capo_observabilityadmin.types.connector_summary

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.connector_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorSummaries:
    import capo_observabilityadmin.types.connector_summary

    out: ConnectorSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.connector_summary.deserialize_json(item)
        )
    return out
