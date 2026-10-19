"""Generated from Smithy shape ``com.amazonaws.workmail#PersonalAccessTokenConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.personal_access_token_configuration_status
    import capo_workmail.types.personal_access_token_lifetime_in_days


class PersonalAccessTokenConfiguration(TypedDict, closed=True):
    status: "capo_workmail.types.personal_access_token_configuration_status.PersonalAccessTokenConfigurationStatus"
    """<p> The status of the Personal Access Token allowed for the organization. </p> <ul> <li> <p> <i>Active</i> - Mailbox users can login to the web application and choose <i>Settings</i> to see the new <i>Personal Access Tokens</i> page to create and delete the Personal Access Tokens. Mailbox users can use the Personal Access Tokens to set up mailbox connection from desktop or mobile email clients.</p> </li> <li> <p> <i>Inactive</i> - Personal Access Tokens are disabled for your organization. Mailbox users can’t create, list, or delete Personal Access Tokens and can’t use them to connect to their mailboxes from desktop or mobile email clients.</p> </li> </ul>"""
    lifetime_in_days: NotRequired[
        "capo_workmail.types.personal_access_token_lifetime_in_days.PersonalAccessTokenLifetimeInDays"
    ]
    """<p> The validity of the Personal Access Token status in days. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonalAccessTokenConfiguration) -> dict:
    out: dict = {}
    import capo_workmail.types.personal_access_token_configuration_status

    out["Status"] = (
        capo_workmail.types.personal_access_token_configuration_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "lifetime_in_days" in value:
        out["LifetimeInDays"] = value["lifetime_in_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PersonalAccessTokenConfiguration:
    out: PersonalAccessTokenConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_workmail.types.personal_access_token_configuration_status

        out["status"] = (
            capo_workmail.types.personal_access_token_configuration_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_workmail.types.personal_access_token_configuration_status.PersonalAccessTokenConfigurationStatus",
            "",
        )
    if data.get("LifetimeInDays") is not None:
        out["lifetime_in_days"] = data["LifetimeInDays"]
    return out
