"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricCharacteristics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.periodic_spikes


class MetricCharacteristics(TypedDict, closed=True):
    periodic_spikes: NotRequired["capo_cloudwatch.types.periodic_spikes.PeriodicSpikes"]
    """<p>Set this parameter to <code>true</code> if values for this metric consistently include spikes that should not be considered to be anomalies. With this set to <code>true</code>, CloudWatch will expect to see spikes that occurred consistently during the model training period, and won't flag future similar spikes as anomalies.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricCharacteristics) -> dict:
    out: dict = {}
    if "periodic_spikes" in value:
        out["PeriodicSpikes"] = value["periodic_spikes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricCharacteristics:
    out: MetricCharacteristics = {}  # type: ignore[typeddict-item]
    if data.get("PeriodicSpikes") is not None:
        out["periodic_spikes"] = data["PeriodicSpikes"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricCharacteristics, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "periodic_spikes" in value:
        pairs.append(
            (
                f"{key_prefix}PeriodicSpikes",
                "true" if value["periodic_spikes"] else "false",
            )
        )


def deserialize_query(el: Element) -> MetricCharacteristics:
    out: MetricCharacteristics = {}  # type: ignore[typeddict-item]
    child_periodic_spikes = el.find("PeriodicSpikes")
    if child_periodic_spikes is not None:
        out["periodic_spikes"] = (child_periodic_spikes.text or "").lower() == "true"
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricCharacteristics) -> dict:
    out: dict = {}
    if "periodic_spikes" in value:
        out["PeriodicSpikes"] = value["periodic_spikes"]
    return out


def deserialize_cbor(data: dict) -> MetricCharacteristics:
    out: MetricCharacteristics = {}  # type: ignore[typeddict-item]
    if data.get("PeriodicSpikes") is not None:
        out["periodic_spikes"] = data["PeriodicSpikes"]
    return out
