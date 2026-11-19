"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.metric_provider_arn
    import capo_compute_optimizer.types.metric_source_provider


class MetricSource(TypedDict, closed=True):
    provider: NotRequired[
        "capo_compute_optimizer.types.metric_source_provider.MetricSourceProvider"
    ]
    """<p> The name of the metric source provider. </p>"""
    provider_arn: NotRequired[
        "capo_compute_optimizer.types.metric_provider_arn.MetricProviderArn"
    ]
    """<p> The ARN of the metric source provider. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricSource) -> dict:
    out: dict = {}
    if "provider" in value:
        import capo_compute_optimizer.types.metric_source_provider

        out["provider"] = (
            capo_compute_optimizer.types.metric_source_provider.serialize_aws_json_1_0(
                value["provider"]
            )
        )
    if "provider_arn" in value:
        out["providerArn"] = value["provider_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricSource:
    out: MetricSource = {}  # type: ignore[typeddict-item]
    if data.get("provider") is not None:
        import capo_compute_optimizer.types.metric_source_provider

        out["provider"] = (
            capo_compute_optimizer.types.metric_source_provider.deserialize_aws_json_1_0(
                data["provider"]
            )
        )
    if data.get("providerArn") is not None:
        out["provider_arn"] = data["providerArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricSource) -> dict:
    out: dict = {}
    if "provider" in value:
        import capo_compute_optimizer.types.metric_source_provider

        out["provider"] = (
            capo_compute_optimizer.types.metric_source_provider.serialize_cbor(
                value["provider"]
            )
        )
    if "provider_arn" in value:
        out["providerArn"] = value["provider_arn"]
    return out


def deserialize_cbor(data: dict) -> MetricSource:
    out: MetricSource = {}  # type: ignore[typeddict-item]
    if data.get("provider") is not None:
        import capo_compute_optimizer.types.metric_source_provider

        out["provider"] = (
            capo_compute_optimizer.types.metric_source_provider.deserialize_cbor(
                data["provider"]
            )
        )
    if data.get("providerArn") is not None:
        out["provider_arn"] = data["providerArn"]
    return out
