"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RedirectActionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.redirect_action_host
    import capo_elastic_load_balancing_v2.types.redirect_action_path
    import capo_elastic_load_balancing_v2.types.redirect_action_port
    import capo_elastic_load_balancing_v2.types.redirect_action_protocol
    import capo_elastic_load_balancing_v2.types.redirect_action_query
    import capo_elastic_load_balancing_v2.types.redirect_action_status_code_enum


class RedirectActionConfig(TypedDict, closed=True):
    protocol: NotRequired[
        "capo_elastic_load_balancing_v2.types.redirect_action_protocol.RedirectActionProtocol"
    ]
    """<p>The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You can't redirect HTTPS to HTTP.</p>"""
    port: NotRequired[
        "capo_elastic_load_balancing_v2.types.redirect_action_port.RedirectActionPort"
    ]
    """<p>The port. You can specify a value from 1 to 65535 or #{port}.</p>"""
    host: NotRequired[
        "capo_elastic_load_balancing_v2.types.redirect_action_host.RedirectActionHost"
    ]
    """<p>The hostname. This component is not percent-encoded. The hostname can contain #{host}.</p>"""
    path: NotRequired[
        "capo_elastic_load_balancing_v2.types.redirect_action_path.RedirectActionPath"
    ]
    """<p>The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.</p>"""
    query: NotRequired[
        "capo_elastic_load_balancing_v2.types.redirect_action_query.RedirectActionQuery"
    ]
    """<p>The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?", as it is automatically added. You can specify any of the reserved keywords.</p>"""
    status_code: NotRequired[
        "capo_elastic_load_balancing_v2.types.redirect_action_status_code_enum.RedirectActionStatusCodeEnum"
    ]
    """<p>The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RedirectActionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "protocol" in value:
        pairs.append((f"{key_prefix}Protocol", str(value["protocol"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "host" in value:
        pairs.append((f"{key_prefix}Host", str(value["host"])))
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    if "query" in value:
        pairs.append((f"{key_prefix}Query", str(value["query"])))
    if "status_code" in value:
        import capo_elastic_load_balancing_v2.types.redirect_action_status_code_enum

        capo_elastic_load_balancing_v2.types.redirect_action_status_code_enum.serialize_query(
            value["status_code"], pairs, f"{key_prefix}StatusCode"
        )


def deserialize_query(el: Element) -> RedirectActionConfig:
    out: RedirectActionConfig = {}  # type: ignore[typeddict-item]
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = str(child_port.text or "")
    child_host = el.find("Host")
    if child_host is not None:
        out["host"] = str(child_host.text or "")
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_query = el.find("Query")
    if child_query is not None:
        out["query"] = str(child_query.text or "")
    child_status_code = el.find("StatusCode")
    if child_status_code is not None:
        import capo_elastic_load_balancing_v2.types.redirect_action_status_code_enum

        out["status_code"] = (
            capo_elastic_load_balancing_v2.types.redirect_action_status_code_enum.deserialize_query(
                child_status_code
            )
        )
    return out
