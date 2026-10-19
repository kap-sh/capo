"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveSourceRetriever``."""

from typing_extensions import TypedDict


class AgenticRetrieveSourceRetriever(TypedDict, closed=True):
    identifier: "str"
    """<p>The unique identifier of the source retriever.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveSourceRetriever) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveSourceRetriever:
    out: AgenticRetrieveSourceRetriever = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
