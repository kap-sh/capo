"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.string


class SNOMEDCTDetails(TypedDict, closed=True):
    edition: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> The edition of SNOMED-CT used. The edition used for the InferSNOMEDCT editions is the US edition. </p>"""
    language: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> The language used in the SNOMED-CT ontology. All Amazon Comprehend Medical operations are US English (en). </p>"""
    version_date: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p> The version date of the SNOMED-CT ontology used. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTDetails) -> dict:
    out: dict = {}
    if "edition" in value:
        out["Edition"] = value["edition"]
    if "language" in value:
        out["Language"] = value["language"]
    if "version_date" in value:
        out["VersionDate"] = value["version_date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SNOMEDCTDetails:
    out: SNOMEDCTDetails = {}  # type: ignore[typeddict-item]
    if data.get("Edition") is not None:
        out["edition"] = data["Edition"]
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("VersionDate") is not None:
        out["version_date"] = data["VersionDate"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SNOMEDCTDetails) -> dict:
    out: dict = {}
    if "edition" in value:
        out["Edition"] = value["edition"]
    if "language" in value:
        out["Language"] = value["language"]
    if "version_date" in value:
        out["VersionDate"] = value["version_date"]
    return out


def deserialize_cbor(data: dict) -> SNOMEDCTDetails:
    out: SNOMEDCTDetails = {}  # type: ignore[typeddict-item]
    if data.get("Edition") is not None:
        out["edition"] = data["Edition"]
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("VersionDate") is not None:
        out["version_date"] = data["VersionDate"]
    return out
