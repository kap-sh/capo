"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ConnectionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.idle_timeout


class ConnectionSettings(TypedDict, closed=True):
    idle_timeout: "capo_elastic_load_balancing.types.idle_timeout.IdleTimeout"
    """<p>The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConnectionSettings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}IdleTimeout", str(value["idle_timeout"])))


def deserialize_query(el: Element) -> ConnectionSettings:
    out: ConnectionSettings = {}  # type: ignore[typeddict-item]
    child_idle_timeout = el.find("IdleTimeout")
    if child_idle_timeout is not None:
        out["idle_timeout"] = int(child_idle_timeout.text or "")
    else:
        out["idle_timeout"] = 0
    return out
