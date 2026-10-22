"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayTestTrafficHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string
    import capo_ecs.types.string_list


class GatewayTestTrafficHeader(TypedDict, closed=True):
    name: "capo_ecs.types.string.String"
    """<p>The name of the header to match for test traffic routing.</p>"""
    values: "capo_ecs.types.string_list.StringList"
    """<p>The header values to match for test traffic routing.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayTestTrafficHeader) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_ecs.types.string_list

    out["values"] = capo_ecs.types.string_list.serialize_aws_json_1_1(value["values"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayTestTrafficHeader:
    out: GatewayTestTrafficHeader = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("values") is not None:
        import capo_ecs.types.string_list

        out["values"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["values"]
        )
    else:
        out["values"] = []
    return out
