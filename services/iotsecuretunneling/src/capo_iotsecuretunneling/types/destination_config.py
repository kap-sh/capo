"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#DestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.service_list
    import capo_iotsecuretunneling.types.thing_name


class DestinationConfig(TypedDict, closed=True):
    thing_name: NotRequired["capo_iotsecuretunneling.types.thing_name.ThingName"]
    """<p>The name of the IoT thing to which you want to connect.</p>"""
    services: "capo_iotsecuretunneling.types.service_list.ServiceList"
    """<p>A list of service names that identify the target application. The IoT client running on the destination device reads this value and uses it to look up a port or an IP address and a port. The IoT client instantiates the local proxy, which uses this information to connect to the destination application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationConfig) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    import capo_iotsecuretunneling.types.service_list

    out["services"] = capo_iotsecuretunneling.types.service_list.serialize_aws_json_1_1(
        value["services"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationConfig:
    out: DestinationConfig = {}  # type: ignore[typeddict-item]
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    if data.get("services") is not None:
        import capo_iotsecuretunneling.types.service_list

        out["services"] = (
            capo_iotsecuretunneling.types.service_list.deserialize_aws_json_1_1(
                data["services"]
            )
        )
    else:
        out["services"] = []
    return out
