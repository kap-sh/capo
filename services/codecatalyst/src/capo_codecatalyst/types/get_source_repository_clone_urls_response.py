"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetSourceRepositoryCloneUrlsResponse``."""

from typing_extensions import TypedDict


class GetSourceRepositoryCloneUrlsResponse(TypedDict, closed=True):
    https: "str"
    """<p>The HTTPS URL to use when cloning the source repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSourceRepositoryCloneUrlsResponse) -> dict:
    out: dict = {}
    out["https"] = value["https"]
    return out


def deserialize_json(data: dict) -> GetSourceRepositoryCloneUrlsResponse:
    out: GetSourceRepositoryCloneUrlsResponse = {}  # type: ignore[typeddict-item]
    if data.get("https") is not None:
        out["https"] = data["https"]
    else:
        out["https"] = ""
    return out
