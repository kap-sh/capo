"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExternalMetricsPreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.external_metrics_source


class ExternalMetricsPreference(TypedDict, closed=True):
    source: NotRequired[
        "capo_compute_optimizer.types.external_metrics_source.ExternalMetricsSource"
    ]
    """<p> Contains the source options for external metrics preferences. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExternalMetricsPreference) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_compute_optimizer.types.external_metrics_source

        out["source"] = (
            capo_compute_optimizer.types.external_metrics_source.serialize_aws_json_1_0(
                value["source"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExternalMetricsPreference:
    out: ExternalMetricsPreference = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_compute_optimizer.types.external_metrics_source

        out["source"] = (
            capo_compute_optimizer.types.external_metrics_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExternalMetricsPreference) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_compute_optimizer.types.external_metrics_source

        out["source"] = (
            capo_compute_optimizer.types.external_metrics_source.serialize_cbor(
                value["source"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ExternalMetricsPreference:
    out: ExternalMetricsPreference = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_compute_optimizer.types.external_metrics_source

        out["source"] = (
            capo_compute_optimizer.types.external_metrics_source.deserialize_cbor(
                data["source"]
            )
        )
    return out
