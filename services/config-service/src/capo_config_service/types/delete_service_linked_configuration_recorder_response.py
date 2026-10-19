"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteServiceLinkedConfigurationRecorderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.amazon_resource_name
    import capo_config_service.types.recorder_name


class DeleteServiceLinkedConfigurationRecorderResponse(TypedDict, closed=True):
    arn: "capo_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the specified configuration recorder.</p>"""
    name: "capo_config_service.types.recorder_name.RecorderName"
    """<p>The name of the specified configuration recorder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeleteServiceLinkedConfigurationRecorderResponse,
) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeleteServiceLinkedConfigurationRecorderResponse:
    out: DeleteServiceLinkedConfigurationRecorderResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
