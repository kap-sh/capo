"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegionalStatusDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.region
    import capo_cloudformation.types.regional_status_detail

RegionalStatusDetails: TypeAlias = dict[
    "capo_cloudformation.types.region.Region",
    "capo_cloudformation.types.regional_status_detail.RegionalStatusDetail",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: RegionalStatusDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.regional_status_detail

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.key", str(key)))
        capo_cloudformation.types.regional_status_detail.serialize_query(
            value, pairs, f"{prefix}.entry.{n}.value"
        )


def deserialize_query(el: Element) -> RegionalStatusDetails:
    out: RegionalStatusDetails = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import capo_cloudformation.types.regional_status_detail

        value = capo_cloudformation.types.regional_status_detail.deserialize_query(
            value_element
        )
        out[key] = value
    return out


def serialize_query_flat(
    input_to_serialize: RegionalStatusDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.regional_status_detail

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.key", str(key)))
        capo_cloudformation.types.regional_status_detail.serialize_query(
            value, pairs, f"{prefix}.{n}.value"
        )


def deserialize_query_flat(parent: Element, tag: str) -> RegionalStatusDetails:
    out: RegionalStatusDetails = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import capo_cloudformation.types.regional_status_detail

        value = capo_cloudformation.types.regional_status_detail.deserialize_query(
            value_element
        )
        out[key] = value
    return out
