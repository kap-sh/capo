"""Generated from Smithy shape ``com.amazonaws.neptunedata#QueryLanguageVersion``."""

from typing_extensions import TypedDict


class QueryLanguageVersion(TypedDict, closed=True):
    version: "str"
    """<p>The version of the query language.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryLanguageVersion) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> QueryLanguageVersion:
    out: QueryLanguageVersion = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    return out
