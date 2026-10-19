"""Generated from Smithy shape ``com.amazonaws.b2bi#GenerateMappingResponse``."""

from typing_extensions import NotRequired, TypedDict


class GenerateMappingResponse(TypedDict, closed=True):
    mapping_template: "str"
    """<p>Returns a mapping template based on your inputs.</p>"""
    mapping_accuracy: NotRequired["float"]
    """<p>Returns a percentage that estimates the accuracy of the generated mapping.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GenerateMappingResponse) -> dict:
    out: dict = {}
    out["mappingTemplate"] = value["mapping_template"]
    if "mapping_accuracy" in value:
        out["mappingAccuracy"] = (
            "NaN"
            if value["mapping_accuracy"] != value["mapping_accuracy"]
            else "Infinity"
            if value["mapping_accuracy"] == float("inf")
            else "-Infinity"
            if value["mapping_accuracy"] == float("-inf")
            else value["mapping_accuracy"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GenerateMappingResponse:
    out: GenerateMappingResponse = {}  # type: ignore[typeddict-item]
    if data.get("mappingTemplate") is not None:
        out["mapping_template"] = data["mappingTemplate"]
    else:
        out["mapping_template"] = ""
    if data.get("mappingAccuracy") is not None:
        out["mapping_accuracy"] = float(data["mappingAccuracy"])
    return out
