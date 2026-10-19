"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveCitationReference``."""

from typing_extensions import TypedDict


class AgenticRetrieveCitationReference(TypedDict, closed=True):
    result_index: "int"
    """<p>Index into the results array on the same event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveCitationReference) -> dict:
    out: dict = {}
    out["resultIndex"] = value["result_index"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveCitationReference:
    out: AgenticRetrieveCitationReference = {}  # type: ignore[typeddict-item]
    if data.get("resultIndex") is not None:
        out["result_index"] = data["resultIndex"]
    else:
        out["result_index"] = 0
    return out
