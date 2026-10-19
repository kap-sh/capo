"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutStorageTierPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.storage_tier


class PutStorageTierPolicyRequest(TypedDict, closed=True):
    storage_tier: "capo_cloudwatch_logs.types.storage_tier.StorageTier"
    """<p>The storage tier to set for the account. Use <code>INTELLIGENT_TIERING</code> to automatically optimize storage costs by moving log data to the appropriate tier based on access frequency.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutStorageTierPolicyRequest) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.storage_tier

    out["storageTier"] = capo_cloudwatch_logs.types.storage_tier.serialize_aws_json_1_1(
        value["storage_tier"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutStorageTierPolicyRequest:
    out: PutStorageTierPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("storageTier") is not None:
        import capo_cloudwatch_logs.types.storage_tier

        out["storage_tier"] = (
            capo_cloudwatch_logs.types.storage_tier.deserialize_aws_json_1_1(
                data["storageTier"]
            )
        )
    else:
        import typing

        out["storage_tier"] = typing.cast(
            "capo_cloudwatch_logs.types.storage_tier.StorageTier", ""
        )
    return out
