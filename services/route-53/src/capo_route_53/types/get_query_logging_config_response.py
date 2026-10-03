"""Generated from Smithy shape ``com.amazonaws.route53#GetQueryLoggingConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.query_logging_config


class GetQueryLoggingConfigResponse(TypedDict, closed=True):
    query_logging_config: "capo_route_53.types.query_logging_config.QueryLoggingConfig"
    """<p>A complex type that contains information about the query logging configuration that you specified in a <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetQueryLoggingConfig.html">GetQueryLoggingConfig</a> request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetQueryLoggingConfigResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.query_logging_config

    capo_route_53.types.query_logging_config.serialize_xml(
        value["query_logging_config"], el, "QueryLoggingConfig"
    )


def deserialize_xml(el: Element) -> GetQueryLoggingConfigResponse:
    out: GetQueryLoggingConfigResponse = {}  # type: ignore[typeddict-item]
    child_query_logging_config = el.find("QueryLoggingConfig")
    if child_query_logging_config is not None:
        import capo_route_53.types.query_logging_config

        out["query_logging_config"] = (
            capo_route_53.types.query_logging_config.deserialize_xml(
                child_query_logging_config
            )
        )
    else:
        raise DeserializationError(
            "GetQueryLoggingConfigResponse.query_logging_config required"
        )
    return out
