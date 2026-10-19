"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name_list


class DescribeDomainsRequest(TypedDict, closed=True):
    domain_names: "capo_opensearch.types.domain_name_list.DomainNameList"
    """<p>Array of OpenSearch Service domain names that you want information about. You must specify at least one domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainsRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.domain_name_list

    out["DomainNames"] = capo_opensearch.types.domain_name_list.serialize_json(
        value["domain_names"]
    )
    return out


def deserialize_json(data: dict) -> DescribeDomainsRequest:
    out: DescribeDomainsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainNames") is not None:
        import capo_opensearch.types.domain_name_list

        out["domain_names"] = capo_opensearch.types.domain_name_list.deserialize_json(
            data["DomainNames"]
        )
    else:
        out["domain_names"] = []
    return out
