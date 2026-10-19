"""Generated from Smithy shape ``com.amazonaws.networkfirewall#PublishMetricAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.dimensions


class PublishMetricAction(TypedDict, closed=True):
    dimensions: "capo_network_firewall.types.dimensions.Dimensions"
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublishMetricAction) -> dict:
    out: dict = {}
    import capo_network_firewall.types.dimensions

    out["Dimensions"] = capo_network_firewall.types.dimensions.serialize_aws_json_1_0(
        value["dimensions"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PublishMetricAction:
    out: PublishMetricAction = {}  # type: ignore[typeddict-item]
    if data.get("Dimensions") is not None:
        import capo_network_firewall.types.dimensions

        out["dimensions"] = (
            capo_network_firewall.types.dimensions.deserialize_aws_json_1_0(
                data["Dimensions"]
            )
        )
    else:
        out["dimensions"] = []
    return out
