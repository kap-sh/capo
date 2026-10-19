"""Generated from Smithy shape ``com.amazonaws.odb#ListSystemVersionsInput``."""

from typing_extensions import NotRequired, TypedDict


class ListSystemVersionsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    gi_version: "str"
    """<p>The software version of the Exadata Grid Infrastructure (GI).</p>"""
    shape: "str"
    """<p>The Exadata hardware system model.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSystemVersionsInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["giVersion"] = value["gi_version"]
    out["shape"] = value["shape"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSystemVersionsInput:
    out: ListSystemVersionsInput = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("giVersion") is not None:
        out["gi_version"] = data["giVersion"]
    else:
        out["gi_version"] = ""
    if data.get("shape") is not None:
        out["shape"] = data["shape"]
    else:
        out["shape"] = ""
    return out
