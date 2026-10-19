"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetAutoMergingPreviewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.long
    import capo_customer_profiles.types.name


class GetAutoMergingPreviewResponse(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    number_of_matches_in_sample: "capo_customer_profiles.types.long.long"
    """<p>The number of match groups in the domain that have been reviewed in this preview dry run.</p>"""
    number_of_profiles_in_sample: "capo_customer_profiles.types.long.long"
    """<p>The number of profiles found in this preview dry run.</p>"""
    number_of_profiles_will_be_merged: "capo_customer_profiles.types.long.long"
    """<p>The number of profiles that would be merged if this wasn't a preview dry run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutoMergingPreviewResponse) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["NumberOfMatchesInSample"] = value.get("number_of_matches_in_sample", 0)
    out["NumberOfProfilesInSample"] = value.get("number_of_profiles_in_sample", 0)
    out["NumberOfProfilesWillBeMerged"] = value.get(
        "number_of_profiles_will_be_merged", 0
    )
    return out


def deserialize_json(data: dict) -> GetAutoMergingPreviewResponse:
    out: GetAutoMergingPreviewResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    if data.get("NumberOfMatchesInSample") is not None:
        out["number_of_matches_in_sample"] = data["NumberOfMatchesInSample"]
    else:
        out["number_of_matches_in_sample"] = 0
    if data.get("NumberOfProfilesInSample") is not None:
        out["number_of_profiles_in_sample"] = data["NumberOfProfilesInSample"]
    else:
        out["number_of_profiles_in_sample"] = 0
    if data.get("NumberOfProfilesWillBeMerged") is not None:
        out["number_of_profiles_will_be_merged"] = data["NumberOfProfilesWillBeMerged"]
    else:
        out["number_of_profiles_will_be_merged"] = 0
    return out
