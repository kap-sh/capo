"""Generated from Smithy shape ``com.amazonaws.quicksight#LimitsProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.profile_description
    import capo_quicksight.types.profile_id
    import capo_quicksight.types.profile_name
    import capo_quicksight.types.resource_arn
    import capo_quicksight.types.resource_limits_map
    import capo_quicksight.types.timestamp


class LimitsProfile(TypedDict, closed=True):
    profile_id: "capo_quicksight.types.profile_id.ProfileId"
    """<p>The unique identifier for the limits profile.</p>"""
    arn: "capo_quicksight.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the limits profile.</p>"""
    account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the limits profile.</p>"""
    profile_name: "capo_quicksight.types.profile_name.ProfileName"
    """<p>The display name of the limits profile.</p>"""
    description: NotRequired[
        "capo_quicksight.types.profile_description.ProfileDescription"
    ]
    """<p>The description of the limits profile.</p>"""
    resource_limits: "capo_quicksight.types.resource_limits_map.ResourceLimitsMap"
    """<p>A map of resource types to their limit values.</p>"""
    created_at: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The date and time that the limits profile was created.</p>"""
    updated_at: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The date and time that the limits profile was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitsProfile) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["arn"] = value["arn"]
    out["accountId"] = value["account_id"]
    out["profileName"] = value["profile_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_quicksight.types.resource_limits_map

    out["resourceLimits"] = capo_quicksight.types.resource_limits_map.serialize_json(
        value["resource_limits"]
    )
    import capo_quicksight.types.timestamp

    out["createdAt"] = capo_quicksight.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_quicksight.types.timestamp

    out["updatedAt"] = capo_quicksight.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> LimitsProfile:
    out: LimitsProfile = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("profileName") is not None:
        out["profile_name"] = data["profileName"]
    else:
        out["profile_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("resourceLimits") is not None:
        import capo_quicksight.types.resource_limits_map

        out["resource_limits"] = (
            capo_quicksight.types.resource_limits_map.deserialize_json(
                data["resourceLimits"]
            )
        )
    else:
        out["resource_limits"] = {}
    if data.get("createdAt") is not None:
        import capo_quicksight.types.timestamp

        out["created_at"] = capo_quicksight.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_quicksight.types.timestamp

        out["updated_at"] = capo_quicksight.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
