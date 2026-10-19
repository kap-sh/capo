"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListDomainsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_summary_list
    import capo_cloudwatchomni.types.next_token


class ListDomainsOutput(TypedDict, closed=True):
    items: "capo_cloudwatchomni.types.domain_summary_list.DomainSummaryList"
    """The list of domain summaries."""
    next_token: NotRequired["capo_cloudwatchomni.types.next_token.NextToken"]
    """A token to retrieve the next page of results, or null if there are no more results."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDomainsOutput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.domain_summary_list

    out["items"] = capo_cloudwatchomni.types.domain_summary_list.serialize_cbor(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDomainsOutput:
    out: ListDomainsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_cloudwatchomni.types.domain_summary_list

        out["items"] = capo_cloudwatchomni.types.domain_summary_list.deserialize_cbor(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
