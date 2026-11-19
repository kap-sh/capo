"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMTrait``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.float
    import capo_comprehendmedical.types.icd10_cm_trait_name


class ICD10CMTrait(TypedDict, closed=True):
    name: NotRequired[
        "capo_comprehendmedical.types.icd10_cm_trait_name.ICD10CMTraitName"
    ]
    """<p>Provides a name or contextual description about the trait.</p>"""
    score: NotRequired["capo_comprehendmedical.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend Medical has that the segment of text is correctly recognized as a trait.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMTrait) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_comprehendmedical.types.icd10_cm_trait_name

        out["Name"] = (
            capo_comprehendmedical.types.icd10_cm_trait_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> ICD10CMTrait:
    out: ICD10CMTrait = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_comprehendmedical.types.icd10_cm_trait_name

        out["name"] = (
            capo_comprehendmedical.types.icd10_cm_trait_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ICD10CMTrait) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_comprehendmedical.types.icd10_cm_trait_name

        out["Name"] = capo_comprehendmedical.types.icd10_cm_trait_name.serialize_cbor(
            value["name"]
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_cbor(data: dict) -> ICD10CMTrait:
    out: ICD10CMTrait = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_comprehendmedical.types.icd10_cm_trait_name

        out["name"] = capo_comprehendmedical.types.icd10_cm_trait_name.deserialize_cbor(
            data["Name"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out
