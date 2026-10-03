"""Generated from Smithy shape ``com.amazonaws.securityhub#Sequence``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.actors_list
    import capo_securityhub.types.indicators_list
    import capo_securityhub.types.network_endpoints_list
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.signals_list


class Sequence(TypedDict, closed=True):
    uid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Unique identifier of the attack sequence. </p>"""
    actors: NotRequired["capo_securityhub.types.actors_list.ActorsList"]
    """<p> Provides information about the actors involved in the attack sequence. </p>"""
    endpoints: NotRequired[
        "capo_securityhub.types.network_endpoints_list.NetworkEndpointsList"
    ]
    """<p> Contains information about the network endpoints that were used in the attack sequence. </p>"""
    signals: NotRequired["capo_securityhub.types.signals_list.SignalsList"]
    """<p> Contains information about the signals involved in the attack sequence. </p>"""
    sequence_indicators: NotRequired[
        "capo_securityhub.types.indicators_list.IndicatorsList"
    ]
    """<p> Contains information about the indicators observed in the attack sequence. The values for <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Signal.html">SignalIndicators</a> are a subset of the values for <code>SequenceIndicators</code>, but the values for these fields don't always match 1:1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sequence) -> dict:
    out: dict = {}
    if "uid" in value:
        out["Uid"] = value["uid"]
    if "actors" in value:
        import capo_securityhub.types.actors_list

        out["Actors"] = capo_securityhub.types.actors_list.serialize_json(
            value["actors"]
        )
    if "endpoints" in value:
        import capo_securityhub.types.network_endpoints_list

        out["Endpoints"] = capo_securityhub.types.network_endpoints_list.serialize_json(
            value["endpoints"]
        )
    if "signals" in value:
        import capo_securityhub.types.signals_list

        out["Signals"] = capo_securityhub.types.signals_list.serialize_json(
            value["signals"]
        )
    if "sequence_indicators" in value:
        import capo_securityhub.types.indicators_list

        out["SequenceIndicators"] = (
            capo_securityhub.types.indicators_list.serialize_json(
                value["sequence_indicators"]
            )
        )
    return out


def deserialize_json(data: dict) -> Sequence:
    out: Sequence = {}  # type: ignore[typeddict-item]
    if data.get("Uid") is not None:
        out["uid"] = data["Uid"]
    if data.get("Actors") is not None:
        import capo_securityhub.types.actors_list

        out["actors"] = capo_securityhub.types.actors_list.deserialize_json(
            data["Actors"]
        )
    if data.get("Endpoints") is not None:
        import capo_securityhub.types.network_endpoints_list

        out["endpoints"] = (
            capo_securityhub.types.network_endpoints_list.deserialize_json(
                data["Endpoints"]
            )
        )
    if data.get("Signals") is not None:
        import capo_securityhub.types.signals_list

        out["signals"] = capo_securityhub.types.signals_list.deserialize_json(
            data["Signals"]
        )
    if data.get("SequenceIndicators") is not None:
        import capo_securityhub.types.indicators_list

        out["sequence_indicators"] = (
            capo_securityhub.types.indicators_list.deserialize_json(
                data["SequenceIndicators"]
            )
        )
    return out
