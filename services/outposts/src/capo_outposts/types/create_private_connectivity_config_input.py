"""Generated from Smithy shape ``com.amazonaws.outposts#CreatePrivateConnectivityConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.outpost_id
    import capo_outposts.types.vpc_information_list


class CreatePrivateConnectivityConfigInput(TypedDict, closed=True):
    outpost_id: "capo_outposts.types.outpost_id.OutpostId"
    """<p>The ID or ARN of the Outpost.</p>"""
    vpc_information_list: "capo_outposts.types.vpc_information_list.VpcInformationList"
    """<p>Information about the VPC used for private connectivity, including the VPC, its subnets, and an associated VPC endpoint. You can specify at most one entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrivateConnectivityConfigInput) -> dict:
    out: dict = {}
    import capo_outposts.types.vpc_information_list

    out["VpcInformationList"] = capo_outposts.types.vpc_information_list.serialize_json(
        value["vpc_information_list"]
    )
    return out


def deserialize_json(data: dict) -> CreatePrivateConnectivityConfigInput:
    out: CreatePrivateConnectivityConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("VpcInformationList") is not None:
        import capo_outposts.types.vpc_information_list

        out["vpc_information_list"] = (
            capo_outposts.types.vpc_information_list.deserialize_json(
                data["VpcInformationList"]
            )
        )
    else:
        out["vpc_information_list"] = []
    return out
