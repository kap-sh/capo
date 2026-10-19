"""Generated from Smithy shape ``com.amazonaws.configservice#RetentionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.retention_configuration_name
    import capo_config_service.types.retention_period_in_days


class RetentionConfiguration(TypedDict, closed=True):
    name: "capo_config_service.types.retention_configuration_name.RetentionConfigurationName"
    """<p>The name of the retention configuration object.</p>"""
    retention_period_in_days: (
        "capo_config_service.types.retention_period_in_days.RetentionPeriodInDays"
    )
    """<p>Number of days Config stores your historical information.</p> <note> <p>Currently, only applicable to the configuration item history.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetentionConfiguration) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RetentionPeriodInDays"] = value["retention_period_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetentionConfiguration:
    out: RetentionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RetentionPeriodInDays") is not None:
        out["retention_period_in_days"] = data["RetentionPeriodInDays"]
    else:
        out["retention_period_in_days"] = 0
    return out
