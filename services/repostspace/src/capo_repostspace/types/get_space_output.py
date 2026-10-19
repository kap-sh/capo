"""Generated from Smithy shape ``com.amazonaws.repostspace#GetSpaceOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_repostspace.types.arn
    import capo_repostspace.types.client_id
    import capo_repostspace.types.configuration_status
    import capo_repostspace.types.content_size
    import capo_repostspace.types.group_admins
    import capo_repostspace.types.identity_store_id
    import capo_repostspace.types.kms_key
    import capo_repostspace.types.provisioning_status
    import capo_repostspace.types.roles
    import capo_repostspace.types.space_description
    import capo_repostspace.types.space_id
    import capo_repostspace.types.space_name
    import capo_repostspace.types.storage_limit
    import capo_repostspace.types.supported_email_domains_status
    import capo_repostspace.types.tier_level
    import capo_repostspace.types.url
    import capo_repostspace.types.user_admins
    import capo_repostspace.types.user_count
    import capo_repostspace.types.vanity_domain_status


class GetSpaceOutput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    arn: "capo_repostspace.types.arn.Arn"
    """<p>The ARN of the private re:Post.</p>"""
    name: "capo_repostspace.types.space_name.SpaceName"
    """<p>The name of the private re:Post.</p>"""
    status: "capo_repostspace.types.provisioning_status.ProvisioningStatus"
    """<p>The creation or deletion status of the private re:Post.</p>"""
    configuration_status: (
        "capo_repostspace.types.configuration_status.ConfigurationStatus"
    )
    """<p>The configuration status of the private re:Post.</p>"""
    client_id: "capo_repostspace.types.client_id.ClientId"
    """<p>The Identity Center identifier for the Application Instance.</p>"""
    identity_store_id: NotRequired[
        "capo_repostspace.types.identity_store_id.IdentityStoreId"
    ]
    """<p/>"""
    application_arn: NotRequired["capo_repostspace.types.arn.Arn"]
    """<p/>"""
    description: NotRequired[
        "capo_repostspace.types.space_description.SpaceDescription"
    ]
    """<p>The description of the private re:Post.</p>"""
    vanity_domain_status: (
        "capo_repostspace.types.vanity_domain_status.VanityDomainStatus"
    )
    """<p>The approval status of the custom subdomain.</p>"""
    vanity_domain: "capo_repostspace.types.url.Url"
    """<p>The custom subdomain that you use to access your private re:Post. All custom subdomains must be approved by AWS before use.</p>"""
    random_domain: "capo_repostspace.types.url.Url"
    """<p>The AWS generated subdomain of the private re:Post</p>"""
    customer_role_arn: NotRequired["capo_repostspace.types.arn.Arn"]
    """<p>The IAM role that grants permissions to the private re:Post to convert unanswered questions into AWS support tickets.</p>"""
    create_date_time: "datetime.datetime"
    """<p>The date when the private re:Post was created.</p>"""
    delete_date_time: NotRequired["datetime.datetime"]
    """<p>The date when the private re:Post was deleted.</p>"""
    tier: "capo_repostspace.types.tier_level.TierLevel"
    """<p>The pricing tier of the private re:Post.</p>"""
    storage_limit: "capo_repostspace.types.storage_limit.StorageLimit"
    """<p>The storage limit of the private re:Post.</p>"""
    user_admins: NotRequired["capo_repostspace.types.user_admins.UserAdmins"]
    """<p>The list of users that are administrators of the private re:Post.</p>"""
    group_admins: NotRequired["capo_repostspace.types.group_admins.GroupAdmins"]
    """<p>The list of groups that are administrators of the private re:Post.</p>"""
    roles: NotRequired["capo_repostspace.types.roles.Roles"]
    """<p>A map of accessor identifiers and their roles.</p>"""
    user_kms_key: NotRequired["capo_repostspace.types.kms_key.KMSKey"]
    """<p>The custom AWS KMS key ARN that’s used for the AWS KMS encryption.</p>"""
    user_count: NotRequired["capo_repostspace.types.user_count.UserCount"]
    """<p>The number of users that have onboarded to the private re:Post.</p>"""
    content_size: NotRequired["capo_repostspace.types.content_size.ContentSize"]
    """<p>The content size of the private re:Post.</p>"""
    supported_email_domains: NotRequired[
        "capo_repostspace.types.supported_email_domains_status.SupportedEmailDomainsStatus"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSpaceOutput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["status"] = value["status"]
    import capo_repostspace.types.configuration_status

    out["configurationStatus"] = (
        capo_repostspace.types.configuration_status.serialize_json(
            value["configuration_status"]
        )
    )
    out["clientId"] = value["client_id"]
    if "identity_store_id" in value:
        out["identityStoreId"] = value["identity_store_id"]
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_repostspace.types.vanity_domain_status

    out["vanityDomainStatus"] = (
        capo_repostspace.types.vanity_domain_status.serialize_json(
            value["vanity_domain_status"]
        )
    )
    out["vanityDomain"] = value["vanity_domain"]
    out["randomDomain"] = value["random_domain"]
    if "customer_role_arn" in value:
        out["customerRoleArn"] = value["customer_role_arn"]
    import capo_repostspace._protocol.serialize

    out["createDateTime"] = capo_repostspace._protocol.serialize.fmt_date_time(
        value["create_date_time"]
    )
    if "delete_date_time" in value:
        import capo_repostspace._protocol.serialize

        out["deleteDateTime"] = capo_repostspace._protocol.serialize.fmt_date_time(
            value["delete_date_time"]
        )
    import capo_repostspace.types.tier_level

    out["tier"] = capo_repostspace.types.tier_level.serialize_json(value["tier"])
    out["storageLimit"] = value["storage_limit"]
    if "user_admins" in value:
        import capo_repostspace.types.user_admins

        out["userAdmins"] = capo_repostspace.types.user_admins.serialize_json(
            value["user_admins"]
        )
    if "group_admins" in value:
        import capo_repostspace.types.group_admins

        out["groupAdmins"] = capo_repostspace.types.group_admins.serialize_json(
            value["group_admins"]
        )
    if "roles" in value:
        import capo_repostspace.types.roles

        out["roles"] = capo_repostspace.types.roles.serialize_json(value["roles"])
    if "user_kms_key" in value:
        out["userKMSKey"] = value["user_kms_key"]
    if "user_count" in value:
        out["userCount"] = value["user_count"]
    if "content_size" in value:
        out["contentSize"] = value["content_size"]
    if "supported_email_domains" in value:
        import capo_repostspace.types.supported_email_domains_status

        out["supportedEmailDomains"] = (
            capo_repostspace.types.supported_email_domains_status.serialize_json(
                value["supported_email_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSpaceOutput:
    out: GetSpaceOutput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("configurationStatus") is not None:
        import capo_repostspace.types.configuration_status

        out["configuration_status"] = (
            capo_repostspace.types.configuration_status.deserialize_json(
                data["configurationStatus"]
            )
        )
    else:
        import typing

        out["configuration_status"] = typing.cast(
            "capo_repostspace.types.configuration_status.ConfigurationStatus", ""
        )
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        out["client_id"] = ""
    if data.get("identityStoreId") is not None:
        out["identity_store_id"] = data["identityStoreId"]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("vanityDomainStatus") is not None:
        import capo_repostspace.types.vanity_domain_status

        out["vanity_domain_status"] = (
            capo_repostspace.types.vanity_domain_status.deserialize_json(
                data["vanityDomainStatus"]
            )
        )
    else:
        import typing

        out["vanity_domain_status"] = typing.cast(
            "capo_repostspace.types.vanity_domain_status.VanityDomainStatus", ""
        )
    if data.get("vanityDomain") is not None:
        out["vanity_domain"] = data["vanityDomain"]
    else:
        out["vanity_domain"] = ""
    if data.get("randomDomain") is not None:
        out["random_domain"] = data["randomDomain"]
    else:
        out["random_domain"] = ""
    if data.get("customerRoleArn") is not None:
        out["customer_role_arn"] = data["customerRoleArn"]
    if data.get("createDateTime") is not None:
        import datetime

        out["create_date_time"] = datetime.datetime.fromisoformat(
            data["createDateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["create_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("deleteDateTime") is not None:
        import datetime

        out["delete_date_time"] = datetime.datetime.fromisoformat(
            data["deleteDateTime"].replace("Z", "+00:00")
        )
    if data.get("tier") is not None:
        import capo_repostspace.types.tier_level

        out["tier"] = capo_repostspace.types.tier_level.deserialize_json(data["tier"])
    else:
        import typing

        out["tier"] = typing.cast("capo_repostspace.types.tier_level.TierLevel", "")
    if data.get("storageLimit") is not None:
        out["storage_limit"] = data["storageLimit"]
    else:
        out["storage_limit"] = 0
    if data.get("userAdmins") is not None:
        import capo_repostspace.types.user_admins

        out["user_admins"] = capo_repostspace.types.user_admins.deserialize_json(
            data["userAdmins"]
        )
    if data.get("groupAdmins") is not None:
        import capo_repostspace.types.group_admins

        out["group_admins"] = capo_repostspace.types.group_admins.deserialize_json(
            data["groupAdmins"]
        )
    if data.get("roles") is not None:
        import capo_repostspace.types.roles

        out["roles"] = capo_repostspace.types.roles.deserialize_json(data["roles"])
    if data.get("userKMSKey") is not None:
        out["user_kms_key"] = data["userKMSKey"]
    if data.get("userCount") is not None:
        out["user_count"] = data["userCount"]
    if data.get("contentSize") is not None:
        out["content_size"] = data["contentSize"]
    if data.get("supportedEmailDomains") is not None:
        import capo_repostspace.types.supported_email_domains_status

        out["supported_email_domains"] = (
            capo_repostspace.types.supported_email_domains_status.deserialize_json(
                data["supportedEmailDomains"]
            )
        )
    return out


def redact_sensitive(value: GetSpaceOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "supported_email_domains" in value:
        import capo_repostspace.types.supported_email_domains_status

        out["supported_email_domains"] = (
            capo_repostspace.types.supported_email_domains_status.redact_sensitive(
                value["supported_email_domains"]
            )
        )
    return out
