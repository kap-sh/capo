"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormConcept``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.string


class RxNormConcept(TypedDict, closed=True):
    description: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>The description of the RxNorm concept.</p>"""
    code: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>RxNorm concept ID, also known as the RxCUI.</p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has that the entity is accurately linked to the reported RxNorm concept.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormConcept) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> RxNormConcept:
    out: RxNormConcept = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RxNormConcept) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "code" in value:
        out["Code"] = value["code"]
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_cbor(data: dict) -> RxNormConcept:
    out: RxNormConcept = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out
