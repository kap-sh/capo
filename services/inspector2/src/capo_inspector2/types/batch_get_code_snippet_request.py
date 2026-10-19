"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetCodeSnippetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.finding_arns


class BatchGetCodeSnippetRequest(TypedDict, closed=True):
    finding_arns: "capo_inspector2.types.finding_arns.FindingArns"
    """<p>An array of finding ARNs for the findings you want to retrieve code snippets from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCodeSnippetRequest) -> dict:
    out: dict = {}
    import capo_inspector2.types.finding_arns

    out["findingArns"] = capo_inspector2.types.finding_arns.serialize_json(
        value["finding_arns"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetCodeSnippetRequest:
    out: BatchGetCodeSnippetRequest = {}  # type: ignore[typeddict-item]
    if data.get("findingArns") is not None:
        import capo_inspector2.types.finding_arns

        out["finding_arns"] = capo_inspector2.types.finding_arns.deserialize_json(
            data["findingArns"]
        )
    else:
        out["finding_arns"] = []
    return out
