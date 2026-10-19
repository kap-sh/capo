"""Generated from Smithy shape ``com.amazonaws.iam#PutAccountPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.account_properties_map_type


class PutAccountPropertiesRequest(TypedDict, closed=True):
    properties: "capo_iam.types.account_properties_map_type.accountPropertiesMapType"
    """<p>A map of property key-value pairs to set. All keys must belong to the same namespace.</p> <p>Each key uses the format <code>Namespace/PropertyName</code>. The key must contain exactly one <code>/</code> separating the namespace from the property name, and cannot start or end with <code>/</code>.</p> <p>The service validates each value based on the property key's expected type. For example, boolean properties expect <code>true</code> or <code>false</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutAccountPropertiesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.account_properties_map_type

    capo_iam.types.account_properties_map_type.serialize_query(
        value["properties"], pairs, f"{key_prefix}Properties"
    )


def deserialize_query(el: Element) -> PutAccountPropertiesRequest:
    out: PutAccountPropertiesRequest = {}  # type: ignore[typeddict-item]
    child_properties = el.find("Properties")
    if child_properties is not None:
        import capo_iam.types.account_properties_map_type

        out["properties"] = (
            capo_iam.types.account_properties_map_type.deserialize_query(
                child_properties
            )
        )
    else:
        out["properties"] = {}
    return out
