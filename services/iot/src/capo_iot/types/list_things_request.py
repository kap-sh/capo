"""Generated from Smithy shape ``com.amazonaws.iot#ListThingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.attribute_name
    import capo_iot.types.attribute_value
    import capo_iot.types.next_token
    import capo_iot.types.registry_max_results
    import capo_iot.types.thing_type_name
    import capo_iot.types.use_prefix_attribute_value


class ListThingsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: NotRequired["capo_iot.types.registry_max_results.RegistryMaxResults"]
    """<p>The maximum number of results to return in this operation.</p>"""
    attribute_name: NotRequired["capo_iot.types.attribute_name.AttributeName"]
    """<p>The attribute name used to search for things.</p>"""
    attribute_value: NotRequired["capo_iot.types.attribute_value.AttributeValue"]
    """<p>The attribute value used to search for things.</p>"""
    thing_type_name: NotRequired["capo_iot.types.thing_type_name.ThingTypeName"]
    """<p>The name of the thing type used to search for things.</p>"""
    use_prefix_attribute_value: NotRequired[
        "capo_iot.types.use_prefix_attribute_value.usePrefixAttributeValue"
    ]
    """<p>When <code>true</code>, the action returns the thing resources with attribute values that start with the <code>attributeValue</code> provided.</p> <p>When <code>false</code>, or not present, the action returns only the thing resources with attribute values that match the entire <code>attributeValue</code> provided. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThingsRequest:
    out: ListThingsRequest = {}  # type: ignore[typeddict-item]
    return out
