"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateOutboundConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.connection_alias
    import capo_opensearch.types.connection_mode
    import capo_opensearch.types.connection_properties
    import capo_opensearch.types.domain_information_container


class CreateOutboundConnectionRequest(TypedDict, closed=True):
    local_domain_info: (
        "capo_opensearch.types.domain_information_container.DomainInformationContainer"
    )
    """<p>Name and Region of the source (local) domain.</p>"""
    remote_domain_info: (
        "capo_opensearch.types.domain_information_container.DomainInformationContainer"
    )
    """<p>Name and Region of the destination (remote) domain.</p>"""
    connection_alias: "capo_opensearch.types.connection_alias.ConnectionAlias"
    """<p>Name of the connection.</p>"""
    connection_mode: NotRequired["capo_opensearch.types.connection_mode.ConnectionMode"]
    """<p>The connection mode.</p>"""
    connection_properties: NotRequired[
        "capo_opensearch.types.connection_properties.ConnectionProperties"
    ]
    """<p>The <code>ConnectionProperties</code> for the outbound connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutboundConnectionRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.domain_information_container

    out["LocalDomainInfo"] = (
        capo_opensearch.types.domain_information_container.serialize_json(
            value["local_domain_info"]
        )
    )
    import capo_opensearch.types.domain_information_container

    out["RemoteDomainInfo"] = (
        capo_opensearch.types.domain_information_container.serialize_json(
            value["remote_domain_info"]
        )
    )
    out["ConnectionAlias"] = value["connection_alias"]
    if "connection_mode" in value:
        import capo_opensearch.types.connection_mode

        out["ConnectionMode"] = capo_opensearch.types.connection_mode.serialize_json(
            value["connection_mode"]
        )
    if "connection_properties" in value:
        import capo_opensearch.types.connection_properties

        out["ConnectionProperties"] = (
            capo_opensearch.types.connection_properties.serialize_json(
                value["connection_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateOutboundConnectionRequest:
    out: CreateOutboundConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("LocalDomainInfo") is not None:
        import capo_opensearch.types.domain_information_container

        out["local_domain_info"] = (
            capo_opensearch.types.domain_information_container.deserialize_json(
                data["LocalDomainInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOutboundConnectionRequest.local_domain_info required"
        )
    if data.get("RemoteDomainInfo") is not None:
        import capo_opensearch.types.domain_information_container

        out["remote_domain_info"] = (
            capo_opensearch.types.domain_information_container.deserialize_json(
                data["RemoteDomainInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateOutboundConnectionRequest.remote_domain_info required"
        )
    if data.get("ConnectionAlias") is not None:
        out["connection_alias"] = data["ConnectionAlias"]
    else:
        out["connection_alias"] = ""
    if data.get("ConnectionMode") is not None:
        import capo_opensearch.types.connection_mode

        out["connection_mode"] = capo_opensearch.types.connection_mode.deserialize_json(
            data["ConnectionMode"]
        )
    if data.get("ConnectionProperties") is not None:
        import capo_opensearch.types.connection_properties

        out["connection_properties"] = (
            capo_opensearch.types.connection_properties.deserialize_json(
                data["ConnectionProperties"]
            )
        )
    return out
