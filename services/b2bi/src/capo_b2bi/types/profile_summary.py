"""Generated from Smithy shape ``com.amazonaws.b2bi#ProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.business_name
    import capo_b2bi.types.created_date
    import capo_b2bi.types.log_group_name
    import capo_b2bi.types.logging
    import capo_b2bi.types.modified_date
    import capo_b2bi.types.profile_id
    import capo_b2bi.types.profile_name


class ProfileSummary(TypedDict, closed=True):
    profile_id: "capo_b2bi.types.profile_id.ProfileId"
    """<p>Returns the unique, system-generated identifier for the profile.</p>"""
    name: "capo_b2bi.types.profile_name.ProfileName"
    """<p>Returns the display name for profile.</p>"""
    business_name: "capo_b2bi.types.business_name.BusinessName"
    """<p>Returns the name for the business associated with this profile.</p>"""
    logging: NotRequired["capo_b2bi.types.logging.Logging"]
    """<p>Specifies whether or not logging is enabled for this profile.</p>"""
    log_group_name: NotRequired["capo_b2bi.types.log_group_name.LogGroupName"]
    """<p>Returns the name of the logging group.</p>"""
    created_at: "capo_b2bi.types.created_date.CreatedDate"
    """<p>Returns the timestamp for creation date and time of the profile.</p>"""
    modified_at: NotRequired["capo_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns the timestamp that identifies the most recent date and time that the profile was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileSummary) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["name"] = value["name"]
    out["businessName"] = value["business_name"]
    if "logging" in value:
        import capo_b2bi.types.logging

        out["logging"] = capo_b2bi.types.logging.serialize_aws_json_1_0(
            value["logging"]
        )
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    import capo_b2bi.types.created_date

    out["createdAt"] = capo_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "modified_at" in value:
        import capo_b2bi.types.modified_date

        out["modifiedAt"] = capo_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProfileSummary:
    out: ProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("businessName") is not None:
        out["business_name"] = data["businessName"]
    else:
        out["business_name"] = ""
    if data.get("logging") is not None:
        import capo_b2bi.types.logging

        out["logging"] = capo_b2bi.types.logging.deserialize_aws_json_1_0(
            data["logging"]
        )
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    if data.get("createdAt") is not None:
        import capo_b2bi.types.created_date

        out["created_at"] = capo_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("modifiedAt") is not None:
        import capo_b2bi.types.modified_date

        out["modified_at"] = capo_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    return out
