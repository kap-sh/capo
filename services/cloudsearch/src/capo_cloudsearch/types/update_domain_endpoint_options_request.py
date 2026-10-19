"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateDomainEndpointOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_endpoint_options
    import capo_cloudsearch.types.domain_name


class UpdateDomainEndpointOptionsRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    """<p>A string that represents the name of a domain.</p>"""
    domain_endpoint_options: (
        "capo_cloudsearch.types.domain_endpoint_options.DomainEndpointOptions"
    )
    """<p>Whether to require that all requests to the domain arrive over HTTPS. We recommend Policy-Min-TLS-1-2-2019-07 for TLSSecurityPolicy. For compatibility with older clients, the default is Policy-Min-TLS-1-0-2019-07. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateDomainEndpointOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    import capo_cloudsearch.types.domain_endpoint_options

    capo_cloudsearch.types.domain_endpoint_options.serialize_query(
        value["domain_endpoint_options"], pairs, f"{key_prefix}DomainEndpointOptions"
    )


def deserialize_query(el: Element) -> UpdateDomainEndpointOptionsRequest:
    out: UpdateDomainEndpointOptionsRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_domain_endpoint_options = el.find("DomainEndpointOptions")
    if child_domain_endpoint_options is not None:
        import capo_cloudsearch.types.domain_endpoint_options

        out["domain_endpoint_options"] = (
            capo_cloudsearch.types.domain_endpoint_options.deserialize_query(
                child_domain_endpoint_options
            )
        )
    else:
        raise DeserializationError(
            "UpdateDomainEndpointOptionsRequest.domain_endpoint_options required"
        )
    return out
