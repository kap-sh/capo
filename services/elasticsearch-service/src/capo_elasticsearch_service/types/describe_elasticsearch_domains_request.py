"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name_list


class DescribeElasticsearchDomainsRequest(TypedDict, closed=True):
    domain_names: "capo_elasticsearch_service.types.domain_name_list.DomainNameList"
    """<p>The Elasticsearch domains for which you want information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchDomainsRequest) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.domain_name_list

    out["DomainNames"] = (
        capo_elasticsearch_service.types.domain_name_list.serialize_json(
            value["domain_names"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchDomainsRequest:
    out: DescribeElasticsearchDomainsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainNames") is not None:
        import capo_elasticsearch_service.types.domain_name_list

        out["domain_names"] = (
            capo_elasticsearch_service.types.domain_name_list.deserialize_json(
                data["DomainNames"]
            )
        )
    else:
        out["domain_names"] = []
    return out
