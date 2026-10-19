"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#RetentionProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.magnetic_store_retention_period_in_days
    import capo_timestream_write.types.memory_store_retention_period_in_hours


class RetentionProperties(TypedDict, closed=True):
    memory_store_retention_period_in_hours: "capo_timestream_write.types.memory_store_retention_period_in_hours.MemoryStoreRetentionPeriodInHours"
    """<p>The duration for which data must be stored in the memory store. </p>"""
    magnetic_store_retention_period_in_days: "capo_timestream_write.types.magnetic_store_retention_period_in_days.MagneticStoreRetentionPeriodInDays"
    """<p>The duration for which data must be stored in the magnetic store. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RetentionProperties) -> dict:
    out: dict = {}
    out["MemoryStoreRetentionPeriodInHours"] = value[
        "memory_store_retention_period_in_hours"
    ]
    out["MagneticStoreRetentionPeriodInDays"] = value[
        "magnetic_store_retention_period_in_days"
    ]
    return out


def deserialize_aws_json_1_0(data: dict) -> RetentionProperties:
    out: RetentionProperties = {}  # type: ignore[typeddict-item]
    if data.get("MemoryStoreRetentionPeriodInHours") is not None:
        out["memory_store_retention_period_in_hours"] = data[
            "MemoryStoreRetentionPeriodInHours"
        ]
    else:
        out["memory_store_retention_period_in_hours"] = 0
    if data.get("MagneticStoreRetentionPeriodInDays") is not None:
        out["magnetic_store_retention_period_in_days"] = data[
            "MagneticStoreRetentionPeriodInDays"
        ]
    else:
        out["magnetic_store_retention_period_in_days"] = 0
    return out
