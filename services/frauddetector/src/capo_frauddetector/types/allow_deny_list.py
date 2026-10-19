"""Generated from Smithy shape ``com.amazonaws.frauddetector#AllowDenyList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.no_dash_identifier
    import capo_frauddetector.types.time
    import capo_frauddetector.types.variable_type


class AllowDenyList(TypedDict, closed=True):
    name: "capo_frauddetector.types.no_dash_identifier.noDashIdentifier"
    """<p> The name of the list. </p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p> The description of the list. </p>"""
    variable_type: NotRequired["capo_frauddetector.types.variable_type.variableType"]
    """<p> The variable type of the list. </p>"""
    created_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p> The time the list was created. </p>"""
    updated_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p> The time the list was last updated. </p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p> The ARN of the list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowDenyList) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "updated_time" in value:
        out["updatedTime"] = value["updated_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AllowDenyList:
    out: AllowDenyList = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("variableType") is not None:
        out["variable_type"] = data["variableType"]
    if data.get("createdTime") is not None:
        out["created_time"] = data["createdTime"]
    if data.get("updatedTime") is not None:
        out["updated_time"] = data["updatedTime"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
