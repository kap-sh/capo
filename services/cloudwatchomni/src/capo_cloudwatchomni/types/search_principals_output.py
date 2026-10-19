"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#SearchPrincipalsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.principal_search_result_list
    import capo_cloudwatchomni.types.search_principals_next_token


class SearchPrincipalsOutput(TypedDict, closed=True):
    results: "capo_cloudwatchomni.types.principal_search_result_list.PrincipalSearchResultList"
    """The list of matching principals."""
    next_token: NotRequired[
        "capo_cloudwatchomni.types.search_principals_next_token.SearchPrincipalsNextToken"
    ]
    """A token to retrieve the next page of results, or null if there are no more results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchPrincipalsOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.principal_search_result_list

    out["results"] = (
        capo_cloudwatchomni.types.principal_search_result_list.serialize_cbor(
            value["results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> SearchPrincipalsOutput:
    out: SearchPrincipalsOutput = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_cloudwatchomni.types.principal_search_result_list

        out["results"] = (
            capo_cloudwatchomni.types.principal_search_result_list.deserialize_cbor(
                data["results"]
            )
        )
    else:
        out["results"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
