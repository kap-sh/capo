"""Generated from Smithy shape ``com.amazonaws.configservice#PutRetentionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.retention_period_in_days


class PutRetentionConfigurationRequest(TypedDict, closed=True):
    retention_period_in_days: (
        "capo_config_service.types.retention_period_in_days.RetentionPeriodInDays"
    )
    """<p>Number of days Config stores your historical information.</p> <note> <p>Currently, only applicable to the configuration item history.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRetentionConfigurationRequest) -> dict:
    out: dict = {}
    out["RetentionPeriodInDays"] = value["retention_period_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRetentionConfigurationRequest:
    out: PutRetentionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("RetentionPeriodInDays") is not None:
        out["retention_period_in_days"] = data["RetentionPeriodInDays"]
    else:
        out["retention_period_in_days"] = 0
    return out
