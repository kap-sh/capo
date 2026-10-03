"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.client_token
    import capo_sso_admin.types.name_type
    import capo_sso_admin.types.tag_list


class CreateInstanceRequest(TypedDict, closed=True):
    name: NotRequired["capo_sso_admin.types.name_type.NameType"]
    """<p>The name of the instance of IAM Identity Center.</p>"""
    client_token: NotRequired["capo_sso_admin.types.client_token.ClientToken"]
    """<p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    tags: NotRequired["capo_sso_admin.types.tag_list.TagList"]
    """<p>Specifies tags to be attached to the instance of IAM Identity Center.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInstanceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_sso_admin.types.tag_list

        out["Tags"] = capo_sso_admin.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInstanceRequest:
    out: CreateInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_sso_admin.types.tag_list

        out["tags"] = capo_sso_admin.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
