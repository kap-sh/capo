"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTestTrafficHeaderMatchRules``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class ServiceConnectTestTrafficHeaderMatchRules(TypedDict, closed=True):
    exact: "capo_ecs.types.string.String"
    """<p>The exact value that the HTTP header must match for the test traffic routing rule to apply. This provides precise control over which requests are routed to the new service revision during blue/green deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectTestTrafficHeaderMatchRules) -> dict:
    out: dict = {}
    out["exact"] = value["exact"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectTestTrafficHeaderMatchRules:
    out: ServiceConnectTestTrafficHeaderMatchRules = {}  # type: ignore[typeddict-item]
    if data.get("exact") is not None:
        out["exact"] = data["exact"]
    else:
        out["exact"] = ""
    return out
