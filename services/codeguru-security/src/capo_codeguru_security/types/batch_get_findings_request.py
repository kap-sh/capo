"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#BatchGetFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.finding_identifiers


class BatchGetFindingsRequest(TypedDict, closed=True):
    finding_identifiers: (
        "capo_codeguru_security.types.finding_identifiers.FindingIdentifiers"
    )
    """<p>A list of finding identifiers. Each identifier consists of a <code>scanName</code> and a <code>findingId</code>. You retrieve the <code>findingId</code> when you call <code>GetFindings</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingsRequest) -> dict:
    out: dict = {}
    import capo_codeguru_security.types.finding_identifiers

    out["findingIdentifiers"] = (
        capo_codeguru_security.types.finding_identifiers.serialize_json(
            value["finding_identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetFindingsRequest:
    out: BatchGetFindingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("findingIdentifiers") is not None:
        import capo_codeguru_security.types.finding_identifiers

        out["finding_identifiers"] = (
            capo_codeguru_security.types.finding_identifiers.deserialize_json(
                data["findingIdentifiers"]
            )
        )
    else:
        out["finding_identifiers"] = []
    return out
