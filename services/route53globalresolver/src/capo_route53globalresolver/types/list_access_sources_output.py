"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListAccessSourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.access_sources


class ListAccessSourcesOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    access_sources: "capo_route53globalresolver.types.access_sources.AccessSources"
    """<p>An array containing information about the access sources, such as the ID, CIDR etc.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessSourcesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_route53globalresolver.types.access_sources

    out["accessSources"] = (
        capo_route53globalresolver.types.access_sources.serialize_json(
            value["access_sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAccessSourcesOutput:
    out: ListAccessSourcesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("accessSources") is not None:
        import capo_route53globalresolver.types.access_sources

        out["access_sources"] = (
            capo_route53globalresolver.types.access_sources.deserialize_json(
                data["accessSources"]
            )
        )
    else:
        out["access_sources"] = []
    return out
