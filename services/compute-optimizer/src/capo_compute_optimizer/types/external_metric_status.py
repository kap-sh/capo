"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExternalMetricStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.external_metric_status_code
    import capo_compute_optimizer.types.external_metric_status_reason


class ExternalMetricStatus(TypedDict, closed=True):
    status_code: NotRequired[
        "capo_compute_optimizer.types.external_metric_status_code.ExternalMetricStatusCode"
    ]
    """<p> The status code for Compute Optimizer's integration with an external metrics provider. </p>"""
    status_reason: NotRequired[
        "capo_compute_optimizer.types.external_metric_status_reason.ExternalMetricStatusReason"
    ]
    """<p> The reason for Compute Optimizer's integration status with your external metric provider. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExternalMetricStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import capo_compute_optimizer.types.external_metric_status_code

        out["statusCode"] = (
            capo_compute_optimizer.types.external_metric_status_code.serialize_aws_json_1_0(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExternalMetricStatus:
    out: ExternalMetricStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        import capo_compute_optimizer.types.external_metric_status_code

        out["status_code"] = (
            capo_compute_optimizer.types.external_metric_status_code.deserialize_aws_json_1_0(
                data["statusCode"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExternalMetricStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import capo_compute_optimizer.types.external_metric_status_code

        out["statusCode"] = (
            capo_compute_optimizer.types.external_metric_status_code.serialize_cbor(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_cbor(data: dict) -> ExternalMetricStatus:
    out: ExternalMetricStatus = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        import capo_compute_optimizer.types.external_metric_status_code

        out["status_code"] = (
            capo_compute_optimizer.types.external_metric_status_code.deserialize_cbor(
                data["statusCode"]
            )
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
