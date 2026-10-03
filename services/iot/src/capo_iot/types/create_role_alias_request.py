"""Generated from Smithy shape ``com.amazonaws.iot#CreateRoleAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.credential_duration_seconds
    import capo_iot.types.role_alias
    import capo_iot.types.role_arn
    import capo_iot.types.tag_list


class CreateRoleAliasRequest(TypedDict, closed=True):
    role_alias: "capo_iot.types.role_alias.RoleAlias"
    """<p>The role alias that points to a role ARN. This allows you to change the role without having to update the device.</p>"""
    role_arn: "capo_iot.types.role_arn.RoleArn"
    """<p>The role ARN.</p>"""
    credential_duration_seconds: NotRequired[
        "capo_iot.types.credential_duration_seconds.CredentialDurationSeconds"
    ]
    """<p>How long (in seconds) the credentials will be valid. The default value is 3,600 seconds.</p> <p>This value must be less than or equal to the maximum session duration of the IAM role that the role alias references.</p>"""
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the role alias.</p> <note> <p>For URI Request parameters use format: ...key1=value1&key2=value2...</p> <p>For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."</p> <p>For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoleAliasRequest) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    if "credential_duration_seconds" in value:
        out["credentialDurationSeconds"] = value["credential_duration_seconds"]
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRoleAliasRequest:
    out: CreateRoleAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateRoleAliasRequest.role_arn required")
    if data.get("credentialDurationSeconds") is not None:
        out["credential_duration_seconds"] = data["credentialDurationSeconds"]
    if data.get("tags") is not None:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    return out
