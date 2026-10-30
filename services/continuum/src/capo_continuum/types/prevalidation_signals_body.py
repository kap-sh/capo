"""Generated from Smithy shape ``com.amazonaws.continuum#PrevalidationSignalsBody``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.issue_artifact_producer_name
    import capo_continuum.types.prevalidation_signals


class PrevalidationSignalsBody(TypedDict, closed=True):
    produced_by: NotRequired[
        "capo_continuum.types.issue_artifact_producer_name.IssueArtifactProducerName"
    ]
    """The agent that produced this signal set."""
    signals: NotRequired[
        "capo_continuum.types.prevalidation_signals.PrevalidationSignals"
    ]
    """The signals backing the Issue's proposed severity."""


# --- restJson1 ser/de ---
def serialize_json(value: PrevalidationSignalsBody) -> dict:
    out: dict = {}
    if "produced_by" in value:
        out["producedBy"] = value["produced_by"]
    if "signals" in value:
        import capo_continuum.types.prevalidation_signals

        out["signals"] = capo_continuum.types.prevalidation_signals.serialize_json(
            value["signals"]
        )
    return out


def deserialize_json(data: dict) -> PrevalidationSignalsBody:
    out: PrevalidationSignalsBody = {}  # type: ignore[typeddict-item]
    if data.get("producedBy") is not None:
        out["produced_by"] = data["producedBy"]
    if data.get("signals") is not None:
        import capo_continuum.types.prevalidation_signals

        out["signals"] = capo_continuum.types.prevalidation_signals.deserialize_json(
            data["signals"]
        )
    return out
