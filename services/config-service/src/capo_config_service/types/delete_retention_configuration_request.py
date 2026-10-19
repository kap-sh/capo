"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteRetentionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.retention_configuration_name


class DeleteRetentionConfigurationRequest(TypedDict, closed=True):
    retention_configuration_name: "capo_config_service.types.retention_configuration_name.RetentionConfigurationName"
    """<p>The name of the retention configuration to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRetentionConfigurationRequest) -> dict:
    out: dict = {}
    out["RetentionConfigurationName"] = value["retention_configuration_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRetentionConfigurationRequest:
    out: DeleteRetentionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("RetentionConfigurationName") is not None:
        out["retention_configuration_name"] = data["RetentionConfigurationName"]
    else:
        out["retention_configuration_name"] = ""
    return out
