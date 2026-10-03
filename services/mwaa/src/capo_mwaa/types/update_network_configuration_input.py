"""Generated from Smithy shape ``com.amazonaws.mwaa#UpdateNetworkConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mwaa.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mwaa.types.security_group_list


class UpdateNetworkConfigurationInput(TypedDict, closed=True):
    security_group_ids: "capo_mwaa.types.security_group_list.SecurityGroupList"
    """<p>A list of security group IDs. A security group must be attached to the same VPC as the subnets. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html">Security in your VPC on Amazon MWAA</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateNetworkConfigurationInput) -> dict:
    out: dict = {}
    import capo_mwaa.types.security_group_list

    out["SecurityGroupIds"] = capo_mwaa.types.security_group_list.serialize_json(
        value["security_group_ids"]
    )
    return out


def deserialize_json(data: dict) -> UpdateNetworkConfigurationInput:
    out: UpdateNetworkConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("SecurityGroupIds") is not None:
        import capo_mwaa.types.security_group_list

        out["security_group_ids"] = (
            capo_mwaa.types.security_group_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNetworkConfigurationInput.security_group_ids required"
        )
    return out
