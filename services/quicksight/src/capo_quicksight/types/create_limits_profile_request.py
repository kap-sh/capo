"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateLimitsProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.create_limits_profile_request_client_token_string
    import capo_quicksight.types.create_limits_profile_request_resource_limits_map
    import capo_quicksight.types.profile_description
    import capo_quicksight.types.profile_name


class CreateLimitsProfileRequest(TypedDict, closed=True):
    account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the limits profile.</p>"""
    profile_name: "capo_quicksight.types.profile_name.ProfileName"
    """<p>A display name for the limits profile.</p>"""
    description: NotRequired[
        "capo_quicksight.types.profile_description.ProfileDescription"
    ]
    """<p>A description for the limits profile.</p>"""
    resource_limits: "capo_quicksight.types.create_limits_profile_request_resource_limits_map.CreateLimitsProfileRequestResourceLimitsMap"
    """<p>A map of resource types to their limit values for this profile.</p>"""
    client_token: "capo_quicksight.types.create_limits_profile_request_client_token_string.CreateLimitsProfileRequestClientTokenString"
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLimitsProfileRequest) -> dict:
    out: dict = {}
    out["profileName"] = value["profile_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_quicksight.types.create_limits_profile_request_resource_limits_map

    out["resourceLimits"] = (
        capo_quicksight.types.create_limits_profile_request_resource_limits_map.serialize_json(
            value["resource_limits"]
        )
    )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateLimitsProfileRequest:
    out: CreateLimitsProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("profileName") is not None:
        out["profile_name"] = data["profileName"]
    else:
        out["profile_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("resourceLimits") is not None:
        import capo_quicksight.types.create_limits_profile_request_resource_limits_map

        out["resource_limits"] = (
            capo_quicksight.types.create_limits_profile_request_resource_limits_map.deserialize_json(
                data["resourceLimits"]
            )
        )
    else:
        out["resource_limits"] = {}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    return out
