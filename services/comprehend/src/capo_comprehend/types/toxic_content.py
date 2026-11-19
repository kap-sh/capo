"""Generated from Smithy shape ``com.amazonaws.comprehend#ToxicContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float
    import capo_comprehend.types.toxic_content_type


class ToxicContent(TypedDict, closed=True):
    name: NotRequired["capo_comprehend.types.toxic_content_type.ToxicContentType"]
    """<p>The name of the toxic content type.</p>"""
    score: NotRequired["capo_comprehend.types.float.Float"]
    """<p> Model confidence in the detected content type. Value range is zero to one, where one is highest confidence.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ToxicContent) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_comprehend.types.toxic_content_type

        out["Name"] = capo_comprehend.types.toxic_content_type.serialize_aws_json_1_1(
            value["name"]
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


def deserialize_aws_json_1_1(data: dict) -> ToxicContent:
    out: ToxicContent = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_comprehend.types.toxic_content_type

        out["name"] = capo_comprehend.types.toxic_content_type.deserialize_aws_json_1_1(
            data["Name"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ToxicContent) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_comprehend.types.toxic_content_type

        out["Name"] = capo_comprehend.types.toxic_content_type.serialize_cbor(
            value["name"]
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_cbor(data: dict) -> ToxicContent:
    out: ToxicContent = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_comprehend.types.toxic_content_type

        out["name"] = capo_comprehend.types.toxic_content_type.deserialize_cbor(
            data["Name"]
        )
    if data.get("Score") is not None:
        out["score"] = float(data["Score"])
    return out
