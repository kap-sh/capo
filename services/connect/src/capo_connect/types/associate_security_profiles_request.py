"""Generated from Smithy shape ``com.amazonaws.connect#AssociateSecurityProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.entity_arn
    import capo_connect.types.entity_type
    import capo_connect.types.instance_id
    import capo_connect.types.security_profiles


class AssociateSecurityProfilesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p> The identifier of the Amazon Connect instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance. </p>"""
    security_profiles: "capo_connect.types.security_profiles.SecurityProfiles"
    """<p> List of Security Profile Object. </p>"""
    entity_type: "capo_connect.types.entity_type.EntityType"
    """<p> Only supported type is AI_AGENT. </p>"""
    entity_arn: "capo_connect.types.entity_arn.EntityArn"
    """<p> Arn of a Q in Connect AI Agent. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSecurityProfilesRequest) -> dict:
    out: dict = {}
    import capo_connect.types.security_profiles

    out["SecurityProfiles"] = capo_connect.types.security_profiles.serialize_json(
        value["security_profiles"]
    )
    import capo_connect.types.entity_type

    out["EntityType"] = capo_connect.types.entity_type.serialize_json(
        value["entity_type"]
    )
    out["EntityArn"] = value["entity_arn"]
    return out


def deserialize_json(data: dict) -> AssociateSecurityProfilesRequest:
    out: AssociateSecurityProfilesRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecurityProfiles") is not None:
        import capo_connect.types.security_profiles

        out["security_profiles"] = (
            capo_connect.types.security_profiles.deserialize_json(
                data["SecurityProfiles"]
            )
        )
    else:
        out["security_profiles"] = []
    if data.get("EntityType") is not None:
        import capo_connect.types.entity_type

        out["entity_type"] = capo_connect.types.entity_type.deserialize_json(
            data["EntityType"]
        )
    else:
        import typing

        out["entity_type"] = typing.cast(
            "capo_connect.types.entity_type.EntityType", ""
        )
    if data.get("EntityArn") is not None:
        out["entity_arn"] = data["EntityArn"]
    else:
        out["entity_arn"] = ""
    return out
