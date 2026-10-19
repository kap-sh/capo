"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemEventIncludedData``."""

from typing_extensions import TypedDict


class RelatedItemEventIncludedData(TypedDict, closed=True):
    include_content: "bool"
    """<p>Details of what related item data is published through the case event stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemEventIncludedData) -> dict:
    out: dict = {}
    out["includeContent"] = value["include_content"]
    return out


def deserialize_json(data: dict) -> RelatedItemEventIncludedData:
    out: RelatedItemEventIncludedData = {}  # type: ignore[typeddict-item]
    if data.get("includeContent") is not None:
        out["include_content"] = data["includeContent"]
    else:
        out["include_content"] = False
    return out
