"""Generated from Smithy shape ``com.amazonaws.inspector2#SearchVulnerabilitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.next_token
    import capo_inspector2.types.vulnerabilities


class SearchVulnerabilitiesResponse(TypedDict, closed=True):
    vulnerabilities: "capo_inspector2.types.vulnerabilities.Vulnerabilities"
    """<p>Details about the listed vulnerability.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchVulnerabilitiesResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.vulnerabilities

    out["vulnerabilities"] = capo_inspector2.types.vulnerabilities.serialize_json(
        value["vulnerabilities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchVulnerabilitiesResponse:
    out: SearchVulnerabilitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("vulnerabilities") is not None:
        import capo_inspector2.types.vulnerabilities

        out["vulnerabilities"] = capo_inspector2.types.vulnerabilities.deserialize_json(
            data["vulnerabilities"]
        )
    else:
        out["vulnerabilities"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
