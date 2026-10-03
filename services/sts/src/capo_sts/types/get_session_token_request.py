"""Generated from Smithy shape ``com.amazonaws.sts#GetSessionTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.duration_seconds_type
    import capo_sts.types.minimum_session_token_size_type
    import capo_sts.types.serial_number_type
    import capo_sts.types.token_code_type


class GetSessionTokenRequest(TypedDict, closed=True):
    duration_seconds: NotRequired[
        "capo_sts.types.duration_seconds_type.durationSecondsType"
    ]
    """<p>The duration, in seconds, that the credentials should remain valid. Acceptable durations for IAM user sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours), with 43,200 seconds (12 hours) as the default. Sessions for Amazon Web Services account owners are restricted to a maximum of 3,600 seconds (one hour). If the duration is longer than one hour, the session for Amazon Web Services account owners defaults to one hour.</p>"""
    serial_number: NotRequired["capo_sts.types.serial_number_type.serialNumberType"]
    """<p>The identification number of the MFA device that is associated with the IAM user who is making the <code>GetSessionToken</code> call. Specify this value if the IAM user has a policy that requires MFA authentication. The value is either the serial number for a hardware device (such as <code>GAHT12345678</code>) or an Amazon Resource Name (ARN) for a virtual device (such as <code>arn:aws:iam::123456789012:mfa/user</code>). You can find the device for an IAM user by going to the Amazon Web Services Management Console and viewing the user's security credentials. </p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>"""
    token_code: NotRequired["capo_sts.types.token_code_type.tokenCodeType"]
    """<p>The value provided by the MFA device, if MFA is required. If any policy requires the IAM user to submit an MFA code, specify this value. If MFA authentication is required, the user must provide a code when requesting a set of temporary security credentials. A user who fails to provide the code receives an "access denied" response when requesting resources that require MFA authentication.</p> <p>The format for this parameter, as described by its regex pattern, is a sequence of six numeric digits.</p>"""
    minimum_session_token_size: NotRequired[
        "capo_sts.types.minimum_session_token_size_type.minimumSessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSessionTokenRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "duration_seconds" in value:
        pairs.append((f"{key_prefix}DurationSeconds", str(value["duration_seconds"])))
    if "serial_number" in value:
        pairs.append((f"{key_prefix}SerialNumber", str(value["serial_number"])))
    if "token_code" in value:
        pairs.append((f"{key_prefix}TokenCode", str(value["token_code"])))
    if "minimum_session_token_size" in value:
        pairs.append(
            (
                f"{key_prefix}MinimumSessionTokenSize",
                str(value["minimum_session_token_size"]),
            )
        )


def deserialize_query(el: Element) -> GetSessionTokenRequest:
    out: GetSessionTokenRequest = {}  # type: ignore[typeddict-item]
    child_duration_seconds = el.find("DurationSeconds")
    if child_duration_seconds is not None:
        out["duration_seconds"] = int(child_duration_seconds.text or "")
    child_serial_number = el.find("SerialNumber")
    if child_serial_number is not None:
        out["serial_number"] = str(child_serial_number.text or "")
    child_token_code = el.find("TokenCode")
    if child_token_code is not None:
        out["token_code"] = str(child_token_code.text or "")
    child_minimum_session_token_size = el.find("MinimumSessionTokenSize")
    if child_minimum_session_token_size is not None:
        out["minimum_session_token_size"] = int(
            child_minimum_session_token_size.text or ""
        )
    return out
