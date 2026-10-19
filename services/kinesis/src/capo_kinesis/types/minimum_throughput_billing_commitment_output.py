"""Generated from Smithy shape ``com.amazonaws.kinesis#MinimumThroughputBillingCommitmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.minimum_throughput_billing_commitment_output_status
    import capo_kinesis.types.timestamp


class MinimumThroughputBillingCommitmentOutput(TypedDict, closed=True):
    status: "capo_kinesis.types.minimum_throughput_billing_commitment_output_status.MinimumThroughputBillingCommitmentOutputStatus"
    """<p>The current status of the minimum throughput billing commitment.</p>"""
    started_at: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The timestamp when the commitment was started.</p>"""
    ended_at: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The timestamp when the commitment was ended.</p>"""
    earliest_allowed_end_at: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The earliest timestamp when the commitment can be ended.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MinimumThroughputBillingCommitmentOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.minimum_throughput_billing_commitment_output_status

    out["Status"] = (
        capo_kinesis.types.minimum_throughput_billing_commitment_output_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "started_at" in value:
        import capo_kinesis.types.timestamp

        out["StartedAt"] = capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_kinesis.types.timestamp

        out["EndedAt"] = capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["ended_at"]
        )
    if "earliest_allowed_end_at" in value:
        import capo_kinesis.types.timestamp

        out["EarliestAllowedEndAt"] = (
            capo_kinesis.types.timestamp.serialize_aws_json_1_1(
                value["earliest_allowed_end_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MinimumThroughputBillingCommitmentOutput:
    out: MinimumThroughputBillingCommitmentOutput = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_kinesis.types.minimum_throughput_billing_commitment_output_status

        out["status"] = (
            capo_kinesis.types.minimum_throughput_billing_commitment_output_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_kinesis.types.minimum_throughput_billing_commitment_output_status.MinimumThroughputBillingCommitmentOutputStatus",
            "",
        )
    if data.get("StartedAt") is not None:
        import capo_kinesis.types.timestamp

        out["started_at"] = capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
            data["StartedAt"]
        )
    if data.get("EndedAt") is not None:
        import capo_kinesis.types.timestamp

        out["ended_at"] = capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
            data["EndedAt"]
        )
    if data.get("EarliestAllowedEndAt") is not None:
        import capo_kinesis.types.timestamp

        out["earliest_allowed_end_at"] = (
            capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["EarliestAllowedEndAt"]
            )
        )
    return out
