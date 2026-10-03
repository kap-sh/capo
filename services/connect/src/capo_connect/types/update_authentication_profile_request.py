"""Generated from Smithy shape ``com.amazonaws.connect#UpdateAuthenticationProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.access_token_duration
    import capo_connect.types.authentication_profile_description
    import capo_connect.types.authentication_profile_id
    import capo_connect.types.authentication_profile_name
    import capo_connect.types.boolean
    import capo_connect.types.inactivity_duration
    import capo_connect.types.instance_id
    import capo_connect.types.ip_cidr_list


class UpdateAuthenticationProfileRequest(TypedDict, closed=True):
    authentication_profile_id: (
        "capo_connect.types.authentication_profile_id.AuthenticationProfileId"
    )
    """<p>A unique identifier for the authentication profile. </p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: NotRequired[
        "capo_connect.types.authentication_profile_name.AuthenticationProfileName"
    ]
    """<p>The name for the authentication profile.</p>"""
    description: NotRequired[
        "capo_connect.types.authentication_profile_description.AuthenticationProfileDescription"
    ]
    """<p>The description for the authentication profile.</p>"""
    allowed_ips: NotRequired["capo_connect.types.ip_cidr_list.IpCidrList"]
    """<p>A list of IP address range strings that are allowed to access the instance. For more information on how to configure IP addresses, see<a href="https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts">Configure session timeouts</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    blocked_ips: NotRequired["capo_connect.types.ip_cidr_list.IpCidrList"]
    """<p>A list of IP address range strings that are blocked from accessing the instance. For more information on how to configure IP addresses, For more information on how to configure IP addresses, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-ip-based-ac">Configure IP-based access control</a> in the <i>Connect Customer Administrator Guide</i>. </p>"""
    periodic_session_duration: NotRequired[
        "capo_connect.types.access_token_duration.AccessTokenDuration"
    ]
    """<p>The short lived session duration configuration for users logged in to Connect Customer, in minutes. This value determines the maximum possible time before an agent is authenticated. For more information, For more information on how to configure IP addresses, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts">Configure session timeouts</a> in the <i>Connect Customer Administrator Guide</i>. </p>"""
    session_inactivity_duration: NotRequired[
        "capo_connect.types.inactivity_duration.InactivityDuration"
    ]
    """<p>The period, in minutes, before an agent is automatically signed out of the contact center when they go inactive.</p>"""
    session_inactivity_handling_enabled: NotRequired[
        "capo_connect.types.boolean.Boolean"
    ]
    """<p>Determines if automatic logout on user inactivity is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAuthenticationProfileRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "allowed_ips" in value:
        import capo_connect.types.ip_cidr_list

        out["AllowedIps"] = capo_connect.types.ip_cidr_list.serialize_json(
            value["allowed_ips"]
        )
    if "blocked_ips" in value:
        import capo_connect.types.ip_cidr_list

        out["BlockedIps"] = capo_connect.types.ip_cidr_list.serialize_json(
            value["blocked_ips"]
        )
    if "periodic_session_duration" in value:
        out["PeriodicSessionDuration"] = value["periodic_session_duration"]
    if "session_inactivity_duration" in value:
        out["SessionInactivityDuration"] = value["session_inactivity_duration"]
    if "session_inactivity_handling_enabled" in value:
        out["SessionInactivityHandlingEnabled"] = value[
            "session_inactivity_handling_enabled"
        ]
    return out


def deserialize_json(data: dict) -> UpdateAuthenticationProfileRequest:
    out: UpdateAuthenticationProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AllowedIps") is not None:
        import capo_connect.types.ip_cidr_list

        out["allowed_ips"] = capo_connect.types.ip_cidr_list.deserialize_json(
            data["AllowedIps"]
        )
    if data.get("BlockedIps") is not None:
        import capo_connect.types.ip_cidr_list

        out["blocked_ips"] = capo_connect.types.ip_cidr_list.deserialize_json(
            data["BlockedIps"]
        )
    if data.get("PeriodicSessionDuration") is not None:
        out["periodic_session_duration"] = data["PeriodicSessionDuration"]
    if data.get("SessionInactivityDuration") is not None:
        out["session_inactivity_duration"] = data["SessionInactivityDuration"]
    if data.get("SessionInactivityHandlingEnabled") is not None:
        out["session_inactivity_handling_enabled"] = data[
            "SessionInactivityHandlingEnabled"
        ]
    return out
