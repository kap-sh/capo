"""Generated from Smithy shape ``com.amazonaws.securityhub#CriticalitySource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.criticality_source_type
    import capo_securityhub.types.non_empty_string


class CriticalitySource(TypedDict, closed=True):
    source: NotRequired[
        "capo_securityhub.types.criticality_source_type.CriticalitySourceType"
    ]
    """<p>The source of the criticality.</p>"""
    reason: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The reason the criticality was assigned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CriticalitySource) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_securityhub.types.criticality_source_type

        out["Source"] = capo_securityhub.types.criticality_source_type.serialize_json(
            value["source"]
        )
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> CriticalitySource:
    out: CriticalitySource = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        import capo_securityhub.types.criticality_source_type

        out["source"] = capo_securityhub.types.criticality_source_type.deserialize_json(
            data["Source"]
        )
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out
