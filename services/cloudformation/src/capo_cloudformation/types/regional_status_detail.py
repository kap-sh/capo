"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegionalStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.regional_stages


class RegionalStatusDetail(TypedDict, closed=True):
    stages: NotRequired["capo_cloudformation.types.regional_stages.RegionalStages"]
    """<p>The progress information for the individual stages of the operation in this Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegionalStatusDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stages" in value:
        import capo_cloudformation.types.regional_stages

        capo_cloudformation.types.regional_stages.serialize_query(
            value["stages"], pairs, f"{key_prefix}Stages"
        )


def deserialize_query(el: Element) -> RegionalStatusDetail:
    out: RegionalStatusDetail = {}  # type: ignore[typeddict-item]
    child_stages = el.find("Stages")
    if child_stages is not None:
        import capo_cloudformation.types.regional_stages

        out["stages"] = capo_cloudformation.types.regional_stages.deserialize_query(
            child_stages
        )
    return out
