"""Generated from Smithy shape ``com.amazonaws.kendra#UserIdentityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.identity_attribute_name


class UserIdentityConfiguration(TypedDict, closed=True):
    identity_attribute_name: NotRequired[
        "capo_kendra.types.identity_attribute_name.IdentityAttributeName"
    ]
    """<p>The IAM Identity Center field name that contains the identifiers of your users, such as their emails. This is used for <a href="https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html">user context filtering</a> and for granting access to your Amazon Kendra experience. You must set up IAM Identity Center with Amazon Kendra. You must include your users and groups in your Access Control List when you ingest documents into your index. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/getting-started-aws-sso.html">Getting started with an IAM Identity Center identity source</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserIdentityConfiguration) -> dict:
    out: dict = {}
    if "identity_attribute_name" in value:
        out["IdentityAttributeName"] = value["identity_attribute_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserIdentityConfiguration:
    out: UserIdentityConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("IdentityAttributeName") is not None:
        out["identity_attribute_name"] = data["IdentityAttributeName"]
    return out
