"""Generated from Smithy shape ``com.amazonaws.b2bi#GetProfileResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.business_name
    import capo_b2bi.types.created_date
    import capo_b2bi.types.email
    import capo_b2bi.types.log_group_name
    import capo_b2bi.types.logging
    import capo_b2bi.types.modified_date
    import capo_b2bi.types.phone
    import capo_b2bi.types.profile_id
    import capo_b2bi.types.profile_name
    import capo_b2bi.types.resource_arn


class GetProfileResponse(TypedDict, closed=True):
    profile_id: "capo_b2bi.types.profile_id.ProfileId"
    """<p>Returns the unique, system-generated identifier for the profile.</p>"""
    profile_arn: "capo_b2bi.types.resource_arn.ResourceArn"
    """<p>Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>"""
    name: "capo_b2bi.types.profile_name.ProfileName"
    """<p>Returns the name of the profile, used to identify it.</p>"""
    email: NotRequired["capo_b2bi.types.email.Email"]
    """<p>Returns the email address associated with this customer profile.</p>"""
    phone: "capo_b2bi.types.phone.Phone"
    """<p>Returns the phone number associated with the profile.</p>"""
    business_name: "capo_b2bi.types.business_name.BusinessName"
    """<p>Returns the name for the business associated with this profile.</p>"""
    logging: NotRequired["capo_b2bi.types.logging.Logging"]
    """<p>Returns whether or not logging is enabled for this profile.</p>"""
    log_group_name: NotRequired["capo_b2bi.types.log_group_name.LogGroupName"]
    """<p>Returns the name of the logging group.</p>"""
    created_at: "capo_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the transformer.</p>"""
    modified_at: NotRequired["capo_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp for last time the profile was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProfileResponse) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["profileArn"] = value["profile_arn"]
    out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    out["phone"] = value["phone"]
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


def deserialize_aws_json_1_0(data: dict) -> GetProfileResponse:
    out: GetProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    else:
        out["profile_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("email") is not None:
        out["email"] = data["email"]
    if data.get("phone") is not None:
        out["phone"] = data["phone"]
    else:
        out["phone"] = ""
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


def redact_sensitive(value: GetProfileResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        out["email"] = "*** Sensitive Data Redacted ***"
    if "phone" in value:
        out["phone"] = "*** Sensitive Data Redacted ***"
    return out
