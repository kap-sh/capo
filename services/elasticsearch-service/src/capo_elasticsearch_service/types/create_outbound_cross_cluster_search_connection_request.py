"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CreateOutboundCrossClusterSearchConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.connection_alias
    import capo_elasticsearch_service.types.domain_information


class CreateOutboundCrossClusterSearchConnectionRequest(TypedDict, closed=True):
    source_domain_info: (
        "capo_elasticsearch_service.types.domain_information.DomainInformation"
    )
    """<p>Specifies the <code><a>DomainInformation</a></code> for the source Elasticsearch domain.</p>"""
    destination_domain_info: (
        "capo_elasticsearch_service.types.domain_information.DomainInformation"
    )
    """<p>Specifies the <code><a>DomainInformation</a></code> for the destination Elasticsearch domain.</p>"""
    connection_alias: (
        "capo_elasticsearch_service.types.connection_alias.ConnectionAlias"
    )
    """<p>Specifies the connection alias that will be used by the customer for this connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutboundCrossClusterSearchConnectionRequest) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.domain_information

    out["SourceDomainInfo"] = (
        capo_elasticsearch_service.types.domain_information.serialize_json(
            value["source_domain_info"]
        )
    )
    import capo_elasticsearch_service.types.domain_information

    out["DestinationDomainInfo"] = (
        capo_elasticsearch_service.types.domain_information.serialize_json(
            value["destination_domain_info"]
        )
    )
    out["ConnectionAlias"] = value["connection_alias"]
    return out


def deserialize_json(data: dict) -> CreateOutboundCrossClusterSearchConnectionRequest:
    out: CreateOutboundCrossClusterSearchConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceDomainInfo") is not None:
        import capo_elasticsearch_service.types.domain_information

        out["source_domain_info"] = (
            capo_elasticsearch_service.types.domain_information.deserialize_json(
                data["SourceDomainInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOutboundCrossClusterSearchConnectionRequest.source_domain_info required"
        )
    if data.get("DestinationDomainInfo") is not None:
        import capo_elasticsearch_service.types.domain_information

        out["destination_domain_info"] = (
            capo_elasticsearch_service.types.domain_information.deserialize_json(
                data["DestinationDomainInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOutboundCrossClusterSearchConnectionRequest.destination_domain_info required"
        )
    if data.get("ConnectionAlias") is not None:
        out["connection_alias"] = data["ConnectionAlias"]
    else:
        out["connection_alias"] = ""
    return out
