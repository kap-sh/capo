"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSSavingsEstimationMode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ebs_savings_estimation_mode_source


class EBSSavingsEstimationMode(TypedDict, closed=True):
    source: NotRequired[
        "capo_compute_optimizer.types.ebs_savings_estimation_mode_source.EBSSavingsEstimationModeSource"
    ]
    """<p> Describes the source for calculating the savings opportunity for Amazon EBS volumes. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSSavingsEstimationMode) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_compute_optimizer.types.ebs_savings_estimation_mode_source

        out["source"] = (
            capo_compute_optimizer.types.ebs_savings_estimation_mode_source.serialize_aws_json_1_0(
                value["source"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EBSSavingsEstimationMode:
    out: EBSSavingsEstimationMode = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_compute_optimizer.types.ebs_savings_estimation_mode_source

        out["source"] = (
            capo_compute_optimizer.types.ebs_savings_estimation_mode_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EBSSavingsEstimationMode) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_compute_optimizer.types.ebs_savings_estimation_mode_source

        out["source"] = (
            capo_compute_optimizer.types.ebs_savings_estimation_mode_source.serialize_cbor(
                value["source"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> EBSSavingsEstimationMode:
    out: EBSSavingsEstimationMode = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_compute_optimizer.types.ebs_savings_estimation_mode_source

        out["source"] = (
            capo_compute_optimizer.types.ebs_savings_estimation_mode_source.deserialize_cbor(
                data["source"]
            )
        )
    return out
