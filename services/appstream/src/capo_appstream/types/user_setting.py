"""Generated from Smithy shape ``com.amazonaws.appstream#UserSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.action
    import capo_appstream.types.integer
    import capo_appstream.types.permission


class UserSetting(TypedDict, closed=True):
    action: NotRequired["capo_appstream.types.action.Action"]
    """<p>The action you want to enable or disable. Choose from the following:</p> <dl> <dt>AUTO_TIME_ZONE_REDIRECTION</dt> <dd> <p>Controls whether the streaming session's time zone matches the time zone of your local device.</p> </dd> <dt>CLIPBOARD_COPY_FROM_LOCAL_DEVICE</dt> <dd> <p>Controls whether you can copy data from your local device and paste it into the streaming session.</p> </dd> <dt>CLIPBOARD_COPY_TO_LOCAL_DEVICE</dt> <dd> <p>Controls whether you can copy data from the streaming session and paste it to your local device.</p> </dd> <dt>DOMAIN_PASSWORD_SIGNIN</dt> <dd> <p>Controls whether you can sign in to a domain-joined streaming session by using your password.</p> </dd> <dt>DOMAIN_SMART_CARD_SIGNIN</dt> <dd> <p>Controls whether you can sign in to a domain-joined streaming session by using a smart card.</p> </dd> <dt>FILE_DOWNLOAD</dt> <dd> <p>Controls whether you can download files from the streaming session to your local device.</p> </dd> <dt>FILE_UPLOAD</dt> <dd> <p>Controls whether you can upload files from your local device to the streaming session.</p> </dd> <dt>PRINTING_TO_LOCAL_DEVICE</dt> <dd> <p>Controls whether you can print from the streaming session to a printer on your local device.</p> </dd> <dt>SMART_CARD_REDIRECTION</dt> <dd> <p>Controls whether smart cards connected to your local device are redirected into the streaming session. Applications in the session can access the local smart card for use cases such as authentication, digital signing, and email encryption.</p> </dd> </dl> <note> <p>Smart card redirection was on by default for existing streaming sessions that use a Windows single-session fleet. To preserve that behavior, <code>SMART_CARD_REDIRECTION</code> is <code>ENABLED</code> by default on existing stacks associated with Windows single-session fleets. To turn it off, call <code>UpdateStack</code> with <code>SMART_CARD_REDIRECTION</code> set to <code>DISABLED</code>, and use an image that includes the latest WorkSpaces Applications agent version.</p> </note>"""
    permission: NotRequired["capo_appstream.types.permission.Permission"]
    """<p>Specifies whether to turn the action on or off.</p>"""
    maximum_length: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>Specifies the number of characters that can be copied by end users from the local device to the remote session, and to the local device from the remote session.</p> <p>This can be specified only for the <code>CLIPBOARD_COPY_FROM_LOCAL_DEVICE</code> and <code>CLIPBOARD_COPY_TO_LOCAL_DEVICE</code> actions.</p> <p>This defaults to 20,971,520 (20 MB) when unspecified and the permission is <code>ENABLED</code>. This can't be specified when the permission is <code>DISABLED</code>. </p> <p>The value can be between 1 and 20,971,520 (20 MB).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserSetting) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_appstream.types.action

        out["Action"] = capo_appstream.types.action.serialize_aws_json_1_1(
            value["action"]
        )
    if "permission" in value:
        import capo_appstream.types.permission

        out["Permission"] = capo_appstream.types.permission.serialize_aws_json_1_1(
            value["permission"]
        )
    if "maximum_length" in value:
        out["MaximumLength"] = value["maximum_length"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserSetting:
    out: UserSetting = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_appstream.types.action

        out["action"] = capo_appstream.types.action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if data.get("Permission") is not None:
        import capo_appstream.types.permission

        out["permission"] = capo_appstream.types.permission.deserialize_aws_json_1_1(
            data["Permission"]
        )
    if data.get("MaximumLength") is not None:
        out["maximum_length"] = data["MaximumLength"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UserSetting) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_appstream.types.action

        out["Action"] = capo_appstream.types.action.serialize_cbor(value["action"])
    if "permission" in value:
        import capo_appstream.types.permission

        out["Permission"] = capo_appstream.types.permission.serialize_cbor(
            value["permission"]
        )
    if "maximum_length" in value:
        out["MaximumLength"] = value["maximum_length"]
    return out


def deserialize_cbor(data: dict) -> UserSetting:
    out: UserSetting = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_appstream.types.action

        out["action"] = capo_appstream.types.action.deserialize_cbor(data["Action"])
    if data.get("Permission") is not None:
        import capo_appstream.types.permission

        out["permission"] = capo_appstream.types.permission.deserialize_cbor(
            data["Permission"]
        )
    if data.get("MaximumLength") is not None:
        out["maximum_length"] = data["MaximumLength"]
    return out
