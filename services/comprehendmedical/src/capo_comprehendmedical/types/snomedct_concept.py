"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTConcept``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.string


class SNOMEDCTConcept(TypedDict, closed=True):
    description: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> The description of the SNOMED-CT concept. </p>"""
    code: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> The numeric ID for the SNOMED-CT concept. </p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p> The level of confidence Amazon Comprehend Medical has that the entity should be linked to the identified SNOMED-CT concept. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTConcept) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "code" in value:
        out["Code"] = value["code"]
    if "score" in value:
        out["Score"] = (
            "NaN"
            if value["score"] != value["score"]
            else "Infinity"
            if value["score"] == float("inf")
            else "-Infinity"
            if value["score"] == float("-inf")
            else value["score"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SNOMEDCTConcept:
    out: SNOMEDCTConcept = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTConcept) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "code" in value:
        out["Code"] = value["code"]
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_cbor(data: dict) -> SNOMEDCTConcept:
    out: SNOMEDCTConcept = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out
