"""Generated from Smithy shape ``com.amazonaws.connecthealth#ListDomainsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_summary_list


class ListDomainsOutput(TypedDict, closed=True):
    domains: "capo_connecthealth.types.domain_summary_list.DomainSummaryList"
    """<p>List of Domains.</p>"""
    next_token: NotRequired["str"]
    """<p>Token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsOutput) -> dict:
    out: dict = {}
    import capo_connecthealth.types.domain_summary_list

    out["domains"] = capo_connecthealth.types.domain_summary_list.serialize_json(
        value["domains"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsOutput:
    out: ListDomainsOutput = {}  # type: ignore[typeddict-item]
    if data.get("domains") is not None:
        import capo_connecthealth.types.domain_summary_list

        out["domains"] = capo_connecthealth.types.domain_summary_list.deserialize_json(
            data["domains"]
        )
    else:
        out["domains"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
