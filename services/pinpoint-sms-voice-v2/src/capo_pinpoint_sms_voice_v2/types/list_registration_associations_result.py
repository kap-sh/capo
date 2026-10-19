"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ListRegistrationAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.next_token
    import capo_pinpoint_sms_voice_v2.types.registration_association_metadata_list
    import capo_pinpoint_sms_voice_v2.types.registration_type


class ListRegistrationAssociationsResult(TypedDict, closed=True):
    registration_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration.</p>"""
    registration_id: "str"
    """<p>The unique identifier for the registration.</p>"""
    registration_type: (
        "capo_pinpoint_sms_voice_v2.types.registration_type.RegistrationType"
    )
    """<p>The type of registration form. The list of <b>RegistrationTypes</b> can be found using the <a>DescribeRegistrationTypeDefinitions</a> action.</p>"""
    registration_associations: "capo_pinpoint_sms_voice_v2.types.registration_association_metadata_list.RegistrationAssociationMetadataList"
    """<p>An array of RegistrationAssociationMetadata objects.</p>"""
    next_token: NotRequired["capo_pinpoint_sms_voice_v2.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRegistrationAssociationsResult) -> dict:
    out: dict = {}
    out["RegistrationArn"] = value["registration_arn"]
    out["RegistrationId"] = value["registration_id"]
    out["RegistrationType"] = value["registration_type"]
    import capo_pinpoint_sms_voice_v2.types.registration_association_metadata_list

    out["RegistrationAssociations"] = (
        capo_pinpoint_sms_voice_v2.types.registration_association_metadata_list.serialize_aws_json_1_0(
            value["registration_associations"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRegistrationAssociationsResult:
    out: ListRegistrationAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationArn") is not None:
        out["registration_arn"] = data["RegistrationArn"]
    else:
        out["registration_arn"] = ""
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    if data.get("RegistrationType") is not None:
        out["registration_type"] = data["RegistrationType"]
    else:
        out["registration_type"] = ""
    if data.get("RegistrationAssociations") is not None:
        import capo_pinpoint_sms_voice_v2.types.registration_association_metadata_list

        out["registration_associations"] = (
            capo_pinpoint_sms_voice_v2.types.registration_association_metadata_list.deserialize_aws_json_1_0(
                data["RegistrationAssociations"]
            )
        )
    else:
        out["registration_associations"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
