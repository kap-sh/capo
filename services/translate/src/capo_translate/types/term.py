"""Generated from Smithy shape ``com.amazonaws.translate#Term``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.string


class Term(TypedDict, closed=True):
    source_text: NotRequired["capo_translate.types.string.String"]
    """<p>The source text of the term being translated by the custom terminology.</p>"""
    target_text: NotRequired["capo_translate.types.string.String"]
    """<p>The target text of the term being translated by the custom terminology.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Term) -> dict:
    out: dict = {}
    if "source_text" in value:
        out["SourceText"] = value["source_text"]
    if "target_text" in value:
        out["TargetText"] = value["target_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Term:
    out: Term = {}  # type: ignore[typeddict-item]
    if data.get("SourceText") is not None:
        out["source_text"] = data["SourceText"]
    if data.get("TargetText") is not None:
        out["target_text"] = data["TargetText"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Term) -> dict:
    out: dict = {}
    if "source_text" in value:
        out["SourceText"] = value["source_text"]
    if "target_text" in value:
        out["TargetText"] = value["target_text"]
    return out


def deserialize_cbor(data: dict) -> Term:
    out: Term = {}  # type: ignore[typeddict-item]
    if data.get("SourceText") is not None:
        out["source_text"] = data["SourceText"]
    if data.get("TargetText") is not None:
        out["target_text"] = data["TargetText"]
    return out
