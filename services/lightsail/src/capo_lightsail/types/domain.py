"""Generated from Smithy shape ``com.amazonaws.lightsail#Domain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.domain_entry_list
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.registered_domain_delegation_info
    import capo_lightsail.types.resource_location
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class Domain(TypedDict, closed=True):
    name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the domain.</p>"""
    arn: NotRequired["capo_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the domain recordset (<code>arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE</code>).</p>"""
    support_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The date when the domain recordset was created.</p>"""
    location: NotRequired["capo_lightsail.types.resource_location.ResourceLocation"]
    """<p>The AWS Region and Availability Zones where the domain recordset was created.</p>"""
    resource_type: NotRequired["capo_lightsail.types.resource_type.ResourceType"]
    """<p>The resource type. </p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>"""
    domain_entries: NotRequired[
        "capo_lightsail.types.domain_entry_list.DomainEntryList"
    ]
    """<p>An array of key-value pairs containing information about the domain entries.</p>"""
    registered_domain_delegation_info: NotRequired[
        "capo_lightsail.types.registered_domain_delegation_info.RegisteredDomainDelegationInfo"
    ]
    """<p>An object that describes the state of the Route 53 domain delegation to a Lightsail DNS zone.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Domain) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "location" in value:
        import capo_lightsail.types.resource_location

        out["location"] = capo_lightsail.types.resource_location.serialize_aws_json_1_1(
            value["location"]
        )
    if "resource_type" in value:
        import capo_lightsail.types.resource_type

        out["resourceType"] = capo_lightsail.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "domain_entries" in value:
        import capo_lightsail.types.domain_entry_list

        out["domainEntries"] = (
            capo_lightsail.types.domain_entry_list.serialize_aws_json_1_1(
                value["domain_entries"]
            )
        )
    if "registered_domain_delegation_info" in value:
        import capo_lightsail.types.registered_domain_delegation_info

        out["registeredDomainDelegationInfo"] = (
            capo_lightsail.types.registered_domain_delegation_info.serialize_aws_json_1_1(
                value["registered_domain_delegation_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Domain:
    out: Domain = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("supportCode") is not None:
        out["support_code"] = data["supportCode"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("location") is not None:
        import capo_lightsail.types.resource_location

        out["location"] = (
            capo_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if data.get("resourceType") is not None:
        import capo_lightsail.types.resource_type

        out["resource_type"] = (
            capo_lightsail.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("domainEntries") is not None:
        import capo_lightsail.types.domain_entry_list

        out["domain_entries"] = (
            capo_lightsail.types.domain_entry_list.deserialize_aws_json_1_1(
                data["domainEntries"]
            )
        )
    if data.get("registeredDomainDelegationInfo") is not None:
        import capo_lightsail.types.registered_domain_delegation_info

        out["registered_domain_delegation_info"] = (
            capo_lightsail.types.registered_domain_delegation_info.deserialize_aws_json_1_1(
                data["registeredDomainDelegationInfo"]
            )
        )
    return out
