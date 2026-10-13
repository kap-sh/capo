"""Generated from Smithy shape ``com.amazonaws.guardduty#Sequence``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.actors
    import capo_guardduty.types.additional_sequence_types
    import capo_guardduty.types.indicators
    import capo_guardduty.types.network_endpoints
    import capo_guardduty.types.resources
    import capo_guardduty.types.sequence_description
    import capo_guardduty.types.signals
    import capo_guardduty.types.string


class Sequence(TypedDict, closed=True):
    uid: NotRequired["capo_guardduty.types.string.String"]
    """<p>Unique identifier of the attack sequence.</p>"""
    description: NotRequired[
        "capo_guardduty.types.sequence_description.SequenceDescription"
    ]
    """<p>Description of the attack sequence.</p>"""
    actors: NotRequired["capo_guardduty.types.actors.Actors"]
    """<p>Contains information about the actors involved in the attack sequence.</p>"""
    resources: NotRequired["capo_guardduty.types.resources.Resources"]
    """<p>Contains information about the resources involved in the attack sequence.</p>"""
    endpoints: NotRequired["capo_guardduty.types.network_endpoints.NetworkEndpoints"]
    """<p>Contains information about the network endpoints that were used in the attack sequence.</p>"""
    signals: NotRequired["capo_guardduty.types.signals.Signals"]
    """<p>Contains information about the signals involved in the attack sequence.</p>"""
    sequence_indicators: NotRequired["capo_guardduty.types.indicators.Indicators"]
    """<p>Contains information about the indicators observed in the attack sequence.</p>"""
    additional_sequence_types: NotRequired[
        "capo_guardduty.types.additional_sequence_types.AdditionalSequenceTypes"
    ]
    """<p>Additional types of sequences that may be associated with the attack sequence finding, providing further context about the nature of the detected threat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sequence) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "description" in value:
        out["description"] = value["description"]
    if "actors" in value:
        import capo_guardduty.types.actors

        out["actors"] = capo_guardduty.types.actors.serialize_json(value["actors"])
    if "resources" in value:
        import capo_guardduty.types.resources

        out["resources"] = capo_guardduty.types.resources.serialize_json(
            value["resources"]
        )
    if "endpoints" in value:
        import capo_guardduty.types.network_endpoints

        out["endpoints"] = capo_guardduty.types.network_endpoints.serialize_json(
            value["endpoints"]
        )
    if "signals" in value:
        import capo_guardduty.types.signals

        out["signals"] = capo_guardduty.types.signals.serialize_json(value["signals"])
    if "sequence_indicators" in value:
        import capo_guardduty.types.indicators

        out["sequenceIndicators"] = capo_guardduty.types.indicators.serialize_json(
            value["sequence_indicators"]
        )
    if "additional_sequence_types" in value:
        import capo_guardduty.types.additional_sequence_types

        out["additionalSequenceTypes"] = (
            capo_guardduty.types.additional_sequence_types.serialize_json(
                value["additional_sequence_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> Sequence:
    out: Sequence = {}  # type: ignore[typeddict-item]
    if data.get("uid") is not None:
        out["uid"] = data["uid"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("actors") is not None:
        import capo_guardduty.types.actors

        out["actors"] = capo_guardduty.types.actors.deserialize_json(data["actors"])
    if data.get("resources") is not None:
        import capo_guardduty.types.resources

        out["resources"] = capo_guardduty.types.resources.deserialize_json(
            data["resources"]
        )
    if data.get("endpoints") is not None:
        import capo_guardduty.types.network_endpoints

        out["endpoints"] = capo_guardduty.types.network_endpoints.deserialize_json(
            data["endpoints"]
        )
    if data.get("signals") is not None:
        import capo_guardduty.types.signals

        out["signals"] = capo_guardduty.types.signals.deserialize_json(data["signals"])
    if data.get("sequenceIndicators") is not None:
        import capo_guardduty.types.indicators

        out["sequence_indicators"] = capo_guardduty.types.indicators.deserialize_json(
            data["sequenceIndicators"]
        )
    if data.get("additionalSequenceTypes") is not None:
        import capo_guardduty.types.additional_sequence_types

        out["additional_sequence_types"] = (
            capo_guardduty.types.additional_sequence_types.deserialize_json(
                data["additionalSequenceTypes"]
            )
        )
    return out


def redact_sensitive(value: Sequence) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resources" in value:
        import capo_guardduty.types.resources

        out["resources"] = capo_guardduty.types.resources.redact_sensitive(
            value["resources"]
        )
    return out
