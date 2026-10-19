"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UpdateActiveModelVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.model_version


class UpdateActiveModelVersionRequest(TypedDict, closed=True):
    model_name: "capo_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the machine learning model for which the active model version is being set.</p>"""
    model_version: "capo_lookoutequipment.types.model_version.ModelVersion"
    """<p>The version of the machine learning model for which the active model version is being set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateActiveModelVersionRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateActiveModelVersionRequest:
    out: UpdateActiveModelVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ModelName") is not None:
        out["model_name"] = data["ModelName"]
    else:
        out["model_name"] = ""
    if data.get("ModelVersion") is not None:
        out["model_version"] = data["ModelVersion"]
    else:
        out["model_version"] = 0
    return out
