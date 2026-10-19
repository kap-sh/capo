"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DataArtifact``."""

from typing_extensions import NotRequired, TypedDict


class DataArtifact(TypedDict, closed=True):
    description: NotRequired["str"]
    """<p>A description of the data artifact.</p>"""
    resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the data artifact.</p>"""
    resource_type: "str"
    """<p>The type of the data artifact resource.</p>"""
    data_classification: "str"
    """<p>The classification of sensitive data contained in the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataArtifact) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    out["resourceType"] = value["resource_type"]
    out["dataClassification"] = value["data_classification"]
    return out


def deserialize_json(data: dict) -> DataArtifact:
    out: DataArtifact = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("dataClassification") is not None:
        out["data_classification"] = data["dataClassification"]
    else:
        out["data_classification"] = ""
    return out
