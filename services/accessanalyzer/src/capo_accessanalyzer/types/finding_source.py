"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.finding_source_detail
    import capo_accessanalyzer.types.finding_source_type


class FindingSource(TypedDict, closed=True):
    type: "capo_accessanalyzer.types.finding_source_type.FindingSourceType"
    """<p>Indicates the type of access that generated the finding.</p>"""
    detail: NotRequired[
        "capo_accessanalyzer.types.finding_source_detail.FindingSourceDetail"
    ]
    """<p>Includes details about how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSource) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "detail" in value:
        import capo_accessanalyzer.types.finding_source_detail

        out["detail"] = capo_accessanalyzer.types.finding_source_detail.serialize_json(
            value["detail"]
        )
    return out


def deserialize_json(data: dict) -> FindingSource:
    out: FindingSource = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("detail") is not None:
        import capo_accessanalyzer.types.finding_source_detail

        out["detail"] = (
            capo_accessanalyzer.types.finding_source_detail.deserialize_json(
                data["detail"]
            )
        )
    return out
