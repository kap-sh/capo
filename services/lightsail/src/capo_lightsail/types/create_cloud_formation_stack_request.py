"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateCloudFormationStackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.instance_entry_list


class CreateCloudFormationStackRequest(TypedDict, closed=True):
    instances: "capo_lightsail.types.instance_entry_list.InstanceEntryList"
    """<p>An array of parameters that will be used to create the new Amazon EC2 instance. You can only pass one instance entry at a time in this array. You will get an invalid parameter error if you pass more than one instance entry in this array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCloudFormationStackRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.instance_entry_list

    out["instances"] = capo_lightsail.types.instance_entry_list.serialize_aws_json_1_1(
        value["instances"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCloudFormationStackRequest:
    out: CreateCloudFormationStackRequest = {}  # type: ignore[typeddict-item]
    if data.get("instances") is not None:
        import capo_lightsail.types.instance_entry_list

        out["instances"] = (
            capo_lightsail.types.instance_entry_list.deserialize_aws_json_1_1(
                data["instances"]
            )
        )
    else:
        out["instances"] = []
    return out
