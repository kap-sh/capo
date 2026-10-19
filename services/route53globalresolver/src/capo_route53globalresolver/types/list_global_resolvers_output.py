"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListGlobalResolversOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.global_resolvers


class ListGlobalResolversOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    global_resolvers: (
        "capo_route53globalresolver.types.global_resolvers.GlobalResolvers"
    )
    """<p>Paginated list of Global Resolvers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGlobalResolversOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_route53globalresolver.types.global_resolvers

    out["globalResolvers"] = (
        capo_route53globalresolver.types.global_resolvers.serialize_json(
            value["global_resolvers"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListGlobalResolversOutput:
    out: ListGlobalResolversOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("globalResolvers") is not None:
        import capo_route53globalresolver.types.global_resolvers

        out["global_resolvers"] = (
            capo_route53globalresolver.types.global_resolvers.deserialize_json(
                data["globalResolvers"]
            )
        )
    else:
        out["global_resolvers"] = []
    return out
