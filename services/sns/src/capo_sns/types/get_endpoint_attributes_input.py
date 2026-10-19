"""Generated from Smithy shape ``com.amazonaws.sns#GetEndpointAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.string


class GetEndpointAttributesInput(TypedDict, closed=True):
    endpoint_arn: "capo_sns.types.string.String"
    """<p> <code>EndpointArn</code> for <code>GetEndpointAttributes</code> input.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetEndpointAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EndpointArn", str(value["endpoint_arn"])))


def deserialize_query(el: Element) -> GetEndpointAttributesInput:
    out: GetEndpointAttributesInput = {}  # type: ignore[typeddict-item]
    child_endpoint_arn = el.find("EndpointArn")
    if child_endpoint_arn is not None:
        out["endpoint_arn"] = str(child_endpoint_arn.text or "")
    else:
        out["endpoint_arn"] = ""
    return out
