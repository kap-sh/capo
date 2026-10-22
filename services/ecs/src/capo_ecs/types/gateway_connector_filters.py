"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectorFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.access_type_list


class GatewayConnectorFilters(TypedDict, closed=True):
    access_types: NotRequired["capo_ecs.types.access_type_list.AccessTypeList"]
    """<p>The access types of the gateway ingress paths that the connector applies to.</p> <p>The access type can be one of the following values:</p> <ul> <li> <p> <code>PUBLIC</code> - The ingress path is publicly accessible.</p> </li> <li> <p> <code>PRIVATE</code> - The ingress path is only accessible privately.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectorFilters) -> dict:
    out: dict = {}
    if "access_types" in value:
        import capo_ecs.types.access_type_list

        out["accessTypes"] = capo_ecs.types.access_type_list.serialize_aws_json_1_1(
            value["access_types"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayConnectorFilters:
    out: GatewayConnectorFilters = {}  # type: ignore[typeddict-item]
    if data.get("accessTypes") is not None:
        import capo_ecs.types.access_type_list

        out["access_types"] = capo_ecs.types.access_type_list.deserialize_aws_json_1_1(
            data["accessTypes"]
        )
    return out
